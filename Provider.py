from BaseModel import *


class Provider(BaseModel):
    Name = CharField()
    Number = CharField()

    def SelectProvider(self, strnumber, condition=None):
        request = None
        if condition is None:
            request = Provider.select().limit(18).offset(18 * (strnumber - 1))
        else:
            request = Provider.select().where(Provider.Id.contains(condition) |
                                              Provider.Name.contains(condition) |
                                              Provider.Number.contains(condition)) \
                .limit(18).offset(18 * (strnumber - 1))
        result = []
        for i in range(len(request)):
            stroka = [request[i].Id, request[i].Name, request[i].Number]
            result.append(stroka)
        return result

    def Merge(self, atr):
        if atr[1] is not None and atr[2] is not None:
            if atr[0] is not None:
                res = Provider.select().where(Provider.Id == int(atr[0].text()))
                if len(res) != 0:
                    Provider.update({Provider.Name: atr[1].text(), Provider.Number: atr[2].text()})\
                        .where(Provider.Id == int(atr[0].text())).execute()
                else:
                    Provider.insert(Name=atr[1].text(), Number=atr[2].text()).execute()
            else:
                Provider.insert(Name=atr[1].text(), Number=atr[2].text()).execute()

    class Meta:
        table_name = 'Provider'
