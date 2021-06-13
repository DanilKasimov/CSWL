from Provider import *
from Cafe import *


class Product(BaseModel):
    Name = CharField()
    Count = IntegerField()
    provider_id = ForeignKeyField(Provider)
    cafe_id = ForeignKeyField(Cafe)

    def Merge(self, atr):
        print(1)
        if atr[1] is not None and atr[3] is not None:
            if atr[0] is not None:
                res = Product.select().where(Product.Id == int(atr[0].text()))
                if len(res) != 0:
                    Product.update({Product.Name: atr[1].text(),
                                    Product.provider_id: atr[2],
                                    Product.Count: int(atr[3].text()),
                                    Product.cafe_id: atr[4]}).where(Product.Id == int(atr[0].text())).execute()
                else:
                    print(atr)
                    Product.insert(Name=atr[1].text(),
                                   provider_id=atr[2],
                                   Count=int(atr[3].text()),
                                   cafe_id=atr[4]).execute()
            else:
                print(atr)
                Product.insert(Name=atr[1].text(),
                               provider_id=atr[2],
                               Count=int(atr[3].text()),
                               cafe_id=atr[4]).execute()

    def SelectProduct(self, strnumber, condition=None):
        if condition is None:
            request = Product.select().join(Provider, JOIN.LEFT_OUTER) \
                .switch(Product).join(Cafe, JOIN.LEFT_OUTER).limit(18).offset(18 * (strnumber - 1))
        else:
            request = Product.select().join(Provider, JOIN.LEFT_OUTER) \
                .switch(Product).join(Cafe, JOIN.LEFT_OUTER).where(Product.Name.contains(condition)
                                                                   | Product.Count.contains(condition)) \
                .limit(18).offset(18 * (strnumber - 1))
        result = []
        for i in range(len(request)):
            stroka = [request[i].Id, request[i].Name, str(request[i].Count)]
            # Provider
            buf = Provider.select().where(Provider.Id != request[i].provider_id)
            comb = [str(Provider.select().where(Provider.Id == request[i].provider_id)[0].Id) + " " +
                    Provider.select().where(Provider.Id == request[i].provider_id)[0].Name]
            for j in range(len(buf)):
                comb.append(str(buf[j].Id) + " " + buf[j].Name)
            stroka.append(comb)
            # Cafe
            buf = Cafe.select().where(Cafe.Id != request[i].cafe_id)
            comb = [str(Cafe.select().where(Cafe.Id == request[i].cafe_id)[0].Id) + " " +
                    str(Cafe.select().where(Cafe.Id == request[i].cafe_id)[0].Name)]
            for j in range(len(buf)):
                comb.append(str(buf[j].Id) + " " + str(buf[j].Name))
            stroka.append(comb)
            result.append(stroka)
        return result

    class Meta:
        table_name = 'Product'
