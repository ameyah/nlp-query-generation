CREATE DATABASE  IF NOT EXISTS `restaurants` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `restaurants`;
-- MySQL dump 10.13  Distrib 5.7.12, for linux-glibc2.5 (x86_64)
--
-- Host: localhost    Database: restaurants
-- ------------------------------------------------------
-- Server version	5.7.13-0ubuntu0.16.04.2

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
) ENGINE=InnoDB AUTO_INCREMENT=112 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `restaurants`
--

LOCK TABLES `restaurants` WRITE;
/*!40000 ALTER TABLE `restaurants` DISABLE KEYS */;
INSERT INTO `restaurants` VALUES (1,'Jurassic Pork','Adams',NULL,'Italian',NULL,'NEAR'),(4,'Donut District','Santa Monica',NULL,'Chinese',NULL,'FAR'),(5,'Howzit Go Inn','Marina Del Rey',NULL,'Mexican',NULL,'FAR'),(6,'Dolly Random','Beverly Hills',NULL,'Indian',NULL,'AVERAGE'),(7,'Jump Jack','USC',NULL,'Indian',NULL,'NEAR'),(8,'Jute Box','Adams',NULL,'Italian',NULL,'NEAR'),(11,'Humburger','Marina Del Rey',NULL,'Chinese',NULL,'FAR'),(12,'Brunchilli','USC',NULL,'Mexican',NULL,'NEAR'),(13,'Donut Babe','Adams',NULL,'Korean',NULL,'NEAR'),(14,'Housedown','Santa Monica',NULL,'Indian',NULL,'FAR'),(15,'Aquafire','Marina Del Rey',NULL,'Italian',NULL,'FAR'),(18,'Doctor Coffee','Downtown',NULL,'Chinese',NULL,'AVERAGE'),(19,'Aquacine','Adams',NULL,'Mexican',NULL,'NEAR'),(20,'Antimatter','Santa Monica',NULL,'Korean',NULL,'FAR'),(21,'Buddha Bait','Beverly Hills',NULL,'Indian',NULL,'AVERAGE'),(22,'Jumpstart','Santa Monica',NULL,'Italian',NULL,'FAR'),(25,'Jupitor Place','Adams',NULL,'Chinese',NULL,'NEAR'),(26,'Django’s','Santa Monica',NULL,'Korean',NULL,'FAR'),(27,'Buddha Bite','Downtown',NULL,'Korean',NULL,'AVERAGE'),(28,'Guru Cricket','Adams',NULL,'Korean',NULL,'NEAR'),(29,'Jupiter Trolley','Marina Del Rey',NULL,'Italian',NULL,'FAR'),(32,'Domina','Beverly Hills',NULL,'Chinese',NULL,'AVERAGE'),(33,'House of Chedder','USC',NULL,'Mexican',NULL,'NEAR'),(34,'Mantro','Marina Del Rey',NULL,'Korean',NULL,'FAR'),(35,'Dote','USC',NULL,'Indian',NULL,'NEAR'),(36,'Jumpstack','USC',NULL,'Italian',NULL,'NEAR'),(39,'Guru Planet','Santa Monica',NULL,'Chinese',NULL,'FAR'),(40,'Masquerade','Downtown',NULL,'Mexican',NULL,'AVERAGE'),(41,'Dolly Random','Beverly Hills',NULL,'Korean',NULL,'AVERAGE'),(43,'Guru Cricket','Adams',NULL,'Indian',NULL,'NEAR'),(44,'Django’s','Santa Monica',NULL,'Italian',NULL,'FAR'),(47,'Marvane','Downtown',NULL,'Chinese',NULL,'AVERAGE'),(48,'Antimatter','Santa Monica',NULL,'Mexican',NULL,'FAR'),(49,'Buddha Bite','Downtown',NULL,'Indian',NULL,'AVERAGE'),(51,'Doctor Coffee','Downtown',NULL,'Mexican',NULL,'AVERAGE'),(52,'Guru','Beverly Hills',NULL,'Mexican',NULL,'AVERAGE'),(53,'Buddha Bait','Beverly Hills',NULL,'Korean',NULL,'AVERAGE'),(54,'Jump Jack','USC',NULL,'Mexican',NULL,'NEAR'),(55,'Domina','Beverly Hills',NULL,'Italian',NULL,'AVERAGE'),(58,'House of Chedder','USC',NULL,'Chinese',NULL,'NEAR'),(59,'Aquacine','Adams',NULL,'Korean',NULL,'NEAR'),(60,'Jupiter Trolley','Marina Del Rey',NULL,'Korean',NULL,'FAR'),(61,'Jumpstart','Santa Monica',NULL,'Indian',NULL,'FAR'),(62,'Mantro','Marina Del Rey',NULL,'Italian',NULL,'FAR'),(65,'Humburger','Marina Del Rey',NULL,'Mexican',NULL,'FAR'),(66,'Maple Thor','Beverly Hills',NULL,'Mexican',NULL,'AVERAGE'),(67,'Brunchilli','USC',NULL,'Korean',NULL,'NEAR'),(68,'Jute Box','Adams',NULL,'Indian',NULL,'NEAR'),(69,'Dote','USC',NULL,'Italian',NULL,'NEAR'),(72,'Donut District','Santa Monica',NULL,'Italian',NULL,'FAR'),(73,'Martha’s Rump Roast','Marina Del Rey',NULL,'Mexican',NULL,'FAR'),(74,'Howzit Go Inn','Marina Del Rey',NULL,'Korean',NULL,'FAR'),(76,'Guru Planet','Santa Monica',NULL,'Indian',NULL,'FAR'),(77,'Masquerade','Downtown',NULL,'Italian',NULL,'AVERAGE'),(80,'Guru Cricket','Adams',NULL,'Chinese',NULL,'NEAR'),(81,'Django’s','Santa Monica',NULL,'Mexican',NULL,'FAR'),(82,'Aquafire','Marina Del Rey',NULL,'Korean',NULL,'FAR'),(84,'Marvane','Downtown',NULL,'Indian',NULL,'AVERAGE'),(85,'Antimatter','Santa Monica',NULL,'Indian',NULL,'FAR'),(86,'Buddha Bite','Downtown',NULL,'Mexican',NULL,'AVERAGE'),(87,'Jurassic Pork','Adams',NULL,'Indian',NULL,'NEAR'),(88,'Doctor Coffee','Downtown',NULL,'Italian',NULL,'AVERAGE'),(91,'Jump Jack','USC',NULL,'Chinese',NULL,'NEAR'),(92,'Domina','Beverly Hills',NULL,'Mexican',NULL,'AVERAGE'),(93,'Jupitor Place','Adams',NULL,'Korean',NULL,'NEAR'),(94,'Anocha','USC',NULL,'Indian',NULL,'NEAR'),(95,'House of Chedder','USC',NULL,'Italian',NULL,'NEAR'),(98,'Jumpstart','Santa Monica',NULL,'Chinese',NULL,'FAR'),(99,'Mantro','Marina Del Rey',NULL,'Mexican',NULL,'FAR'),(100,'Mardi Grub','Beverly Hills',NULL,'Korean',NULL,'AVERAGE'),(101,'Housedown','Santa Monica',NULL,'Chinese',NULL,'FAR'),(102,'Humburger','Marina Del Rey',NULL,'Italian',NULL,'FAR'),(105,'Jute Box','Adams',NULL,'Chinese',NULL,'NEAR'),(106,'Dote','USC',NULL,'Mexican',NULL,'NEAR'),(107,'Buddha Bowl','Downtown',NULL,'Korean',NULL,'AVERAGE'),(109,'Donut District','Santa Monica',NULL,'Indian',NULL,'FAR'),(110,'Martha’s Rump Roast','Marina Del Rey',NULL,'Italian',NULL,'FAR'),(111,'Anocha','USC',NULL,'Mexican',NULL,'NEAR');
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

--
-- Dumping routines for database 'restaurants'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-11-05 18:31:07
