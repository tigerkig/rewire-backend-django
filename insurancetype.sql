/*
SQLyog Community v13.1.7 (64 bit)
MySQL - 10.4.21-MariaDB : Database - rewire
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`rewire` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `rewire`;

/*Table structure for table `core_insurancetype` */

DROP TABLE IF EXISTS `core_insurancetype`;

CREATE TABLE `core_insurancetype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(225) NOT NULL,
  `imgPath` varchar(225) NOT NULL,
  `perDayPrice` int(225) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4;

/*Data for the table `core_insurancetype` */

insert  into `core_insurancetype`(`id`,`name`,`imgPath`,`perDayPrice`) values 
(1,'Saúde','',100),
(2,'Carro','',50),
(3,'Habitação','',150),
(4,'Óculos','',60),
(5,'Dental','',40),
(6,'Animal','',35),
(7,'Equipamento','',26),
(8,'Eletrodomésticos','',30),
(9,'Viagem','',60),
(10,'Mobilidade','',98),
(11,'Joias','',16),
(12,'Trabalho','',66);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
