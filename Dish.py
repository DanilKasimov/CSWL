from Visitor import *
from Recipe import *
from Creating import *


class Dish(BaseModel):
    Name = CharField()
    recipe_id = ForeignKeyField(Recipe)
    creating_id = ForeignKeyField(Creating)
    visitor_id = ForeignKeyField(Visitor)

    def SelectDish(self, strnumber, condition=None):
        if condition is None:
            request = Dish.select().join(Recipe, JOIN.LEFT_OUTER) \
                .switch(Dish).join(Creating, JOIN.LEFT_OUTER) \
                .switch(Dish).join(Visitor, JOIN.LEFT_OUTER).limit(18).offset(18 * (strnumber - 1))
        else:
            request = Dish.select().join(Recipe, JOIN.LEFT_OUTER) \
                .switch(Dish).join(Creating, JOIN.LEFT_OUTER) \
                .switch(Dish).join(Visitor, JOIN.LEFT_OUTER).where(Dish.Id.contains(condition) |
                                                                   Dish.Name.contains(condition)) \
                .limit(18).offset(18 * (strnumber - 1))
        result = []
        for i in range(len(request)):
            stroka = [request[i].Id, request[i].Name]
            # Recipe
            buf = Recipe.select().where(Recipe.Id != request[i].recipe_id)
            comb = [str(Recipe.select().where(Recipe.Id == request[i].recipe_id)[0].Id) + " " +
                    Recipe.select().where(Recipe.Id == request[i].recipe_id)[0].Name]
            for j in range(len(buf)):
                comb.append(str(buf[j].Id) + " " + buf[j].Name)
            stroka.append(comb)
            # Creating
            buf = Creating.select().where(Creating.Id != request[i].creating_id)
            comb = [str(Creating.select().where(Creating.Id == request[i].creating_id)[0].Id) + " " +
                    str(Creating.select().where(Creating.Id == request[i].creating_id)[0].Time)]
            for j in range(len(buf)):
                comb.append(str(buf[j].Id) + " " + str(buf[j].Time))
            stroka.append(comb)
            # Visitor
            buf = Visitor.select().where(Visitor.Id != request[i].visitor_id)
            comb = [str(Visitor.select().where(Visitor.Id == request[i].visitor_id)[0].Id) + " " +
                    Visitor.select().where(Visitor.Id == request[i].visitor_id)[0].Name]
            for j in range(len(buf)):
                comb.append(str(buf[j].Id) + " " + buf[j].Name)
            stroka.append(comb)
            result.append(stroka)
        return result

    def Merge(self, atr):
        if atr[1] is not None:
            if atr[0] is not None:
                res = Dish.select().where(Dish.Id == int(atr[0].text()))
                if len(res) != 0:
                    Dish.update({Dish.Name: atr[1].text(),
                                 Dish.recipe_id: atr[2],
                                 Dish.creating_id: atr[3],
                                 Dish.visitor_id: atr[4]}).where(Dish.Id == int(atr[0].text())).execute()
                else:
                    Dish.insert(Name=atr[1].text(), recipe_id=atr[2], creating_id=atr[3], visitor_id=atr[4]).execute()
            else:
                Dish.insert(Name=atr[1].text(), recipe_id=atr[2], creating_id=atr[3], visitor_id=atr[4]).execute()

    class Meta:
        table_name = 'Dish'
