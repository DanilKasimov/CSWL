from BaseModel import *


class Waiter(BaseModel):
    Name = CharField()
    Experience = IntegerField()

    def SelectWaiter(self, strnumber, condition=None):
        if condition is None:
            request = Waiter.select().limit(18).offset(18 * (strnumber - 1))
        else:
            request = Waiter.select().where(Waiter.Id.contains(condition) |
                                            Waiter.Name.contains(condition) |
                                            Waiter.Experience.contains(condition))\
                .limit(18).offset(18 * (strnumber - 1))
        result = []
        for i in range(len(request)):
            stroka = [request[i].Id, request[i].Name, request[i].Experience]
            result.append(stroka)
        return result

    def Merge(self, atr):
        if atr[1] is not None and atr[2] is not None:
            if atr[0] is not None:
                res = Waiter.select().where(Waiter.Id == int(atr[0].text()))
                if len(res) != 0:
                    Waiter.update({Waiter.Name: atr[1].text(), Waiter.Experience: atr[2].text()})\
                        .where(Waiter.Id == int(atr[0].text())).execute()
                else:
                    Waiter.insert(Name=atr[1].text(), Experience=atr[2].text()).execute()
            else:
                Waiter.insert(Name=atr[1].text(), Experience=atr[2].text()).execute()

    class Meta:
        table_name = 'Waiter'
