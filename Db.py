from mysql.connector import connect, errors
import re


class Db:
    def __init__(self, host, database, user, password):
        self.conn = connect(host=host, database=database, user=user, password=password)
        self.last_query = ""

    def Format(self, text):
        text = str(text)
        return re.sub('[^A-Za-z0-9а-яА-ЯЁё ]+', '', text)

    def Select(self, table=None, main_query=None, condition=None, strnumber=None):
        cursor = self.conn.cursor()
        query = ""
        if main_query is None:
            if table == 'Заведение':
                query = "With CafeTable AS (SELECT *, row_number() OVER (order by idcafe) as RowNumb FROM cswl1.cafe) " \
                        "SELECT idcafe, cafename, caferating, ownername FROM CafeTable  " \
                        "LEFT JOIN cswl1.owner ON cafetable.idowner = owner.idowner "
            if table == 'Готовка':
                query = "With CreatingTable AS (SELECT *, row_number() OVER (order by idcreating) as RowNumb " \
                        "FROM cswl1.creating) " \
                        "SELECT idcreating, creatingtime, cookaname FROM CreatingTable " \
                        "LEFT JOIN cswl1.cook ON creatingtable.idcook = cook.idcook "
            if table == 'Блюдо':
                query = "With DishTable AS (SELECT *, row_number() OVER (order by iddish) as RowNumb FROM cswl1.dish) " \
                        "SELECT iddish, dishname, recipename, creatingtime, visitorname FROM DishTable " \
                        "LEFT JOIN cswl1.recipe ON DishTable.idrecipe = recipe.idrecipe " \
                        "LEFT JOIN cswl1.creating ON DishTable.idcreating = creating.idcreating " \
                        "LEFT JOIN cswl1.visitor ON DishTable.idvisitor = visitor.idvisitor "
            if table == 'Ингридиент':
                query = "With IngrTable AS (SELECT *, row_number() OVER (order by idingridient) as RowNumb " \
                        "FROM cswl1.ingridient) " \
                        "SELECT idingridient, ingridientcount, recipename, productname FROM IngrTable " \
                        "LEFT JOIN cswl1.recipe ON IngrTable.idrecipe = recipe.idrecipe " \
                        "LEFT JOIN cswl1.product ON IngrTable.idproduct = product.idproduct "
            if table == 'Владелец':
                query = "With OwnerTable AS (SELECT *, row_number() OVER (order by idowner) " \
                        "as RowNumb FROM cswl1.owner) " \
                        "SELECT idowner, ownername, ownernumber FROM OwnerTable "
            if table == 'Продукт':
                query = "With ProductTable AS (SELECT *, row_number() OVER (order by idproduct) as RowNumb " \
                        "FROM cswl1.Product) " \
                        "SELECT idproduct, productname, providername, productcount, cafename FROM ProductTable " \
                        "LEFT JOIN cswl1.provider ON ProductTable.idprovider = provider.idprovider " \
                        "LEFT JOIN cswl1.cafe ON ProductTable.idcafe = cafe.idcafe "
            if table == 'Поставщик':
                query = "With ProviderTable AS (SELECT *, row_number() OVER (order by idprovider) as RowNumb " \
                        "FROM cswl1.Provider) " \
                        "SELECT idprovider, providername, providernumber FROM ProviderTable "
            if table == 'Рецепт':
                query = "With RecipeTable AS (SELECT *, row_number() OVER (order by idrecipe) as RowNumb " \
                        "FROM cswl1.recipe) " \
                        "SELECT idrecipe, recipename FROM RecipeTable "
            if table == 'Столик':
                query = "With TableTable AS (SELECT *, row_number() OVER (order by idtable) " \
                        "as RowNumb FROM cswl1.table) " \
                        "SELECT idtable, tablellvl, waitername FROM TableTable " \
                        "LEFT JOIN cswl1.waiter ON TableTable.idwaiter = waiter.idwaiter"
            if table == 'Гость':
                query = "With VisitorTable AS (SELECT *, row_number() OVER (order by idvisitor) as RowNumb " \
                        "FROM cswl1.visitor) SELECT idvisitor, visitorname, idtable FROM VisitorTable  "
            if table == 'Официант':
                query = "With WaiterTable AS (SELECT *, row_number() OVER (order by idwaiter) as RowNumb " \
                        "FROM cswl1.waiter) " \
                        "SELECT idwaiter, waitername, waiterexp FROM WaiterTable "
            if table == 'Повар':
                query = "With CookTable AS (SELECT *,row_number() OVER (order by idcook) as RowNumb FROM cswl1.cook) " \
                        "SELECT idcook, cookaname, cookexp, cafename FROM CookTable " \
                        "LEFT JOIN cswl1.cafe ON cooktable.idcafe = cafe.idcafe "
            self.last_query = query
            query = query + " WHERE RowNumb between " + str(18 * (strnumber - 1)) + " and " + str(18 * strnumber)
            if condition is not None:
                query = query + " AND " + condition
        else:
            query = main_query
            if strnumber is not None:
                if query.find("WHERE") != -1:
                    query = query + " AND RowNumb between " + str(18 * (strnumber - 1)) \
                            + " and " + str(18 * strnumber)
                else:
                    query = query + " WHERE RowNumb between " + str(18 * (strnumber - 1)) \
                            + " and " + str(18 * strnumber)
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result

    def Search(self, table, p_usl):
        usl = self.Format(p_usl)
        query = ""
        if table == 'Повар':
            query = " (lower(idcook) like '%{0}%' or lower(cookaname) like '%{0}}%' or lower(cookexp) like '%{0}%' " \
                    "or lower(cafename) like '%{0}%') ".format(usl)
        if table == 'Заведение':
            query = " (lower(idcafe) like '%{0}%' or lower(cafename) like '%{0}%' or lower(caferating)like '%{0}%' " \
                    "or lower(ownername) like '%{0}%') ".format(usl)
        if table == 'Готовка':
            query = " (lower(idcreating) like '%{0}%' or lower(creatingtime) like '%{0}%' " \
                    "or lower(cookaname) like '%{0}%') ".format(usl)
        if table == 'Блюдо':
            query = " (lower(iddish) like '%{0}%' or lower(dishname) like '%{0}%' or lower(recipename) like '%{0}%' " \
                    "or lower(creatingtime) like '%{0}%' or lower(visitorname) like '%{0}%') ".format(usl)
        if table == 'Ингридиент':
            query = " (lower(idingridient) like '%{0}%' or lower(ingridientcount) like '%{0}%' " \
                    "or lower(recipename) like '%{0}%' or lower(productname) like '%{0}%') ".format(usl)
        if table == 'Владелец':
            query = " (lower(idowner) like '%{0}%' or lower(ownername) like '%{0}%' " \
                    "or lower(ownernumber) like '%{0}%') ".format(usl)
        if table == 'Продукт':
            query = " (lower(idproduct) like '%{0}%' or lower(productname) like '%{0}%' " \
                    "or lower(providername) like '%{0}%' or lower(productcount) like '%{0}%' " \
                    "or lower(cafename) like '%{0}%') ".format(usl)
        if table == 'Поставщик':
            query = " (lower(idprovider) like '%{0}%' or lower(providername) like '%{0}%' " \
                    "or lower(providernumber) like '%{0}%') ".format(usl)
        if table == 'Рецепт':
            query = " (lower(idrecipe) like '%{0}%' or lower(recipename) like '%{0}%') ".format(usl)
        if table == 'Столик':
            query = " (lower(idtable) like '%{0}%' or lower(tablellvl) like '%{0}%' " \
                    "or lower(waitername) like '%{0}%') ".format(usl)
        if table == 'Гость':
            query = " (lower(idvisitor) like '%{0}%' or lower(visitorname) like '%{0}%' " \
                    "or lower(idtable) like '%{0}%') ".format(usl)
        if table == 'Официант':
            query = " (lower(idwaiter) like '%{0}%' or lower(waitername) like '%{0}%'" \
                    " or lower(waiterexp) like '%{0}%') "
        res = self.Select(table=table, condition=query, strnumber=1)
        self.last_query += " WHERE " + query
        return res

    def Merge(self, table, values):
        cursor = self.conn.cursor()
        if table == 'Повар':
            buf = []
            result = self.Select(main_query="SELECT idcook from cswl1.cook")
            for i in range(len(result)):
                buf.append(result[i][0])
            if values[1] is not None and values[3] is not None:
                if values[0] is not None:
                    ok = False
                    for i in range(len(buf)):
                        if str(values[0].text()) == str(buf[i]):
                            ok = True
                            break
                    if ok:
                        cursor.execute("UPDATE cswl1.cook "
                                       "SET cookaname = '%s', "
                                       "idcafe = '%s', "
                                       "cookexp = '%s' "
                                       "WHERE idcook = '%s';  "
                                       "" % (self.Format(values[1].text()), str(values[2]),
                                             self.Format(values[3].text()), self.Format(values[0].text())))
                    else:
                        cursor.execute("INSERT INTO cswl1.cook (cookaname, idcafe, cookexp) "
                                       "VALUES('%s','%s','%s'); " % (self.Format(values[1].text()),
                                                                     str(values[2]), self.Format(values[3].text())))
                else:
                    cursor.execute("INSERT INTO cswl1.cook (cookaname, idcafe, cookexp) "
                                   "VALUES('%s','%s','%s'); " % (self.Format(values[1].text()),
                                                                 str(values[2]), self.Format(values[3].text())))
        if table == 'Заведение':
            buf = []
            result = self.Select(main_query="SELECT idcafe from cswl1.cafe")
            for i in range(len(result)):
                buf.append(result[i][0])
            if values[1] is not None and values[2] is not None:
                if values[0] is not None:
                    ok = False
                    for i in range(len(buf)):
                        if str(values[0].text()) == str(buf[i]):
                            ok = True
                            break
                    if ok:
                        cursor.execute("UPDATE cswl1.cafe "
                                       "SET cafename = '%s', "
                                       "caferating = '%s', "
                                       "idowner = '%s' "
                                       "WHERE idcafe = '%s' " % (self.Format(values[1].text()),
                                                                 self.Format(values[2].text()),
                                                                 values[3],
                                                                 self.Format(values[0].text())))

                    else:
                        cursor.execute("INSERT INTO cswl1.cafe(cafename, caferating, idowner)"
                                       "VALUES('%s', '%s', '%s')" % (self.Format(values[1].text()),
                                                                     self.Format(values[2].text()),
                                                                     values[3]))
                else:
                    cursor.execute("INSERT INTO cswl1.cafe(cafename, caferating, idowner)"
                                   "VALUES('%s', '%s', '%s')" % (self.Format(values[1].text()),
                                                                 self.Format(values[2].text()),
                                                                 values[3]))

        if table == 'Готовка':
            buf = []
            result = self.Select(main_query="SELECT idcreating FROM cswl1.creating")
            for i in range(len(result)):
                buf.append(result[i][0])
            if values[0] is not None:
                ok = False
                for i in range(len(buf)):
                    if str(values[0].text()) == str(buf[i]):
                        ok = True
                        break
                if ok:
                    cursor.execute("UPDATE cswl1.creating "
                                   "SET idcook = '%s' "
                                   "WHERE idcreating = '%s' " % (values[1],
                                                                 self.Format(values[0].text())))

                else:
                    cursor.execute("INSERT INTO cswl1.creating(idcook)"
                                   "VALUES('%s')" % (values[1]))
            else:
                cursor.execute("INSERT INTO cswl1.creating(idcook)"
                               "VALUES('%s')" % (values[1]))
        if table == 'Блюдо':
            buf = []
            result = self.Select(main_query="SELECT iddish from cswl1.dish")
            for i in range(len(result)):
                buf.append(result[i][0])
            if values[1] is not None:
                if values[0] is not None:
                    ok = False
                    for j in range(len(buf)):
                        if str(values[0].text()) == str(buf[j]):
                            ok = True
                            break
                    if ok:
                        cursor.execute("UPDATE cswl1.dish "
                                       "SET dishname = '%s', "
                                       "idrecipe = '%s', "
                                       "idcreating = '%s', "
                                       "idvisitor = '%s' "
                                       "WHERE iddish = '%s'" % (self.Format(values[1].text()),
                                                                values[2],
                                                                values[3],
                                                                values[4],
                                                                self.Format(values[0].text())))
                    else:
                        cursor.execute("INSERT INTO cswl1.dish(dishname, idrecipe, idcreating, idvisitor)"
                                       "VALUES('%s', '%s', '%s', '%s')" % (self.Format(values[1].text()),
                                                                           values[2],
                                                                           values[3],
                                                                           values[4]))
                else:
                    cursor.execute("INSERT INTO cswl1.dish(dishname, idrecipe, idcreating, idvisitor)"
                                   "VALUES('%s', '%s', '%s', '%s')" % (self.Format(values[1].text()),
                                                                       values[2],
                                                                       values[3],
                                                                       values[4]))
        if table == 'Ингридиент':
            buf = []
            result = self.Select(main_query="SELECT idingridient from cswl1.ingridient")
            for i in range(len(result)):
                buf.append(result[i][0])
            if values[1] is not None:
                if values[0] is not None:
                    ok = False
                    for j in range(len(buf)):
                        if str(values[0].text()) == str(buf[j]):
                            ok = True
                            break
                    if ok:
                        cursor.execute("UPDATE cswl1.ingridient "
                                       "SET ingridientcount = '%s', "
                                       "idrecipe = '%s', "
                                       "idproduct = '%s' "
                                       "WHERE idingridient = '%s'" % (self.Format(values[1].text()),
                                                                      values[2],
                                                                      values[3],
                                                                      self.Format(values[0].text())))
                    else:
                        cursor.execute("INSERT INTO cswl1.ingridient(ingridientcount, idrecipe, idproduct)"
                                       "VALUES('%s', '%s', '%s')" % (self.Format(values[1].text()),
                                                                     values[2],
                                                                     values[3]))
                else:
                    cursor.execute("INSERT INTO cswl1.ingridient(ingridientcount, idrecipe, idproduct)"
                                   "VALUES('%s', '%s', '%s')" % (self.Format(values[1].text()),
                                                                 values[2],
                                                                 values[3]))
        if table == 'Владелец':
            buf = []
            result = self.Select(main_query="SELECT idowner from cswl1.owner")
            for i in range(len(result)):
                buf.append(result[i][0])
            if values[1] is not None and values[2] is not None:
                if values[0] is not None:
                    ok = False
                    for j in range(len(buf)):
                        if str(values[0].text()) == str(buf[j]):
                            ok = True
                            break
                    if ok:
                        cursor.execute("UPDATE cswl1.owner "
                                       "SET ownername = '%s', "
                                       "ownernumber = '%s' "
                                       "WHERE idowner = '%s'" % (self.Format(values[1].text()),
                                                                 self.Format(values[2].text()),
                                                                 self.Format(values[0].text())))
                    else:
                        cursor.execute("INSERT INTO cswl1.owner(ownername, ownernumber)"
                                       "VALUES('%s', '%s')" % (self.Format(values[1].text()),
                                                               self.Format(values[2].text())))
                else:
                    cursor.execute("INSERT INTO cswl1.owner(ownername, ownernumber)"
                                   "VALUES('%s', '%s')" % (self.Format(values[1].text()),
                                                           self.Format(values[2].text())))
        if table == 'Продукт':
            buf = []
            result = self.Select(main_query="SELECT idproduct from cswl1.product")
            for i in range(len(result)):
                buf.append(result[i][0])
            if values[1] is not None and values[3] is not None:
                if values[0] is not None:
                    ok = False
                    for j in range(len(buf)):
                        if str(values[0].text()) == str(buf[j]):
                            ok = True
                            break
                    if ok:
                        cursor.execute("UPDATE cswl1.product "
                                       "SET productname = '%s', "
                                       "idprovider = '%s', "
                                       "productcount = '%s', "
                                       "idcafe = '%s' "
                                       "WHERE idproduct = '%s'" % (self.Format(values[1].text()),
                                                                   values[2],
                                                                   self.Format(values[3].text()),
                                                                   values[4],
                                                                   self.Format(values[0].text())))
                    else:
                        cursor.execute("INSERT INTO cswl1.product(productname, idprovider, productcount, idcafe)"
                                       "VALUES('%s', '%s', '%s', '%s')" % (self.Format(values[1].text()),
                                                                           values[2],
                                                                           self.Format(values[3].text()),
                                                                           values[4]))
                else:
                    cursor.execute("INSERT INTO cswl1.product(productname, idprovider, productcount, idcafe)"
                                   "VALUES('%s', '%s', '%s', '%s')" % (self.Format(values[1].text()),
                                                                       values[2],
                                                                       self.Format(values[3].text()),
                                                                       values[4]))
        if table == 'Поставщик':
            buf = []
            result = self.Select(main_query="SELECT idprovider from cswl1.provider")
            for i in range(len(result)):
                buf.append(result[i][0])
            if values[1] is not None and values[2] is not None:
                if values[0] is not None:
                    ok = False
                    for j in range(len(buf)):
                        if str(values[0].text()) == str(buf[j]):
                            ok = True
                            break
                    if ok:
                        cursor.execute("UPDATE cswl1.provider "
                                       "SET providername = '%s', "
                                       "providernumber = '%s' "
                                       "WHERE idprovider = '%s' " % (self.Format(values[1].text()),
                                                                     self.Format(values[2].text()),
                                                                     self.Format(values[0].text())))
                    else:
                        cursor.execute("INSERT INTO cswl1.provider(providername, providernumber)"
                                       "VALUES('%s', '%s')" % (self.Format(values[1].text()),
                                                               self.Format(values[2].text())))
                else:
                    cursor.execute("INSERT INTO cswl1.provider(providername, providernumber)"
                                   "VALUES('%s', '%s')" % (self.Format(values[1].text()),
                                                           self.Format(values[2].text())))
        if table == 'Рецепт':
            buf = []
            result = self.Select(main_query="SELECT idrecipe from cswl1.recipe")
            for i in range(len(result)):
                buf.append(result[i][0])
            if values[1] is not None:
                if values[0] is not None:
                    ok = False
                    for j in range(len(buf)):
                        if str(values[0].text()) == str(buf[j]):
                            ok = True
                            break
                    if ok:
                        cursor.execute("UPDATE cswl1.recipe "
                                       "SET recipename = '%s' "
                                       "WHERE idrecipe = '%s'" % (self.Format(values[1].text()),
                                                                  self.Format(values[0].text())))
                    else:
                        cursor.execute("INSERT INTO cswl1.recipe(recipename)"
                                       "VALUES('%s')" % (self.Format(values[1].text())))
                else:
                    cursor = self.conn.cursor()
                    cursor.execute("INSERT INTO cswl1.recipe(recipename)"
                                   "VALUES('%s')" % (self.Format(values[1].text())))

        if table == 'Столик':
            buf = []
            result = self.Select(main_query="SELECT idtable from cswl1.table")
            for i in range(len(result)):
                buf.append(result[i][0])
            if values[1] is not None:
                if values[0] is not None:
                    ok = False
                    for j in range(len(buf)):
                        if str(values[0].text()) == str(buf[j]):
                            ok = True
                            break
                    if ok:
                        cursor.execute("UPDATE cswl1.table "
                                       "SET tablellvl = '%s', "
                                       "idwaiter = '%s' "
                                       "WHERE idtable = '%s'" % (self.Format(values[1].text()),
                                                                 values[2],
                                                                 self.Format(values[0].text())))
                    else:
                        cursor.execute("INSERT INTO cswl1.table(tablellvl, idwaiter)"
                                       "VALUES('%s', '%s')" % (self.Format(values[1].text()),
                                                               values[2]))
                else:
                    cursor.execute("INSERT INTO cswl1.table(tablellvl, idwaiter)"
                                   "VALUES('%s', '%s')" % (self.Format(values[1].text()),
                                                           values[2]))
        if table == 'Гость':
            buf = []
            result = self.Select(main_query="SELECT idvisitor from cswl1.visitor")
            for i in range(len(result)):
                buf.append(result[i][0])
            if values[2] is not None:
                if values[0] is not None:
                    ok = False
                    for j in range(len(buf)):
                        if str(values[0].text()) == str(buf[j]):
                            ok = True
                            break
                    if ok:
                        cursor.execute("UPDATE cswl1.visitor "
                                       "SET idtable = '%s', "
                                       "visitorname = '%s' "
                                       "WHERE idvisitor = '%s'" % (values[1],
                                                                   self.Format(values[2].text()),
                                                                   self.Format(values[0].text())))
                    else:
                        cursor.execute("INSERT INTO cswl1.visitor(idtable, visitorname)"
                                       "VALUES('%s', '%s')" % (values[1],
                                                               self.Format(values[2].text())))
                else:
                    cursor.execute("INSERT INTO cswl1.visitor(idtable, visitorname)"
                                   "VALUES('%s', '%s')" % (values[1],
                                                           self.Format(values[2].text())))
        if table == 'Официант':
            buf = []
            result = self.Select(main_query="SELECT idwaiter from cswl1.waiter")
            for i in range(len(result)):
                buf.append(result[i][0])
            if values[1] is not None and values[2] is not None:
                if values[0] is not None:
                    ok = False
                    for j in range(len(buf)):
                        if str(values[0].text()) == str(buf[j]):
                            ok = True
                            break
                    if ok:
                        cursor.execute("UPDATE cswl1.waiter "
                                       "SET waitername = '%s', "
                                       "waiterexp = '%s' "
                                       "WHERE idwaiter = '%s' " % (self.Format(values[1].text()),
                                                                   self.Format(values[2].text()),
                                                                   self.Format(values[0].text())))
                    else:
                        cursor.execute("INSERT INTO cswl1.waiter(waitername, waiterexp)"
                                       "VALUES('%s', '%s')" % (self.Format(values[1].text()),
                                                               self.Format(values[2].text())))
                else:
                    cursor.execute("INSERT INTO cswl1.waiter(waitername, waiterexp)"
                                   "VALUES('%s', '%s')" % (self.Format(values[1].text()),
                                                           self.Format(values[2].text())))
        cursor.execute("COMMIT;")
        cursor.close()

    def Delete(self, table, id):
        cursor = self.conn.cursor()
        if table == 'Повар':
            cursor.execute("DELETE FROM `cswl1`.`cook` WHERE (`idcook` = '" + id + "');")
        if table == 'Заведение':
            cursor.execute("DELETE FROM `cswl1`.`cafe` WHERE (`idcafe` = '" + id + "');")
        if table == 'Готовка':
            cursor.execute("DELETE FROM `cswl1`.`creating` WHERE (`idcreating` = '" + id + "');")
        if table == 'Блюдо':
            cursor.execute("DELETE FROM `cswl1`.`dish` WHERE (`iddish` = '" + id + "');")
        if table == 'Ингридиент':
            cursor.execute("DELETE FROM `cswl1`.`ingridient` WHERE (`idingridient` = '" + id + "');")
        if table == 'Владелец':
            cursor.execute("DELETE FROM `cswl1`.`owner` WHERE (`idowner` = '" + id + "');")
        if table == 'Продукт':
            cursor.execute("DELETE FROM `cswl1`.`product` WHERE (`idproduct` = '" + id + "');")
        if table == 'Поставщик':
            cursor.execute("DELETE FROM `cswl1`.`provider` WHERE (`idprovider` = '" + id + "');")
        if table == 'Рецепт':
            cursor.execute("DELETE FROM `cswl1`.`recipe` WHERE (`idrecipe` = '" + id + "');")
        if table == 'Столик':
            cursor.execute("DELETE FROM `cswl1`.`table` WHERE (`idtable` = '" + id + "');")
        if table == 'Гость':
            cursor.execute("DELETE FROM `cswl1`.`visitor` WHERE (`idvisitor` = '" + id + "');")
        if table == 'Официант':
            cursor.execute("DELETE FROM `cswl1`.`waiter` WHERE (`idwaiter` = '" + id + "');")
        cursor.execute("COMMIT;")
        cursor.close()
