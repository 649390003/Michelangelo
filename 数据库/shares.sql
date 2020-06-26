/*
SQLyog Enterprise v12.09 (64 bit)
MySQL - 5.5.40 : Database - share
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`share` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `share`;

/*Table structure for table `account` */

DROP TABLE IF EXISTS `account`;

CREATE TABLE `account` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `bankcard` varchar(20) NOT NULL,
  `paypassword` varchar(20) NOT NULL,
  `balance` double NOT NULL,
  `owner_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `account_owner_id_bf84ab8067d398c_fk_auth_user_id` (`owner_id`),
  CONSTRAINT `account_owner_id_bf84ab8067d398c_fk_auth_user_id` FOREIGN KEY (`owner_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

/*Data for the table `account` */

insert  into `account`(`id`,`bankcard`,`paypassword`,`balance`,`owner_id`) values (1,'1000000002','980318',1093272,2),(2,'1111111111','111111',11112222,3);

/*Table structure for table `actrecord` */

DROP TABLE IF EXISTS `actrecord`;

CREATE TABLE `actrecord` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `bstype` tinyint(1) NOT NULL,
  `amount` double NOT NULL,
  `rdate` datetime NOT NULL,
  `isdelete` tinyint(1) NOT NULL,
  `owner_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myShare_record_owner_id_799b76932e870e49_fk_auth_user_id` (`owner_id`),
  CONSTRAINT `myShare_record_owner_id_799b76932e870e49_fk_auth_user_id` FOREIGN KEY (`owner_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

/*Data for the table `actrecord` */

insert  into `actrecord`(`id`,`bstype`,`amount`,`rdate`,`isdelete`,`owner_id`) values (1,1,100,'2020-05-13 14:55:23',0,2),(2,0,100,'2020-05-13 16:36:32',1,2),(3,1,10000,'2020-05-15 14:28:24',0,2),(4,1,100000,'2020-05-16 09:18:44',0,2),(5,1,1000000,'2020-05-19 04:48:56',0,2),(6,1,11222,'2020-05-19 04:49:53',0,2),(7,0,500,'2020-05-19 05:06:56',0,2),(8,1,11111111,'2020-05-19 11:49:49',1,3),(9,1,11111,'2020-05-19 11:51:57',0,3),(10,0,10000,'2020-05-19 11:57:57',0,3);

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group__permission_id_235b47599848459f_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group_permission_group_id_2e22b9f3a6a4aa4d_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_group__permission_id_235b47599848459f_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  CONSTRAINT `auth__content_type_id_53102fcce120ab9d_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=utf8;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add colsing price',7,'add_colsingprice'),(20,'Can change colsing price',7,'change_colsingprice'),(21,'Can delete colsing price',7,'delete_colsingprice'),(22,'Can add user info',8,'add_userinfo'),(23,'Can change user info',8,'change_userinfo'),(24,'Can delete user info',8,'delete_userinfo'),(25,'Can add shares',9,'add_shares'),(26,'Can change shares',9,'change_shares'),(27,'Can delete shares',9,'delete_shares'),(28,'Can add profit',10,'add_profit'),(29,'Can change profit',10,'change_profit'),(30,'Can delete profit',10,'delete_profit'),(31,'Can add account',11,'add_account'),(32,'Can change account',11,'change_account'),(33,'Can delete account',11,'delete_account'),(34,'Can add buy order',12,'add_buyorder'),(35,'Can change buy order',12,'change_buyorder'),(36,'Can delete buy order',12,'delete_buyorder'),(37,'Can add sell order',13,'add_sellorder'),(38,'Can change sell order',13,'change_sellorder'),(39,'Can delete sell order',13,'delete_sellorder'),(40,'Can add record',14,'add_record'),(41,'Can change record',14,'change_record'),(42,'Can delete record',14,'delete_record'),(43,'Can add share daily info',15,'add_sharedailyinfo'),(44,'Can change share daily info',15,'change_sharedailyinfo'),(45,'Can delete share daily info',15,'delete_sharedailyinfo');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

/*Data for the table `auth_user` */

insert  into `auth_user`(`id`,`password`,`last_login`,`is_superuser`,`username`,`first_name`,`last_name`,`email`,`is_staff`,`is_active`,`date_joined`) values (1,'pbkdf2_sha256$20000$yUMo8iXZNgZL$JZf8UhwGu/PL4ptf3evYy03zkU+3yuE9hc7CA57lnRE=','2020-05-13 14:19:12',1,'admin','','','admin@163.com',1,1,'2020-05-12 12:56:29'),(2,'pbkdf2_sha256$20000$ACzu8oiWUHjp$5cNUv+YDgsbsynd8S2nD52o9WNAlLeNoUggqfGmtMCs=','2020-05-19 12:42:23',0,'pqh','','','',0,1,'2020-05-12 14:31:29'),(3,'pbkdf2_sha256$20000$ofTQqTKukzHa$QPgohFo/qVBlWnnd+tD6+hHgmriAsmVsZFv1+Odl3+Y=','2020-05-19 11:17:01',0,'admin111','','','',0,1,'2020-05-19 10:14:39');

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_3b45197425c5df09_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_3b45197425c5df09_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_14324a3742672dac_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_u_permission_id_64e3a18b6c02fe0b_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_user_user_permissi_user_id_6cf93854d91155fc_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `auth_user_u_permission_id_64e3a18b6c02fe0b_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `buyorder` */

DROP TABLE IF EXISTS `buyorder`;

CREATE TABLE `buyorder` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `expectprice` double NOT NULL,
  `buynum` int(11) NOT NULL,
  `isSuccess` tinyint(1) NOT NULL,
  `ordertime` datetime NOT NULL,
  `owner_id` int(11) NOT NULL,
  `share_id` int(11) NOT NULL,
  `remark` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `buyorder_owner_id_79e819b5068b34dc_fk_auth_user_id` (`owner_id`),
  KEY `buyorder_6dcc1338` (`share_id`),
  CONSTRAINT `buyorder_owner_id_79e819b5068b34dc_fk_auth_user_id` FOREIGN KEY (`owner_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `buyorder_share_id_7c94cd595541de3f_fk_shares_id` FOREIGN KEY (`share_id`) REFERENCES `shares` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

/*Data for the table `buyorder` */

insert  into `buyorder`(`id`,`expectprice`,`buynum`,`isSuccess`,`ordertime`,`owner_id`,`share_id`,`remark`) values (1,55,100,0,'2020-05-15 14:56:12',2,3,'股票价格未达到您的购买价'),(2,92,100,1,'2020-05-15 15:02:16',2,1,'购买成功'),(3,95,100,1,'2020-05-16 09:20:18',2,1,'购买成功'),(4,102,100,1,'2020-05-16 09:28:25',2,1,'购买成功'),(5,97,50,1,'2020-05-16 12:07:59',2,1,'购买成功'),(6,90,100,1,'2020-05-16 12:12:34',2,1,'购买成功'),(7,90,100,1,'2020-05-16 12:13:10',2,1,'购买成功'),(8,111.12,500,0,'2020-05-19 13:11:12',2,1,'股票价格未达到您的购买价'),(9,100,100,0,'2020-05-19 15:20:40',2,1,'股票价格未达到您的购买价');

/*Table structure for table `colsing_price` */

DROP TABLE IF EXISTS `colsing_price`;

CREATE TABLE `colsing_price` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sclose` double NOT NULL,
  `sdate` date NOT NULL,
  `smonth` int(11) NOT NULL,
  `sweek` int(11) NOT NULL,
  `sweekday` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `colsing_price` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `djang_content_type_id_5e549c09ddbac664_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_3e31fe17cfe93b74_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_user_id_3e31fe17cfe93b74_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `djang_content_type_id_5e549c09ddbac664_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_73f6751c12b254b0_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(11,'myShare','account'),(12,'myShare','buyorder'),(7,'myShare','colsingprice'),(10,'myShare','profit'),(14,'myShare','record'),(13,'myShare','sellorder'),(15,'myShare','sharedailyinfo'),(9,'myShare','shares'),(8,'myShare','userinfo'),(6,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values (1,'contenttypes','0001_initial','2020-05-12 12:55:41'),(2,'auth','0001_initial','2020-05-12 12:55:41'),(3,'admin','0001_initial','2020-05-12 12:55:41'),(4,'contenttypes','0002_remove_content_type_name','2020-05-12 12:55:41'),(5,'auth','0002_alter_permission_name_max_length','2020-05-12 12:55:42'),(6,'auth','0003_alter_user_email_max_length','2020-05-12 12:55:42'),(7,'auth','0004_alter_user_username_opts','2020-05-12 12:55:42'),(8,'auth','0005_alter_user_last_login_null','2020-05-12 12:55:42'),(9,'auth','0006_require_contenttypes_0002','2020-05-12 12:55:42'),(10,'myShare','0001_initial','2020-05-12 12:55:42'),(11,'sessions','0001_initial','2020-05-12 12:55:42'),(12,'myShare','0002_auto_20200513_1709','2020-05-13 09:09:27'),(13,'myShare','0003_auto_20200513_1719','2020-05-13 09:20:11'),(14,'myShare','0004_record','2020-05-13 14:47:19'),(15,'myShare','0005_auto_20200513_2258','2020-05-13 14:58:57'),(16,'myShare','0006_sharedailyinfo','2020-05-15 06:27:21'),(17,'myShare','0007_auto_20200515_1454','2020-05-15 06:54:37'),(18,'myShare','0008_buyorder_remark','2020-05-15 14:37:14'),(19,'myShare','0009_auto_20200516_1829','2020-05-16 10:29:51'),(20,'myShare','0010_auto_20200517_2126','2020-05-17 13:28:19'),(21,'myShare','0011_auto_20200519_1251','2020-05-19 04:51:35'),(22,'myShare','0012_auto_20200519_1253','2020-05-19 04:53:37');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values ('h9xodzq8w6sh68lx3fim0nreow8t3xd4','MDQwMDhjZTBhZjNmOTFjMDQ5MzBhY2QwMDlkZjU1ZGNkMDRlOWVlNDp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0Y2M0YWEyNzI0ODRlNDhhODI1Y2VhNzIwM2Q1YWJiN2YxMjQ3NTI4In0=','2020-06-02 12:42:23');

/*Table structure for table `profit` */

DROP TABLE IF EXISTS `profit`;

CREATE TABLE `profit` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `buyrate` double NOT NULL,
  `nowrate` double NOT NULL,
  `sharenum` int(11) NOT NULL,
  `owner_id` int(11) NOT NULL,
  `share_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `profit_owner_id_381776735d70aa77_fk_auth_user_id` (`owner_id`),
  KEY `profit_6dcc1338` (`share_id`),
  CONSTRAINT `profit_owner_id_381776735d70aa77_fk_auth_user_id` FOREIGN KEY (`owner_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `profit_share_id_42229360eb458ae_fk_shares_id` FOREIGN KEY (`share_id`) REFERENCES `shares` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

/*Data for the table `profit` */

insert  into `profit`(`id`,`buyrate`,`nowrate`,`sharenum`,`owner_id`,`share_id`) values (4,90,90.3,80,2,1),(5,90,90.3,100,2,1);

/*Table structure for table `sellorder` */

DROP TABLE IF EXISTS `sellorder`;

CREATE TABLE `sellorder` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `expectprice` double NOT NULL,
  `sellnum` int(11) NOT NULL,
  `isSuccess` tinyint(1) NOT NULL,
  `ordertime` datetime NOT NULL,
  `owner_id` int(11) NOT NULL,
  `share_id` int(11) NOT NULL,
  `remark` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `sellorder_owner_id_3a238038117058e0_fk_auth_user_id` (`owner_id`),
  KEY `sellorder_6dcc1338` (`share_id`),
  CONSTRAINT `sellorder_owner_id_3a238038117058e0_fk_auth_user_id` FOREIGN KEY (`owner_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `sellorder_share_id_20886d312397e645_fk_shares_id` FOREIGN KEY (`share_id`) REFERENCES `shares` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

/*Data for the table `sellorder` */

insert  into `sellorder`(`id`,`expectprice`,`sellnum`,`isSuccess`,`ordertime`,`owner_id`,`share_id`,`remark`) values (1,100,410,0,'2020-05-16 12:14:27',2,1,'股票价格未达到您的卖出价'),(2,100,410,0,'2020-05-16 12:14:49',2,1,'股票价格未达到您的卖出价'),(3,90,270,1,'2020-05-16 12:59:05',2,1,'出售成功'),(4,100,50,0,'2020-05-19 15:25:14',2,1,'股票价格未达到您的卖出价');

/*Table structure for table `sharedailyinfo` */

DROP TABLE IF EXISTS `sharedailyinfo`;

CREATE TABLE `sharedailyinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `highestp` double NOT NULL,
  `lowestp` double NOT NULL,
  `startp` double NOT NULL,
  `closep` double NOT NULL,
  `share_id` int(11) NOT NULL,
  `infotimes` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `sharedailyinfo_share_id_47f7bb0a4171eaed_fk_shares_id` (`share_id`),
  CONSTRAINT `sharedailyinfo_share_id_47f7bb0a4171eaed_fk_shares_id` FOREIGN KEY (`share_id`) REFERENCES `shares` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;

/*Data for the table `sharedailyinfo` */

insert  into `sharedailyinfo`(`id`,`highestp`,`lowestp`,`startp`,`closep`,`share_id`,`infotimes`) values (1,54.03,51.94,53,53.48,2,1),(2,54,52.9,53.48,53.97,2,2),(4,38.61,36.7,39,36.7,3,1),(5,93.04,88.46,94,91.13,1,1),(6,94.8,92.02,91.13,92.86,1,2),(7,58.4,53.94,53.97,58.4,2,3),(8,37.07,33.84,36.7,34.18,3,2),(9,102.146,94.72,92.86,102.146,1,3),(10,105.23,101.02,102.146,101.02,1,4),(11,99.99,96.97,101.02,97.94,1,5),(12,95.98,88.53,97.94,90.3,1,6);

/*Table structure for table `shares` */

DROP TABLE IF EXISTS `shares`;

CREATE TABLE `shares` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sname` varchar(20) NOT NULL,
  `snumber` varchar(10) NOT NULL,
  `issuenum` int(11) NOT NULL,
  `issuedate` datetime NOT NULL,
  `hprice` double NOT NULL,
  `lprice` double NOT NULL,
  `nprice` double NOT NULL,
  `isDelete` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

/*Data for the table `shares` */

insert  into `shares`(`id`,`sname`,`snumber`,`issuenum`,`issuedate`,`hprice`,`lprice`,`nprice`,`isDelete`) values (1,'华为','100000',4720,'2020-05-14 12:43:01',105.23,22,90.3,0),(2,'联想','100001',5000,'2020-05-14 12:43:01',87,11,58.4,0),(3,'恒生','100002',5000,'2020-05-14 12:43:01',51,22,34.18,0),(4,'小米','100000',5000,'2020-05-19 14:22:07',55,14,53,0),(5,'京东','100001',5000,'2020-05-19 14:22:07',88,25,26,0),(6,'阿里','100002',5000,'2020-05-19 14:22:07',76,12,60,0),(7,'魅族','100003',5000,'2020-05-19 14:22:07',73,12,52,0),(8,'腾讯','100004',5000,'2020-05-19 14:22:07',76,21,33,0),(9,'网易','100005',5000,'2020-05-19 14:22:07',65,25,33,0),(10,'微软','100006',5000,'2020-05-19 14:22:07',70,22,59,0);

/*Table structure for table `shares_owner` */

DROP TABLE IF EXISTS `shares_owner`;

CREATE TABLE `shares_owner` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `shares_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `shares_id` (`shares_id`,`user_id`),
  KEY `shares_owner_user_id_c5398f8f1f2353c_fk_auth_user_id` (`user_id`),
  CONSTRAINT `shares_owner_shares_id_16a70b97e8c163f8_fk_shares_id` FOREIGN KEY (`shares_id`) REFERENCES `shares` (`id`),
  CONSTRAINT `shares_owner_user_id_c5398f8f1f2353c_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

/*Data for the table `shares_owner` */

insert  into `shares_owner`(`id`,`shares_id`,`user_id`) values (1,1,2),(2,2,2),(3,3,2),(4,4,2),(5,5,2),(6,6,2),(7,7,2),(8,8,2),(9,9,2),(10,10,2);

/*Table structure for table `userinfo` */

DROP TABLE IF EXISTS `userinfo`;

CREATE TABLE `userinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `onlinename` varchar(20) NOT NULL,
  `gender` varchar(5) NOT NULL,
  `mobilephone` varchar(15) NOT NULL,
  `uploadimg` varchar(100) NOT NULL,
  `isDelete` tinyint(1) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `userinfo_user_id_675284f28659203e_fk_auth_user_id` (`user_id`),
  CONSTRAINT `userinfo_user_id_675284f28659203e_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

/*Data for the table `userinfo` */

insert  into `userinfo`(`id`,`onlinename`,`gender`,`mobilephone`,`uploadimg`,`isDelete`,`user_id`) values (1,'陈绰琪','女','55222111','myShare/ccq_img_ncrz4FW.jpg',0,1),(2,'Michelangelo','1','555222111','myShare/3.png',0,2),(3,'陈绰琪','1','000000','myShare/4.png',0,3);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
