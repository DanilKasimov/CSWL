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
-- Table structure for table `cafe`
--

DROP TABLE IF EXISTS `cafe`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cafe` (
  `idcafe` int NOT NULL AUTO_INCREMENT,
  `cafename` varchar(45) NOT NULL,
  `caferating` int NOT NULL,
  `idowner` int NOT NULL,
  PRIMARY KEY (`idcafe`),
  KEY `idowner_idx` (`idowner`),
  CONSTRAINT `idowner` FOREIGN KEY (`idowner`) REFERENCES `owner` (`idowner`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cafe`
--

LOCK TABLES `cafe` WRITE;
/*!40000 ALTER TABLE `cafe` DISABLE KEYS */;
INSERT INTO `cafe` VALUES (1,'SratBucks',3,1),(2,'KFC',5,2),(3,'McDonalds',5,3),(4,'Рожки да ножки',4,2),(5,'HentaCafe',10,1),(6,'Хороший пират',3,3),(7,'Лесная сказка',5,4);
/*!40000 ALTER TABLE `cafe` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cook`
--

DROP TABLE IF EXISTS `cook`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cook` (
  `idcook` int NOT NULL AUTO_INCREMENT,
  `cookaname` varchar(45) NOT NULL,
  `cookexp` int NOT NULL,
  `idcafe` int NOT NULL,
  PRIMARY KEY (`idcook`),
  KEY `idcafe_idx` (`idcafe`) /*!80000 INVISIBLE */,
  CONSTRAINT `idcafe` FOREIGN KEY (`idcafe`) REFERENCES `cafe` (`idcafe`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cook`
--

LOCK TABLES `cook` WRITE;
/*!40000 ALTER TABLE `cook` DISABLE KEYS */;
INSERT INTO `cook` VALUES (1,'Колянов Колян Колянович',11,4),(2,'Гордон Рамзи Джон',15,2),(3,'Славный Друже Обломов',6,1),(4,'Икотов Том Джинджигавович',5,3),(5,'Котов Кот Котович',3,2),(6,'Пренков Александр Радионович',13,2),(7,'Ползуков Паук Жукович',6,2),(8,'Привкин Привик Андреевич',3,2),(10,'Витковсикй Павел Генадьевич',4,2),(12,'Иванов Иван Иванович',11,3),(19,'Юкихира Сома Джойчирович',8,5);
/*!40000 ALTER TABLE `cook` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `creating`
--

DROP TABLE IF EXISTS `creating`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `creating` (
  `idcreating` int NOT NULL AUTO_INCREMENT,
  `creatingtime` datetime DEFAULT CURRENT_TIMESTAMP,
  `idcook` int NOT NULL,
  PRIMARY KEY (`idcreating`),
  KEY `idcook_idx` (`idcook`),
  CONSTRAINT `idcook` FOREIGN KEY (`idcook`) REFERENCES `cook` (`idcook`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `creating`
--

LOCK TABLES `creating` WRITE;
/*!40000 ALTER TABLE `creating` DISABLE KEYS */;
INSERT INTO `creating` VALUES (1,'2021-02-26 15:12:13',1),(2,'2021-03-04 18:18:50',3),(3,'2021-03-04 18:19:35',2),(4,'2021-05-03 19:34:43',4),(5,'2021-05-03 19:39:25',7),(6,'2021-05-28 19:40:00',19);
/*!40000 ALTER TABLE `creating` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dish`
--

DROP TABLE IF EXISTS `dish`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dish` (
  `iddish` int NOT NULL AUTO_INCREMENT,
  `dishname` varchar(45) NOT NULL,
  `idrecipe` int NOT NULL,
  `idcreating` int NOT NULL,
  `idvisitor` int NOT NULL,
  PRIMARY KEY (`iddish`),
  KEY `idvisitor_idx` (`idvisitor`),
  KEY `idcreating_idx` (`idcreating`),
  KEY `idrecipedish_idx` (`idrecipe`),
  CONSTRAINT `idcreating` FOREIGN KEY (`idcreating`) REFERENCES `creating` (`idcreating`),
  CONSTRAINT `idrecipedish` FOREIGN KEY (`idrecipe`) REFERENCES `recipe` (`idrecipe`),
  CONSTRAINT `idvisitor` FOREIGN KEY (`idvisitor`) REFERENCES `visitor` (`idvisitor`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dish`
--

LOCK TABLES `dish` WRITE;
/*!40000 ALTER TABLE `dish` DISABLE KEYS */;
INSERT INTO `dish` VALUES (2,'БигМак',2,2,1),(3,'Кровавая Мэри',4,1,3),(4,'Эсспрессо Вкусный',1,4,3),(5,'Пицца с грибами',3,5,2),(6,'Пюре со сливочным маслом',5,6,4);
/*!40000 ALTER TABLE `dish` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `files`
--

DROP TABLE IF EXISTS `files`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `files` (
  `FileName` varchar(100) DEFAULT NULL,
  `FileHash` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `files`
--

LOCK TABLES `files` WRITE;
/*!40000 ALTER TABLE `files` DISABLE KEYS */;
/*!40000 ALTER TABLE `files` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ingridient`
--

DROP TABLE IF EXISTS `ingridient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ingridient` (
  `idingridient` int NOT NULL AUTO_INCREMENT,
  `ingridientcount` int NOT NULL,
  `idrecipe` int NOT NULL,
  `idproduct` int NOT NULL,
  PRIMARY KEY (`idingridient`),
  KEY `idrecipe_idx` (`idrecipe`),
  KEY `idproduct_idx` (`idproduct`),
  CONSTRAINT `idproduct` FOREIGN KEY (`idproduct`) REFERENCES `product` (`idproduct`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `idrecipe` FOREIGN KEY (`idrecipe`) REFERENCES `recipe` (`idrecipe`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ingridient`
--

LOCK TABLES `ingridient` WRITE;
/*!40000 ALTER TABLE `ingridient` DISABLE KEYS */;
INSERT INTO `ingridient` VALUES (1,2,2,2),(2,2,3,4),(3,4,1,1),(4,3,2,3),(5,12,2,2),(6,13,3,4);
/*!40000 ALTER TABLE `ingridient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `owner`
--

DROP TABLE IF EXISTS `owner`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `owner` (
  `idowner` int NOT NULL AUTO_INCREMENT,
  `ownername` varchar(45) NOT NULL,
  `ownernumber` varchar(45) NOT NULL,
  PRIMARY KEY (`idowner`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `owner`
--

LOCK TABLES `owner` WRITE;
/*!40000 ALTER TABLE `owner` DISABLE KEYS */;
INSERT INTO `owner` VALUES (1,'Семнов Семён Семнович','89235924923'),(2,'Ахмаров Артур Азатович','89763452342'),(3,'Перетягин Илья Олегович','89028494738'),(4,'Кац Максимэль Актимелевич','89323949234'),(5,'Горшенёв Михаил Юрьевич','89234953943');
/*!40000 ALTER TABLE `owner` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product` (
  `idproduct` int NOT NULL AUTO_INCREMENT,
  `productname` varchar(45) NOT NULL,
  `idprovider` int NOT NULL,
  `productcount` int NOT NULL,
  `idcafe` int NOT NULL,
  PRIMARY KEY (`idproduct`),
  KEY `idprovider_idx` (`idprovider`),
  KEY `idprodcafe_idx` (`idcafe`),
  CONSTRAINT `idprodcafe` FOREIGN KEY (`idcafe`) REFERENCES `cafe` (`idcafe`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `idprovider` FOREIGN KEY (`idprovider`) REFERENCES `provider` (`idprovider`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES (1,'Кофе Молотый',1,50,1),(2,'Фарш Говяжий',2,100,3),(3,'Булочки',1,67,3),(4,'Помидоры',4,45,2),(5,'Колбаса',2,213,2),(6,'Курочка',4,42,2);
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `provider`
--

DROP TABLE IF EXISTS `provider`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `provider` (
  `idprovider` int NOT NULL AUTO_INCREMENT,
  `providername` varchar(45) NOT NULL,
  `providernumber` varchar(15) NOT NULL,
  PRIMARY KEY (`idprovider`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `provider`
--

LOCK TABLES `provider` WRITE;
/*!40000 ALTER TABLE `provider` DISABLE KEYS */;
INSERT INTO `provider` VALUES (1,'Иванов Иван Иванович','89012427548'),(2,'Петров Пётр Петрович','89035940392'),(4,'Каждый день','89231940265'),(5,'Пятёрочка','89324594204');
/*!40000 ALTER TABLE `provider` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recipe`
--

DROP TABLE IF EXISTS `recipe`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `recipe` (
  `idrecipe` int NOT NULL AUTO_INCREMENT,
  `recipename` varchar(45) NOT NULL,
  PRIMARY KEY (`idrecipe`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recipe`
--

LOCK TABLES `recipe` WRITE;
/*!40000 ALTER TABLE `recipe` DISABLE KEYS */;
INSERT INTO `recipe` VALUES (1,'Эспрессо'),(2,'Бургер'),(3,'Пицца'),(4,'Коктейль'),(5,'Пюрешка'),(6,'Мясо жаренное');
/*!40000 ALTER TABLE `recipe` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `table`
--

DROP TABLE IF EXISTS `table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `table` (
  `idtable` int NOT NULL AUTO_INCREMENT,
  `tablellvl` varchar(10) NOT NULL,
  `idwaiter` int NOT NULL,
  PRIMARY KEY (`idtable`),
  KEY `idwaiter_idx` (`idwaiter`),
  CONSTRAINT `idwaiter` FOREIGN KEY (`idwaiter`) REFERENCES `waiter` (`idwaiter`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `table`
--

LOCK TABLES `table` WRITE;
/*!40000 ALTER TABLE `table` DISABLE KEYS */;
INSERT INTO `table` VALUES (1,'VIP',1),(2,'ECONOM',3),(3,'ECONOM',2),(4,'VIP',4),(5,'VIP',3);
/*!40000 ALTER TABLE `table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `visitor`
--

DROP TABLE IF EXISTS `visitor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `visitor` (
  `idvisitor` int NOT NULL AUTO_INCREMENT,
  `visitorname` varchar(45) NOT NULL,
  `idtable` int NOT NULL,
  PRIMARY KEY (`idvisitor`),
  KEY `idtable_idx` (`idtable`),
  CONSTRAINT `idtable` FOREIGN KEY (`idtable`) REFERENCES `table` (`idtable`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `visitor`
--

LOCK TABLES `visitor` WRITE;
/*!40000 ALTER TABLE `visitor` DISABLE KEYS */;
INSERT INTO `visitor` VALUES (1,'Марсов Марс Марселевич',4),(2,'Касимов Данил Василевич',3),(3,'Зверев Никита Сергеевич',2),(4,'Елисеева Виталина Анатольевна',3),(5,'Двачевская Алиса Фёдоровна',5);
/*!40000 ALTER TABLE `visitor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `waiter`
--

DROP TABLE IF EXISTS `waiter`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `waiter` (
  `idwaiter` int NOT NULL AUTO_INCREMENT,
  `waitername` varchar(45) NOT NULL,
  `waiterexp` int NOT NULL,
  PRIMARY KEY (`idwaiter`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `waiter`
--

LOCK TABLES `waiter` WRITE;
/*!40000 ALTER TABLE `waiter` DISABLE KEYS */;
INSERT INTO `waiter` VALUES (1,'Валерьева Валерия Валерьевна',2),(2,'Олегов Олег Олегович',4),(3,'Соков Сока Катарович',6),(4,'Михаил Юрьевич ГоршенёвЖив',12),(5,'Еотова Катя Андреевна',3);
/*!40000 ALTER TABLE `waiter` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-06-06 13:54:41
