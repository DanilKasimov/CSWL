from Waiter import *


class Stolik(BaseModel):
    TableLevel = CharField()
    waiter_id = ForeignKeyField(Waiter)

    def SelectStolik(self, strnumber, condition=None):
        if condition is None:
            request = Stolik.select().join(Waiter, JOIN.LEFT_OUTER).limit(18).offset(18 * (strnumber - 1))
        else:
            request = Stolik.select().join(Waiter, JOIN.LEFT_OUTER).where(Stolik.Id.contains(condition) |
                                                                          Stolik.TableLevel.contains(condition))\
                .limit(18).offset(18 * (strnumber - 1))
        result = []
        for i in range(len(request)):
            stroka = [request[i].Id, request[i].TableLevel]
            buf = Waiter.select().where(Waiter.Id != request[i].waiter_id)
            comb = [str(Waiter.select().where(Waiter.Id == request[i].waiter_id)[0].Id) + " " +
                    Waiter.select().where(Waiter.Id == request[i].waiter_id)[0].Name]
            for j in range(len(buf)):
                comb.append(str(buf[j].Id) + " " + buf[j].Name)
            stroka.append(comb)
            result.append(stroka)
        return result

    def Merge(self, atr):
        if atr[1] is not None:
            if atr[0] is not None:
                res = Stolik.select().where(Stolik.Id == int(atr[0].text()))
                if len(res) != 0:
                    Stolik.update({Stolik.TableLevel: atr[1].text(), Stolik.waiter_id: atr[2]})\
                        .where(Stolik.Id == int(atr[0].text())).execute()
                else:
                    Stolik.insert(TableLevel=atr[1].text(), waiter_id=atr[2]).execute()
            else:
                Stolik.insert(TableLevel=atr[1].text(), waiter_id=atr[2]).execute()

    class Meta:
        table_name = 'Stolik'
