-- MySQL dump 10.13  Distrib 8.0.36, for Linux (x86_64)
--
-- Host: localhost    Database: biblioteca
-- ------------------------------------------------------
-- Server version	8.0.37-0ubuntu0.24.04.1

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
-- Table structure for table `Autor`
--

DROP TABLE IF EXISTS `Autor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Autor` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(255) DEFAULT NULL,
  `obra_fisica_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `obra_fisica_id` (`obra_fisica_id`),
  CONSTRAINT `Autor_ibfk_1` FOREIGN KEY (`obra_fisica_id`) REFERENCES `ObraFisica` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Autor`
--

LOCK TABLES `Autor` WRITE;
/*!40000 ALTER TABLE `Autor` DISABLE KEYS */;
INSERT INTO `Autor` VALUES (1,'George RR Martin',17),(2,'George RR Martin',19),(3,'George RR Martin',20),(4,'George RR Martin',21),(5,'George RR Martin',22),(6,'George RR Martin',23),(7,'Maquiavel',24),(8,'Maquiavel',25),(9,'Maquiavel',26),(10,'Maquiavel',27),(11,'Maquiavel',28),(12,'Maquiavel',30),(13,'Maquiavel',32),(14,'Maquiavel',34),(15,'joao',35),(16,'jorge',36),(17,'jorge',38),(18,'jorge',39),(19,'jorge',40),(20,'jorge',41),(21,'jorge',42),(22,'jorge',43),(23,'jorge',44),(24,'jorge',45),(25,'jorge',46),(26,'jorge',47),(27,'jorge',48),(28,'jorge',49),(29,'jorge',50),(30,'jorge',51),(31,'jorge',52),(32,'jorge',53),(33,'jorge',54),(34,'jorge',55),(35,'jorge',56),(36,'jorge',57);
/*!40000 ALTER TABLE `Autor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Avaliacoes`
--

DROP TABLE IF EXISTS `Avaliacoes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Avaliacoes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `comentario` text,
  `exemplar_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `exemplar_id` (`exemplar_id`),
  CONSTRAINT `Avaliacoes_ibfk_1` FOREIGN KEY (`exemplar_id`) REFERENCES `Exemplar` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Avaliacoes`
--

LOCK TABLES `Avaliacoes` WRITE;
/*!40000 ALTER TABLE `Avaliacoes` DISABLE KEYS */;
/*!40000 ALTER TABLE `Avaliacoes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Emprestimo`
--

DROP TABLE IF EXISTS `Emprestimo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Emprestimo` (
  `id` int NOT NULL,
  `usuario_id` int DEFAULT NULL,
  `obra_fisica_id` int DEFAULT NULL,
  `data_emprestimo` date DEFAULT NULL,
  `data_devolucao_prevista` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `usuario_id` (`usuario_id`),
  KEY `obra_fisica_id` (`obra_fisica_id`),
  CONSTRAINT `Emprestimo_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `Usuario` (`id`),
  CONSTRAINT `Emprestimo_ibfk_2` FOREIGN KEY (`obra_fisica_id`) REFERENCES `ObraFisica` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Emprestimo`
--

LOCK TABLES `Emprestimo` WRITE;
/*!40000 ALTER TABLE `Emprestimo` DISABLE KEYS */;
/*!40000 ALTER TABLE `Emprestimo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Exemplar`
--

DROP TABLE IF EXISTS `Exemplar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Exemplar` (
  `id` int NOT NULL AUTO_INCREMENT,
  `numero` int DEFAULT NULL,
  `estado` enum('disponivel','emprestado','reservado') DEFAULT NULL,
  `obra_fisica_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `obra_fisica_id` (`obra_fisica_id`),
  CONSTRAINT `Exemplar_ibfk_1` FOREIGN KEY (`obra_fisica_id`) REFERENCES `ObraFisica` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Exemplar`
--

LOCK TABLES `Exemplar` WRITE;
/*!40000 ALTER TABLE `Exemplar` DISABLE KEYS */;
INSERT INTO `Exemplar` VALUES (1,1,'disponivel',57),(2,2,'disponivel',57),(3,3,'disponivel',57),(4,4,'disponivel',57),(5,5,'disponivel',57);
/*!40000 ALTER TABLE `Exemplar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Livro`
--

DROP TABLE IF EXISTS `Livro`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Livro` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ISBN` varchar(13) DEFAULT NULL,
  `editora` varchar(255) DEFAULT NULL,
  `genero` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `Livro_ibfk_1` FOREIGN KEY (`id`) REFERENCES `ObraFisica` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=58 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Livro`
--

LOCK TABLES `Livro` WRITE;
/*!40000 ALTER TABLE `Livro` DISABLE KEYS */;
INSERT INTO `Livro` VALUES (21,'9788556510785','suma','fantasia'),(22,'9788556510785','suma','fantasia'),(23,'9788656510785','suma','fantasia'),(24,'9788656510785','suma','fantasia'),(25,'9788656510785','suma','fantasia'),(26,'9788656510785','suma','fantasia'),(27,'9788656510785','suma','fantasia'),(28,'9788656510785','suma','fantasia'),(29,'2589631456','suma','fantasia'),(30,'9788656510785','suma','fantasia'),(31,'2589631456','suma','fantasia'),(32,'9788656510785','suma','fantasia'),(33,'2589631456','suma','fantasia'),(34,'9788656510785','suma','fantasia'),(35,'2589631456','suma','fantasia'),(36,'2589631456','leia','terror'),(38,'dracarys','jorge','2020-4-4'),(39,'2589631456','leia','terror'),(40,'2589631456','leia','terror'),(41,'2589631456','leia','terror'),(42,'2589631456','leia','terror'),(43,'2589631456','leia','terror'),(44,'2589631456','leia','terror'),(45,'2589631456','leia','terror'),(46,'2589631456','leia','terror'),(47,'2589631456','leia','terror'),(48,'2589631456','leia','terror'),(49,'2589631456','leia','terror'),(50,'2589631456','leia','terror'),(51,'2589631456','leia','terror'),(52,'2589631456','leia','terror'),(53,'2589631456','leia','terror'),(54,'2589631456','leia','terror'),(55,'2589631456','leia','terror'),(56,'2589631456','leia','terror'),(57,'2589631456','leia','terror');
/*!40000 ALTER TABLE `Livro` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Multas`
--

DROP TABLE IF EXISTS `Multas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Multas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `emprestimo_id` int NOT NULL,
  `valor` float DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `emprestimo_id` (`emprestimo_id`),
  CONSTRAINT `Multas_ibfk_1` FOREIGN KEY (`emprestimo_id`) REFERENCES `Emprestimo` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Multas`
--

LOCK TABLES `Multas` WRITE;
/*!40000 ALTER TABLE `Multas` DISABLE KEYS */;
/*!40000 ALTER TABLE `Multas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ObraFisica`
--

DROP TABLE IF EXISTS `ObraFisica`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ObraFisica` (
  `id` int NOT NULL AUTO_INCREMENT,
  `titulo` varchar(255) DEFAULT NULL,
  `paginas` int DEFAULT NULL,
  `data_publicacao` date DEFAULT NULL,
  `quantidade` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=58 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ObraFisica`
--

LOCK TABLES `ObraFisica` WRITE;
/*!40000 ALTER TABLE `ObraFisica` DISABLE KEYS */;
INSERT INTO `ObraFisica` VALUES (1,'O Senhor dos Anéis',1178,'1954-07-29',10),(2,'O Senhor dos Anéis',1178,'1954-07-29',10),(3,'O Senhor dos Anéis',1178,'1954-07-29',10),(4,'obra',1178,'1954-07-29',10),(5,'A Guerra dos Tronos',1178,'1954-07-29',10),(6,'A Furia dos Reis',1178,'1954-07-29',10),(7,'O Festim dos Corvos',1178,'1954-07-29',10),(8,'A Tormenta de Espadas',1178,'1954-07-29',10),(9,'A Dança dos Dragoes',1178,'1954-07-29',10),(10,'A Guerra dos Tronos',1178,'1954-07-29',10),(11,'A Furia dos Reis',1178,'1954-07-29',10),(12,'O Festim dos Corvos',1178,'1954-07-29',10),(13,'A Tormenta de Espadas',1178,'1954-07-29',10),(14,'A Dança dos Dragoes',1178,'1954-07-29',10),(15,'A Guerra dos Tronos',1178,'1954-07-29',10),(16,'A Guerra dos Tronos',1178,'1954-07-29',10),(17,'A Guerra dos Tronos',1178,'1954-07-29',10),(18,'A Guerra dos Tronos',1178,'1954-07-29',10),(19,'A Guerra dos Tronos',1178,'1954-07-29',10),(20,'A Guerra dos Tronos',1178,'1954-07-29',10),(21,'A Guerra dos Tronos',1178,'1954-07-29',10),(22,'A Guerra dos Tronos',1178,'1954-07-29',10),(23,'A Guerra dos Tronos',1178,'1954-07-29',10),(24,'O principe',1178,'1954-07-29',10),(25,'O principe',1178,'1954-07-29',10),(26,'O principe',1178,'1954-07-29',10),(27,'O principe',1178,'1954-07-29',10),(28,'O principe',1178,'1954-07-29',10),(29,'livro teste',50,'2020-04-04',5),(30,'O principe',1178,'1954-07-29',10),(31,'livro teste',50,'2020-04-04',5),(32,'O principe',1178,'1954-07-29',10),(33,'livro teste',50,'2020-04-04',5),(34,'O principe',1178,'1954-07-29',10),(35,'livro teste',50,'2020-04-04',5),(36,'dracarys',50,'2020-04-04',5),(37,'dracarys',50,'2020-04-04',5),(38,'dracarys',50,'2020-04-04',5),(39,'dracarys',50,'2020-04-04',5),(40,'dracarys',50,'2020-04-04',5),(41,'dracarys',50,'2020-04-04',5),(42,'dracarys',50,'2020-04-04',5),(43,'dracarys',50,'2020-04-04',5),(44,'dracarys',50,'2020-04-04',5),(45,'dracarys',50,'2020-04-04',5),(46,'dracarys',50,'2020-04-04',5),(47,'dracarys',50,'2020-04-04',5),(48,'dracarys',50,'2020-04-04',5),(49,'dracarys',50,'2020-04-04',5),(50,'dracarys',50,'2020-04-04',5),(51,'dracarys',50,'2020-04-04',5),(52,'dracarys',50,'2020-04-04',5),(53,'dracarys',50,'2020-04-04',5),(54,'dracarys',50,'2020-04-04',5),(55,'dracarys',50,'2020-04-04',5),(56,'dracarys',50,'2020-04-04',5),(57,'dracarys',50,'2020-04-04',5);
/*!40000 ALTER TABLE `ObraFisica` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Periodico`
--

DROP TABLE IF EXISTS `Periodico`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Periodico` (
  `id` int NOT NULL,
  `ISSN` varchar(8) DEFAULT NULL,
  `editora` varchar(255) DEFAULT NULL,
  `area_estudo` varchar(255) DEFAULT NULL,
  `volume` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `Periodico_ibfk_1` FOREIGN KEY (`id`) REFERENCES `ObraFisica` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Periodico`
--

LOCK TABLES `Periodico` WRITE;
/*!40000 ALTER TABLE `Periodico` DISABLE KEYS */;
/*!40000 ALTER TABLE `Periodico` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Reserva`
--

DROP TABLE IF EXISTS `Reserva`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Reserva` (
  `id` int NOT NULL,
  `usuario_id` int DEFAULT NULL,
  `obra_fisica_id` int DEFAULT NULL,
  `data_reserva` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `usuario_id` (`usuario_id`),
  KEY `obra_fisica_id` (`obra_fisica_id`),
  CONSTRAINT `Reserva_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `Usuario` (`id`),
  CONSTRAINT `Reserva_ibfk_2` FOREIGN KEY (`obra_fisica_id`) REFERENCES `ObraFisica` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Reserva`
--

LOCK TABLES `Reserva` WRITE;
/*!40000 ALTER TABLE `Reserva` DISABLE KEYS */;
/*!40000 ALTER TABLE `Reserva` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TrabalhoAcademico`
--

DROP TABLE IF EXISTS `TrabalhoAcademico`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `TrabalhoAcademico` (
  `id` int NOT NULL,
  `tipo` enum('dissertacao','monografia') DEFAULT NULL,
  `orientador` varchar(255) DEFAULT NULL,
  `nivel_academico` varchar(255) DEFAULT NULL,
  `area_estudo` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `TrabalhoAcademico_ibfk_1` FOREIGN KEY (`id`) REFERENCES `ObraFisica` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TrabalhoAcademico`
--

LOCK TABLES `TrabalhoAcademico` WRITE;
/*!40000 ALTER TABLE `TrabalhoAcademico` DISABLE KEYS */;
/*!40000 ALTER TABLE `TrabalhoAcademico` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Usuario`
--

DROP TABLE IF EXISTS `Usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Usuario` (
  `id` int NOT NULL,
  `nome` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `cpf` varchar(11) DEFAULT NULL,
  `endereco` varchar(255) DEFAULT NULL,
  `saldo` decimal(10,2) DEFAULT NULL,
  `senha` varchar(255) DEFAULT NULL,
  `tipo` enum('Administrador','Professor','EstudantePosGraduacao','EstudanteGraduacao','Funcionario') DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Usuario`
--

LOCK TABLES `Usuario` WRITE;
/*!40000 ALTER TABLE `Usuario` DISABLE KEYS */;
/*!40000 ALTER TABLE `Usuario` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-17 19:56:18
