-- MySQL dump 10.13  Distrib 8.0.23, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: cswl1
-- ------------------------------------------------------
-- Server version	8.0.23

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Dumping routines for database 'cswl1'
--
/*!50003 DROP PROCEDURE IF EXISTS `del` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `del`(in tablename varchar(50), id integer)
BEGIN
    DECLARE com VARCHAR(100);
    SET com = CONCAT('DELETE FROM ', tablename, ' WHERE ', 'id', tablename, ' = ', id);
    select com;
	SET @sql = com;
	PREPARE getCountrySql FROM @sql;
	EXECUTE getCountrySql;
	DEALLOCATE PREPARE getCountrySql;
    COMMIT;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `get_cafe` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `get_cafe`(IN condit VARCHAR(100), numb1 INTEGER, numb2 INTEGER)
BEGIN
	if condit is not Null then
		With CafeTable AS (SELECT *, row_number() OVER (order by idcafe) as RowNumb FROM cswl1.cafe)
        SELECT idcafe, cafename, caferating, ownername FROM CafeTable
        LEFT JOIN cswl1.owner ON cafetable.idowner = owner.idowner 
        where (lower(idcafe) like concat('%', condit, '%')
        or lower(cafename) like concat('%', condit, '%')
        or lower(caferating) like concat('%', condit, '%')
        or lower(ownername) like concat('%', condit, '%'))
        and RowNumb between numb1 and numb2;
    else
		With CafeTable AS (SELECT *, row_number() OVER (order by idcafe) as RowNumb FROM cswl1.cafe)
        SELECT idcafe, cafename, caferating, ownername FROM CafeTable
        LEFT JOIN cswl1.owner ON cafetable.idowner = owner.idowner 
        where RowNumb between numb1 and numb2;
    end if;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `get_cook` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `get_cook`(IN condit VARCHAR(100), numb1 INTEGER, numb2 INTEGER)
BEGIN
	if condit is not null then
		With CookTable AS (SELECT *,row_number() OVER (order by idcook) as RowNumb FROM cswl1.cook)
        SELECT idcook, cookaname, cookexp, cafename FROM CookTable
        LEFT JOIN cswl1.cafe ON cooktable.idcafe = cafe.idcafe 
        WHERE RowNumb between numb1 and numb2
        and 
        (
			lower(idcook) like concat('%', condit, '%') 
            or lower(cookaname) like concat('%', condit, '%') 
            or lower(cookexp) like concat('%', condit, '%') 
            or lower(cafename) like concat('%', condit, '%')
		);
	else
		With CookTable AS (SELECT *,row_number() OVER (order by idcook) as RowNumb FROM cswl1.cook)
        SELECT idcook, cookaname, cookexp, cafename FROM CookTable
        LEFT JOIN cswl1.cafe ON cooktable.idcafe = cafe.idcafe 
        WHERE RowNumb between numb1 and numb2;
	end if;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `get_creating` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `get_creating`(IN condit VARCHAR(100), numb1 INTEGER, numb2 INTEGER)
BEGIN
	if condit is not Null then
		With CreatingTable AS (SELECT *, row_number() OVER (order by idcreating) as RowNumb
        FROM cswl1.creating) 
        SELECT idcreating, creatingtime, cookaname FROM CreatingTable
		LEFT JOIN cswl1.cook ON creatingtable.idcook = cook.idcook  
        WHERE RowNumb between numb1 and numb2
        and 
        (
			lower(idcreating) like concat('%', condit, '%') 
            or lower(creatingtime) like concat('%', condit, '%') 
            or lower(cookaname) like concat('%', condit, '%') 
        );
    else
		With CreatingTable AS (SELECT *, row_number() OVER (order by idcreating) as RowNumb
        FROM cswl1.creating) 
        SELECT idcreating, creatingtime, cookaname FROM CreatingTable
		LEFT JOIN cswl1.cook ON creatingtable.idcook = cook.idcook  
        WHERE RowNumb between numb1 and numb2;
    end if;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `get_dish` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `get_dish`(IN condit VARCHAR(100), numb1 INTEGER, numb2 INTEGER)
BEGIN
	if condit is not Null then
		With DishTable AS (SELECT *, row_number() OVER (order by iddish) as RowNumb FROM cswl1.dish) 
        SELECT iddish, dishname, recipename, creatingtime, visitorname FROM DishTable 
        LEFT JOIN cswl1.recipe ON DishTable.idrecipe = recipe.idrecipe 
        LEFT JOIN cswl1.creating ON DishTable.idcreating = creating.idcreating 
        LEFT JOIN cswl1.visitor ON DishTable.idvisitor = visitor.idvisitor
        WHERE RowNumb between numb1 and numb2
        and 
        (
			lower(iddish) like concat('%', condit, '%') 
            or lower(dishname) like concat('%', condit, '%') 
            or lower(recipename) like concat('%', condit, '%') 
            or lower(creatingtime) like concat('%', condit, '%') 
            or lower(visitorname) like concat('%', condit, '%') 
        );
    else
		With DishTable AS (SELECT *, row_number() OVER (order by iddish) as RowNumb FROM cswl1.dish) 
        SELECT iddish, dishname, recipename, creatingtime, visitorname FROM DishTable 
        LEFT JOIN cswl1.recipe ON DishTable.idrecipe = recipe.idrecipe 
        LEFT JOIN cswl1.creating ON DishTable.idcreating = creating.idcreating 
        LEFT JOIN cswl1.visitor ON DishTable.idvisitor = visitor.idvisitor
        WHERE RowNumb between numb1 and numb2;
    end if;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `get_ingredient` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `get_ingredient`(IN condit VARCHAR(100), numb1 INTEGER, numb2 INTEGER)
BEGIN
	if condit is not Null then
		With IngrTable AS (SELECT *, row_number() OVER (order by idingridient) as RowNumb 
        FROM cswl1.ingridient)
        SELECT idingridient, ingridientcount, recipename, productname FROM IngrTable 
        LEFT JOIN cswl1.recipe ON IngrTable.idrecipe = recipe.idrecipe 
        LEFT JOIN cswl1.product ON IngrTable.idproduct = product.idproduct 
        WHERE RowNumb between numb1 and numb2
        and 
        (
			lower(idingridient) like concat('%', condit, '%') 
            or lower(ingridientcount) like concat('%', condit, '%') 
            or lower(recipename) like concat('%', condit, '%') 
            or lower(productname) like concat('%', condit, '%') 
        );
    else
		With IngrTable AS (SELECT *, row_number() OVER (order by idingridient) as RowNumb 
        FROM cswl1.ingridient)
        SELECT idingridient, ingridientcount, recipename, productname FROM IngrTable 
        LEFT JOIN cswl1.recipe ON IngrTable.idrecipe = recipe.idrecipe 
        LEFT JOIN cswl1.product ON IngrTable.idproduct = product.idproduct 
        WHERE RowNumb between numb1 and numb2;
    end if;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `get_owner` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `get_owner`(IN condit VARCHAR(100), numb1 INTEGER, numb2 INTEGER)
BEGIN
	IF condit is not NULL then
      With OwnerTable AS (SELECT *, row_number() OVER (order by idowner) as RowNumb FROM cswl1.owner) 
		SELECT idowner, ownername, ownernumber FROM OwnerTable 
        WHERE (lower(idowner) like concat('%', condit, '%') or  lower(ownername) like concat('%', condit, '%')  or lower(ownernumber) like concat('%', condit, '%')) 
        AND RowNumb between numb1 and numb2;
	ELSE
      With OwnerTable AS (SELECT *, row_number() OVER (order by idowner) as RowNumb FROM cswl1.owner) 
		SELECT idowner, ownername, ownernumber FROM OwnerTable
        where RowNumb between numb1 and numb2; 
    END if;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `get_product` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `get_product`(IN condit VARCHAR(100), numb1 INTEGER, numb2 INTEGER)
BEGIN
	if condit is not Null then
		With ProductTable AS (SELECT *, row_number() OVER (order by idproduct) as RowNumb
        FROM cswl1.Product)
        SELECT idproduct, productname, providername, productcount, cafename FROM ProductTable 
        LEFT JOIN cswl1.provider ON ProductTable.idprovider = provider.idprovider 
        LEFT JOIN cswl1.cafe ON ProductTable.idcafe = cafe.idcafe 
        WHERE RowNumb between numb1 and numb2
        and 
        (
			lower(idproduct) like concat('%', condit, '%') 
            or lower(productname) like concat('%', condit, '%') 
            or lower(providername) like concat('%', condit, '%') 
            or lower(productcount) like concat('%', condit, '%') 
            or lower(cafename) like concat('%', condit, '%') 
        );
    else
		With ProductTable AS (SELECT *, row_number() OVER (order by idproduct) as RowNumb
        FROM cswl1.Product)
        SELECT idproduct, productname, providername, productcount, cafename FROM ProductTable 
        LEFT JOIN cswl1.provider ON ProductTable.idprovider = provider.idprovider 
        LEFT JOIN cswl1.cafe ON ProductTable.idcafe = cafe.idcafe 
        WHERE RowNumb between numb1 and numb2;
    end if;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `get_provider` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `get_provider`(IN condit VARCHAR(100), numb1 INTEGER, numb2 INTEGER)
BEGIN
	IF condit is not NULL then
      With ProviderTable AS (SELECT *, row_number() OVER (order by idprovider) as RowNumb FROM cswl1.Provider)
		SELECT idprovider, providername, providernumber FROM ProviderTable 
      WHERE lower(idprovider) like concat('%', condit, '%') or  lower(providername) like concat('%', condit, '%')  or lower(providernumber) like concat('%', condit, '%') 
      AND RowNumb between numb1 and numb2;
	ELSE
       With ProviderTable AS (SELECT *, row_number() OVER (order by idprovider) as RowNumb FROM cswl1.Provider)
		SELECT idprovider, providername, providernumber FROM ProviderTable 
      WHERE RowNumb between numb1 and numb2;
    END if;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `get_recipe` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `get_recipe`(IN condit VARCHAR(100), numb1 INTEGER, numb2 INTEGER)
BEGIN
	if condit is not Null then
		With RecipeTable AS (SELECT *, row_number() OVER (order by idrecipe) as RowNumb
        FROM cswl1.recipe)
        SELECT idrecipe, recipename FROM RecipeTable 
        WHERE RowNumb between numb1 and numb2
        and 
        (
			lower(idrecipe) like concat('%', condit, '%') 
            or lower(recipename) like concat('%', condit, '%') 
        );
    else
		With RecipeTable AS (SELECT *, row_number() OVER (order by idrecipe) as RowNumb
        FROM cswl1.recipe)
        SELECT idrecipe, recipename FROM RecipeTable 
        WHERE RowNumb between numb1 and numb2;
    end if;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `get_table` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `get_table`(IN condit VARCHAR(100), numb1 INTEGER, numb2 INTEGER)
BEGIN
	if condit is not Null then
		With TableTable AS (SELECT *, row_number() OVER (order by idtable) 
        as RowNumb FROM cswl1.table)
        SELECT idtable, tablellvl, waitername FROM TableTable 
        LEFT JOIN cswl1.waiter ON TableTable.idwaiter = waiter.idwaiter
        WHERE RowNumb between numb1 and numb2
        and 
        (
			lower(idtable) like concat('%', condit, '%') 
            or lower(tablellvl) like concat('%', condit, '%') 
            or lower(waitername) like concat('%', condit, '%') 
        );
    else
		With TableTable AS (SELECT *, row_number() OVER (order by idtable) 
        as RowNumb FROM cswl1.table)
        SELECT idtable, tablellvl, waitername FROM TableTable 
        LEFT JOIN cswl1.waiter ON TableTable.idwaiter = waiter.idwaiter
        WHERE RowNumb between numb1 and numb2;
    end if;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `get_visitor` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `get_visitor`(IN condit VARCHAR(100), numb1 INTEGER, numb2 INTEGER)
BEGIN
	if condit is not Null then
		With VisitorTable AS (SELECT *, row_number() OVER (order by idvisitor) as RowNumb 
        FROM cswl1.visitor) SELECT idvisitor, visitorname, idtable FROM VisitorTable  
        WHERE RowNumb between numb1 and numb2
        and 
        (
			lower(idvisitor) like concat('%', condit, '%') 
            or lower(visitorname) like concat('%', condit, '%') 
            or lower(idtable) like concat('%', condit, '%') 
        );
    else
		With VisitorTable AS (SELECT *, row_number() OVER (order by idvisitor) as RowNumb 
        FROM cswl1.visitor) SELECT idvisitor, visitorname, idtable FROM VisitorTable  
        WHERE RowNumb between numb1 and numb2;
    end if;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `get_waiter` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `get_waiter`(IN condit VARCHAR(100), numb1 INTEGER, numb2 INTEGER)
BEGIN
	if condit is not Null then
		With WaiterTable AS (SELECT *, row_number() OVER (order by idwaiter) as RowNumb
        FROM cswl1.waiter)
        SELECT idwaiter, waitername, waiterexp FROM WaiterTable 
        WHERE RowNumb between numb1 and numb2
        and 
        (
			lower(idwaiter) like concat('%', condit, '%') 
            or lower(waitername) like concat('%', condit, '%') 
            or lower(waiterexp) like concat('%', condit, '%') 
        );
    else
		With WaiterTable AS (SELECT *, row_number() OVER (order by idwaiter) as RowNumb
        FROM cswl1.waiter)
        SELECT idwaiter, waitername, waiterexp FROM WaiterTable 
        WHERE RowNumb between numb1 and numb2;
    end if;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `merge_cafe` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `merge_cafe`(in id INTEGER, cafname VARCHAR(45), rating INTEGER, idown INTEGER)
BEGIN
	DECLARE col INTEGER;
    SET SQL_SAFE_UPDATES = 0;
    SELECT Count(*) INTO col FROM cafe where idcafe = id;
    if col != 0 then
		UPDATE cafe
        SET cafename = cafname,
        caferating = rating,
        idowner = idown
        WHERE idcafe = id;
    else
      INSERT INTO cafe(cafename, caferating, idowner)VALUES(cafname, rating, idown);
    end if;
    commit;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `merge_cook` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `merge_cook`(in id INTEGER, cname VARCHAR(45), idcaf INTEGER, exp INTEGER)
BEGIN
	DECLARE col INTEGER;
    SET SQL_SAFE_UPDATES = 0;
    SELECT Count(*) INTO col FROM cook where idcook = id;
    if col != 0 then
		UPDATE cook
        SET cookaname = cname,
        cookexp = exp,
        idcafe = idcaf
        WHERE idcook = id;
    else
      INSERT INTO cook(cookaname, cookexp, idcafe)VALUES(cname, exp, idcaf);
    end if;
    commit;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `merge_creating` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `merge_creating`(in id INTEGER, idc INTEGER)
BEGIN
	DECLARE col INTEGER;
    SET SQL_SAFE_UPDATES = 0;
    SELECT Count(*) INTO col FROM creating where idcreating = id;
    if col != 0 then
		UPDATE creating
        SET creatingtime = now(),
        idcook = idc
        WHERE idcreating = id;
    else
      INSERT INTO creating(idcook)VALUES(idc);
    end if;
    commit;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `merge_dish` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `merge_dish`(in id INTEGER, dname VARCHAR(45), idrec INTEGER, idcr INTEGER, idvis INTEGER)
BEGIN
	DECLARE col INTEGER;
    SET SQL_SAFE_UPDATES = 0;
    SELECT Count(*) INTO col FROM dish where iddish = id;
    if col != 0 then
		UPDATE dish
        SET dishname = dname,
        idrecipe = idrec,
        idcreating = idcr,
        idvisitor = idvis
        WHERE iddish = id;
    else
      INSERT INTO dish(dishname, idrecipe, idcreating, idvisitor)VALUES(dname, idrec, idcr, idvis);
    end if;
    commit;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `merge_ingridient` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `merge_ingridient`(in id INTEGER, icount INTEGER, idrec INTEGER, idprod INTEGER)
BEGIN
	DECLARE col INTEGER;
    SET SQL_SAFE_UPDATES = 0;
    SELECT Count(*) INTO col FROM ingridient where idingridient = id;
    if col != 0 then
		UPDATE ingridient
        SET ingridientcount = icount,
        idrecipe = idrec,
        idproduct = idprod
        WHERE idingridient = id;
    else
      INSERT INTO ingridient(ingridientcount, idrecipe, idproduct)VALUES(icount, idrec, idprod);
    end if;
    commit;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `merge_owner` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `merge_owner`(in id INTEGER, ownname VARCHAR(45), ownumber VARCHAR(45))
BEGIN
	DECLARE col INTEGER;
    SET SQL_SAFE_UPDATES = 0;
    SELECT Count(*) INTO col FROM owner where idowner = id;
    if col != 0 then
		UPDATE owner
        SET ownername = ownname,
        ownernumber = ownumber
        WHERE idowner = id;
    else
      INSERT INTO owner(ownername, ownernumber)VALUES(ownname, ownumber);
    end if;
    commit;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `merge_product` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `merge_product`(in id INTEGER, prname VARCHAR(45), idprov INTEGER, pcount INTEGER, idcaf INTEGER)
BEGIN
	DECLARE col INTEGER;
    SET SQL_SAFE_UPDATES = 0;
    SELECT Count(*) INTO col FROM product where idproduct = id;
    if col != 0 then
		UPDATE product
        SET productname = prname,
        idprovider = idprov,
        productcount = pcount,
        idcafe = idcaf
        WHERE idproduct = id;
    else
      INSERT INTO product(productname, idprovider, productcount, idcafe)VALUES(prname, idprov, pcount, idcaf);
    end if;
    commit;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `merge_provider` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `merge_provider`(in id INTEGER, pname VARCHAR(45), pnumber VARCHAR(15))
BEGIN
	DECLARE col INTEGER;
    SET SQL_SAFE_UPDATES = 0;
    SELECT Count(*) INTO col FROM provider where idprovider = id;
    if col != 0 then
		UPDATE provider
        SET providername = pname,
        providernumber = pnumber
        WHERE idprovider = id;
    else
      INSERT INTO provider(providername, providernumber)VALUES(pname, pnumber);
    end if;
    commit;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `merge_recipe` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `merge_recipe`(in id INTEGER, rname VARCHAR(45))
BEGIN
	DECLARE col INTEGER;
    SET SQL_SAFE_UPDATES = 0;
    SELECT Count(*) INTO col FROM recipe where idrecipe = id;
    if col != 0 then
		UPDATE recipe
        SET recipename = rname
        WHERE idrecipe = id;
    else
      INSERT INTO recipe(recipename)VALUES(rname);
    end if;
    commit;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `merge_table` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `merge_table`(in id INTEGER, tlvl VARCHAR(10), idw INTEGER)
BEGIN
	DECLARE col INTEGER;
    SET SQL_SAFE_UPDATES = 0;
    SELECT Count(*) INTO col FROM cswl1.table where idtable = id;
    if col != 0 then
		UPDATE cswl1.table
        SET tablellvl = tlvl,
        idwaiter = idw
        WHERE idtable = id;
    else
      INSERT INTO cswl1.table(tablellvl, idwaiter)VALUES(tlvl, idw);
    end if;
    commit;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `merge_visitor` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `merge_visitor`(in id INTEGER, idtab INTEGER, visname VARCHAR(45))
BEGIN
	DECLARE col INTEGER;
    SET SQL_SAFE_UPDATES = 0;
    SELECT Count(*) INTO col FROM visitor where idvisitor = id;
    if col != 0 then
		UPDATE visitor
        SET visitorname = visname,
        idtable = idtab
        WHERE idvisitor = id;
    else
      INSERT INTO visitor(visitorname, idtable)VALUES(visname, idtab);
    end if;
    commit;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `merge_waiter` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `merge_waiter`(in id integer, wname VARCHAR(45), expe INTEGER)
BEGIN
	DECLARE col INTEGER;
    SET SQL_SAFE_UPDATES = 0;
    SELECT Count(*) INTO col FROM waiter where idwaiter = id;
    if col != 0 then
		UPDATE waiter
        SET waitername = wname,
        waiterexp = expe
        WHERE idwaiter = id;
    else
      INSERT INTO waiter(waitername, waiterexp)VALUES(wname, expe);
    end if;
    commit;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-06-11  8:58:45
