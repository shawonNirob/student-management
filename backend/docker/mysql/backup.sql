-- MySQL dump 10.13  Distrib 9.2.0, for macos14.7 (arm64)
--
-- Host: localhost    Database: student
-- ------------------------------------------------------
-- Server version	9.2.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('04177bf65867');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `students`
--

DROP TABLE IF EXISTS `students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `students` (
  `id` int NOT NULL AUTO_INCREMENT,
  `student_id` int NOT NULL,
  `university_name` varchar(250) DEFAULT NULL,
  `contact_number` varchar(50) NOT NULL,
  `age` int DEFAULT NULL,
  `gender` varchar(50) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `department` varchar(150) DEFAULT NULL,
  `batch_year` int DEFAULT NULL,
  `level` varchar(50) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `student_id` (`student_id`),
  UNIQUE KEY `contact_number` (`contact_number`),
  UNIQUE KEY `uq_students_email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `students`
--

LOCK TABLES `students` WRITE;
/*!40000 ALTER TABLE `students` DISABLE KEYS */;
INSERT INTO `students` VALUES (1,1001,'RUET','01712345678',21,'Male','Alice Johnson','CSE',2022,'Undergraduate','2025-02-13 04:00:00','2025-02-13 04:00:00',NULL),(2,1002,'RUET','01798765432',22,'Male','Bob Smith','EEE',2023,'Undergraduate','2025-02-13 04:05:00','2025-02-13 04:05:00',NULL),(3,1003,'KUET','01812345678',23,'Female','Charlie Brown','ME',2021,'Graduate','2025-02-13 04:10:00','2025-02-13 04:10:00',NULL),(4,1004,NULL,'01987654321',20,'Male','David Lee','CE',NULL,'Undergraduate','2025-02-13 04:15:00','2025-02-13 04:15:00',NULL),(5,18139,'BUET','0171747',24,'Male','Md Shawon Sarowar','MSE',2018,'Undergraduate','2025-02-15 14:53:35','2025-02-15 14:53:35',NULL),(9,18134,'BUET','0171748',24,'Male','Md Shawon Sarowar','MSE',2018,'Undergraduate','2025-02-15 15:26:11','2025-02-15 15:26:11','shawonnirob16@gmail.com'),(20,18130101,'RUET','01711111111',20,'Male','John Doe','CSE',2017,'Undergraduate','2025-02-15 15:49:09','2025-02-15 15:49:09','jhon@gmail.com'),(21,18130102,'RUET','01722222222',21,'Female','Jane Smith','EEE',2019,'Undergraduate','2025-02-15 15:49:09','2025-02-15 15:49:09','smith@gmail.com'),(22,18130103,'RUET','01733333333',22,'Male','Michael Johnson','ME',2016,'Undergraduate','2025-02-15 15:49:09','2025-02-15 15:49:09','michael@gmail.com'),(23,18130104,'RUET','01744444444',23,'Female','Emily Davis','CE',2018,'Undergraduate','2025-02-15 15:49:09','2025-02-15 15:49:09','davis@gmail.com'),(24,18130105,'RUET','01755555555',24,'Male','David Wilson','ARCH',2020,'Undergraduate','2025-02-15 15:49:09','2025-02-15 15:49:09','david@gmail.com'),(25,18130106,'RUET','01766666666',25,'Female','Sophia Martinez','IPE',2015,'Undergraduate','2025-02-15 15:49:09','2025-02-15 15:49:09','sophia@gmail.com'),(26,18130107,'RUET','01777777777',26,'Male','James Brown','ETE',2017,'Undergraduate','2025-02-15 15:49:09','2025-02-15 15:49:09','james@gmail.com'),(27,18130108,'RUET','01788888888',27,'Female','Olivia Garcia','GCE',2019,'Undergraduate','2025-02-15 15:49:09','2025-02-15 15:49:09','olivia@gmail.com'),(28,18130109,'RUET','01799999999',28,'Male','William Miller','URP',2016,'Undergraduate','2025-02-15 15:49:09','2025-02-15 15:49:09','male@gmail.com'),(29,18130110,'RUET','01700000000',29,'Female','Ava Rodriguez','MTE',2021,'Undergraduate','2025-02-15 15:49:09','2025-02-15 15:49:09','ava@gmail.com');
/*!40000 ALTER TABLE `students` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-02-15 23:27:34
