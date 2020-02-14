-- MySQL dump 10.13  Distrib 8.0.18, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: krps_db
-- ------------------------------------------------------
-- Server version	8.0.18

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
-- Table structure for table `attendance`
--

DROP TABLE IF EXISTS `attendance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `attendance` (
  `id_attendance` int(11) NOT NULL AUTO_INCREMENT,
  `attendance` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `id_lessons` int(11) DEFAULT NULL,
  `id_student` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_attendance`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `attendance`
--

LOCK TABLES `attendance` WRITE;
/*!40000 ALTER TABLE `attendance` DISABLE KEYS */;
/*!40000 ALTER TABLE `attendance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `courses`
--

DROP TABLE IF EXISTS `courses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `courses` (
  `id_course` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `year_education` int(4) NOT NULL,
  `university` varchar(45) NOT NULL,
  `group_name` varchar(45) NOT NULL,
  `hours_eucation` int(11) DEFAULT NULL,
  `comment` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_course`),
  KEY `group_id_idx` (`group_name`)
) ENGINE=InnoDB AUTO_INCREMENT=70 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `courses`
--

LOCK TABLES `courses` WRITE;
/*!40000 ALTER TABLE `courses` DISABLE KEYS */;
INSERT INTO `courses` VALUES (1,'Программирование',2015,'ИрГУПС','ПИ.1-16-1',144,'comment1'),(2,'Математика',2015,'ИрГУПС','ПИ.1-16-1',72,'comment2'),(3,'Алгебра и геометрия',2015,'ИрГУПС','ПИ.1-16-1',188,'comment3'),(4,'Экономика',2015,'ИрГУПС','ПИ.1-16-1',36,'comment4'),(5,'Физика',2015,'ИрГУПС','ПИ.1-16-1',18,'comment5'),(62,'Тестирование',2020,'ВАНЯ ЛОХ','ПИС',56,'Курс такое себе конечно');
/*!40000 ALTER TABLE `courses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `estimation`
--

DROP TABLE IF EXISTS `estimation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `estimation` (
  `id_estimation` int(11) NOT NULL AUTO_INCREMENT,
  `estimation` varchar(45) DEFAULT NULL,
  `id_lesson` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `id_student` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_estimation`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estimation`
--

LOCK TABLES `estimation` WRITE;
/*!40000 ALTER TABLE `estimation` DISABLE KEYS */;
/*!40000 ALTER TABLE `estimation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `group`
--

DROP TABLE IF EXISTS `group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `group` (
  `id_group` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `university` varchar(45) NOT NULL,
  `count_student` int(11) NOT NULL,
  PRIMARY KEY (`id_group`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `group`
--

LOCK TABLES `group` WRITE;
/*!40000 ALTER TABLE `group` DISABLE KEYS */;
INSERT INTO `group` VALUES (1,'ПИ.1-16-1','ИрГУПС',20),(2,'ИС-15','ИрГУПС',25),(3,'БИ-15','ИрГУПС',30);
/*!40000 ALTER TABLE `group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lessons`
--

DROP TABLE IF EXISTS `lessons`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lessons` (
  `id_lesson` int(11) NOT NULL AUTO_INCREMENT,
  `id_course` int(11) NOT NULL,
  `type` varchar(45) NOT NULL,
  `date` date NOT NULL,
  `name` varchar(60) NOT NULL,
  PRIMARY KEY (`id_lesson`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lessons`
--

LOCK TABLES `lessons` WRITE;
/*!40000 ALTER TABLE `lessons` DISABLE KEYS */;
INSERT INTO `lessons` VALUES (1,1,'лаб','2015-01-05','Лаб 1'),(2,2,'лек','2015-01-06','Лек 1'),(3,3,'лек','2015-01-07','Лек 1'),(4,4,'лек','2015-01-07','Лек 1'),(5,3,'лек','2015-01-07','Лек 1'),(6,2,'лек','2015-01-07','Лек 1'),(7,1,'лаб','2015-01-07','Лаб 2'),(8,3,'лаб','2015-01-07','Лаб 1'),(9,4,'лаб','2015-01-07','Лаб 1'),(10,2,'лек','2015-01-07','Лек 2'),(12,1,'Практическое занятие','2020-02-14','В мире птиц');
/*!40000 ALTER TABLE `lessons` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prepods`
--

DROP TABLE IF EXISTS `prepods`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `prepods` (
  `id_prepod` int(11) NOT NULL AUTO_INCREMENT,
  `lastname_prepod` varchar(45) NOT NULL,
  `firstname_prepod` varchar(45) NOT NULL,
  `middlename_prepod` varchar(45) NOT NULL,
  `disciplines_prepod` varchar(45) NOT NULL,
  `department_prepod` varchar(45) NOT NULL,
  `login_prepod` varchar(45) NOT NULL,
  `pass_prepod` varchar(45) NOT NULL,
  PRIMARY KEY (`id_prepod`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prepods`
--

LOCK TABLES `prepods` WRITE;
/*!40000 ALTER TABLE `prepods` DISABLE KEYS */;
INSERT INTO `prepods` VALUES (1,'Иванов','Вадим','Петрович','Программирвоание','ИВТ','dfhnj','fdhjrnf'),(2,'Васильев','Анатолий','Владимирович','Физика','Физика','fghjmt','hgfjtyk'),(3,'Савельева','Анна','Сергеевна','Математика','Математика','dsfhnrt','rthrtmnj');
/*!40000 ALTER TABLE `prepods` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `students`
--

DROP TABLE IF EXISTS `students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `students` (
  `id_students` int(11) NOT NULL AUTO_INCREMENT,
  `lastname_stud` varchar(45) NOT NULL,
  `firstname_stud` varchar(45) NOT NULL,
  `middlename_stud` varchar(45) NOT NULL,
  `group_stud` varchar(15) NOT NULL,
  PRIMARY KEY (`id_students`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `students`
--

LOCK TABLES `students` WRITE;
/*!40000 ALTER TABLE `students` DISABLE KEYS */;
INSERT INTO `students` VALUES (1,'Антонов','Владимир','Сергеевич','ПИ.1-16-1'),(2,'Афонина','Светлана','Алексеевна','ПИ.1-16-1'),(3,'Борисова','Ольга','Олеговна','ПИ.1-16-1'),(4,'Бандера','Степан','Андреевич','ПИ.1-16-1'),(5,'Масхадов','Аслан','Алиевич','ПИ.1-16-1'),(6,'Кадыров','Рамзан','Ахматович','ПИ.1-16-1'),(7,'Дениев','Якуб','Ильясович','ИС-15'),(8,'Павлов','Сергей','Борисович','ИС-15'),(9,'Иванова','Дарья','Викторовна','ИС-15'),(10,'Остапов','Борис','Геннадьевич','ИС-15'),(11,'Борисов','Руслан','Николаевич','БИ-15'),(12,'Иванов','Олег','Викторович','БИ-15');
/*!40000 ALTER TABLE `students` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `university`
--

DROP TABLE IF EXISTS `university`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `university` (
  `id_university` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  PRIMARY KEY (`id_university`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `university`
--

LOCK TABLES `university` WRITE;
/*!40000 ALTER TABLE `university` DISABLE KEYS */;
INSERT INTO `university` VALUES (1,'ИрГУПС');
/*!40000 ALTER TABLE `university` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'krps_db'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-02-14 23:25:58
