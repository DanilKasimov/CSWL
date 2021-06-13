from Product import *
from Recipe import *


class Ingredient(BaseModel):
    Count = IntegerField()
    product_id = ForeignKeyField(Product)
    recipe_id = ForeignKeyField(Recipe)

    def SelectIngredient(self, strnumber, condition=None):
        if condition is None:
            request = Ingredient.select().join(Product, JOIN.LEFT_OUTER) \
                .switch(Ingredient).join(Recipe, JOIN.LEFT_OUTER).limit(18).offset(18 * (strnumber - 1))
        else:
            request = Ingredient.select().join(Product, JOIN.LEFT_OUTER) \
                .switch(Ingredient).join(Recipe, JOIN.LEFT_OUTER).where(Ingredient.Id.contains(condition) |
                                                                        Ingredient.Count.contains(condition))\
                .limit(18).offset(18 * (strnumber - 1))
        result = []
        for i in range(len(request)):
            stroka = [request[i].Id, str(request[i].Count)]
            # Recipe
            buf = Recipe.select().where(Recipe.Id != request[i].recipe_id)
            comb = [str(Recipe.select().where(Recipe.Id == request[i].recipe_id)[0].Id) + " " +
                    Recipe.select().where(Recipe.Id == request[i].recipe_id)[0].Name]
            for j in range(len(buf)):
                comb.append(str(buf[j].Id) + " " + buf[j].Name)
            stroka.append(comb)
            # Product
            buf = Product.select().where(Product.Id != request[i].product_id)
            comb = [str(Product.select().where(Product.Id == request[i].product_id)[0].Id) + " " +
                    str(Product.select().where(Product.Id == request[i].product_id)[0].Name)]
            for j in range(len(buf)):
                comb.append(str(buf[j].Id) + " " + str(buf[j].Name))
            stroka.append(comb)
            result.append(stroka)
        return result

    def Merge(self, atr):
        print(1)
        if atr[1] is not None:
            if atr[0] is not None:
                res = Ingredient.select().where(Ingredient.Id == int(atr[0].text()))
                if len(res) != 0:
                    print(atr[0].text(), atr[1].text(), atr[2], atr[3])
                    Ingredient.update({Ingredient.Count: atr[1].text(),
                                       Ingredient.recipe_id: atr[2],
                                       Ingredient.product_id: atr[3]})\
                        .where(Ingredient.Id == int(atr[0].text())).execute()
                else:
                    Ingredient.insert(Count=atr[1].text(), recipe_id=atr[2], product_id=atr[3]).execute()
            else:
                Ingredient.insert(Count=atr[1].text(), recipe_id=atr[2], product_id=atr[3]).execute()

    class Meta:
        table_name = 'Ingredient'
