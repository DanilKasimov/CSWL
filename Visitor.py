from Stolik import *


class Visitor(BaseModel):
    Name = CharField()
    stolik_id = ForeignKeyField(Stolik)

    def SelectVisitor(self, strnumber, condition=None):
        if condition is None:
            request = Visitor.select().join(Stolik, JOIN.LEFT_OUTER).limit(18).offset(18 * (strnumber - 1))
        else:
            request = Visitor.select().join(Stolik, JOIN.LEFT_OUTER).where(Visitor.Id.contains(condition) |
                                                                           Visitor.Name.contains(condition))\
                .limit(18).offset(18 * (strnumber - 1))
        result = []
        for i in range(len(request)):
            stroka = [request[i].Id, request[i].Name]
            buf = Stolik.select().where(Stolik.Id != request[i].stolik_id)
            comb = [str(Stolik.select().where(Stolik.Id == request[i].stolik_id)[0].Id) + " " +
                    Stolik.select().where(Stolik.Id == request[i].stolik_id)[0].TableLevel]
            for j in range(len(buf)):
                comb.append(str(buf[j].Id) + " " + buf[j].TableLevel)
            stroka.append(comb)
            result.append(stroka)
        return result

    def Merge(self, atr):
        if atr[2] is not None:
            if atr[0] is not None:
                res = Visitor.select().where(Visitor.Id == int(atr[0].text()))
                if len(res) != 0:
                    Visitor.update({Visitor.stolik_id: atr[1], Visitor.Name: atr[2].text()})\
                        .where(Visitor.Id == int(atr[0].text())).execute()
                else:
                    Visitor.insert(stolik_id=atr[1], Name=atr[2].text()).execute()
            else:
                Visitor.insert(stolik_id=atr[1], Name=atr[2].text()).execute()

    class Meta:
        table_name = 'Visitor'
