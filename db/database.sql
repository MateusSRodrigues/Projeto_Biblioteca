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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Autor`
--

LOCK TABLES `Autor` WRITE;
/*!40000 ALTER TABLE `Autor` DISABLE KEYS */;
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
  `nota` int DEFAULT NULL,
  `comentario` text,
  `exemplar_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `exemplar_id` (`exemplar_id`),
  CONSTRAINT `Avaliacoes_ibfk_1` FOREIGN KEY (`exemplar_id`) REFERENCES `Exemplar` (`id`),
  CONSTRAINT `Avaliacoes_chk_1` CHECK ((`nota` between 1 and 5))
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Exemplar`
--

LOCK TABLES `Exemplar` WRITE;
/*!40000 ALTER TABLE `Exemplar` DISABLE KEYS */;
/*!40000 ALTER TABLE `Exemplar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Livro`
--

DROP TABLE IF EXISTS `Livro`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Livro` (
  `id` int NOT NULL,
  `ISBN` varchar(13) DEFAULT NULL,
  `editora` varchar(255) DEFAULT NULL,
  `genero` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `Livro_ibfk_1` FOREIGN KEY (`id`) REFERENCES `ObraFisica` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Livro`
--

LOCK TABLES `Livro` WRITE;
/*!40000 ALTER TABLE `Livro` DISABLE KEYS */;
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
  `id` int NOT NULL,
  `titulo` varchar(255) DEFAULT NULL,
  `autor` varchar(255) DEFAULT NULL,
  `paginas` int DEFAULT NULL,
  `data_publicacao` date DEFAULT NULL,
  `quantidade` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ObraFisica`
--

LOCK TABLES `ObraFisica` WRITE;
/*!40000 ALTER TABLE `ObraFisica` DISABLE KEYS */;
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

-- Dump completed on 2024-06-12  8:05:21
