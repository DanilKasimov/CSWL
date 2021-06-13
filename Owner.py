from BaseModel import *


class Owner(BaseModel):
    Name = CharField()
    Number = CharField()

    def SelectOwner(self, strnumber, condition=None):
        if condition is None:
            request = Owner.select().limit(18).offset(18 * (strnumber - 1))
        else:
            request = Owner.select().where(Owner.Name.contains(condition) |
                                           Owner.Id.contains(condition) |
                                           Owner.Number.contains(condition)).limit(18).offset(18 * (strnumber - 1))
        result = []
        for i in range(len(request)):
            stroka = [request[i].Id, request[i].Name, request[i].Number]
            result.append(stroka)
        return result

    def Merge(self, atr):
        if atr[1] is not None and atr[2] is not None:
            if atr[0] is not None:
                res = Owner.select().where(Owner.Id == int(atr[0].text()))
                if len(res) != 0:
                    Owner.update({Owner.Name: atr[1].text(), Owner.Number: atr[2].text()})\
                        .where(Owner.Id == int(atr[0].text())).execute()
                else:
                    Owner.insert(Name=atr[1].text(), Number=atr[2].text()).execute()
            else:
                Owner.insert(Name=atr[1].text(), Number=atr[2].text()).execute()

    class Meta:
        table_name = 'Owner'
