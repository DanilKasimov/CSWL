from Cook import *
from datetime import datetime


class Creating(BaseModel):
    Time = DateTimeField(default=datetime.now())
    cook_id = ForeignKeyField(Cook)

    def SelectCreating(self, strnumber, condition=None):
        if condition is None:
            request = Creating.select().join(Cook, JOIN.LEFT_OUTER).limit(18).offset(18 * (strnumber - 1))
        else:
            request = Creating.select().join(Cook, JOIN.LEFT_OUTER).where(Creating.Id.contains(condition) |
                                                                          Creating.Time.contains(condition))\
                .limit(18).offset(18 * (strnumber - 1))
        result = []
        for i in range(len(request)):
            stroka = [request[i].Id, request[i].Time]
            buf = Cook.select().where(Cook.Id != request[i].cook_id)
            comb = [str(Cook.select().where(Cook.Id == request[i].cook_id)[0].Id) + " " +
                    Cook.select().where(Cook.Id == request[i].cook_id)[0].Name]
            for j in range(len(buf)):
                comb.append(str(buf[j].Id) + " " + buf[j].Name)
            stroka.append(comb)
            result.append(stroka)
        return result

    def Merge(self, atr):
        if atr[0] is not None:
            res = Creating.select().where(Creating.Id == int(atr[0].text()))
            if len(res) != 0:
                Creating.update({Creating.cook_id: atr[1]}).where(Creating.Id == int(atr[0].text())).execute()
            else:
                Creating.insert(cook_id=atr[1]).execute()
        else:
            Creating.insert(cook_id=atr[1]).execute()

    class Meta:
        table_name = 'Creating'
