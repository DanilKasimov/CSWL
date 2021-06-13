from Owner import *



class Cafe(BaseModel):
    Name = CharField()
    Rating = IntegerField()
    owner_id = ForeignKeyField(Owner)

    def SelectCafe(self, strnumber, condition=None):
        if condition is None:
            request = Cafe.select().join(Owner, JOIN.LEFT_OUTER).limit(18).offset(18 * (strnumber - 1))
        else:
            request = Cafe.select().join(Owner, JOIN.LEFT_OUTER).where(Cafe.Name.contains(condition) |
                                                                       Cafe.Rating.contains(condition))\
                .limit(18).offset(18 * (strnumber - 1))

        result = []
        for i in range(len(request)):
            print(2)
            stroka = [request[i].Id, request[i].Name, request[i].Rating]
            print(3)
            buf = Owner.select().where(Owner.Id != request[i].owner_id)
            print(44)
            comb = [str(Owner.select().where(Owner.Id == request[i].owner_id)[0].Id) + " " +
                    Owner.select().where(Owner.Id == request[i].owner_id)[0].Name]
            print(5)
            for j in range(len(buf)):
                comb.append(str(buf[j].Id) + " " + buf[j].Name)
            print(6)
            stroka.append(comb)
            print(7)
            result.append(stroka)
        return result

    def Merge(self, atr):
        if atr[1] is not None and atr[2] is not None:
            if atr[0] is not None:
                res = Cafe.select().where(Cafe.Id == int(atr[0].text()))
                if len(res) != 0:
                    Cafe.update({Cafe.Name: atr[1].text(),
                                 Cafe.Rating: int(atr[2].text()),
                                 Cafe.owner_id: atr[3]}).where(Cafe.Id == int(atr[0].text())).execute()
                else:
                    Cafe.insert(Name=atr[1].text(), Rating=int(atr[2].text()), owner_id=atr[3]).execute()
            else:
                Cafe.insert(Name=atr[1].text(), Rating=int(atr[2].text()), owner_id=atr[3]).execute()

    class Meta:
        table_name = 'Cafe'

