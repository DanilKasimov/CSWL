from mysql.connector import connect, Error
import re


class Db:
    def __init__(self, host, database, user, password):
        self.conn = connect(host=host, database=database, user=user, password=password)
        self.last_query = ""

    def Format(self, text):
        text = str(text)
        return re.sub('[^A-Za-z0-9а-яА-ЯЁё ]+', '', text)

    def Close(self):
        self.conn.close()

    def Select(self, table=None, main_query=None, condition=None, strnumber=None):
        cursor = self.conn.cursor()
        query = ""
        if main_query is None:
            args = [condition, str(18 * (strnumber - 1)), str(18 * strnumber)]
            if table == 'Заведение':
                query = "get_cafe"
            if table == 'Готовка':
                query = "get_creating"
            if table == 'Блюдо':
                query = "get_dish"
            if table == 'Ингридиент':
                query = "get_ingredient"
            if table == 'Владелец':
                query = "get_owner"
            if table == 'Продукт':
                query = "get_product"
            if table == 'Поставщик':
                query = "get_provider"
            if table == 'Рецепт':
                query = "get_recipe"
            if table == 'Столик':
                query = "get_table"
            if table == 'Гость':
                query = "get_visitor"
            if table == 'Официант':
                query = "get_waiter"
            if table == 'Повар':
                query = "get_cook"
            result = []
            try:
                cursor.callproc(query, args)
                for i in cursor.stored_results():
                    result = i.fetchall()
                cursor.close()
            except Error as e:
                print(e)
            return result
        else:
            query = main_query
            if strnumber is not None:
                if query.find("WHERE") != -1:
                    query = query + " AND RowNumb between %s and %s " % (str(18 * (strnumber - 1)), str(18 * strnumber))
                else:
                    query = query + " WHERE RowNumb between %s and %s " % (str(18 * (strnumber - 1)), str(18 * strnumber))
            cursor.execute(query)
            return cursor.fetchall()

    def Search(self, table, p_usl):
        usl = self.Format(p_usl)
        res = self.Select(table=table, condition=usl, strnumber=1)
        return res

    def Translate(self, table):
        query = ""
        if table == 'Заведение':
            query = "cafe"
        if table == 'Готовка':
            query = "creating"
        if table == 'Блюдо':
            query = "dish"
        if table == 'Ингридиент':
            query = "ingridient"
        if table == 'Владелец':
            query = "owner"
        if table == 'Продукт':
            query = "product"
        if table == 'Поставщик':
            query = "provider"
        if table == 'Рецепт':
            query = "recipe"
        if table == 'Столик':
            query = "table"
        if table == 'Гость':
            query = "visitor"
        if table == 'Официант':
            query = "waiter"
        if table == 'Повар':
            query = "cook"
        return query

    def Merge(self, table, values):
        tab = self.Translate(table)
        cursor = self.conn.cursor()
        print(values)
        try:
            cursor.callproc("merge_" + tab, values)
        except Error as e:
            print(e)
        cursor.execute("COMMIT;")
        cursor.close()

    def Delete(self, table, id):
        query = self.Translate(table)
        cursor = self.conn.cursor()
        try:
            cursor.callproc("del", [query, id])
        except Error as e:
            print(e)
        cursor.execute("COMMIT;")
        cursor.close()

