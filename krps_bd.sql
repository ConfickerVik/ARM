-- MySQL dump 10.13  Distrib 8.0.18, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: krps
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
-- Table structure for table `students`
--

DROP TABLE IF EXISTS `students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `students` (
  `s_id` int(11) NOT NULL AUTO_INCREMENT,
  `lastname_stud` varchar(30) DEFAULT NULL,
  `firstname_stud` varchar(30) DEFAULT NULL,
  `middlename_stud` varchar(30) DEFAULT NULL,
  `attend_stud` varchar(1) DEFAULT NULL,
  `group_stud` varchar(10) DEFAULT NULL,
  `val_stud` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`s_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `students`
--

LOCK TABLES `students` WRITE;
/*!40000 ALTER TABLE `students` DISABLE KEYS */;
/*!40000 ALTER TABLE `students` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `training_session`
--

DROP TABLE IF EXISTS `training_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `training_session` (
  `ts_id` int(11) NOT NULL AUTO_INCREMENT,
  `type_ts` varchar(1) DEFAULT NULL,
  `date_ts` date DEFAULT NULL,
  `value_ts` int(11) DEFAULT NULL,
  `attend_stud` varchar(1) DEFAULT NULL,
  `disciplines_ts` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`ts_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `training_session`
--

LOCK TABLES `training_session` WRITE;
/*!40000 ALTER TABLE `training_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `training_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_prepod`
--

DROP TABLE IF EXISTS `users_prepod`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_prepod` (
  `p_id` int(11) NOT NULL AUTO_INCREMENT,
  `lastname_prepod` varchar(30) DEFAULT NULL,
  `firstname_prepod` varchar(30) DEFAULT NULL,
  `middlename_prepod` varchar(30) DEFAULT NULL,
  `department_prepod` varchar(30) DEFAULT NULL,
  `disciplines_prepod` varchar(30) DEFAULT NULL,
  `login_prepod` varchar(20) DEFAULT NULL,
  `pass_prepod` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`p_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_prepod`
--

LOCK TABLES `users_prepod` WRITE;
/*!40000 ALTER TABLE `users_prepod` DISABLE KEYS */;
INSERT INTO `users_prepod` VALUES (1,'kurg','ol','vik','kov','krps','olgalog','olgapass');
/*!40000 ALTER TABLE `users_prepod` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'krps'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-01-24 23:45:45
