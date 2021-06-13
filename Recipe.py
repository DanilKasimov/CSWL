from BaseModel import *


class Recipe(BaseModel):
    Name = CharField()

    def SelectRecipe(self, strnumber, condition=None):
        if condition is None:
            request = Recipe.select().limit(18).offset(18 * (strnumber - 1))
        else:
            request = Recipe.select().where(Recipe.Id.contains(condition) |
                                            Recipe.Name.contains(condition)).limit(18).offset(18 * (strnumber - 1))
        result = []
        for i in range(len(request)):
            stroka = [request[i].Id, request[i].Name]
            result.append(stroka)
        return result

    def Merge(self, atr):
        if atr[1] is not None:
            if atr[0] is not None:
                res = Recipe.select().where(Recipe.Id == int(atr[0].text()))
                if len(res) != 0:
                    Recipe.update({Recipe.Name: atr[1].text()})\
                        .where(Recipe.Id == int(atr[0].text())).execute()
                else:
                    Recipe.insert(Name=atr[1].text()).execute()
            else:
                Recipe.insert(Name=atr[1].text()).execute()

    class Meta:
        table_name = 'Recipe'
