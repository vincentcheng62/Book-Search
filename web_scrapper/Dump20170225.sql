-- MySQL dump 10.13  Distrib 5.7.12, for Win64 (x86_64)
--
-- Host: localhost    Database: adebook
-- ------------------------------------------------------
-- Server version	5.7.17-log

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
-- Table structure for table `adebookdb`
--

DROP TABLE IF EXISTS `adebookdb`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `adebookdb` (
  `SALE_PRICE` text,
  `ISBN10` text,
  `KEYOWRD` text,
  `TITLE` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `adebookdb`
--

LOCK TABLES `adebookdb` WRITE;
/*!40000 ALTER TABLE `adebookdb` DISABLE KEYS */;
INSERT INTO `adebookdb` VALUES ('US$ 29.77','0520040910','python','Python A Study of Delphic Myth and Its Origins by Joseph Fontenrose 1980 Hardcover'),('None','1783555149','python','None'),('US$ 4.27','0201748843','python','Python: Visual QuickStart Guide'),('None','1449379109','python','None'),('None','1119070783','python','None'),('US$ 43.16','0763751863','python','Python For Bioinformatics (Jones and Bartlett Series in Biomedical Informatics)'),('None','0596555717','python','None'),('US$ 5.24','0321112547','python','Text Processing in Python'),('US$ 12.95','1593274076','python','Python for Kids: A Playful Introduction to Programming'),('None','0596550642','database','None'),('US$ 1.00','0321210255','database','Database Systems: A Practical Approach to Design, Implementation and Management (4th Edition) (International Computer Science Series)'),('US$ 24.57','0262693143','database','Readings in Database Systems'),('US$ 35.29','0816653518','database','Otaku: Japan\'s Database Animals'),('None','128410642X','database','None'),('US$ 3.48','1558605002','database','Database Modeling & Design (Mo'),('None','1118081366','database','None'),('None','1449673899','perl','None'),('US$ 32.50','073571228X','perl','Perl for C Programmers'),('US$ 42.95','158112550X','perl','On Perl: Perl for Students and Professionals'),('None','144937882X','perl','None'),('US$ 35.87','0970029721','perl','Perl for Bioinformatics'),('US$ 7.45','0201615711','perl','Network Programming with Perl'),('US$ 3.48','1565923987','perl','Mastering Algorithms with Perl'),('US$ 3.48','0764547836','perl','Applied Perl'),('US$ 3.61','0596002068','perl','Programming Web Services with Perl'),('US$ 8.42','0321553578','sql','SQL: Visual QuickStart Guide (3rd Edition) (Visual QuickStart Guide)'),('US$ 3.48','0072228857','sql','SQL: A Beginner\'s Guide, Second Edition'),('US$ 31.39','0122205316','sql','SQL: Practical Guide for Developers (Paperback)'),('US$ 469.60','0968955339','sql','Clarion Databases & SQL, A Practial Handbook of Database Design, Flat File & SQL Data Management, and Clarion Data Handling Tricks'),('US$ 4.13','0672324512','sql','Sams Teach Yourself SQL in 21 Days (4th Edition) (Sams Teach Yourself)'),('None','0596554257','sql','None'),('None','0071592563','sql','None'),('US$ 7.93','0201700476','sql','The Guru\'s Guide to SQL Server Architecture and Internals'),('US$ 4.49','0131002775','sql','Oracle SQL Interactive Workbook (2nd Edition)'),('None','1591400112','data mining','None'),('None','0471474886','data mining','None'),('None','0080475582','data mining','None'),('None','0123814804','data mining','None'),('None','3642231667','data mining','None'),('None','0080890369','data mining','None'),('US$ 8.97','1402073887','data mining','Data Mining and Decision Support: Integration and Collaboration (The Springer International Series in Engineering and Computer Science)'),('US$ 14.54','026208290X','data mining','Principles of Data Mining'),('US$ 16.30','8173713804','data mining','Data Mining Techniques'),('US$ 64.66','158603796X','parallel computing','Parallel Computing: Architectures, Algorithms and Applications (Advances in Parallel Computing)'),('US$ 6.83','8120306384','parallel computing','Elements of Parallel Computing'),('None','0470934638','parallel computing','None'),('US$ 18.00','1558605401','parallel computing','Industrial Strength Parallel Computing'),('US$ 3.80','8122423876','parallel computing','Parallel Computing'),('None','1420028685','parallel computing','None'),('US$ 3.48','0131909681','parallel computing','Introduction to Distributed and Parallel Computing, An'),('None','0470349484','parallel computing','None'),('US$ 99.30','9051991967','parallel computing','Parallel Computing: Technology and Practice (PCAT-94), (Transputer and Occam Engineering Systems, 43)'),('US$ 158.20','0824782534','statistics','U-Statistics: Theory and Practice, by Lee'),('None','1449397816','statistics','None'),('US$ 10.17','0486623491','statistics','The Foundations of Statistics'),('US$ 3.96','0803934211','statistics','Statistics: A Spectator Sport (Written Communication Annual)'),('US$ 49.99','0387402721','statistics','All of Statistics A Concise Course in Statistical Inference'),('US$ 11.99','0486436047','statistics','Statistics of Extremes'),('None','0804705968','statistics','None'),('US$ 4.96','0486637603','statistics','Principles of Statistics (Dover Books on Mathematics)'),('US$ 39.15','0691005478','statistics','Mathematical Methods of Statistics. (PMS-9)'),('US$ 19.19','0816638462','technology','Bodies in Technology (Paperback)'),('US$ 22.43','031333028X','technology','The Book: The Life Story of a Technology (Greenwood Technographies)'),('US$ 3.81','0262731738','technology','Technology and Social Inclusion: Rethinking the Digital Divide'),('US$ 25.85','0521543320','technology','Technology and Global Change'),('None','0080540635','technology','None'),('US$ 1.99','0538745789','technology','Succeeding with Technology (New Perspectives Series: Concepts)'),('US$ 8.97','1573563374','robotics','Robotics: A Reference Guide to the New Technology'),('None','1848160070','robotics','None'),('US$ 85.34','1846286417','robotics','Robotics'),('US$ 8.06','026263354X','robotics','Robotics Primer'),('US$ 4.30','8189866389','robotics','Robotics'),('US$ 3.48','0822557746','robotics','Robotics (Cool Science)'),('US$ 3.61','0126185204','robotics','Robotics, Second Edition: Designing the Mechanisms for Automated Machinery'),('None','3319325523','robotics','None'),('None','1449631576','robotics','None'),('US$ 40.72','0521663504','data structures','Purely Functional Data Structures'),('None','1259083047','data structures','None'),('None','9332900930','data structures','None'),('None','8184316593','data structures','None'),('None','8184317743','data structures','None'),('US$ 10.00','0534492525','data structures','Data Structures and Algorithms in Java, Second Edition'),('None','8184310846','data structures','None'),('None','8184311842','data structures','None'),('None','9812791248','data structures','None'),('US$ 5.59','1423901789','information','Management Information Systems, Sixth Edition'),('US$ 12.41','0521580447','information','The Physics of Information Technology'),('US$ 3.48','0735562458','information','Privacy, Information And Technology (Aspen Elective)'),('None','1930708459','information','None'),('US$ 5.02','0199546320','information','Designing Management Information Systems'),('US$ 3.48','1573565210','information','Milestones in Computer Science and Information Technology'),('None','1847876528','information','None'),('None','9381335052','information','None'),('US$ 75.00','157387230X','information','Theories of Information Behavior'),('None','0323141560','computer vision','None'),('US$ 76.30','1402032749','computer vision','Machine Learning in Computer Vision (Computational Imaging and Vision)'),('None','1848829353','computer vision','None'),('US$ 23.75','0262061589','computer vision','3 Dimensional Computer Vision, by Faugeras'),('None','1846280656','computer vision','None'),('None','1447141504','computer vision','None'),('US$ 57.79','0521766877','computer vision','Computer Vision for Visual Effects'),('None','9814343005','computer vision','None');
/*!40000 ALTER TABLE `adebookdb` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-02-25  1:22:10
