CREATE DATABASE  IF NOT EXISTS `restaurants` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `restaurants`;
-- MySQL dump 10.13  Distrib 5.7.12, for Win64 (x86_64)
--
-- Host: localhost    Database: restaurants
-- ------------------------------------------------------
-- Server version	5.7.16-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `restaurants`
--

DROP TABLE IF EXISTS `restaurants`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `restaurants` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `location` varchar(45) DEFAULT NULL,
  `rating` int(1) DEFAULT NULL,
  `cuisine` varchar(45) DEFAULT NULL,
  `price` varchar(45) DEFAULT NULL,
  `distance` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=134 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `restaurants`
--

LOCK TABLES `restaurants` WRITE;
/*!40000 ALTER TABLE `restaurants` DISABLE KEYS */;
INSERT INTO `restaurants` VALUES (1,'Jurassic Pork','Adams',2,'Italian','CHEAP','NEAR'),(4,'Donut District','Santa Monica',4,'Chinese','AVERAGE','FAR'),(5,'Howzit Go Inn','Marina Del Rey',1,'Mexican','CHEAP','FAR'),(6,'Dolly Random','Beverly Hills',5,'Indian','CHEAP','AVERAGE'),(7,'Jump Jack','USC',1,'Indian','EXPENSIVE','NEAR'),(8,'Jute Box','Adams',5,'Italian','AVERAGE','NEAR'),(11,'Humburger','Marina Del Rey',3,'Chinese','AVERAGE','FAR'),(12,'Brunchilli','USC',3,'Mexican','EXPENSIVE','NEAR'),(13,'Donut Babe','Adams',2,'Korean','EXPENSIVE','NEAR'),(14,'Housedown','Santa Monica',2,'Indian','AVERAGE','FAR'),(15,'Aquafire','Marina Del Rey',3,'Italian','AVERAGE','FAR'),(18,'Doctor Coffee','Downtown',1,'Chinese','AVERAGE','AVERAGE'),(19,'Aquacine','Adams',1,'Mexican','AVERAGE','NEAR'),(20,'Antimatter','Santa Monica',1,'Korean','CHEAP','FAR'),(21,'Buddha Bait','Beverly Hills',1,'Indian','AVERAGE','AVERAGE'),(22,'Jumpstart','Santa Monica',4,'Italian','CHEAP','FAR'),(25,'Jupitor Place','Adams',4,'Chinese','AVERAGE','NEAR'),(26,'Django’s','Santa Monica',3,'Korean','CHEAP','FAR'),(27,'Buddha Bite','Downtown',3,'Korean','AVERAGE','AVERAGE'),(28,'Guru Cricket','Adams',5,'Korean','CHEAP','NEAR'),(29,'Jupiter Trolley','Marina Del Rey',2,'Italian','CHEAP','FAR'),(32,'Domina','Beverly Hills',5,'Chinese','CHEAP','AVERAGE'),(33,'House of Chedder','USC',2,'Mexican','CHEAP','NEAR'),(34,'Mantro','Marina Del Rey',4,'Korean','AVERAGE','FAR'),(35,'Dote','USC',4,'Indian','CHEAP','NEAR'),(36,'Jumpstack','USC',3,'Italian','AVERAGE','NEAR'),(39,'Guru Planet','Santa Monica',5,'Chinese','AVERAGE','FAR'),(40,'Masquerade','Downtown',4,'Mexican','AVERAGE','AVERAGE'),(41,'Dolly Random','Beverly Hills',5,'Korean','EXPENSIVE','AVERAGE'),(43,'Guru Cricket','Adams',5,'Indian','AVERAGE','NEAR'),(44,'Django’s','Santa Monica',3,'Italian','AVERAGE','FAR'),(47,'Marvane','Downtown',3,'Chinese','EXPENSIVE','AVERAGE'),(48,'Antimatter','Santa Monica',1,'Mexican','CHEAP','FAR'),(49,'Buddha Bite','Downtown',3,'Indian','EXPENSIVE','AVERAGE'),(51,'Doctor Coffee','Downtown',1,'Mexican','CHEAP','AVERAGE'),(52,'Guru','Beverly Hills',2,'Mexican','CHEAP','AVERAGE'),(53,'Buddha Bait','Beverly Hills',1,'Korean','CHEAP','AVERAGE'),(54,'Jump Jack','USC',1,'Mexican','AVERAGE','NEAR'),(55,'Domina','Beverly Hills',5,'Italian','AVERAGE','AVERAGE'),(58,'House of Chedder','USC',2,'Chinese','EXPENSIVE','NEAR'),(59,'Aquacine','Adams',1,'Korean','CHEAP','NEAR'),(60,'Jupiter Trolley','Marina Del Rey',2,'Korean','AVERAGE','FAR'),(61,'Jumpstart','Santa Monica',4,'Indian','AVERAGE','FAR'),(62,'Mantro','Marina Del Rey',4,'Italian','AVERAGE','FAR'),(65,'Humburger','Marina Del Rey',3,'Mexican','CHEAP','FAR'),(66,'Maple Thor','Beverly Hills',3,'Mexican','EXPENSIVE','AVERAGE'),(67,'Brunchilli','USC',3,'Korean','AVERAGE','NEAR'),(68,'Jute Box','Adams',5,'Indian','CHEAP','NEAR'),(69,'Dote','USC',4,'Italian','AVERAGE','NEAR'),(72,'Donut District','Santa Monica',4,'Italian','CHEAP','FAR'),(73,'Martha’s Rump Roast','Marina Del Rey',5,'Mexican','AVERAGE','FAR'),(74,'Howzit Go Inn','Marina Del Rey',1,'Korean','EXPENSIVE','FAR'),(76,'Guru Planet','Santa Monica',5,'Indian','CHEAP','FAR'),(77,'Masquerade','Downtown',4,'Italian','CHEAP','AVERAGE'),(80,'Guru Cricket','Adams',5,'Chinese','AVERAGE','NEAR'),(81,'Django’s','Santa Monica',3,'Mexican','EXPENSIVE','FAR'),(82,'Aquafire','Marina Del Rey',3,'Korean','EXPENSIVE','FAR'),(84,'Marvane','Downtown',3,'Indian','CHEAP','AVERAGE'),(85,'Antimatter','Santa Monica',1,'Indian','AVERAGE','FAR'),(86,'Buddha Bite','Downtown',3,'Mexican','CHEAP','AVERAGE'),(87,'Jurassic Pork','Adams',2,'Indian','EXPENSIVE','NEAR'),(88,'Doctor Coffee','Downtown',1,'Italian','CHEAP','AVERAGE'),(91,'Jump Jack','USC',1,'Chinese','CHEAP','NEAR'),(92,'Domina','Beverly Hills',5,'Mexican','AVERAGE','AVERAGE'),(93,'Jupitor Place','Adams',4,'Korean','AVERAGE','NEAR'),(94,'Anocha','USC',3,'Indian','AVERAGE','NEAR'),(95,'House of Chedder','USC',2,'Italian','AVERAGE','NEAR'),(98,'Jumpstart','Santa Monica',4,'Chinese','EXPENSIVE','FAR'),(99,'Mantro','Marina Del Rey',4,'Mexican','AVERAGE','FAR'),(100,'Mardi Grub','Beverly Hills',3,'Korean','CHEAP','AVERAGE'),(101,'Housedown','Santa Monica',2,'Chinese','CHEAP','FAR'),(102,'Humburger','Marina Del Rey',3,'Italian','EXPENSIVE','FAR'),(105,'Jute Box','Adams',5,'Chinese','AVERAGE','NEAR'),(106,'Dote','USC',4,'Mexican','CHEAP','NEAR'),(107,'Buddha Bowl','Downtown',2,'Korean','EXPENSIVE','AVERAGE'),(109,'Donut District','Santa Monica',4,'Indian','CHEAP','FAR'),(110,'Martha’s Rump Roast','Marina Del Rey',5,'Italian','EXPENSIVE','FAR'),(111,'Anocha','USC',3,'Mexican','CHEAP','NEAR'),(112,'Anocha','USC',3,'Italian','CHEAP','NEAR'),(113,'Anocha','USC',3,'Korean','AVERAGE','NEAR'),(114,'Park Motel','USC',2,'Korean','AVERAGE','NEAR'),(115,'Park Motel','USC',2,'Indian','AVERAGE','NEAR'),(116,'Park Motel','USC',2,'Italian','AVERAGE','NEAR'),(117,'Cafe del Rey','Marina Del Rey',5,'Italian','AVERAGE','FAR'),(118,'Cafe del Rey','Marina Del Rey',5,'Mexican','AVERAGE','FAR'),(119,'Cafe del Rey','Marina Del Rey',5,'Korean','AVERAGE','FAR'),(120,'The Upper West','Santa Monica',4,'Korean','CHEAP','FAR'),(121,'The Upper West','Santa Monica',4,'Chinese','CHEAP','FAR'),(122,'The Upper West','Santa Monica',4,'Indian','CHEAP','FAR'),(123,'Citizen','Beverly Hills',3,'Indian','AVERAGE','AVERAGE'),(124,'Citizen','Beverly Hills',3,'Mexican','AVERAGE','AVERAGE'),(125,'Citizen','Beverly Hills',3,'Chinese','AVERAGE','AVERAGE'),(126,'Citizen','Beverly Hills',3,'Korean','AVERAGE','AVERAGE'),(127,'The Holy Grill','Downtown',1,'Korean','EXPENSIVE','AVERAGE'),(128,'The Holy Grill','Downtown',1,'Indian','EXPENSIVE','AVERAGE'),(129,'The Holy Grill','Downtown',5,'Korean','EXPENSIVE','AVERAGE'),(130,'The Holy Grill','Downtown',4,'Chinese','EXPENSIVE','AVERAGE'),(131,'Golden City','Adams',3,'Chinese','CHEAP','NEAR'),(132,'Golden City','Adams',3,'Korean','CHEAP','NEAR'),(133,'Golden City','Adams',4,'Mexican','CHEAP','NEAR');
/*!40000 ALTER TABLE `restaurants` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_profiles`
--

DROP TABLE IF EXISTS `user_profiles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_profiles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `price_preference` varchar(45) DEFAULT NULL,
  `location_preference` varchar(45) DEFAULT NULL,
  `cuisine_preference` varchar(45) DEFAULT NULL,
  `rating_preference` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_profiles`
--

LOCK TABLES `user_profiles` WRITE;
/*!40000 ALTER TABLE `user_profiles` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_profiles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'restaurants'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-11-27 19:19:15
