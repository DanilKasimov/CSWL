from BaseModel import *
from Provider import *
from Owner import *
from Cafe import *
from Cook import *
from Creating import *
from Waiter import *
from Visitor import *
from Stolik import *
from Recipe import *
from Product import *
from Ingredient import *
from Dish import *
import re
from peewee import *
from mysql.connector import cursor, connect


class Db:
    def __init__(self):
        self.last_query = ""
        self.conn = connect(host='localhost', database='cswl3orm', user='root', password='Danilka210300')

    def Format(self, text):
        text = str(text)
        return re.sub('[^A-Za-z0-9а-яА-ЯЁё ]+', '', text)

    def Close(self):
        self.conn.close()

    def Select(self, table=None, strnumber=None):

        if table == 'Заведение':
            print(1)
            return Cafe().SelectCafe(strnumber)

        if table == 'Готовка':
            return Creating().SelectCreating(strnumber)

        if table == 'Блюдо':
            return Dish().SelectDish(strnumber)

        if table == 'Ингридиент':
            return Ingredient().SelectIngredient(strnumber)

        if table == 'Владелец':
            return Owner().SelectOwner(strnumber)

        if table == 'Продукт':
            return Product().SelectProduct(strnumber)

        if table == 'Поставщик':
            return Provider().SelectProvider(strnumber)

        if table == 'Рецепт':
            return Recipe().SelectRecipe(strnumber)

        if table == 'Столик':
            return Stolik().SelectStolik(strnumber)

        if table == 'Гость':
            return Visitor().SelectVisitor(strnumber)

        if table == 'Официант':
            return Waiter().SelectWaiter(strnumber)

        if table == 'Повар':
            return Cook().SelectCook(strnumber)

    def Search(self, table, znach, strnumber):
        if table == 'Поставщик':
            return Provider().SelectProvider(strnumber, condition=znach)
        if table == 'Продукт':
            return Product().SelectProduct(strnumber, condition=znach)
        if table == 'Владелец':
            return Owner().SelectOwner(strnumber, condition=znach)
        if table == 'Заведение':
            return Cafe().SelectCafe(strnumber, condition=znach)
        if table == 'Повар':
            return Cook().SelectCook(strnumber, condition=znach)
        if table == 'Готовка':
            return Creating().SelectCreating(strnumber, condition=znach)
        if table == 'Блюдо':
            return Dish().SelectDish(strnumber, condition=znach)
        if table == 'Рецепт':
            return Recipe().SelectRecipe(strnumber, condition=znach)
        if table == 'Ингридиент':
            return Ingredient().SelectIngredient(strnumber, condition=znach)
        if table == 'Гость':
            return Visitor().SelectVisitor(strnumber, condition=znach)
        if table == 'Столик':
            return Stolik().SelectStolik(strnumber, condition=znach)
        if table == 'Официант':
            return Waiter().SelectWaiter(strnumber, condition=znach)

    def Merge(self, table, atr):
        if table == 'Поставщик':
            Provider().Merge(atr)
        if table == 'Продукт':
            Product().Merge(atr)
        if table == 'Владелец':
            Owner().Merge(atr)
        if table == 'Заведение':
            Cafe().Merge(atr)
        if table == 'Повар':
            Cook().Merge(atr)
        if table == 'Готовка':
            Creating().Merge(atr)
        if table == 'Блюдо':
            Dish().Merge(atr)
        if table == 'Рецепт':
            Recipe().Merge(atr)
        if table == 'Ингридиент':
            Ingredient().Merge(atr)
        if table == 'Гость':
            Visitor().Merge(atr)
        if table == 'Столик':
            Stolik().Merge(atr)
        if table == 'Официант':
            Waiter().Merge(atr)

    def Delete(self, table, id):
        Del = None
        if table == 'Поставщик':
            Del = Provider.delete().where(Provider.Id == id)
        if table == 'Продукт':
            Del = Product.delete().where(Product.Id == id)
        if table == 'Владелец':
            Del = Owner.delete().where(Owner.Id == id)
        if table == 'Заведение':
            Del = Cafe.delete().where(Cafe.Id == id)
        if table == 'Повар':
            Del = Cook.delete().where(Cook.Id == id)
        if table == 'Готовка':
            Del = Creating.delete().where(Creating.Id == id)
        if table == 'Блюдо':
            Del = Dish.delete().where(Dish.Id == id)
        if table == 'Рецепт':
            Del = Recipe.delete().where(Recipe.Id == id)
        if table == 'Ингридиент':
            Del = Ingredient.delete().where(Ingredient.Id == id)
        if table == 'Гость':
            Del = Visitor.delete().where(Visitor.Id == id)
        if table == 'Столик':
            Del = Stolik.delete().where(Stolik.Id == id)
        if table == 'Официант':
            Del = Waiter.delete().where(Waiter.Id == id)
        Del.execute()
