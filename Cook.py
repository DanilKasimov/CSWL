from Cafe import *


class Cook(BaseModel):
    Name = CharField()
    Experience = IntegerField()
    cafe_id = ForeignKeyField(Cafe)

    def SelectCook(self, strnumber, condition=None):
        if condition is None:
            request = Cook.select().join(Cafe, JOIN.LEFT_OUTER).limit(18).offset(18 * (strnumber - 1))
        else:
            request = Cook.select().join(Cafe, JOIN.LEFT_OUTER).where(Cook.Id.contains(condition) |
                                                                      Cook.Name.contains(condition) |
                                                                      Cook.Experience.contains(condition))\
                .limit(18).offset(18 * (strnumber - 1))
        result = []
        for i in range(len(request)):
            stroka = [request[i].Id, request[i].Name, request[i].Experience]
            buf = Cafe.select().where(Cafe.Id != request[i].cafe_id)
            comb = [str(Cafe.select().where(Cafe.Id == request[i].cafe_id)[0].Id) + " " +
                    Cafe.select().where(Cafe.Id == request[i].cafe_id)[0].Name]
            for j in range(len(buf)):
                comb.append(str(buf[j].Id) + " " + buf[j].Name)
            stroka.append(comb)
            result.append(stroka)
        return result

    def Merge(self, atr):
        if atr[1] is not None and atr[3] is not None:
            if atr[0] is not None:
                res = Cook.select().where(Cook.Id == int(atr[0].text()))
                if len(res) != 0:
                    Cook.update({Cook.Name: atr[1].text(), Cook.cafe_id: atr[2], Cook.Experience: int(atr[3].text())})\
                        .where(Cook.Id == int(atr[0].text())).execute()
                else:
                    Cook.insert(Name=atr[1].text(), cafe_id=atr[2], Experience=int(atr[3].text())).execute()
            else:
                Cook.insert(Name=atr[1].text(), cafe_id=atr[2], Experience=int(atr[3].text())).execute()

    class Meta:
        table_name = 'Cook'
