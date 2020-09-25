-- MySQL dump 10.13  Distrib 5.7.29, for Linux (x86_64)
--
-- Host: localhost    Database: agile_database
-- ------------------------------------------------------
-- Server version	5.7.29-0ubuntu0.18.04.1

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
-- Table structure for table `account_ar_organization`
--

DROP TABLE IF EXISTS `account_ar_organization`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_ar_organization` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `org_id` varchar(50) NOT NULL,
  `organization_name` varchar(100) NOT NULL,
  `organization_url` varchar(50) NOT NULL,
  `address` longtext NOT NULL,
  `subscription_level` varchar(50) NOT NULL,
  `created_dt` datetime(6) NOT NULL,
  `update_dt` datetime(6) NOT NULL,
  `created_by_id` int(11) DEFAULT NULL,
  `organization_status_id` int(11) DEFAULT NULL,
  `update_by_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `org_id` (`org_id`),
  KEY `account_ar_organization_created_by_id_85144d93_fk_auth_user_id` (`created_by_id`),
  KEY `account_ar_organizat_organization_status__6685de96_fk_account_a` (`organization_status_id`),
  KEY `account_ar_organization_update_by_id_a0e92895_fk_auth_user_id` (`update_by_id`),
  CONSTRAINT `account_ar_organizat_organization_status__6685de96_fk_account_a` FOREIGN KEY (`organization_status_id`) REFERENCES `account_ar_organization_status` (`id`),
  CONSTRAINT `account_ar_organization_created_by_id_85144d93_fk_auth_user_id` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `account_ar_organization_update_by_id_a0e92895_fk_auth_user_id` FOREIGN KEY (`update_by_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_ar_organization`
--

LOCK TABLES `account_ar_organization` WRITE;
/*!40000 ALTER TABLE `account_ar_organization` DISABLE KEYS */;
INSERT INTO `account_ar_organization` VALUES (1,'eDpuPGmuej','digimomk','digimonk.in','','','2020-03-04 11:43:08.671072','2020-03-04 11:43:08.671097',2,NULL,2),(2,'bL8MDj4U6v','Agile Ready LLC','beagileready.com','','','2020-03-05 00:59:18.120625','2020-03-05 00:59:18.120647',22,NULL,22);
/*!40000 ALTER TABLE `account_ar_organization` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_ar_organization_status`
--

DROP TABLE IF EXISTS `account_ar_organization_status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_ar_organization_status` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `status_key` varchar(50) NOT NULL,
  `status_desc` longtext NOT NULL,
  `created_dt` datetime(6) NOT NULL,
  `update_dt` datetime(6) NOT NULL,
  `created_by_id` int(11) DEFAULT NULL,
  `update_by_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `account_ar_organizat_created_by_id_ffa4c0b7_fk_auth_user` (`created_by_id`),
  KEY `account_ar_organizat_update_by_id_f035d77c_fk_auth_user` (`update_by_id`),
  CONSTRAINT `account_ar_organizat_created_by_id_ffa4c0b7_fk_auth_user` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `account_ar_organizat_update_by_id_f035d77c_fk_auth_user` FOREIGN KEY (`update_by_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_ar_organization_status`
--

LOCK TABLES `account_ar_organization_status` WRITE;
/*!40000 ALTER TABLE `account_ar_organization_status` DISABLE KEYS */;
/*!40000 ALTER TABLE `account_ar_organization_status` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_ar_user`
--

DROP TABLE IF EXISTS `account_ar_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_ar_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(50) NOT NULL,
  `address` varchar(255) NOT NULL,
  `city` varchar(255) NOT NULL,
  `state` varchar(255) NOT NULL,
  `zip` int(11) NOT NULL,
  `country` varchar(50) NOT NULL,
  `phone` bigint(20) NOT NULL,
  `backup_email` varchar(50) NOT NULL,
  `user_type` varchar(50) NOT NULL,
  `subscription_level` varchar(50) NOT NULL,
  `active_user` int(11) NOT NULL,
  `user_to_invite` int(11) NOT NULL,
  `status` varchar(50) NOT NULL,
  `login_status` tinyint(1) NOT NULL,
  `activate_status` tinyint(1) NOT NULL,
  `verification_status` tinyint(1) NOT NULL,
  `created_by` int(11) NOT NULL,
  `created_dt` datetime(6) NOT NULL,
  `updated_by` int(11) NOT NULL,
  `updated_dt` datetime(6) NOT NULL,
  `org_id_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `terms_accept` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  KEY `account_ar_user_org_id_id_085fcd71_fk_account_ar_organization_id` (`org_id_id`),
  CONSTRAINT `account_ar_user_org_id_id_085fcd71_fk_account_ar_organization_id` FOREIGN KEY (`org_id_id`) REFERENCES `account_ar_organization` (`id`),
  CONSTRAINT `account_ar_user_user_id_66d85621_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_ar_user`
--

LOCK TABLES `account_ar_user` WRITE;
/*!40000 ALTER TABLE `account_ar_user` DISABLE KEYS */;
INSERT INTO `account_ar_user` VALUES (1,'jitendra','','gwalior01','Madhya Pradesh',474004,'India',9617279518,'','Root','Free trial',0,0,'Active',0,0,0,0,'2020-03-04 11:43:08.679777',0,'2020-03-04 11:43:08.679787',1,2,1),(14,'Praveen','','Gwalior','Madhya Pradesh',474006,'India',2233223322,'','User','Free trial',0,0,'Active',0,0,0,1,'2020-02-21 06:46:04.769659',1,'2020-02-21 06:46:04.769667',1,15,1),(15,'','','','state',0,'',0,'','User','Free trial',0,0,'Active',0,0,0,1,'2020-02-21 06:55:35.959854',1,'2020-02-21 06:55:35.959862',1,16,1),(16,'','','','state',0,'',0,'','User','Free trial',0,0,'Active',0,0,0,1,'2020-02-21 06:55:39.574222',1,'2020-02-21 06:55:39.574229',1,17,1),(17,'','','','state',0,'',0,'','User','Free trial',0,0,'Active',0,0,0,1,'2020-02-21 06:56:19.081963',1,'2020-02-21 06:56:19.081970',1,18,1),(18,'Sagar Shrivastava','','','state',474002,'',987458545,'','User','Free trial',0,0,'Active',0,0,0,1,'2020-02-21 06:57:00.843088',1,'2020-02-21 06:57:00.843095',1,19,1),(19,'Ravi Baghel','','GWALIOR','MADHYA PRADESH',474001,'India',212451245124,'','User','Free trial',0,0,'Active',0,0,0,1,'2020-02-21 06:58:29.379447',1,'2020-02-21 06:58:29.379454',1,20,1),(20,'jitendra','','gwalior','state',474004,'india',9617279518,'','User','Free trial',0,0,'Active',0,0,0,2,'2020-03-04 15:03:57.121966',2,'2020-03-04 15:03:57.121977',1,21,1),(21,'Antonio V Timbol','','Jacksonville','FL',32246,'United States',9046140931,'','Root','Free trial',1,5,'Active',0,1,1,0,'2020-03-05 00:59:18.000000',0,'2020-03-05 00:59:18.000000',2,22,1);
/*!40000 ALTER TABLE `account_ar_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_ar_user_profile_permission`
--

DROP TABLE IF EXISTS `account_ar_user_profile_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_ar_user_profile_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ar_user_id` int(11) NOT NULL,
  `aruserprofile_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `account_ar_user_profile__ar_user_id_aruserprofile_4665a6ce_uniq` (`ar_user_id`,`aruserprofile_id`),
  KEY `account_ar_user_prof_aruserprofile_id_7baf24af_fk_account_a` (`aruserprofile_id`),
  CONSTRAINT `account_ar_user_prof_ar_user_id_ed932357_fk_account_a` FOREIGN KEY (`ar_user_id`) REFERENCES `account_ar_user` (`id`),
  CONSTRAINT `account_ar_user_prof_aruserprofile_id_7baf24af_fk_account_a` FOREIGN KEY (`aruserprofile_id`) REFERENCES `account_aruserprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_ar_user_profile_permission`
--

LOCK TABLES `account_ar_user_profile_permission` WRITE;
/*!40000 ALTER TABLE `account_ar_user_profile_permission` DISABLE KEYS */;
INSERT INTO `account_ar_user_profile_permission` VALUES (2,14,1),(1,20,1),(3,21,1);
/*!40000 ALTER TABLE `account_ar_user_profile_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_arhelpcontect`
--

DROP TABLE IF EXISTS `account_arhelpcontect`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_arhelpcontect` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Page_name` varchar(50) NOT NULL,
  `Page_slug` varchar(250) DEFAULT NULL,
  `Topic` varchar(50) NOT NULL,
  `Description` longtext NOT NULL,
  `Information` longtext NOT NULL,
  `Linke_1` varchar(200) DEFAULT NULL,
  `Linke_2` varchar(200) DEFAULT NULL,
  `Linke_3` varchar(200) DEFAULT NULL,
  `create_dt` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `account_arhelpcontect_Page_slug_8000ba52_uniq` (`Page_slug`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_arhelpcontect`
--

LOCK TABLES `account_arhelpcontect` WRITE;
/*!40000 ALTER TABLE `account_arhelpcontect` DISABLE KEYS */;
INSERT INTO `account_arhelpcontect` VALUES (1,'Dashboard','dashboard','Dashboard','Dashboard Page','This Page Provides All Details.','http://203.190.153.20/dashboard','http://203.190.153.20/','http://203.190.153.20/','2020-01-27 13:16:48.000000'),(2,'products-view','products-view','product view','Dashboard Page','This Page Provides All Details.','http://203.190.153.20/products-view','http://203.190.153.20/products-view','http://203.190.153.20/','2020-01-27 13:22:44.000000'),(3,'backlog-view','backlog-view','backlog view','This Page Provides All Details.','This Page Provides All Details.','http://203.190.153.20','http://203.190.153.20','http://203.190.153.20','2020-01-27 13:28:26.000000'),(4,'user-story-view','user-story-view','user-story-view','Dashboard Page','This Page Provides All Details.','http://203.190.153.20','http://203.190.153.20','http://203.190.153.20','2020-01-27 13:30:25.000000'),(5,'iteration-view','iteration-view','iteration-view','iteration-view','iteration-view','http://203.190.153.20/','http://203.190.153.20/','http://203.190.153.20/','2020-01-27 13:30:52.000000'),(6,'user-profile','user-profile','user-profile','Dashboard Page','This Page Provides All Details.','http://203.190.153.20/','http://203.190.153.20/','http://203.190.153.20/','2020-01-27 13:31:37.000000'),(7,'invite-user','invite-user','invite-user','Dashboard Page','This Page Provides All Details.','http://203.190.153.20/','http://203.190.153.20/','http://203.190.153.20/','2020-01-27 13:35:45.000000'),(8,'manage-epic-capabilities','manage-epic-capabilities','manage-epic-capabilities','Dashboard Page','This Page Provides All Details.','http://203.190.153.20/','http://203.190.153.20/','http://203.190.153.20/','2020-01-27 13:36:32.000000'),(9,'manage-feature','manage-feature','manage-feature','Dashboard Page','This Page Provides All Details.','http://203.190.153.20/','http://203.190.153.20/','http://203.190.153.20/','2020-01-27 13:40:41.000000'),(10,'manage-products','manage-products','manage-products','Dashboard Page','This Page Provides All Details.','http://203.190.153.20/','http://203.190.153.20/','http://203.190.153.20/','2020-01-27 13:40:53.000000'),(11,'manage-team','manage-team','manage-team','Dashboard Page','This Page Provides All Details.','http://203.190.153.20/','http://203.190.153.20/','http://203.190.153.20/','2020-01-27 13:41:18.000000'),(12,'manage-team-member','manage-team-member','manage-team-member','Dashboard Page','This Page Provides All Details.','http://203.190.153.20/','http://203.190.153.20/','http://203.190.153.20/','2020-01-27 13:42:32.000000'),(13,'manage-backlog','manage-backlog','manage-backlog','Dashboard Page','This Page Provides All Details.','http://203.190.153.20/','http://203.190.153.20/','http://203.190.153.20/','2020-01-27 13:42:46.000000'),(14,'manage-iteration','manage-iteration','manage-iteration','Dashboard Page','This Page Provides All Details.','http://203.190.153.20/','http://203.190.153.20/','http://203.190.153.20/','2020-01-27 13:43:04.000000'),(15,'manage-role','manage-role','manage-role','Dashboard Page','This Page Provides All Details.','http://203.190.153.20/','http://203.190.153.20/','http://203.190.153.20/','2020-01-27 13:43:11.000000'),(16,'manage-goals','manage-goals','manage-goals','Dashboard Page','This Page Provides All Details.','http://203.190.153.20/','http://203.190.153.20/','http://203.190.153.20/','2020-01-27 13:43:37.000000'),(17,'manage-benefits','manage-benefits','manage-benefits','Dashboard Page','This Page Provides All Details.','http://203.190.153.20/','http://203.190.153.20/','http://203.190.153.20/','2020-01-27 13:43:56.000000'),(18,'user-story-points','user-story-points','user-story-points','Dashboard Page','This Page Provides All Details.','http://203.190.153.20/','http://203.190.153.20/','http://203.190.153.20/','2020-01-27 13:44:15.000000'),(19,'account-settings','account-settings','account-settings','Dashboard Page','This Page Provides All Details.','http://203.190.153.20/','http://203.190.153.20/','http://203.190.153.20/','2020-01-27 13:45:01.000000'),(20,'user-profile/add-profile','user-profile/add-profile','Add Profile','Dashboard Page user-profile/add-profile','This Page Provides All Details. user-profile/add-profile','http://203.190.153.20/','http://203.190.153.20/','http://203.190.153.20/','2020-01-27 14:59:58.000000'),(21,'manage-epic-capabilities/add-epic-capabilities','manage-epic-capabilities/add-epic-capabilities','manage-epic-capabilities/add-epic-capabilities','Description','Information.','http://203.190.153.20/','http://203.190.153.20/','http://203.190.153.20/','2020-01-27 15:12:01.000000'),(22,'manage-iteration/add-iteration','manage-iteration/add-iteration','add iterationv','Description add iteration','Information. add iteration','http://203.190.153.20/','http://203.190.153.20/','http://203.190.153.20/','2020-01-27 15:15:22.000000');
/*!40000 ALTER TABLE `account_arhelpcontect` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_arshowcolumns`
--

DROP TABLE IF EXISTS `account_arshowcolumns`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_arshowcolumns` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Table_name` varchar(50) NOT NULL,
  `columnName` longtext NOT NULL,
  `ORG_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `account_arshowcolumns_user_id_57f94786_fk_account_ar_user_id` (`user_id`),
  KEY `account_arshowcolumn_ORG_id_75c98cc2_fk_account_a` (`ORG_id`),
  CONSTRAINT `account_arshowcolumn_ORG_id_75c98cc2_fk_account_a` FOREIGN KEY (`ORG_id`) REFERENCES `account_ar_organization` (`id`),
  CONSTRAINT `account_arshowcolumns_user_id_57f94786_fk_account_ar_user_id` FOREIGN KEY (`user_id`) REFERENCES `account_ar_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_arshowcolumns`
--

LOCK TABLES `account_arshowcolumns` WRITE;
/*!40000 ALTER TABLE `account_arshowcolumns` DISABLE KEYS */;
INSERT INTO `account_arshowcolumns` VALUES (1,'AR_PRODUCT','Team_parent,Children_backlog_list,Product_name,Product_description,Business_unit,Product_size,Product_score,US_quality_threshold,ORG_ID,create_by,create_dt,update_by,update_dt,capability,feature',1,1),(2,'AR_BACKLOG','team_list,product_parent,title,children_us_list,owner,backlog_score,Backlog_size,BL_STATUS,ORG_ID,created_by,created_dt,updated_by,updated_dt',1,1),(3,'AR_USER_STORY','backlog_parent,owner,title,story_tri_part_text,acceptance_criteria,ac_readability_score,conversation,convo_readability_score,attachments,autoscoring_on,archive_indicator,readiness_quality_score,story_points,user_story_status,ORG_id,UST_ID,ar_user,created_by,created_dt,updated_by,updated_dt',1,20),(4,'ArIterations','IterationId,IterationName,Product,Backlog,owner,StartDate,EndDate,Description,UserStory,Team,IterationScore,IterationSize,ORG_ID,create_by,create_dt,update_by,update_dt',1,1);
/*!40000 ALTER TABLE `account_arshowcolumns` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_aruserprofile`
--

DROP TABLE IF EXISTS `account_aruserprofile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_aruserprofile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `profile_key` varchar(50) NOT NULL,
  `create_dt` datetime(6) NOT NULL,
  `update_dt` datetime(6) NOT NULL,
  `ORG_ID_id` int(11) DEFAULT NULL,
  `create_by_id` int(11) NOT NULL,
  `update_by_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `account_aruserprofile_create_by_id_5d5f4148_fk_auth_user_id` (`create_by_id`),
  KEY `account_aruserprofile_update_by_id_aceb0d9d_fk_auth_user_id` (`update_by_id`),
  KEY `account_aruserprofil_ORG_ID_id_7ece99ca_fk_account_a` (`ORG_ID_id`),
  CONSTRAINT `account_aruserprofil_ORG_ID_id_7ece99ca_fk_account_a` FOREIGN KEY (`ORG_ID_id`) REFERENCES `account_ar_organization` (`id`),
  CONSTRAINT `account_aruserprofile_create_by_id_5d5f4148_fk_auth_user_id` FOREIGN KEY (`create_by_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `account_aruserprofile_update_by_id_aceb0d9d_fk_auth_user_id` FOREIGN KEY (`update_by_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_aruserprofile`
--

LOCK TABLES `account_aruserprofile` WRITE;
/*!40000 ALTER TABLE `account_aruserprofile` DISABLE KEYS */;
INSERT INTO `account_aruserprofile` VALUES (1,'producer','2020-03-04 15:26:21.739724','2020-03-04 15:26:21.739734',1,2,2);
/*!40000 ALTER TABLE `account_aruserprofile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_aruserprofilepermission`
--

DROP TABLE IF EXISTS `account_aruserprofilepermission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_aruserprofilepermission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `activites` varchar(80) NOT NULL,
  `editor` tinyint(1) NOT NULL,
  `viewer` tinyint(1) NOT NULL,
  `create_dt` datetime(6) NOT NULL,
  `update_dt` datetime(6) NOT NULL,
  `ORG_ID_id` int(11) DEFAULT NULL,
  `create_by_id` int(11) NOT NULL,
  `profile_key_id` int(11) DEFAULT NULL,
  `update_by_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `account_aruserprofil_create_by_id_21f94912_fk_auth_user` (`create_by_id`),
  KEY `account_aruserprofil_update_by_id_4e77d715_fk_auth_user` (`update_by_id`),
  KEY `account_aruserprofil_ORG_ID_id_ab5acdc3_fk_account_a` (`ORG_ID_id`),
  KEY `account_aruserprofil_profile_key_id_54a344a1_fk_account_a` (`profile_key_id`),
  CONSTRAINT `account_aruserprofil_ORG_ID_id_ab5acdc3_fk_account_a` FOREIGN KEY (`ORG_ID_id`) REFERENCES `account_ar_organization` (`id`),
  CONSTRAINT `account_aruserprofil_create_by_id_21f94912_fk_auth_user` FOREIGN KEY (`create_by_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `account_aruserprofil_profile_key_id_54a344a1_fk_account_a` FOREIGN KEY (`profile_key_id`) REFERENCES `account_aruserprofile` (`id`),
  CONSTRAINT `account_aruserprofil_update_by_id_4e77d715_fk_auth_user` FOREIGN KEY (`update_by_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_aruserprofilepermission`
--

LOCK TABLES `account_aruserprofilepermission` WRITE;
/*!40000 ALTER TABLE `account_aruserprofilepermission` DISABLE KEYS */;
INSERT INTO `account_aruserprofilepermission` VALUES (1,'Product View',0,1,'2020-03-04 15:27:17.309840','2020-03-04 15:33:44.198051',1,2,1,2),(2,'Backlog View',0,1,'2020-03-04 15:27:17.313664','2020-03-04 15:33:44.202866',1,2,1,2),(3,'User Story View',0,1,'2020-03-04 15:27:17.332925','2020-03-04 15:33:44.212556',1,2,1,2),(4,'Iteration View',0,1,'2020-03-04 15:27:17.342727','2020-03-04 15:33:44.222165',1,2,1,2),(5,'Invite New User',1,1,'2020-03-04 15:27:17.352037','2020-03-04 15:33:44.232210',1,2,1,2),(6,'Manage Epic Capability',0,1,'2020-03-04 15:27:17.361723','2020-03-04 15:33:44.241799',1,2,1,2),(7,'Manage Features',0,1,'2020-03-04 15:27:17.371301','2020-03-04 15:33:44.251484',1,2,1,2),(8,'Manage Products',0,1,'2020-03-04 15:27:17.381055','2020-03-04 15:33:44.261202',1,2,1,2),(9,'Manage Teams',0,1,'2020-03-04 15:27:17.390653','2020-03-04 15:33:44.270876',1,2,1,2),(10,'Manage Team Members',1,1,'2020-03-04 15:27:17.400318','2020-03-04 15:33:44.280506',1,2,1,2),(11,'Manage Backlogs',0,1,'2020-03-04 15:27:17.410040','2020-03-04 15:33:44.290226',1,2,1,2),(12,'Manage Iterations',0,1,'2020-03-04 15:27:17.419609','2020-03-04 15:33:44.299918',1,2,1,2),(13,'Manage Roles',0,1,'2020-03-04 15:27:17.429097','2020-03-04 15:33:44.309337',1,2,1,2),(14,'Manage Goals',0,1,'2020-03-04 15:27:17.438881','2020-03-04 15:33:44.318947',1,2,1,2),(15,'Manage Benefits',0,1,'2020-03-04 15:27:17.448496','2020-03-04 15:33:44.328574',1,2,1,2),(16,'Manage User Story Points',0,1,'2020-03-04 15:27:17.458028','2020-03-04 15:33:44.338342',1,2,1,2),(17,'Manage Import Data',0,1,'2020-03-04 15:27:17.467539','2020-03-04 15:33:44.347935',1,2,1,2),(18,'Manage Export Data',0,1,'2020-03-04 15:27:17.477112','2020-03-04 15:33:44.357554',1,2,1,2);
/*!40000 ALTER TABLE `account_aruserprofilepermission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_aruserstoryscoringpoints`
--

DROP TABLE IF EXISTS `account_aruserstoryscoringpoints`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_aruserstoryscoringpoints` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Score_key` varchar(50) NOT NULL,
  `Score_for` varchar(50) NOT NULL,
  `Keyword` longtext NOT NULL,
  `Last_Update` datetime(6) NOT NULL,
  `Score_one` int(11) NOT NULL,
  `Score_three` int(11) NOT NULL,
  `Score_two` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_aruserstoryscoringpoints`
--

LOCK TABLES `account_aruserstoryscoringpoints` WRITE;
/*!40000 ALTER TABLE `account_aruserstoryscoringpoints` DISABLE KEYS */;
INSERT INTO `account_aruserstoryscoringpoints` VALUES (4,'Conjunction Set','Unitary Scoring Points','for, and, nor, but, yet, after, although, because since, than, though, unless, until, whenever whereas, wherever, while','2020-01-23 11:12:24.000000',10,1,5),(5,'Role_text','Component Scoring Points Table','Developer, Technical Lead, Product Owner, Scrum Master, Manager, Project Manager, Product Manager, Business Person, Business Man, Business Woman, Man, Woman, Child, System, Admin, System Admin, Operator, Merchant, Cardholder, Site Member','2020-01-23 11:34:04.000000',10,0,2),(6,'Goal_text','Component Scoring Points Table','Read, write, post, reconcile','2020-01-23 11:34:45.000000',10,0,2),(7,'Benefit_text','Component Scoring Points Table','Learn, adapt, view, understand','2020-01-23 11:35:30.000000',5,0,1),(8,'Role_Tag','Component Scoring Points Table','As a, As an','2020-01-24 07:15:05.000000',15,0,0),(9,'Goal_Tag','Component Scoring Points Table','I want , I require , I need','2020-01-24 07:16:45.000000',15,0,0),(10,'Benefit_Tag','Component Scoring Points Table','so That','2020-01-24 07:17:44.000000',10,0,0);
/*!40000 ALTER TABLE `account_aruserstoryscoringpoints` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_csvfilesuplodaded`
--

DROP TABLE IF EXISTS `account_csvfilesuplodaded`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_csvfilesuplodaded` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `attachments` varchar(100) NOT NULL,
  `csvUseFor` varchar(50) NOT NULL,
  `updated_dt` datetime(6) NOT NULL,
  `created_dt` datetime(6) NOT NULL,
  `ORG_ID_id` int(11) DEFAULT NULL,
  `created_by_id` int(11) NOT NULL,
  `updated_by_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `account_csvfilesuplo_created_by_id_eab0986a_fk_account_a` (`created_by_id`),
  KEY `account_csvfilesuplo_updated_by_id_5664403f_fk_account_a` (`updated_by_id`),
  KEY `account_csvfilesuplo_ORG_ID_id_2f9f0576_fk_account_a` (`ORG_ID_id`),
  CONSTRAINT `account_csvfilesuplo_ORG_ID_id_2f9f0576_fk_account_a` FOREIGN KEY (`ORG_ID_id`) REFERENCES `account_ar_organization` (`id`),
  CONSTRAINT `account_csvfilesuplo_created_by_id_eab0986a_fk_account_a` FOREIGN KEY (`created_by_id`) REFERENCES `account_ar_user` (`id`),
  CONSTRAINT `account_csvfilesuplo_updated_by_id_5664403f_fk_account_a` FOREIGN KEY (`updated_by_id`) REFERENCES `account_ar_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_csvfilesuplodaded`
--

LOCK TABLES `account_csvfilesuplodaded` WRITE;
/*!40000 ALTER TABLE `account_csvfilesuplodaded` DISABLE KEYS */;
/*!40000 ALTER TABLE `account_csvfilesuplodaded` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_notification`
--

DROP TABLE IF EXISTS `account_notification`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_notification` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `page_name` varchar(50) NOT NULL,
  `notification_key` varchar(50) NOT NULL,
  `notification_desc` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=154 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_notification`
--

LOCK TABLES `account_notification` WRITE;
/*!40000 ALTER TABLE `account_notification` DISABLE KEYS */;
INSERT INTO `account_notification` VALUES (1,'Manage Epic Capability','Add','Epic capability added successfully ! '),(2,'Manage Epic Capability','Remove_error','Oops! This capability likely has features attached to it and is unable to be deleted. If you want to delete this capability, please delete all attached features. '),(3,'User Story View','choose_columns','Do you want to rearrange column order ? '),(4,'Manage Feature','Remove_error','Oops! This feature likely has features attached to it and is unable to be deleted. If you want to delete this feature, please delete all attached features. '),(5,'Manage Products','Remove_error','Oops! This product likely has features attached to it and is unable to be deleted. If you want to delete this product, please delete all attached features. '),(6,'Manage Team','Remove_error','Oops! This team likely has features attached to it and is unable to be deleted. If you want to delete this team, please delete all attached features. '),(7,'Manage Team Members','Remove_error','Oops! This team member likely has features attached to it and is unable to be deleted. If you want to delete this team member, please delete all attached features. '),(8,'Manage Backlog','Remove_error','Oops! This backlog likely has features attached to it and is unable to be deleted. If you want to delete this backlog, please delete all attached features. '),(9,'Manage Iteration','Remove_error','Oops! This iteration likely has features attached to it and is unable to be deleted. If you want to delete this iteration, please delete all attached features. '),(10,'Manage Role','Remove_error','Oops! This role likely has features attached to it and is unable to be deleted. If you want to delete this role, please delete all attached features. '),(11,'Manage Goal','Remove_error','Oops! This goal likely has features attached to it and is unable to be deleted. If you want to delete this goal, please delete all attached features. '),(12,'Manage Benefit','Remove_error','Oops! This benefit likely has features attached to it and is unable to be deleted. If you want to delete this benefit, please delete all attached features.  '),(13,'Manage User Story Points','Remove_error','Oops! This story point likely has features attached to it and is unable to be deleted. If you want to delete this story point, please delete all attached features. '),(14,'View Products','choose_columns','Do you want to rearrange column order ? '),(15,'Backlog View','choose_columns','Do you want to rearrange column order ? '),(16,'Iteration View','choose_columns','Do you want to rearrange column order ? '),(17,'Manage Feature','Add','Feature added successfully ! '),(18,'Manage Products','Add','Product added successfully ! '),(19,'Manage Team','Add','Team added successfully ! '),(20,'Manage Team Members','Add','Team Members added successfully ! '),(21,'Manage Backlog','Add','Backlog added successfully ! '),(22,'Manage Iteration','Add','Iteration added successfully ! '),(23,'Manage Role','Add','Role added successfully ! '),(24,'Manage Goal','Add','Goal added successfully ! '),(25,'Manage Benefit','Add','Benefit added successfully ! '),(26,'Manage User Story Points','Add','User story points added successfully ! '),(27,'Manage Epic Capability','Remove','Epic capability removed ! '),(28,'Manage Feature','Remove','Feature removed ! '),(29,'Manage Products','Remove','Product removed ! '),(30,'Manage Team','Remove','Team removed ! '),(31,'Manage Team Members','Remove','Team members removed ! '),(32,'Manage Backlog','Remove','Backlog removed ! '),(33,'Manage Iteration','Remove','Iteration removed ! '),(34,'Manage Role','Remove','Role removed ! '),(35,'Manage Goal','Remove','Goal removed ! '),(36,'Manage Benefit','Remove','Benefit removed ! '),(37,'Manage User Story Points','Remove','User story points removed ! '),(38,'Manage Epic Capability','Update','Epic capability update successfully ! '),(39,'Manage Feature','Update','Feature update successfully ! '),(40,'Manage Products','Update','Product update successfully ! '),(41,'Manage Team','Update','Team update successfully ! '),(42,'Manage Team Members','Update','Team members update successfully ! '),(43,'Manage Backlog','Update','Backlog update successfully ! '),(44,'Manage Iteration','Update','Iteration update successfully ! '),(45,'Manage Role','Update','Role update successfully ! '),(46,'Manage Goal','Update','Goal update successfully ! '),(47,'Manage Benefit','Update','Benefit update successfully ! '),(48,'Manage User Story Points','Update','User story points update successfully ! '),(49,'Manage Backlog','Exists','Backlog already exists. '),(50,'Manage Backlog','Permission','You don\'t have permission for manage backlog ! '),(51,'Manage Backlog','Rearrange','Table column order rearranged successfully.'),(52,'Manage Epic Capability','Exists','Epic capability already exists. '),(53,'Manage Feature','Exists','Feature already exists. '),(54,'Manage Products','Exists','Product already exists.'),(55,'Manage Team','Exists','Team already exists. '),(56,'Manage Team Members','Exists','Team Members already exists. '),(57,'Manage Iteration','Exists','Iteration already exists. '),(58,'Manage Role','Exists','Role already exists. '),(59,'Manage Goal','Exists','Goal already exists. '),(60,'Manage Benefit','Exists','Benefit already exists. '),(61,'Manage User Story Points','Exists','User story points already exists. '),(62,'Manage Epic Capability','Permission','You don\'t have permission for manage epic capability ! '),(63,'Manage Feature','Permission','You don\'t have permission for manage feature ! '),(64,'Manage Products','Permission','You don\'t have permission for manage product !'),(65,'Manage Team','Permission','You don\'t have permission for manage team ! '),(66,'Manage Team Members','Permission','You don\'t have permission for manage team members !  '),(67,'Manage Iteration','Permission','You don\'t have permission for manage iteration ! '),(68,'Manage Role','Permission','You don\'t have permission for manage role ! '),(69,'Manage Goal','Permission','You don\'t have permission for manage goal ! '),(70,'Manage Benefit','Permission','You don\'t have permission for manage benefit ! '),(71,'Manage User Story Points','Permission','You don\'t have permission for manage user story points ! '),(72,'User Story View','Rearrange','Table column order rearranged successfully.'),(73,'View Products','Rearrange','Table column order rearranged successfully.'),(74,'Manage Iteration','Rearrange','Table column order rearranged successfully.'),(75,'User Story View','Exists','User story already exists. '),(76,'E mail','Exists','E-mail already exists !'),(77,'User Story View','Update','User story update successfully ! '),(78,'User Story View','Remove','User story removed ! '),(79,'User Story View','Add','User story added successfully ! '),(80,'User Story View','Remove_error','Oops! This user story likely has features attached to it and is unable to be deleted. If you want to delete this user story, please delete all attached features. '),(81,'Manage User Profile','Permission','You don\'t have permission for manage user profile ! '),(82,'Manage User Profile','Update','User profile update successfully ! '),(83,'Manage User Profile','Remove','User profile removed ! '),(84,'Manage User Profile Permissions','Add','User profile permissions added successfully !'),(85,'Manage User Profile','Remove_error','Oops! This user profile likely has features attached to it and is unable to be deleted. If you want to delete this user profile , please delete all attached features. '),(86,'Manage User Profile','Exists','User profile already exists. '),(87,'authorized','authorized','Warning! You are not authorized person. '),(88,'Phone','Exists','Phone no. is already exists ! '),(89,'Organization Url','Exists','Organization URL is already exists ! '),(90,'Registration','Done','Registration successful, verification link is sent to your registered email '),(91,'Account Settings','Done','Profile updated successfully !'),(92,'Account Settings','Not Done','Profile not updated !'),(93,'Feedback','Send','Feedback send successfully !'),(95,'Manage Epic Capability','Remove Request','Do you want to remove this epic capability ?'),(96,'User Story View','Remove Request','Do you want to remove this user story view ?'),(97,'Manage Feature','Remove Request','Do you want to remove this feature ?'),(98,'Manage Products','Remove Request','Do you want to remove this product ?'),(99,'Manage Team','Remove Request','Do you want to remove this team ?'),(100,'Manage Team Members','Remove Request','Do you want to remove this team members ?'),(101,'Manage Backlog','Remove Request','Do you want to remove this backlog ?'),(102,'Manage Iteration','Remove Request','Do you want to remove this iteration ?'),(103,'Manage Role','Remove Request','Do you want to remove this role ?'),(104,'Manage Goal','Remove Request','Do you want to remove this goal ?'),(105,'Manage Benefit','Remove Request','Do you want to remove this benefit ?'),(106,'Manage User Story Points','Remove Request','Do you want to remove this user story points ?'),(107,'Manage User Story Points','Not_Remove','User story points not removed.'),(108,'Manage Benefit','Not_Remove','Benefit not removed.'),(109,'Manage Goal','Not_Remove','Goal not removed.'),(110,'Manage Role','Not_Remove','Role not removed.'),(111,'Manage Iteration','Not_Remove','Iteration not removed.'),(112,'Manage Backlog','Not_Remove','Backlog not removed.'),(113,'Manage Team Members','Not_Remove','Team members not removed.'),(114,'Manage Team','Not_Remove','Team not removed.'),(115,'Manage Products','Not_Remove','Product not removed.'),(116,'Manage Feature','Not_Remove','Feature not removed.'),(117,'User Story View','Not_Remove','User story view not removed.'),(118,'Manage Epic Capability','Not_Remove','Epic capability not removed.'),(119,'Manage Epic Capability','Remove_Success','Epic capability removed successfully '),(120,'User Story View','Remove_Success','User story view removed successfully.'),(121,'Manage Feature','Remove_Success','Feature removed successfully.'),(122,'Manage Products','Remove_Success','Product removed successfully.'),(123,'Manage Team','Remove_Success','Team removed successfully.'),(124,'Manage Team Members','Remove_Success','Team members removed successfully.'),(125,'Manage Backlog','Remove_Success','Backlog removed successfully.'),(126,'Manage Iteration','Remove_Success','Iteration removed successfully.'),(127,'Manage Role','Remove_Success','Role removed successfully.'),(128,'Manage Goal','Remove_Success','Goal removed successfully.'),(129,'Manage Benefit','Remove_Success','Benefit removed successfully.'),(130,'Manage User Story Points','Remove_Success','User story points removed successfully.'),(131,'Authorized','Error','You are not authorized person. ! '),(132,'Sign_Up','Send','Link is send to your email id !'),(133,'Sign_Up','Not_Send','Email is not registered !'),(134,'Manage Iteration','Rearrange_Request','Do you want to rearrange column order ?'),(135,'User Story View','Rearrange_Request','Do you want to rearrange column order ?'),(136,'Manage Backlog','Rearrange_Request','Do you want to rearrange column order ?'),(137,'Manage Products','Rearrange_Request','Do you want to rearrange column order ? '),(138,'User Story View','Copy_Request','Do you want to created copy of selected Stories ?'),(139,'Manage User Profile','Not_Remove','User profile view not removed.'),(140,'Manage User Profile','Remove Request','Do you want to remove this user profile ?'),(141,'Manage User Profile','Remove_Success','User profile points removed successfully.'),(142,'Invitation','Sent','Invitation link has been sent to'),(143,'Invitation','NOt_Sent','Invalid E-mail !'),(144,'Login','Not_Active_Root','Your account is not active please contact with your root admin.'),(145,'Login','Not_Active','Username and password is incorrect & maybe your account is not activate click <b style=\'color:#03a9f4\' data-toggle=\'modal\'  data-target=\'#varification_ling\'>here</b> to get the verification link !'),(146,'User Story View','Copy_Story','Select the story if you want to create a copy ! '),(147,'Manage User Profile Permissions','Update','User profile permissions updated !'),(148,'Import_file','Not_related','This CSV file is not related to your organization.'),(149,'Import_file','Invalid_file','This  is not a CSV file.'),(150,'Import_file','upload','CSV Uploaded successfully !'),(151,'Import_file','Invalid Name','Invalid name please rename file.'),(152,'Manage Team Members','change_root_user','Root user change successfully.'),(153,'Account Settings','data_reset_done','All table data reset successfully.');
/*!40000 ALTER TABLE `account_notification` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=145 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add attachment',7,'add_attachment'),(26,'Can change attachment',7,'change_attachment'),(27,'Can delete attachment',7,'delete_attachment'),(28,'Can view attachment',7,'view_attachment'),(29,'Can add a r_organization_status',8,'add_ar_organization_status'),(30,'Can change a r_organization_status',8,'change_ar_organization_status'),(31,'Can delete a r_organization_status',8,'delete_ar_organization_status'),(32,'Can view a r_organization_status',8,'view_ar_organization_status'),(33,'Can add a r_organization',9,'add_ar_organization'),(34,'Can change a r_organization',9,'change_ar_organization'),(35,'Can delete a r_organization',9,'delete_ar_organization'),(36,'Can view a r_organization',9,'view_ar_organization'),(37,'Can add ar user profile',10,'add_aruserprofile'),(38,'Can change ar user profile',10,'change_aruserprofile'),(39,'Can delete ar user profile',10,'delete_aruserprofile'),(40,'Can view ar user profile',10,'view_aruserprofile'),(41,'Can add ar user profile permission',11,'add_aruserprofilepermission'),(42,'Can change ar user profile permission',11,'change_aruserprofilepermission'),(43,'Can delete ar user profile permission',11,'delete_aruserprofilepermission'),(44,'Can view ar user profile permission',11,'view_aruserprofilepermission'),(45,'Can add ar_user',12,'add_ar_user'),(46,'Can change ar_user',12,'change_ar_user'),(47,'Can delete ar_user',12,'delete_ar_user'),(48,'Can view ar_user',12,'view_ar_user'),(49,'Can add ar showcolumns',13,'add_arshowcolumns'),(50,'Can change ar showcolumns',13,'change_arshowcolumns'),(51,'Can delete ar showcolumns',13,'delete_arshowcolumns'),(52,'Can view ar showcolumns',13,'view_arshowcolumns'),(53,'Can add csv files uplodaded',14,'add_csvfilesuplodaded'),(54,'Can change csv files uplodaded',14,'change_csvfilesuplodaded'),(55,'Can delete csv files uplodaded',14,'delete_csvfilesuplodaded'),(56,'Can view csv files uplodaded',14,'view_csvfilesuplodaded'),(57,'Can add notification',15,'add_notification'),(58,'Can change notification',15,'change_notification'),(59,'Can delete notification',15,'delete_notification'),(60,'Can view notification',15,'view_notification'),(61,'Can add ar user story scoring points',16,'add_aruserstoryscoringpoints'),(62,'Can change ar user story scoring points',16,'change_aruserstoryscoringpoints'),(63,'Can delete ar user story scoring points',16,'delete_aruserstoryscoringpoints'),(64,'Can view ar user story scoring points',16,'view_aruserstoryscoringpoints'),(65,'Can add ar help contect',17,'add_arhelpcontect'),(66,'Can change ar help contect',17,'change_arhelpcontect'),(67,'Can delete ar help contect',17,'delete_arhelpcontect'),(68,'Can view ar help contect',17,'view_arhelpcontect'),(69,'Can add a r_u s_status',18,'add_ar_us_status'),(70,'Can change a r_u s_status',18,'change_ar_us_status'),(71,'Can delete a r_u s_status',18,'delete_ar_us_status'),(72,'Can view a r_u s_status',18,'view_ar_us_status'),(73,'Can add a r_u s_type',19,'add_ar_us_type'),(74,'Can change a r_u s_type',19,'change_ar_us_type'),(75,'Can delete a r_u s_type',19,'delete_ar_us_type'),(76,'Can view a r_u s_type',19,'view_ar_us_type'),(77,'Can add a r_use r_story',20,'add_ar_user_story'),(78,'Can change a r_use r_story',20,'change_ar_user_story'),(79,'Can delete a r_use r_story',20,'delete_ar_user_story'),(80,'Can view a r_use r_story',20,'view_ar_user_story'),(81,'Can add a r_team',21,'add_ar_team'),(82,'Can change a r_team',21,'change_ar_team'),(83,'Can delete a r_team',21,'delete_ar_team'),(84,'Can view a r_team',21,'view_ar_team'),(85,'Can add a r_product',22,'add_ar_product'),(86,'Can change a r_product',22,'change_ar_product'),(87,'Can delete a r_product',22,'delete_ar_product'),(88,'Can view a r_product',22,'view_ar_product'),(89,'Can add a r_epi c_capability',23,'add_ar_epic_capability'),(90,'Can change a r_epi c_capability',23,'change_ar_epic_capability'),(91,'Can delete a r_epi c_capability',23,'delete_ar_epic_capability'),(92,'Can view a r_epi c_capability',23,'view_ar_epic_capability'),(93,'Can add a r_feature',24,'add_ar_feature'),(94,'Can change a r_feature',24,'change_ar_feature'),(95,'Can delete a r_feature',24,'delete_ar_feature'),(96,'Can view a r_feature',24,'view_ar_feature'),(97,'Can add cms_manage',25,'add_cms_manage'),(98,'Can change cms_manage',25,'change_cms_manage'),(99,'Can delete cms_manage',25,'delete_cms_manage'),(100,'Can view cms_manage',25,'view_cms_manage'),(101,'Can add a r_backlo g_status',26,'add_ar_backlog_status'),(102,'Can change a r_backlo g_status',26,'change_ar_backlog_status'),(103,'Can delete a r_backlo g_status',26,'delete_ar_backlog_status'),(104,'Can view a r_backlo g_status',26,'view_ar_backlog_status'),(105,'Can add a r_backlog',27,'add_ar_backlog'),(106,'Can change a r_backlog',27,'change_ar_backlog'),(107,'Can delete a r_backlog',27,'delete_ar_backlog'),(108,'Can view a r_backlog',27,'view_ar_backlog'),(109,'Can add ar iterations',28,'add_ariterations'),(110,'Can change ar iterations',28,'change_ariterations'),(111,'Can delete ar iterations',28,'delete_ariterations'),(112,'Can view ar iterations',28,'view_ariterations'),(113,'Can add ar role',29,'add_arrole'),(114,'Can change ar role',29,'change_arrole'),(115,'Can delete ar role',29,'delete_arrole'),(116,'Can view ar role',29,'view_arrole'),(117,'Can add ar user story points',30,'add_aruserstorypoints'),(118,'Can change ar user story points',30,'change_aruserstorypoints'),(119,'Can delete ar user story points',30,'delete_aruserstorypoints'),(120,'Can view ar user story points',30,'view_aruserstorypoints'),(121,'Can add ar feedback',31,'add_arfeedback'),(122,'Can change ar feedback',31,'change_arfeedback'),(123,'Can delete ar feedback',31,'delete_arfeedback'),(124,'Can view ar feedback',31,'view_arfeedback'),(125,'Can add ar manage goals',32,'add_armanagegoals'),(126,'Can change ar manage goals',32,'change_armanagegoals'),(127,'Can delete ar manage goals',32,'delete_armanagegoals'),(128,'Can view ar manage goals',32,'view_armanagegoals'),(129,'Can add ar manage benefits',33,'add_armanagebenefits'),(130,'Can change ar manage benefits',33,'change_armanagebenefits'),(131,'Can delete ar manage benefits',33,'delete_armanagebenefits'),(132,'Can view ar manage benefits',33,'view_armanagebenefits'),(133,'Can add export_data_info',34,'add_export_data_info'),(134,'Can change export_data_info',34,'change_export_data_info'),(135,'Can delete export_data_info',34,'delete_export_data_info'),(136,'Can view export_data_info',34,'view_export_data_info'),(137,'Can add import_files_data',35,'add_import_files_data'),(138,'Can change import_files_data',35,'change_import_files_data'),(139,'Can delete import_files_data',35,'delete_import_files_data'),(140,'Can view import_files_data',35,'view_import_files_data'),(141,'Can add dommy_data',36,'add_dommy_data'),(142,'Can change dommy_data',36,'change_dommy_data'),(143,'Can delete dommy_data',36,'delete_dommy_data'),(144,'Can view dommy_data',36,'view_dommy_data');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$150000$kFBHjIWZR9oB$p/O3yBlt4GlEeO+1lDRCG1qkdtYNSB8jVmYXu2aTyUo=','2020-03-07 12:50:17.860880',1,'be@agile+ready','Tony','Timbol','info@agileready.net',1,1,'2020-03-04 09:57:10.000000'),(2,'pbkdf2_sha256$150000$q6I0IUbyxcCW$bnKQbNDl+6scVuIa9qpjh2/f4yoaA78Co6wHPp3hKdE=','2020-03-07 13:21:32.096434',0,'jitendra.n@digimonk.in','','','jitendra.n@digimonk.in',0,1,'2020-03-04 11:43:08.536279'),(15,'pbkdf2_sha256$150000$QIloJJIqJLKY$Mes8lzExNNlgR4b2sQP69Y0qchuBjKMU2Yz89FHA1tA=',NULL,0,'praveen.vaidhya@digimonk.in','','','praveen.vaidhya@digimonk.in',0,1,'2020-03-04 14:40:49.743911'),(16,'pbkdf2_sha256$150000$VXifltez0gub$slp18Y+tPLvTU7UvJCcTnCEyDqsSGqTxdgOvu/qXiCI=',NULL,0,'ravi.bhghel@digimonk.in','','','ravi.bhghel@digimonk.in',0,0,'2020-03-04 14:40:50.008371'),(17,'pbkdf2_sha256$150000$8sOtjQU8lA5n$qy3PWkiCgHMVJHvv6rjgTxB9Wf4I2pwm9KRpOmAZyrE=',NULL,0,'sagar.srivastava@digimonk.in','','','sagar.srivastava@digimonk.in',0,0,'2020-03-04 14:40:51.341670'),(18,'pbkdf2_sha256$150000$xotv02G5tJiZ$e1Tjq5mRH/14M8mjGL8wxHCHEbS3h614fXLRNONctyg=',NULL,0,'ravi.bhaghel@digimonk.in','','','ravi.bhaghel@digimonk.in',0,0,'2020-03-04 14:40:52.437846'),(19,'pbkdf2_sha256$150000$azUENahMzZYZ$RDq4UrTQzTxe2Qg1lVpWRsubTBrYRl3QBLRCHmfO6Wg=',NULL,0,'sagar.shrivastava@digimonk.in','','','sagar.shrivastava@digimonk.in',0,1,'2020-03-04 14:40:53.637334'),(20,'pbkdf2_sha256$150000$DwVwhaBljmOO$Lz9PPzE985t6F3zGoTLO4YN5D4djn9lWaENg3xXq14E=',NULL,0,'ravi.baghel@digimonk.in','','','ravi.baghel@digimonk.in',0,1,'2020-03-04 14:40:53.754732'),(21,'pbkdf2_sha256$150000$2041V9ReGFe6$GMvNpUKWd439fmzcSCPgdfMmdpe9/fYwW+xU3vI2DpM=','2020-03-04 16:06:36.434145',0,'jitulodhi2010@gmail.com','','','jitulodhi2010@gmail.com',0,1,'2020-03-04 15:03:56.996810'),(22,'pbkdf2_sha256$150000$LA5OIVGVwaNI$GgkTQyoNUoZHehJdyCDF2YKPGpcsO1/NlOh03JaJnO8=','2020-03-05 00:59:56.141562',0,'ttimbol@comcast.net','','','ttimbol@comcast.net',0,1,'2020-03-05 00:59:17.987603'),(23,'pbkdf2_sha256$150000$891hAWQfl0DZ$8fBbtHC4Qzsuo5kR3WOlAeM2IV48o0uVvVat3eNHI1w=','2020-03-07 12:49:39.250757',0,'prod1_digi_admin','Digimonk','DjangoAdmin','harry@digimonk.in',1,1,'2020-03-07 12:43:13.000000'),(24,'pbkdf2_sha256$150000$QjX2ZPDkZxxf$jju7+fyWH48njwTdDglTtp8GmmxF84yCnuzjL5sok18=','2020-03-07 13:29:16.121014',1,'beagileready','','','deepak@digimonk.in',1,1,'2020-03-07 13:17:11.275470');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=143 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
INSERT INTO `auth_user_user_permissions` VALUES (1,23,1),(2,23,2),(3,23,3),(4,23,4),(5,23,5),(6,23,6),(7,23,7),(8,23,8),(9,23,9),(10,23,10),(11,23,11),(12,23,12),(13,23,13),(14,23,16),(15,23,17),(16,23,18),(17,23,19),(18,23,20),(19,23,21),(20,23,22),(21,23,23),(22,23,24),(23,23,25),(24,23,26),(25,23,27),(26,23,28),(27,23,29),(28,23,30),(29,23,31),(30,23,32),(31,23,33),(32,23,34),(33,23,35),(34,23,36),(35,23,37),(36,23,38),(37,23,39),(38,23,40),(39,23,41),(40,23,42),(41,23,43),(42,23,44),(43,23,45),(44,23,46),(45,23,47),(46,23,48),(47,23,49),(48,23,50),(49,23,51),(50,23,52),(51,23,53),(52,23,54),(53,23,55),(54,23,56),(55,23,57),(56,23,58),(57,23,59),(58,23,60),(59,23,61),(60,23,62),(61,23,63),(62,23,64),(63,23,65),(64,23,66),(65,23,67),(66,23,68),(67,23,69),(68,23,70),(69,23,71),(70,23,72),(71,23,73),(72,23,74),(73,23,75),(74,23,76),(75,23,77),(76,23,78),(77,23,79),(78,23,80),(79,23,81),(80,23,82),(81,23,83),(82,23,84),(83,23,85),(84,23,86),(85,23,87),(86,23,88),(87,23,89),(88,23,90),(89,23,91),(90,23,92),(91,23,93),(92,23,94),(93,23,95),(94,23,96),(95,23,97),(96,23,98),(97,23,99),(98,23,100),(99,23,101),(100,23,102),(101,23,103),(102,23,104),(103,23,105),(104,23,106),(105,23,107),(106,23,108),(107,23,109),(108,23,110),(109,23,111),(110,23,112),(111,23,113),(112,23,114),(113,23,115),(114,23,116),(115,23,117),(116,23,118),(117,23,119),(118,23,120),(119,23,121),(120,23,122),(121,23,123),(122,23,124),(123,23,125),(124,23,126),(125,23,127),(126,23,128),(127,23,129),(128,23,130),(129,23,131),(130,23,132),(131,23,133),(132,23,134),(133,23,135),(134,23,136),(135,23,137),(136,23,138),(137,23,139),(138,23,140),(139,23,141),(140,23,142),(141,23,143),(142,23,144);
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `data_import_export_dommy_data`
--

DROP TABLE IF EXISTS `data_import_export_dommy_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `data_import_export_dommy_data` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `files` varchar(100) NOT NULL,
  `file_name` varchar(50) NOT NULL,
  `file_data` longtext NOT NULL,
  `upload_status` tinyint(1) NOT NULL,
  `error_log` varchar(100) DEFAULT NULL,
  `created_date` datetime(6) NOT NULL,
  `priority` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `data_import_export_dommy_data`
--

LOCK TABLES `data_import_export_dommy_data` WRITE;
/*!40000 ALTER TABLE `data_import_export_dommy_data` DISABLE KEYS */;
/*!40000 ALTER TABLE `data_import_export_dommy_data` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `data_import_export_export_data_info`
--

DROP TABLE IF EXISTS `data_import_export_export_data_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `data_import_export_export_data_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `folder_name` varchar(50) NOT NULL,
  `files_name` longtext NOT NULL,
  `created_dt` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `data_import_export_export_data_info`
--

LOCK TABLES `data_import_export_export_data_info` WRITE;
/*!40000 ALTER TABLE `data_import_export_export_data_info` DISABLE KEYS */;
INSERT INTO `data_import_export_export_data_info` VALUES (1,'digimomk',',,static/explode_data_files/csv/digimomk_ORG/4_3_2020/Ar_user.csv,,static/explode_data_files/csv/digimomk_ORG/4_3_2020/AR_team.csv,,static/explode_data_files/csv/digimomk_ORG/4_3_2020/AR_product.csv,,static/explode_data_files/csv/digimomk_ORG/4_3_2020/AR_BACKLOG.csv,,static/explode_data_files/csv/digimomk_ORG/4_3_2020/AR_EPIC_CAPABILITY.csv,,static/explode_data_files/csv/digimomk_ORG/4_3_2020/AR_FEATURE.csv,,static/explode_data_files/csv/digimomk_ORG/4_3_2020/ArUserStoryPoints.csv,,static/explode_data_files/csv/digimomk_ORG/4_3_2020/AR_USER_STORY.csv,,static/explode_data_files/csv/digimomk_ORG/4_3_2020/ArIterations.csv,,static/explode_data_files/csv/digimomk_ORG/4_3_2020/ArRole.csv,,static/explode_data_files/csv/digimomk_ORG/4_3_2020/ArManageGoals.csv,,static/explode_data_files/csv/digimomk_ORG/4_3_2020/ArManageBenefits.csv','2020-03-04 15:35:03.656731');
/*!40000 ALTER TABLE `data_import_export_export_data_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `data_import_export_import_files_data`
--

DROP TABLE IF EXISTS `data_import_export_import_files_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `data_import_export_import_files_data` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `file_data` longtext NOT NULL,
  `created_date` datetime(6) NOT NULL,
  `ORG_ID_id` int(11) DEFAULT NULL,
  `created_by_id` int(11) DEFAULT NULL,
  `error_log` varchar(100) DEFAULT NULL,
  `file_name` varchar(50) NOT NULL,
  `files` varchar(100) NOT NULL,
  `upload_status` tinyint(1) NOT NULL,
  `priority` int(11) NOT NULL,
  `dommy_set` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `data_import_export_i_ORG_ID_id_f8bf3b5e_fk_account_a` (`ORG_ID_id`),
  KEY `data_import_export_i_created_by_id_c839efe8_fk_account_a` (`created_by_id`),
  CONSTRAINT `data_import_export_i_ORG_ID_id_f8bf3b5e_fk_account_a` FOREIGN KEY (`ORG_ID_id`) REFERENCES `account_ar_organization` (`id`),
  CONSTRAINT `data_import_export_i_created_by_id_c839efe8_fk_account_a` FOREIGN KEY (`created_by_id`) REFERENCES `account_ar_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `data_import_export_import_files_data`
--

LOCK TABLES `data_import_export_import_files_data` WRITE;
/*!40000 ALTER TABLE `data_import_export_import_files_data` DISABLE KEYS */;
INSERT INTO `data_import_export_import_files_data` VALUES (3,'6 total users.,,0 user import.,,6 user email already exists.,,0 user is active.,,0 other error','2020-03-04 10:12:19.000000',NULL,NULL,'/implode_data/errors/Agile_ORG/5_3_2020/Ar_user.txt','Ar_user','implode_data/Ar_user_3HdONhz_K0yCg7d.csv',1,1,1),(4,'6 total teams.,,4 team import.,,1 team already exists.5 other error','2020-03-04 10:14:33.000000',NULL,NULL,'/implode_data/errors/Agile_ORG/5_3_2020/AR_team.txt','AR_team','implode_data/AR_team_1M8Ufoc_TKCQJd8.csv',0,2,1),(5,'4 total product.,,2 product import.,,1 backlog already exists.1 other error','2020-03-04 10:16:05.000000',NULL,NULL,'/implode_data/errors/Agile_ORG/5_3_2020/AR_product.txt','AR_product','implode_data/AR_product_RyxkVvf_yZ8vUTX.csv',0,3,1),(6,'9 total backlog.,,8 backlog import.,,1 backlog already exists.0 other error','2020-03-04 10:17:20.000000',NULL,NULL,'/implode_data/errors/Agile_ORG/5_3_2020/AR_BACKLOG.txt','AR_BACKLOG','implode_data/AR_BACKLOG_7Locx4N_pmQkjLN.csv',0,4,1),(7,'5 total Epic capability .,,4 Epic capability  import.,,0 other error','2020-03-04 10:19:22.000000',NULL,NULL,'/implode_data/errors/Agile_ORG/5_3_2020/AR_EPIC_CAPABILITY.txt','AR_EPIC_CAPABILITY','implode_data/AR_EPIC_CAPABILITY_TIpxzQj_Jm5j3ky.csv',0,5,1),(8,'3 total Role .,,3 Role  import.,,0 other error','2020-03-04 10:20:34.000000',NULL,NULL,'/implode_data/errors/Agile_ORG/5_3_2020/ArRole.txt','ArRole','implode_data/ArRole_8YnazXm_ZwruM4m.csv',0,6,1),(9,'4 total Goal .,,4 Goal  import.,,0 other error','2020-03-04 10:22:13.000000',NULL,NULL,'/implode_data/errors/Agile_ORG/5_3_2020/ArManageGoals.txt','ArManageGoals','implode_data/ArManageGoals_8rHIgA8_oXWLkeg.csv',0,7,1),(10,'3 total Benefits .,,3 Benefits  import.,,0 other error','2020-03-04 10:23:37.000000',NULL,NULL,'/implode_data/errors/Agile_ORG/5_3_2020/ArManageBenefits.txt','ArManageBenefits','implode_data/ArManageBenefits_iF7XiQL_AwyMjIN.csv',0,8,1),(11,'10 total Role .,,9 Role  import.,,1 backlog already exists.0 other error','2020-03-04 10:25:06.000000',NULL,NULL,'/implode_data/errors/Agile_ORG/5_3_2020/ArUserStoryPoints.txt','ArUserStoryPoints','implode_data/ArUserStoryPoints_44kokJ6_qQUJFTG.csv',0,9,1),(12,'2 total user story.,,1 sotryes import.,,1 storyes exists.,,0 other error','2020-03-04 10:26:14.000000',NULL,NULL,'/implode_data/errors/Agile_ORG/5_3_2020/AR_USER_STORY.txt','AR_USER_STORY','implode_data/AR_USER_STORY_hE6XpKi_NtHwAuk.csv',0,10,1),(13,'9 total feature.,,8 feature import.,,1 backlog already exists.0 other error','2020-03-04 10:27:30.000000',NULL,NULL,'/implode_data/errors/Agile_ORG/5_3_2020/AR_FEATURE.txt','AR_FEATURE','implode_data/AR_FEATURE_utS1j17_dPWde6N.csv',0,11,1),(14,'2 total Iterations .,,1 Iterations  import.,,1 other error','2020-03-04 10:28:13.000000',NULL,NULL,'/implode_data/errors/Agile_ORG/5_3_2020/ArIterations.txt','ArIterations','implode_data/ArIterations_mu3Mf50_PTjpcFr.csv',0,12,1);
/*!40000 ALTER TABLE `data_import_export_import_files_data` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=225 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2020-03-04 10:03:04.239266','22','add iterationv',1,'new through import_export',17,1),(2,'2020-03-04 10:03:04.248039','21','manage-epic-capabilities/add-epic-capabilities',1,'new through import_export',17,1),(3,'2020-03-04 10:03:04.257677','20','Add Profile',1,'new through import_export',17,1),(4,'2020-03-04 10:03:04.267310','19','account-settings',1,'new through import_export',17,1),(5,'2020-03-04 10:03:04.277074','18','user-story-points',1,'new through import_export',17,1),(6,'2020-03-04 10:03:04.286635','17','manage-benefits',1,'new through import_export',17,1),(7,'2020-03-04 10:03:04.296179','16','manage-goals',1,'new through import_export',17,1),(8,'2020-03-04 10:03:04.305820','15','manage-role',1,'new through import_export',17,1),(9,'2020-03-04 10:03:04.315441','14','manage-iteration',1,'new through import_export',17,1),(10,'2020-03-04 10:03:04.324945','13','manage-backlog',1,'new through import_export',17,1),(11,'2020-03-04 10:03:04.334456','12','manage-team-member',1,'new through import_export',17,1),(12,'2020-03-04 10:03:04.344042','11','manage-team',1,'new through import_export',17,1),(13,'2020-03-04 10:03:04.353560','10','manage-products',1,'new through import_export',17,1),(14,'2020-03-04 10:03:04.363182','9','manage-feature',1,'new through import_export',17,1),(15,'2020-03-04 10:03:04.372742','8','manage-epic-capabilities',1,'new through import_export',17,1),(16,'2020-03-04 10:03:04.382466','7','invite-user',1,'new through import_export',17,1),(17,'2020-03-04 10:03:04.392002','6','user-profile',1,'new through import_export',17,1),(18,'2020-03-04 10:03:04.401588','5','iteration-view',1,'new through import_export',17,1),(19,'2020-03-04 10:03:04.411165','4','user-story-view',1,'new through import_export',17,1),(20,'2020-03-04 10:03:04.420720','3','backlog view',1,'new through import_export',17,1),(21,'2020-03-04 10:03:04.430303','2','product view',1,'new through import_export',17,1),(22,'2020-03-04 10:03:04.439917','1','Dashboard',1,'new through import_export',17,1),(23,'2020-03-04 10:03:32.106451','10','Benefit_Tag',1,'new through import_export',16,1),(24,'2020-03-04 10:03:32.115632','9','Goal_Tag',1,'new through import_export',16,1),(25,'2020-03-04 10:03:32.125433','8','Role_Tag',1,'new through import_export',16,1),(26,'2020-03-04 10:03:32.135217','7','Benefit_text',1,'new through import_export',16,1),(27,'2020-03-04 10:03:32.144891','6','Goal_text',1,'new through import_export',16,1),(28,'2020-03-04 10:03:32.154746','5','Role_text',1,'new through import_export',16,1),(29,'2020-03-04 10:03:32.164322','4','Conjunction Set',1,'new through import_export',16,1),(30,'2020-03-04 10:03:59.739887','153','Notification object (153)',1,'new through import_export',15,1),(31,'2020-03-04 10:03:59.748780','152','Notification object (152)',1,'new through import_export',15,1),(32,'2020-03-04 10:03:59.758506','151','Notification object (151)',1,'new through import_export',15,1),(33,'2020-03-04 10:03:59.768042','150','Notification object (150)',1,'new through import_export',15,1),(34,'2020-03-04 10:03:59.777766','149','Notification object (149)',1,'new through import_export',15,1),(35,'2020-03-04 10:03:59.787380','148','Notification object (148)',1,'new through import_export',15,1),(36,'2020-03-04 10:03:59.797210','147','Notification object (147)',1,'new through import_export',15,1),(37,'2020-03-04 10:03:59.806754','146','Notification object (146)',1,'new through import_export',15,1),(38,'2020-03-04 10:03:59.816402','145','Notification object (145)',1,'new through import_export',15,1),(39,'2020-03-04 10:03:59.826140','144','Notification object (144)',1,'new through import_export',15,1),(40,'2020-03-04 10:03:59.836114','143','Notification object (143)',1,'new through import_export',15,1),(41,'2020-03-04 10:03:59.845531','142','Notification object (142)',1,'new through import_export',15,1),(42,'2020-03-04 10:03:59.855120','141','Notification object (141)',1,'new through import_export',15,1),(43,'2020-03-04 10:03:59.864633','140','Notification object (140)',1,'new through import_export',15,1),(44,'2020-03-04 10:03:59.874365','139','Notification object (139)',1,'new through import_export',15,1),(45,'2020-03-04 10:03:59.884104','138','Notification object (138)',1,'new through import_export',15,1),(46,'2020-03-04 10:03:59.893797','137','Notification object (137)',1,'new through import_export',15,1),(47,'2020-03-04 10:03:59.903459','136','Notification object (136)',1,'new through import_export',15,1),(48,'2020-03-04 10:03:59.913138','135','Notification object (135)',1,'new through import_export',15,1),(49,'2020-03-04 10:03:59.922621','134','Notification object (134)',1,'new through import_export',15,1),(50,'2020-03-04 10:03:59.932199','133','Notification object (133)',1,'new through import_export',15,1),(51,'2020-03-04 10:03:59.941763','132','Notification object (132)',1,'new through import_export',15,1),(52,'2020-03-04 10:03:59.951458','131','Notification object (131)',1,'new through import_export',15,1),(53,'2020-03-04 10:03:59.960938','130','Notification object (130)',1,'new through import_export',15,1),(54,'2020-03-04 10:03:59.970590','129','Notification object (129)',1,'new through import_export',15,1),(55,'2020-03-04 10:03:59.980564','128','Notification object (128)',1,'new through import_export',15,1),(56,'2020-03-04 10:03:59.990092','127','Notification object (127)',1,'new through import_export',15,1),(57,'2020-03-04 10:03:59.999922','126','Notification object (126)',1,'new through import_export',15,1),(58,'2020-03-04 10:04:00.015518','125','Notification object (125)',1,'new through import_export',15,1),(59,'2020-03-04 10:04:00.032660','124','Notification object (124)',1,'new through import_export',15,1),(60,'2020-03-04 10:04:00.039582','123','Notification object (123)',1,'new through import_export',15,1),(61,'2020-03-04 10:04:00.049505','122','Notification object (122)',1,'new through import_export',15,1),(62,'2020-03-04 10:04:00.059039','121','Notification object (121)',1,'new through import_export',15,1),(63,'2020-03-04 10:04:00.068701','120','Notification object (120)',1,'new through import_export',15,1),(64,'2020-03-04 10:04:00.078389','119','Notification object (119)',1,'new through import_export',15,1),(65,'2020-03-04 10:04:00.088089','118','Notification object (118)',1,'new through import_export',15,1),(66,'2020-03-04 10:04:00.097708','117','Notification object (117)',1,'new through import_export',15,1),(67,'2020-03-04 10:04:00.107422','116','Notification object (116)',1,'new through import_export',15,1),(68,'2020-03-04 10:04:00.116985','115','Notification object (115)',1,'new through import_export',15,1),(69,'2020-03-04 10:04:00.126544','114','Notification object (114)',1,'new through import_export',15,1),(70,'2020-03-04 10:04:00.136003','113','Notification object (113)',1,'new through import_export',15,1),(71,'2020-03-04 10:04:00.145919','112','Notification object (112)',1,'new through import_export',15,1),(72,'2020-03-04 10:04:00.155399','111','Notification object (111)',1,'new through import_export',15,1),(73,'2020-03-04 10:04:00.164963','110','Notification object (110)',1,'new through import_export',15,1),(74,'2020-03-04 10:04:00.174596','109','Notification object (109)',1,'new through import_export',15,1),(75,'2020-03-04 10:04:00.184201','108','Notification object (108)',1,'new through import_export',15,1),(76,'2020-03-04 10:04:00.193807','107','Notification object (107)',1,'new through import_export',15,1),(77,'2020-03-04 10:04:00.203433','106','Notification object (106)',1,'new through import_export',15,1),(78,'2020-03-04 10:04:00.212923','105','Notification object (105)',1,'new through import_export',15,1),(79,'2020-03-04 10:04:00.222499','104','Notification object (104)',1,'new through import_export',15,1),(80,'2020-03-04 10:04:00.232065','103','Notification object (103)',1,'new through import_export',15,1),(81,'2020-03-04 10:04:00.241620','102','Notification object (102)',1,'new through import_export',15,1),(82,'2020-03-04 10:04:00.251102','101','Notification object (101)',1,'new through import_export',15,1),(83,'2020-03-04 10:04:00.260610','100','Notification object (100)',1,'new through import_export',15,1),(84,'2020-03-04 10:04:00.270198','99','Notification object (99)',1,'new through import_export',15,1),(85,'2020-03-04 10:04:00.279722','98','Notification object (98)',1,'new through import_export',15,1),(86,'2020-03-04 10:04:00.289217','97','Notification object (97)',1,'new through import_export',15,1),(87,'2020-03-04 10:04:00.298891','96','Notification object (96)',1,'new through import_export',15,1),(88,'2020-03-04 10:04:00.308400','95','Notification object (95)',1,'new through import_export',15,1),(89,'2020-03-04 10:04:00.318087','93','Notification object (93)',1,'new through import_export',15,1),(90,'2020-03-04 10:04:00.327673','92','Notification object (92)',1,'new through import_export',15,1),(91,'2020-03-04 10:04:00.337157','91','Notification object (91)',1,'new through import_export',15,1),(92,'2020-03-04 10:04:00.346744','90','Notification object (90)',1,'new through import_export',15,1),(93,'2020-03-04 10:04:00.356201','89','Notification object (89)',1,'new through import_export',15,1),(94,'2020-03-04 10:04:00.365776','88','Notification object (88)',1,'new through import_export',15,1),(95,'2020-03-04 10:04:00.375374','87','Notification object (87)',1,'new through import_export',15,1),(96,'2020-03-04 10:04:00.385045','86','Notification object (86)',1,'new through import_export',15,1),(97,'2020-03-04 10:04:00.394665','85','Notification object (85)',1,'new through import_export',15,1),(98,'2020-03-04 10:04:00.404188','84','Notification object (84)',1,'new through import_export',15,1),(99,'2020-03-04 10:04:00.413897','83','Notification object (83)',1,'new through import_export',15,1),(100,'2020-03-04 10:04:00.423389','82','Notification object (82)',1,'new through import_export',15,1),(101,'2020-03-04 10:04:00.433087','81','Notification object (81)',1,'new through import_export',15,1),(102,'2020-03-04 10:04:00.442889','80','Notification object (80)',1,'new through import_export',15,1),(103,'2020-03-04 10:04:00.452573','79','Notification object (79)',1,'new through import_export',15,1),(104,'2020-03-04 10:04:00.462243','78','Notification object (78)',1,'new through import_export',15,1),(105,'2020-03-04 10:04:00.471847','77','Notification object (77)',1,'new through import_export',15,1),(106,'2020-03-04 10:04:00.481487','76','Notification object (76)',1,'new through import_export',15,1),(107,'2020-03-04 10:04:00.491053','75','Notification object (75)',1,'new through import_export',15,1),(108,'2020-03-04 10:04:00.500665','74','Notification object (74)',1,'new through import_export',15,1),(109,'2020-03-04 10:04:00.510480','73','Notification object (73)',1,'new through import_export',15,1),(110,'2020-03-04 10:04:00.520123','72','Notification object (72)',1,'new through import_export',15,1),(111,'2020-03-04 10:04:00.529880','71','Notification object (71)',1,'new through import_export',15,1),(112,'2020-03-04 10:04:00.539717','70','Notification object (70)',1,'new through import_export',15,1),(113,'2020-03-04 10:04:00.549225','69','Notification object (69)',1,'new through import_export',15,1),(114,'2020-03-04 10:04:00.558915','68','Notification object (68)',1,'new through import_export',15,1),(115,'2020-03-04 10:04:00.568619','67','Notification object (67)',1,'new through import_export',15,1),(116,'2020-03-04 10:04:00.578137','66','Notification object (66)',1,'new through import_export',15,1),(117,'2020-03-04 10:04:00.587708','65','Notification object (65)',1,'new through import_export',15,1),(118,'2020-03-04 10:04:00.597266','64','Notification object (64)',1,'new through import_export',15,1),(119,'2020-03-04 10:04:00.606836','63','Notification object (63)',1,'new through import_export',15,1),(120,'2020-03-04 10:04:00.616438','62','Notification object (62)',1,'new through import_export',15,1),(121,'2020-03-04 10:04:00.626022','61','Notification object (61)',1,'new through import_export',15,1),(122,'2020-03-04 10:04:00.635764','60','Notification object (60)',1,'new through import_export',15,1),(123,'2020-03-04 10:04:00.645268','59','Notification object (59)',1,'new through import_export',15,1),(124,'2020-03-04 10:04:00.655143','58','Notification object (58)',1,'new through import_export',15,1),(125,'2020-03-04 10:04:00.664627','57','Notification object (57)',1,'new through import_export',15,1),(126,'2020-03-04 10:04:00.674189','56','Notification object (56)',1,'new through import_export',15,1),(127,'2020-03-04 10:04:00.683864','55','Notification object (55)',1,'new through import_export',15,1),(128,'2020-03-04 10:04:00.693601','54','Notification object (54)',1,'new through import_export',15,1),(129,'2020-03-04 10:04:00.703249','53','Notification object (53)',1,'new through import_export',15,1),(130,'2020-03-04 10:04:00.712858','52','Notification object (52)',1,'new through import_export',15,1),(131,'2020-03-04 10:04:00.722639','51','Notification object (51)',1,'new through import_export',15,1),(132,'2020-03-04 10:04:00.732189','50','Notification object (50)',1,'new through import_export',15,1),(133,'2020-03-04 10:04:00.741775','49','Notification object (49)',1,'new through import_export',15,1),(134,'2020-03-04 10:04:00.751294','48','Notification object (48)',1,'new through import_export',15,1),(135,'2020-03-04 10:04:00.760955','47','Notification object (47)',1,'new through import_export',15,1),(136,'2020-03-04 10:04:00.770553','46','Notification object (46)',1,'new through import_export',15,1),(137,'2020-03-04 10:04:00.780098','45','Notification object (45)',1,'new through import_export',15,1),(138,'2020-03-04 10:04:00.789645','44','Notification object (44)',1,'new through import_export',15,1),(139,'2020-03-04 10:04:00.799347','43','Notification object (43)',1,'new through import_export',15,1),(140,'2020-03-04 10:04:00.808949','42','Notification object (42)',1,'new through import_export',15,1),(141,'2020-03-04 10:04:00.818524','41','Notification object (41)',1,'new through import_export',15,1),(142,'2020-03-04 10:04:00.828135','40','Notification object (40)',1,'new through import_export',15,1),(143,'2020-03-04 10:04:00.837772','39','Notification object (39)',1,'new through import_export',15,1),(144,'2020-03-04 10:04:00.847378','38','Notification object (38)',1,'new through import_export',15,1),(145,'2020-03-04 10:04:00.857004','37','Notification object (37)',1,'new through import_export',15,1),(146,'2020-03-04 10:04:00.866647','36','Notification object (36)',1,'new through import_export',15,1),(147,'2020-03-04 10:04:00.876302','35','Notification object (35)',1,'new through import_export',15,1),(148,'2020-03-04 10:04:00.885984','34','Notification object (34)',1,'new through import_export',15,1),(149,'2020-03-04 10:04:00.895663','33','Notification object (33)',1,'new through import_export',15,1),(150,'2020-03-04 10:04:00.905209','32','Notification object (32)',1,'new through import_export',15,1),(151,'2020-03-04 10:04:00.914854','31','Notification object (31)',1,'new through import_export',15,1),(152,'2020-03-04 10:04:00.924466','30','Notification object (30)',1,'new through import_export',15,1),(153,'2020-03-04 10:04:00.934005','29','Notification object (29)',1,'new through import_export',15,1),(154,'2020-03-04 10:04:00.943879','28','Notification object (28)',1,'new through import_export',15,1),(155,'2020-03-04 10:04:00.953490','27','Notification object (27)',1,'new through import_export',15,1),(156,'2020-03-04 10:04:00.963041','26','Notification object (26)',1,'new through import_export',15,1),(157,'2020-03-04 10:04:00.972680','25','Notification object (25)',1,'new through import_export',15,1),(158,'2020-03-04 10:04:00.982288','24','Notification object (24)',1,'new through import_export',15,1),(159,'2020-03-04 10:04:00.991886','23','Notification object (23)',1,'new through import_export',15,1),(160,'2020-03-04 10:04:01.001412','22','Notification object (22)',1,'new through import_export',15,1),(161,'2020-03-04 10:04:01.011047','21','Notification object (21)',1,'new through import_export',15,1),(162,'2020-03-04 10:04:01.020654','20','Notification object (20)',1,'new through import_export',15,1),(163,'2020-03-04 10:04:01.030536','19','Notification object (19)',1,'new through import_export',15,1),(164,'2020-03-04 10:04:01.040236','18','Notification object (18)',1,'new through import_export',15,1),(165,'2020-03-04 10:04:01.049925','17','Notification object (17)',1,'new through import_export',15,1),(166,'2020-03-04 10:04:01.059504','16','Notification object (16)',1,'new through import_export',15,1),(167,'2020-03-04 10:04:01.069134','15','Notification object (15)',1,'new through import_export',15,1),(168,'2020-03-04 10:04:01.078672','14','Notification object (14)',1,'new through import_export',15,1),(169,'2020-03-04 10:04:01.088224','13','Notification object (13)',1,'new through import_export',15,1),(170,'2020-03-04 10:04:01.097774','12','Notification object (12)',1,'new through import_export',15,1),(171,'2020-03-04 10:04:01.107396','11','Notification object (11)',1,'new through import_export',15,1),(172,'2020-03-04 10:04:01.116880','10','Notification object (10)',1,'new through import_export',15,1),(173,'2020-03-04 10:04:01.126479','9','Notification object (9)',1,'new through import_export',15,1),(174,'2020-03-04 10:04:01.136043','8','Notification object (8)',1,'new through import_export',15,1),(175,'2020-03-04 10:04:01.145649','7','Notification object (7)',1,'new through import_export',15,1),(176,'2020-03-04 10:04:01.155430','6','Notification object (6)',1,'new through import_export',15,1),(177,'2020-03-04 10:04:01.165054','5','Notification object (5)',1,'new through import_export',15,1),(178,'2020-03-04 10:04:01.174748','4','Notification object (4)',1,'new through import_export',15,1),(179,'2020-03-04 10:04:01.184425','3','Notification object (3)',1,'new through import_export',15,1),(180,'2020-03-04 10:04:01.193848','2','Notification object (2)',1,'new through import_export',15,1),(181,'2020-03-04 10:04:01.203569','1','Notification object (1)',1,'new through import_export',15,1),(182,'2020-03-04 10:08:56.978568','1','ArUserStoryPoints',1,'[{\"added\": {}}]',35,1),(183,'2020-03-04 10:08:57.020178','2','ArUserStoryPoints',1,'[{\"added\": {}}]',35,1),(184,'2020-03-04 10:09:09.262430','1','ArUserStoryPoints',3,'',35,1),(185,'2020-03-04 10:09:39.697851','2','ArUserStoryPoints',2,'[{\"changed\": {\"fields\": [\"priority\", \"dommy_set\"]}}]',35,1),(186,'2020-03-04 10:10:58.000458','2','ArUserStoryPoints',3,'',35,1),(187,'2020-03-04 10:14:33.178892','3','Ar_user',1,'[{\"added\": {}}]',35,1),(188,'2020-03-04 10:16:04.981622','4','AR_team',1,'[{\"added\": {}}]',35,1),(189,'2020-03-04 10:17:19.702592','5','AR_product',1,'[{\"added\": {}}]',35,1),(190,'2020-03-04 10:19:22.087163','6','AR_BACKLOG',1,'[{\"added\": {}}]',35,1),(191,'2020-03-04 10:20:33.805736','7','AR_EPIC_CAPABILITY',1,'[{\"added\": {}}]',35,1),(192,'2020-03-04 10:22:13.284299','8','ArRole',1,'[{\"added\": {}}]',35,1),(193,'2020-03-04 10:23:37.341029','9','ArManageGoals',1,'[{\"added\": {}}]',35,1),(194,'2020-03-04 10:25:06.229943','10','ArManageBenefits',1,'[{\"added\": {}}]',35,1),(195,'2020-03-04 10:26:13.812793','11','ArUserStoryPoints',1,'[{\"added\": {}}]',35,1),(196,'2020-03-04 10:27:30.605552','12','AR_USER_STORY',1,'[{\"added\": {}}]',35,1),(197,'2020-03-04 10:28:12.748843','13','AR_FEATURE',1,'[{\"added\": {}}]',35,1),(198,'2020-03-04 10:29:16.255675','14','ArIterations',1,'[{\"added\": {}}]',35,1),(199,'2020-03-04 10:42:51.219416','1','User Story Rating',1,'[{\"added\": {}}]',25,1),(200,'2020-03-04 10:43:24.216973','2','When Do We Need It',1,'[{\"added\": {}}]',25,1),(201,'2020-03-04 10:43:53.909141','3','What Are We Building',1,'[{\"added\": {}}]',25,1),(202,'2020-03-04 10:44:53.085942','4','Who Should Use Agile Ready',1,'[{\"added\": {}}]',25,1),(203,'2020-03-04 10:45:57.333644','5','Why Agile Ready',1,'[{\"added\": {}}]',25,1),(204,'2020-03-04 10:46:43.622933','6','Team Edition help you get User Stories Ready Fast',1,'[{\"added\": {}}]',25,1),(205,'2020-03-04 10:47:24.983162','7','A Day in the life of an Agile Ready User',1,'[{\"added\": {}}]',25,1),(206,'2020-03-04 11:12:18.096222','1','Archive',1,'[{\"added\": {}}]',26,1),(207,'2020-03-04 11:13:29.492280','2','Active',1,'[{\"added\": {}}]',26,1),(208,'2020-03-04 11:13:47.683439','3','New',1,'[{\"added\": {}}]',26,1),(209,'2020-03-04 11:19:24.630192','1','None',1,'[{\"added\": {}}]',18,1),(210,'2020-03-04 11:19:54.355091','2','Not Ready',1,'[{\"added\": {}}]',18,1),(211,'2020-03-04 11:20:22.197645','3','Ideation',1,'[{\"added\": {}}]',18,1),(212,'2020-03-04 11:20:59.915295','4','Pending',1,'[{\"added\": {}}]',18,1),(213,'2020-03-04 11:21:33.217940','5','Active',1,'[{\"added\": {}}]',18,1),(214,'2020-03-04 11:22:11.752255','1','None',1,'[{\"added\": {}}]',19,1),(215,'2020-03-04 11:22:37.294039','2','Non-Functional Requirement',1,'[{\"added\": {}}]',19,1),(216,'2020-03-04 11:23:09.120247','3','Discovery',1,'[{\"added\": {}}]',19,1),(217,'2020-03-04 11:23:36.712494','4','Functional',1,'[{\"added\": {}}]',19,1),(218,'2020-03-06 03:26:48.467252','1','beagileready',2,'[{\"changed\": {\"fields\": [\"first_name\", \"last_name\", \"email\"]}}]',4,1),(219,'2020-03-06 03:30:50.352313','1','be@agile+ready',2,'[{\"changed\": {\"fields\": [\"username\"]}}]',4,1),(220,'2020-03-07 12:18:54.349824','21','Antonio V Timbol',2,'[]',12,1),(221,'2020-03-07 12:22:25.892942','21','Antonio V Timbol',2,'[{\"changed\": {\"fields\": [\"profile_permission\", \"activate_status\"]}}]',12,1),(222,'2020-03-07 12:25:16.867315','21','Antonio V Timbol',2,'[{\"changed\": {\"fields\": [\"active_user\", \"user_to_invite\", \"verification_status\"]}}]',12,1),(223,'2020-03-07 12:43:13.635510','23','prod1_digi_admin',1,'[{\"added\": {}}]',4,1),(224,'2020-03-07 12:49:17.922259','23','prod1_digi_admin',2,'[{\"changed\": {\"fields\": [\"first_name\", \"last_name\", \"email\", \"is_staff\", \"user_permissions\"]}}]',4,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (17,'account','arhelpcontect'),(13,'account','arshowcolumns'),(10,'account','aruserprofile'),(11,'account','aruserprofilepermission'),(16,'account','aruserstoryscoringpoints'),(9,'account','ar_organization'),(8,'account','ar_organization_status'),(12,'account','ar_user'),(14,'account','csvfilesuplodaded'),(15,'account','notification'),(1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(36,'data_import_export','dommy_data'),(34,'data_import_export','export_data_info'),(35,'data_import_export','import_files_data'),(7,'django_summernote','attachment'),(31,'feedback','arfeedback'),(25,'helpuser','cms_manage'),(27,'manage_backlogs','ar_backlog'),(26,'manage_backlogs','ar_backlog_status'),(33,'manage_benefits','armanagebenefits'),(23,'manage_epic_capability','ar_epic_capability'),(24,'manage_features','ar_feature'),(32,'manage_goals','armanagegoals'),(28,'manage_iterations','ariterations'),(22,'manage_product','ar_product'),(21,'manage_product','ar_team'),(29,'manage_role','arrole'),(6,'sessions','session'),(30,'user_story_points','aruserstorypoints'),(20,'user_story_view','ar_user_story'),(18,'user_story_view','ar_us_status'),(19,'user_story_view','ar_us_type');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=131 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2020-02-01 10:19:40.609232'),(2,'auth','0001_initial','2020-02-01 10:19:41.070027'),(3,'account','0001_initial','2020-02-01 10:19:43.674041'),(4,'account','0002_auto_20200114_0653','2020-02-01 10:19:49.712055'),(5,'account','0003_auto_20200116_1001','2020-02-01 10:19:49.736537'),(6,'account','0004_notification','2020-02-01 10:19:49.811308'),(7,'account','0005_aruserstoryscoringpoints','2020-02-01 10:19:49.894046'),(8,'account','0006_auto_20200123_1105','2020-02-01 10:19:50.402154'),(9,'account','0007_auto_20200123_1109','2020-02-01 10:19:50.439509'),(10,'account','0008_arhelpcontect','2020-02-01 10:19:50.516815'),(11,'account','0009_auto_20200127_1335','2020-02-01 10:19:50.590830'),(12,'account','0010_auto_20200127_1456','2020-02-01 10:19:50.597598'),(13,'account','0011_auto_20200127_1459','2020-02-01 10:19:50.643415'),(14,'account','0012_auto_20200127_1515','2020-02-01 10:19:50.659507'),(15,'account','0013_auto_20200201_0607','2020-02-01 10:19:50.713292'),(16,'account','0014_auto_20200201_0824','2020-02-01 10:19:50.724992'),(17,'admin','0001_initial','2020-02-01 10:19:50.813203'),(18,'admin','0002_logentry_remove_auto_add','2020-02-01 10:19:51.197561'),(19,'admin','0003_logentry_add_action_flag_choices','2020-02-01 10:19:51.214278'),(20,'contenttypes','0002_remove_content_type_name','2020-02-01 10:19:51.496548'),(21,'auth','0002_alter_permission_name_max_length','2020-02-01 10:19:51.525608'),(22,'auth','0003_alter_user_email_max_length','2020-02-01 10:19:51.562740'),(23,'auth','0004_alter_user_username_opts','2020-02-01 10:19:51.585765'),(24,'auth','0005_alter_user_last_login_null','2020-02-01 10:19:51.723872'),(25,'auth','0006_require_contenttypes_0002','2020-02-01 10:19:51.733179'),(26,'auth','0007_alter_validators_add_error_messages','2020-02-01 10:19:51.757845'),(27,'auth','0008_alter_user_username_max_length','2020-02-01 10:19:51.786872'),(28,'auth','0009_alter_user_last_name_max_length','2020-02-01 10:19:51.821856'),(29,'auth','0010_alter_group_name_max_length','2020-02-01 10:19:51.851130'),(30,'auth','0011_update_proxy_permissions','2020-02-01 10:19:51.879631'),(31,'django_summernote','0001_initial','2020-02-01 10:19:51.954894'),(32,'django_summernote','0002_update-help_text','2020-02-01 10:19:51.964801'),(33,'feedback','0001_initial','2020-02-01 10:19:52.046040'),(34,'feedback','0002_auto_20200113_0755','2020-02-01 10:19:52.432292'),(35,'helpuser','0001_initial','2020-02-01 10:19:52.524698'),(36,'manage_product','0001_initial','2020-02-01 10:19:53.281982'),(37,'manage_product','0002_auto_20200114_0653','2020-02-01 10:19:56.578790'),(38,'manage_product','0003_auto_20200122_0913','2020-02-01 10:19:56.655854'),(39,'manage_product','0004_auto_20200123_1242','2020-02-01 10:19:56.872255'),(40,'manage_product','0005_remove_ar_product_children_backlog_list','2020-02-01 10:19:57.031074'),(41,'manage_backlogs','0001_initial','2020-02-01 10:19:57.218147'),(42,'manage_backlogs','0002_auto_20200114_0653','2020-02-01 10:20:00.717907'),(43,'manage_backlogs','0003_auto_20200115_0611','2020-02-01 10:20:00.798264'),(44,'manage_backlogs','0004_auto_20200115_0613','2020-02-01 10:20:00.859343'),(45,'manage_backlogs','0005_auto_20200125_1345','2020-02-01 10:20:01.115905'),(46,'manage_backlogs','0006_auto_20200128_1016','2020-02-01 10:20:01.396305'),(47,'manage_backlogs','0007_remove_ar_backlog_children_us_list','2020-02-01 10:20:01.593936'),(48,'manage_backlogs','0008_auto_20200130_0734','2020-02-01 10:20:02.658250'),(49,'manage_benefits','0001_initial','2020-02-01 10:20:03.198760'),(50,'manage_epic_capability','0001_initial','2020-02-01 10:20:03.928737'),(51,'manage_epic_capability','0002_auto_20200114_0653','2020-02-01 10:20:05.363155'),(52,'user_story_view','0001_initial','2020-02-01 10:20:05.703240'),(53,'manage_features','0001_initial','2020-02-01 10:20:08.402296'),(54,'manage_features','0002_auto_20200113_0755','2020-02-01 10:20:10.031434'),(55,'manage_features','0003_auto_20200114_0653','2020-02-01 10:20:10.451586'),(56,'manage_goals','0001_initial','2020-02-01 10:20:10.633032'),(57,'manage_iterations','0001_initial','2020-02-01 10:20:11.380146'),(58,'manage_iterations','0002_auto_20200114_0653','2020-02-01 10:20:14.224682'),(59,'manage_role','0001_initial','2020-02-01 10:20:14.332265'),(60,'manage_role','0002_arrole_org_id','2020-02-01 10:20:14.866943'),(61,'manage_role','0003_arrole_use','2020-02-01 10:20:15.250161'),(62,'sessions','0001_initial','2020-02-01 10:20:15.332586'),(63,'user_story_points','0001_initial','2020-02-01 10:20:15.537544'),(64,'user_story_points','0002_auto_20200109_1433','2020-02-01 10:20:15.924481'),(65,'user_story_points','0003_auto_20200115_0709','2020-02-01 10:20:15.994713'),(66,'user_story_points','0004_aruserstorypoints_org_id','2020-02-01 10:20:16.165194'),(67,'user_story_points','0005_auto_20200116_1155','2020-02-01 10:20:16.921985'),(68,'user_story_points','0006_auto_20200130_0902','2020-02-01 10:20:16.979366'),(69,'user_story_view','0002_auto_20200114_0653','2020-02-01 10:20:20.083603'),(70,'user_story_view','0003_auto_20200114_1001','2020-02-01 10:20:20.397657'),(71,'user_story_view','0004_auto_20200124_1046','2020-02-01 10:20:21.544583'),(72,'user_story_view','0005_auto_20200128_1024','2020-02-01 10:20:21.875082'),(73,'account','0014_auto_20200201_1142','2020-02-01 11:42:51.706050'),(74,'account','0015_auto_20200201_1255','2020-02-01 12:55:47.399848'),(75,'account','0002_auto_20200205_0603','2020-02-08 14:37:27.063002'),(76,'account','0003_auto_20200208_1437','2020-02-08 14:37:27.078131'),(77,'feedback','0002_auto_20200205_0603','2020-02-08 14:37:27.097028'),(78,'helpuser','0002_auto_20200205_0603','2020-02-08 14:37:27.149807'),(79,'manage_backlogs','0002_auto_20200205_0603','2020-02-08 14:37:27.196528'),(80,'manage_benefits','0002_auto_20200205_0603','2020-02-08 14:37:27.222776'),(81,'manage_epic_capability','0002_auto_20200208_1437','2020-02-08 14:37:27.254417'),(82,'manage_features','0002_auto_20200205_0603','2020-02-08 14:37:27.284793'),(83,'manage_goals','0002_auto_20200205_0603','2020-02-08 14:37:27.325253'),(84,'manage_iterations','0002_auto_20200204_0547','2020-02-08 14:37:27.392302'),(85,'manage_iterations','0003_auto_20200204_0548','2020-02-08 14:37:27.468140'),(86,'manage_iterations','0004_auto_20200204_0556','2020-02-08 14:37:28.036798'),(87,'manage_iterations','0005_auto_20200205_0603','2020-02-08 14:37:28.076219'),(88,'manage_iterations','0006_auto_20200205_0740','2020-02-08 14:37:28.691699'),(89,'account','0004_auto_20200211_0603','2020-02-11 06:04:08.411870'),(90,'manage_iterations','0007_auto_20200205_0946','2020-02-11 06:06:30.136563'),(91,'manage_iterations','0008_auto_20200205_0949','2020-02-11 06:06:30.669200'),(92,'manage_iterations','0009_auto_20200205_0951','2020-02-11 06:06:31.419085'),(93,'manage_iterations','0010_auto_20200208_0754','2020-02-11 06:06:31.732728'),(94,'manage_product','0002_auto_20200205_0603','2020-02-11 06:06:31.820573'),(95,'manage_role','0002_auto_20200205_0603','2020-02-11 06:06:31.856509'),(96,'user_story_points','0002_auto_20200205_0603','2020-02-11 06:06:31.893073'),(97,'user_story_view','0002_auto_20200205_0521','2020-02-11 06:06:31.928202'),(98,'user_story_view','0003_auto_20200205_0603','2020-02-11 06:06:31.994358'),(99,'user_story_view','0004_auto_20200205_1033','2020-02-11 06:06:32.344522'),(100,'user_story_view','0005_auto_20200207_0739','2020-02-11 06:06:32.916834'),(101,'user_story_view','0006_auto_20200208_0757','2020-02-11 06:06:33.208277'),(102,'account','0003_ar_user_terms_accept','2020-03-04 09:51:29.956524'),(103,'account','0004_auto_20200304_0951','2020-03-04 09:51:29.964561'),(104,'data_import_export','0001_initial','2020-03-04 09:51:30.042251'),(105,'data_import_export','0002_file_info_import_files_data','2020-03-04 09:51:30.327896'),(106,'data_import_export','0003_auto_20200214_0723','2020-03-04 09:51:31.477630'),(107,'data_import_export','0004_auto_20200214_1158','2020-03-04 09:51:31.934432'),(108,'data_import_export','0005_import_files_data_upload_status','2020-03-04 09:51:32.113314'),(109,'data_import_export','0006_import_files_data_priority','2020-03-04 09:51:32.296298'),(110,'data_import_export','0007_dommy_data','2020-03-04 09:51:32.377960'),(111,'data_import_export','0008_auto_20200221_1354','2020-03-04 09:51:32.601657'),(112,'data_import_export','0009_auto_20200229_0801','2020-03-04 09:51:32.713118'),(113,'data_import_export','0010_auto_20200229_0803','2020-03-04 09:51:32.953595'),(114,'data_import_export','0011_auto_20200229_0805','2020-03-04 09:51:33.200872'),(115,'helpuser','0003_auto_20200225_1328','2020-03-04 09:51:33.361023'),(116,'helpuser','0004_auto_20200225_1333','2020-03-04 09:51:33.796375'),(117,'helpuser','0005_auto_20200225_1340','2020-03-04 09:51:33.853360'),(118,'manage_backlogs','0003_auto_20200229_1758','2020-03-04 09:51:34.512482'),(119,'manage_epic_capability','0002_auto_20200304_0951','2020-03-04 09:51:34.557443'),(120,'manage_features','0003_auto_20200224_1156','2020-03-04 09:51:34.848605'),(121,'user_story_view','0007_auto_20200224_0758','2020-03-04 09:51:35.761077'),(122,'user_story_view','0008_auto_20200229_1802','2020-03-04 09:51:36.862871'),(123,'manage_backlogs','0004_auto_20200304_1104','2020-03-04 11:04:25.364034'),(124,'manage_backlogs','0005_auto_20200304_1104','2020-03-04 11:05:02.240915'),(125,'manage_backlogs','0006_auto_20200304_1111','2020-03-04 11:12:03.800335'),(126,'user_story_view','0009_auto_20200304_1118','2020-03-04 11:18:33.032119'),(127,'manage_backlogs','0004_auto_20200304_1737','2020-03-07 13:17:39.707979'),(128,'user_story_view','0009_auto_20200304_1737','2020-03-07 13:17:40.904262'),(129,'account','0004_auto_20200307_1326','2020-03-07 13:26:24.156201'),(130,'manage_epic_capability','0002_auto_20200307_1326','2020-03-07 13:26:24.193416');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('aeek5nife7w3lmjhtk1agukslttaplqd','NzI5NTVkMGNhMDM2MTRjZWUxMmI3MDE0OTJiYzlkN2UxMmNlNGZhNDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI1ZDk5YWYyNzRkZWM3NjU2N2E2YzdlYjU3M2U1NTA1OGQ2YWI0Nzg4In0=','2020-03-20 03:12:16.029841'),('euohwen98ui3nkempxisfbew3pk7n4ve','Y2E5YzEyYTVhNjFhNWJiMDM1M2FjOGM3ZTMxNDFhMWM1OTZjM2I4Mzp7InVzZXJfaWQiOjEsIm9yZ19pZCI6MSwidXNlcl9uYW1lIjoiaml0ZW5kcmEiLCJ1c2VyX3R5cGUiOiJSb290IiwiX2F1dGhfdXNlcl9pZCI6IjIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6Ijc4YjU5MTU5NzlmZTcwMWE5N2VjNzMyNzNlZTU0M2VmNzU0MDU0OGQifQ==','2020-03-21 13:21:32.099235'),('eutfsgq1sqxh53yjks5240mbj2n581rq','ZmU2MzQyN2UxNmU4Mzc1MjQ1ZWU1Njg1YmJiYjU0ZjEzNzQ0ZmFhYjp7InVzZXJfaWQiOjIwLCJvcmdfaWQiOjEsInVzZXJfbmFtZSI6ImppdGVuZHJhIiwidXNlcl90eXBlIjoiVXNlciIsIl9hdXRoX3VzZXJfaWQiOiIyMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiOGE1ZjczYzYyNjcwY2RiYzljYjhiZDFmMDcxN2ExMzNhYzAwZTIyZSJ9','2020-03-18 15:31:03.822634'),('f75sz7aci03iimimvbgoh1evabnhy61g','NTBkNWY0OTg2OGVkM2JjMzJlMTU3ODM4ZDUwMGIyZTdkYTA5YTlmNzp7InVzZXJfaWQiOjEsIm9yZ19pZCI6MSwidXNlcl9uYW1lIjoiaml0ZW5kcmEiLCJfYXV0aF91c2VyX2lkIjoiMiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNzhiNTkxNTk3OWZlNzAxYTk3ZWM3MzI3M2VlNTQzZWY3NTQwNTQ4ZCJ9','2020-03-19 05:57:56.861834'),('ff83xdrx4tjulskpje83cj8v19hpyk30','MzE5YWUzZTQ0ODgxYjMwMDFkN2FhNWMyOTY1ZGZhMmJiN2VlMDg0ZTp7Il9hdXRoX3VzZXJfaWQiOiIyNCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMTk1YTBjZDZlYzJmM2NmZDIwNzkxNTUyMzZlYTk3MjI2OTY0NTMwZCJ9','2020-03-21 13:18:02.712995'),('fghzmfzusd4h7obkfdmy8b5xmiq1xrne','MTEwOTdmNDdkZGMxNTU1NjY3ODNhMDQ0NjA1ZDk3NjFmOGE4NWIyMDp7InVzZXJfaWQiOjEsIm9yZ19pZCI6MSwidXNlcl9uYW1lIjoiaml0ZW5kcmEiLCJ1c2VyX3R5cGUiOiJSb290IiwiX2F1dGhfdXNlcl9pZCI6IjIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjA4ZTQ2Y2QyNzhmY2VlZGYzYTk1MTNjYjhlMjJkZjM1Nzg2ZTQ5ZDMifQ==','2020-03-18 11:49:53.782253'),('fv08zvq335zxwizj9v3pgksl6vspmi1m','MTEwOTdmNDdkZGMxNTU1NjY3ODNhMDQ0NjA1ZDk3NjFmOGE4NWIyMDp7InVzZXJfaWQiOjEsIm9yZ19pZCI6MSwidXNlcl9uYW1lIjoiaml0ZW5kcmEiLCJ1c2VyX3R5cGUiOiJSb290IiwiX2F1dGhfdXNlcl9pZCI6IjIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjA4ZTQ2Y2QyNzhmY2VlZGYzYTk1MTNjYjhlMjJkZjM1Nzg2ZTQ5ZDMifQ==','2020-03-19 05:25:48.938444'),('i1gu6oy61wsrne5y0nzhbuxz7amdihp0','YmFjZjdjYjI3MTFiNjdlOTkwYmZlMTAxYWJmODBlY2I4ZWZlZDUwNTp7InVzZXJfaWQiOjEsIm9yZ19pZCI6MSwidXNlcl90eXBlIjoiUm9vdCIsIl9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIwOGU0NmNkMjc4ZmNlZWRmM2E5NTEzY2I4ZTIyZGYzNTc4NmU0OWQzIiwidXNlcl9uYW1lIjoiaml0ZW5kcmEifQ==','2020-03-18 14:40:39.161746'),('jbglr05yl6cplgxsqby6hnawqmr1r9nd','MTEwOTdmNDdkZGMxNTU1NjY3ODNhMDQ0NjA1ZDk3NjFmOGE4NWIyMDp7InVzZXJfaWQiOjEsIm9yZ19pZCI6MSwidXNlcl9uYW1lIjoiaml0ZW5kcmEiLCJ1c2VyX3R5cGUiOiJSb290IiwiX2F1dGhfdXNlcl9pZCI6IjIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjA4ZTQ2Y2QyNzhmY2VlZGYzYTk1MTNjYjhlMjJkZjM1Nzg2ZTQ5ZDMifQ==','2020-03-18 15:15:57.484800'),('ngffildqjcnhefjqitjdxi8e2maooudc','ZmU2MzQyN2UxNmU4Mzc1MjQ1ZWU1Njg1YmJiYjU0ZjEzNzQ0ZmFhYjp7InVzZXJfaWQiOjIwLCJvcmdfaWQiOjEsInVzZXJfbmFtZSI6ImppdGVuZHJhIiwidXNlcl90eXBlIjoiVXNlciIsIl9hdXRoX3VzZXJfaWQiOiIyMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiOGE1ZjczYzYyNjcwY2RiYzljYjhiZDFmMDcxN2ExMzNhYzAwZTIyZSJ9','2020-03-18 16:06:36.447082'),('v5ujj4my90eq1riq2ffzoidctdyme6lk','MzE5YWUzZTQ0ODgxYjMwMDFkN2FhNWMyOTY1ZGZhMmJiN2VlMDg0ZTp7Il9hdXRoX3VzZXJfaWQiOiIyNCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMTk1YTBjZDZlYzJmM2NmZDIwNzkxNTUyMzZlYTk3MjI2OTY0NTMwZCJ9','2020-03-21 13:29:16.131491'),('vfk2n29drhgi2f5lxv1j4ewyeuqk3q2f','MzdjNWYxZjIxNTMyYWU5ZTI3NGFmNmRlMTY0MDM4ZWFlMGFjZGRiYjp7InVzZXJfaWQiOjIwLCJvcmdfaWQiOjEsInVzZXJfbmFtZSI6IiIsInVzZXJfdHlwZSI6IlVzZXIiLCJfYXV0aF91c2VyX2lkIjoiMjEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjhhNWY3M2M2MjY3MGNkYmM5Y2I4YmQxZjA3MTdhMTMzYWMwMGUyMmUifQ==','2020-03-18 15:07:15.219660'),('xdewfu1c77rtklrizaeivw5o0kf11st6','NzI5NTVkMGNhMDM2MTRjZWUxMmI3MDE0OTJiYzlkN2UxMmNlNGZhNDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI1ZDk5YWYyNzRkZWM3NjU2N2E2YzdlYjU3M2U1NTA1OGQ2YWI0Nzg4In0=','2020-03-18 09:58:34.699679'),('yih1ig2snca7cd8efwifm8ms82zyl63k','MTEwOTdmNDdkZGMxNTU1NjY3ODNhMDQ0NjA1ZDk3NjFmOGE4NWIyMDp7InVzZXJfaWQiOjEsIm9yZ19pZCI6MSwidXNlcl9uYW1lIjoiaml0ZW5kcmEiLCJ1c2VyX3R5cGUiOiJSb290IiwiX2F1dGhfdXNlcl9pZCI6IjIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjA4ZTQ2Y2QyNzhmY2VlZGYzYTk1MTNjYjhlMjJkZjM1Nzg2ZTQ5ZDMifQ==','2020-03-18 14:45:17.793775');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_summernote_attachment`
--

DROP TABLE IF EXISTS `django_summernote_attachment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_summernote_attachment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `file` varchar(100) NOT NULL,
  `uploaded` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_summernote_attachment`
--

LOCK TABLES `django_summernote_attachment` WRITE;
/*!40000 ALTER TABLE `django_summernote_attachment` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_summernote_attachment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `feedback_arfeedback`
--

DROP TABLE IF EXISTS `feedback_arfeedback`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `feedback_arfeedback` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `page_name` varchar(50) NOT NULL,
  `feedback_nature` longtext NOT NULL,
  `feedback_information` longtext NOT NULL,
  `attachments` varchar(100) NOT NULL,
  `created_dt` datetime(6) NOT NULL,
  `created_by_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `feedback_arfeedback_created_by_id_729091f3_fk_account_ar_user_id` (`created_by_id`),
  CONSTRAINT `feedback_arfeedback_created_by_id_729091f3_fk_account_ar_user_id` FOREIGN KEY (`created_by_id`) REFERENCES `account_ar_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feedback_arfeedback`
--

LOCK TABLES `feedback_arfeedback` WRITE;
/*!40000 ALTER TABLE `feedback_arfeedback` DISABLE KEYS */;
INSERT INTO `feedback_arfeedback` VALUES (1,'Iteration View','Irritating Bug','hi','04_03_2020_15_12_23_198629.ppk','2020-03-04 15:12:23.199522',1),(2,'Manage Iteration','Irritating Bug','','','2020-03-04 15:23:38.622394',1),(3,'Manage Export','Irritating Bug',' hi','05_03_2020_05_30_56_719079.ppk','2020-03-05 05:30:56.720818',1),(4,'Manage User Story Point','Irritating Bug','nt','05_03_2020_05_48_55_367820.ppk','2020-03-05 05:48:55.368209',1),(5,'Manage Iteration','Irritating Bug','g','05_03_2020_05_49_40_106309.ppk','2020-03-05 05:49:40.106751',1);
/*!40000 ALTER TABLE `feedback_arfeedback` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `helpuser_cms_manage`
--

DROP TABLE IF EXISTS `helpuser_cms_manage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `helpuser_cms_manage` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `keyword` varchar(50) NOT NULL,
  `title` varchar(50) NOT NULL,
  `help_description` longtext NOT NULL,
  `created_dt` datetime(6) NOT NULL,
  `updated_dt` datetime(6) NOT NULL,
  `created_by_id` int(11) DEFAULT NULL,
  `updated_by_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `helpuser_cms_manage_created_by_id_d36e0c0e_fk_auth_user_id` (`created_by_id`),
  KEY `helpuser_cms_manage_updated_by_id_c7ccedb2_fk_auth_user_id` (`updated_by_id`),
  CONSTRAINT `helpuser_cms_manage_created_by_id_d36e0c0e_fk_auth_user_id` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `helpuser_cms_manage_updated_by_id_c7ccedb2_fk_auth_user_id` FOREIGN KEY (`updated_by_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `helpuser_cms_manage`
--

LOCK TABLES `helpuser_cms_manage` WRITE;
/*!40000 ALTER TABLE `helpuser_cms_manage` DISABLE KEYS */;
INSERT INTO `helpuser_cms_manage` VALUES (1,'User-Story-Rating','User Story Rating','<p><span style=\"color: rgb(44, 53, 57); font-family: Montserrat, sans-serif; font-size: 17px; letter-spacing: 0.2px; text-align: justify;\">A properly formatted User Story has three parts, Role, Goal and Benefit. This format has become the de-facto standard in Agile development. Agile ready calls this a three part or tri-part statement adopting a widely used term. Agile Ready measure how good a user story is against this de-facto standard. How close is the user story in question to this format, “As a \"Role\" I want \"Goal\" so that \"Benefit”.&nbsp;</span><span id=\"dots\" style=\"color: rgb(44, 53, 57); font-family: Montserrat, sans-serif; font-size: 17px; letter-spacing: 0.2px; text-align: justify;\">...</span><br></p>','2020-03-04 10:41:45.000000','2020-03-04 10:41:45.000000',1,1),(2,'When-Do-We-Need-It','When Do We Need It','<p>Better user stories are needed immediately and Agile Ready is designed to help your content authors write better user stories faster.&nbsp;<br></p>','2020-03-04 10:42:51.000000','2020-03-04 10:42:51.000000',1,1),(3,'What-Are-We-Building','What Are We Building','<p class=\"MsoNormal\">The team at Agile Ready has built Team Edition and is building Enterprise Edition as two products that can meet the diverse needs of the Agile development marketplace.<o:p></o:p></p><p class=\"MsoNormal\">Team Edition is designed for small to medium sized business with less than 10 teams while Enterprise Edition is designed for large corporate and global environments with large number of teams.<o:p></o:p></p><p></p><p class=\"MsoNormal\">Whatever sized business you are in, Agile Ready can help you write better user stories faster.&nbsp;</p>','2020-03-04 10:43:24.000000','2020-03-04 10:43:24.000000',1,1),(4,'Who-Should-Use-Agile-Ready','Who Should Use Agile Ready','<p class=\"MsoNormal\">Agile Ready is designed to help people who write user stories write them better. This means anyone who is involved in understanding business requirements and design specifications and needs to write high quality user stories should use Agile Ready.<o:p></o:p></p><p class=\"MsoNormal\">This means people like Business Owners, Product Managers, Product Owners, Business or Systems Analysts, Scrum Masters, and/or any Agile Team member.<o:p></o:p></p><p class=\"MsoNormal\">How each of the people described use Agile Ready may vary. That is why Agile Ready’s profile permission model allows different people in different roles to view and edit user stories and other data inside Agile Ready.</p>','2020-03-04 10:43:54.000000','2020-03-04 10:43:54.000000',1,1),(5,'Why-Agile-Ready','Why Agile Ready','<p class=\"mid-txt\" style=\"text-align: justify; font-size: 17px; letter-spacing: 0.2px; line-height: 30px; width: 1110px; color: rgb(44, 53, 57); font-family: Montserrat, sans-serif; margin: 20px auto !important;\">Bad User Story writing is easy but costly (time, quality, dollars). Good User Story writing is hard but invaluable. Good to Great User Story writing is made easier with Agile Ready, a best practice authoring and rating system.</p><p style=\"margin-bottom: 1rem; text-align: justify; font-size: 16px; letter-spacing: 0.2px; line-height: 30px; color: rgb(44, 53, 57); font-family: Montserrat, sans-serif;\">Bad User Stories delay agile teams in creating high quality code. This costs time and money. Good User Stories help the business state clear intentions that the agile team can solution easier and faster.</p><p style=\"margin-bottom: 1rem; text-align: justify; font-size: 16px; letter-spacing: 0.2px; line-height: 30px; color: rgb(44, 53, 57); font-family: Montserrat, sans-serif;\">A two-week (10 business days) sprint or iteration for an 8 person team can cost between $16,000 to $64,000 upwards to over $100,000 depending on hourly rates.<span id=\"dots\">...</span></p>','2020-03-04 10:44:53.000000','2020-03-04 10:44:53.000000',1,1),(6,'Team-Edition-help-you-get-User-Stories-Ready-Fast','Team Edition help you get User Stories Ready Fast','<p><span style=\"color: rgb(44, 53, 57); font-family: Montserrat, sans-serif; font-size: 16px; letter-spacing: 0.2px; text-align: justify;\">Write better user stories using Agile Ready’s Rating System. Write User Stories Faster as a team. Invite other users to join your team.</span><br></p>','2020-03-04 10:45:57.000000','2020-03-04 10:45:57.000000',1,1),(7,'A-Day-in-the-life-of-an-Agile-Ready-User','A Day in the life of an Agile Ready User','<p><span style=\"color: rgb(44, 53, 57); font-family: Montserrat, sans-serif; font-size: 16px; letter-spacing: 0.2px; text-align: justify;\">Shannon is a Product Owner for three teams, GirlBand, DarkMatter and SealTeam7. Something big is about to happen and Agile Ready will be a big help.</span><br></p>','2020-03-04 10:46:44.000000','2020-03-04 10:46:44.000000',1,1);
/*!40000 ALTER TABLE `helpuser_cms_manage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manage_backlogs_ar_backlog`
--

DROP TABLE IF EXISTS `manage_backlogs_ar_backlog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `manage_backlogs_ar_backlog` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `owner_id` int(11) DEFAULT NULL,
  `backlog_score` int(11) NOT NULL,
  `Backlog_size` int(11) NOT NULL,
  `created_dt` datetime(6) NOT NULL,
  `updated_dt` datetime(6) NOT NULL,
  `BL_STATUS_id` int(11) DEFAULT NULL,
  `ORG_ID_id` int(11) DEFAULT NULL,
  `created_by_id` int(11) NOT NULL,
  `product_parent_id` int(11) DEFAULT NULL,
  `updated_by_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `manage_backlogs_ar_b_created_by_id_5db191b8_fk_account_a` (`created_by_id`),
  KEY `manage_backlogs_ar_b_updated_by_id_219902c4_fk_account_a` (`updated_by_id`),
  KEY `manage_backlogs_ar_b_BL_STATUS_id_a2571bc6_fk_manage_ba` (`BL_STATUS_id`),
  KEY `manage_backlogs_ar_b_ORG_ID_id_f5011c7a_fk_account_a` (`ORG_ID_id`),
  KEY `manage_backlogs_ar_b_product_parent_id_fc95f2f7_fk_manage_pr` (`product_parent_id`),
  KEY `manage_backlogs_ar_backlog_owner_id_d5643658` (`owner_id`),
  CONSTRAINT `manage_backlogs_ar_b_BL_STATUS_id_a2571bc6_fk_manage_ba` FOREIGN KEY (`BL_STATUS_id`) REFERENCES `manage_backlogs_ar_backlog_status` (`id`),
  CONSTRAINT `manage_backlogs_ar_b_ORG_ID_id_f5011c7a_fk_account_a` FOREIGN KEY (`ORG_ID_id`) REFERENCES `account_ar_organization` (`id`),
  CONSTRAINT `manage_backlogs_ar_b_created_by_id_5db191b8_fk_account_a` FOREIGN KEY (`created_by_id`) REFERENCES `account_ar_user` (`id`),
  CONSTRAINT `manage_backlogs_ar_b_owner_id_d5643658_fk_account_a` FOREIGN KEY (`owner_id`) REFERENCES `account_ar_user` (`id`),
  CONSTRAINT `manage_backlogs_ar_b_product_parent_id_fc95f2f7_fk_manage_pr` FOREIGN KEY (`product_parent_id`) REFERENCES `manage_product_ar_product` (`id`),
  CONSTRAINT `manage_backlogs_ar_b_updated_by_id_219902c4_fk_account_a` FOREIGN KEY (`updated_by_id`) REFERENCES `account_ar_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manage_backlogs_ar_backlog`
--

LOCK TABLES `manage_backlogs_ar_backlog` WRITE;
/*!40000 ALTER TABLE `manage_backlogs_ar_backlog` DISABLE KEYS */;
INSERT INTO `manage_backlogs_ar_backlog` VALUES (19,'None',NULL,0,0,'2020-03-04 14:40:49.686733','2020-03-04 14:40:49.686749',NULL,1,1,NULL,1),(20,'Backlog One for P1 (example)',14,0,0,'2020-02-21 07:25:14.785925','2020-02-21 07:25:14.785938',3,1,14,NULL,14),(21,'Backlog Two for P1 (example)',14,0,0,'2020-02-21 07:26:08.542732','2020-02-21 07:26:08.542766',3,1,14,NULL,14),(22,'Backlog for P2 (example)',14,0,0,'2020-02-21 07:26:44.543466','2020-03-04 15:21:21.553791',3,1,14,8,1),(23,'FlexTeam BL 1 (example)',14,0,0,'2020-02-21 07:30:51.824100','2020-02-21 07:30:51.824116',3,1,14,NULL,14),(24,'FlexTeam BL 2 (example)',14,0,0,'2020-02-21 07:32:57.523763','2020-02-21 07:32:57.523776',3,1,14,NULL,14),(25,'Ticket Masters BL (example)',1,0,0,'2020-02-21 07:34:16.316535','2020-03-04 15:14:41.552932',3,1,14,9,1),(26,'Mmasters API Pilot (example)',14,0,0,'2020-02-21 07:34:39.209712','2020-03-04 15:13:46.558458',3,1,14,9,1),(27,'Mmasters Phone ID (example)',18,0,0,'2020-02-21 07:38:01.560188','2020-03-04 15:13:59.673851',3,1,14,9,1),(28,'digi',1,0,0,'2020-03-04 14:48:41.450268','2020-03-05 05:16:59.404039',1,1,1,8,1),(30,'None',NULL,0,0,'2020-03-05 00:59:18.196510','2020-03-05 00:59:18.196526',NULL,2,21,NULL,21),(31,'Backlog One for P1 (example)',21,0,0,'2020-02-21 07:25:14.785925','2020-02-21 07:25:14.785938',3,2,21,NULL,21),(32,'Backlog Two for P1 (example)',21,0,0,'2020-02-21 07:26:08.542732','2020-02-21 07:26:08.542766',3,2,21,NULL,21),(33,'Backlog for P2 (example)',21,0,0,'2020-02-21 07:26:44.543466','2020-02-21 07:26:44.543478',3,2,21,12,21),(34,'FlexTeam BL 1 (example)',21,0,0,'2020-02-21 07:30:51.824100','2020-02-21 07:30:51.824116',3,2,21,NULL,21),(35,'FlexTeam BL 2 (example)',21,0,0,'2020-02-21 07:32:57.523763','2020-02-21 07:32:57.523776',3,2,21,NULL,21),(36,'Ticket Masters BL (example)',21,0,0,'2020-02-21 07:34:16.316535','2020-02-21 07:34:16.316548',3,2,21,13,21),(37,'Mmasters API Pilot (example)',21,0,0,'2020-02-21 07:34:39.209712','2020-02-21 07:34:39.209729',3,2,21,13,21),(38,'Mmasters Phone ID (example)',21,0,0,'2020-02-21 07:38:01.560188','2020-02-21 07:38:01.560209',3,2,21,13,21);
/*!40000 ALTER TABLE `manage_backlogs_ar_backlog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manage_backlogs_ar_backlog_status`
--

DROP TABLE IF EXISTS `manage_backlogs_ar_backlog_status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `manage_backlogs_ar_backlog_status` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `bl_status_key` varchar(50) NOT NULL,
  `bl_status_desc` longtext NOT NULL,
  `create_dt` datetime(6) NOT NULL,
  `update_dt` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manage_backlogs_ar_backlog_status`
--

LOCK TABLES `manage_backlogs_ar_backlog_status` WRITE;
/*!40000 ALTER TABLE `manage_backlogs_ar_backlog_status` DISABLE KEYS */;
INSERT INTO `manage_backlogs_ar_backlog_status` VALUES (1,'Archive','A Backlog, and its associated user stories, are NOT available to being workedbut is viewable in the archive repository','2020-03-04 11:09:53.000000','2020-03-04 11:09:53.000000'),(2,'Active','A Backlog, and its associated user stories, is available to being worked on (edited and reviewed) by one or more authors and is automatically scored if the auto_score flag is on.','2020-03-04 11:12:23.000000','2020-03-04 11:12:23.000000'),(3,'New','A Backlog is created with a title only and other  information','2020-03-04 11:13:30.000000','2020-03-04 11:13:30.000000');
/*!40000 ALTER TABLE `manage_backlogs_ar_backlog_status` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manage_backlogs_ar_backlog_team_list`
--

DROP TABLE IF EXISTS `manage_backlogs_ar_backlog_team_list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `manage_backlogs_ar_backlog_team_list` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ar_backlog_id` int(11) NOT NULL,
  `ar_team_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `manage_backlogs_ar_backl_ar_backlog_id_ar_team_id_63b59aa0_uniq` (`ar_backlog_id`,`ar_team_id`),
  KEY `manage_backlogs_ar_b_ar_team_id_bffebc6a_fk_manage_pr` (`ar_team_id`),
  CONSTRAINT `manage_backlogs_ar_b_ar_backlog_id_05f68c61_fk_manage_ba` FOREIGN KEY (`ar_backlog_id`) REFERENCES `manage_backlogs_ar_backlog` (`id`),
  CONSTRAINT `manage_backlogs_ar_b_ar_team_id_bffebc6a_fk_manage_pr` FOREIGN KEY (`ar_team_id`) REFERENCES `manage_product_ar_team` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manage_backlogs_ar_backlog_team_list`
--

LOCK TABLES `manage_backlogs_ar_backlog_team_list` WRITE;
/*!40000 ALTER TABLE `manage_backlogs_ar_backlog_team_list` DISABLE KEYS */;
INSERT INTO `manage_backlogs_ar_backlog_team_list` VALUES (15,20,12),(16,22,12),(17,23,13),(18,24,13),(19,25,14),(20,26,15),(21,27,15),(22,28,12),(24,31,18),(25,33,18),(26,34,19),(27,35,19),(28,36,20),(29,37,21),(30,38,21);
/*!40000 ALTER TABLE `manage_backlogs_ar_backlog_team_list` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manage_benefits_armanagebenefits`
--

DROP TABLE IF EXISTS `manage_benefits_armanagebenefits`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `manage_benefits_armanagebenefits` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Benefits_id` varchar(50) DEFAULT NULL,
  `Benefits_title` varchar(50) DEFAULT NULL,
  `Benefits_description` longtext NOT NULL,
  `Use_in` longtext NOT NULL,
  `created_dt` datetime(6) NOT NULL,
  `updated_dt` datetime(6) NOT NULL,
  `ORG_ID_id` int(11) DEFAULT NULL,
  `created_by_id` int(11) NOT NULL,
  `updated_by_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `manage_benefits_arma_ORG_ID_id_ef8bd839_fk_account_a` (`ORG_ID_id`),
  KEY `manage_benefits_arma_created_by_id_53a91717_fk_account_a` (`created_by_id`),
  KEY `manage_benefits_arma_updated_by_id_a6e52a42_fk_account_a` (`updated_by_id`),
  CONSTRAINT `manage_benefits_arma_ORG_ID_id_ef8bd839_fk_account_a` FOREIGN KEY (`ORG_ID_id`) REFERENCES `account_ar_organization` (`id`),
  CONSTRAINT `manage_benefits_arma_created_by_id_53a91717_fk_account_a` FOREIGN KEY (`created_by_id`) REFERENCES `account_ar_user` (`id`),
  CONSTRAINT `manage_benefits_arma_updated_by_id_a6e52a42_fk_account_a` FOREIGN KEY (`updated_by_id`) REFERENCES `account_ar_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manage_benefits_armanagebenefits`
--

LOCK TABLES `manage_benefits_armanagebenefits` WRITE;
/*!40000 ALTER TABLE `manage_benefits_armanagebenefits` DISABLE KEYS */;
INSERT INTO `manage_benefits_armanagebenefits` VALUES (7,'AR_BENEFITE_7','I can soar','(example)','','2020-02-21 08:03:57.529166','2020-02-21 08:03:57.529181',1,14,14),(8,'AR_BENEFITE_8','I can recieve an audit','(example)','','2020-02-21 08:04:23.640314','2020-02-21 08:04:23.640331',1,14,14),(9,'AR_BENEFITE_9','I can manage partners','(example)','','2020-02-21 08:04:49.108603','2020-02-21 08:04:49.108617',1,14,14),(10,'AR_BENEFITE_10','bgb','gfdgdfgfgsfs','','2020-03-04 15:38:39.275449','2020-03-04 15:38:39.275458',1,1,1),(11,'AR_BENEFITE_11','I can soar','(example)','','2020-02-21 08:03:57.529166','2020-02-21 08:03:57.529181',2,21,21),(12,'AR_BENEFITE_12','I can recieve an audit','(example)','','2020-02-21 08:04:23.640314','2020-02-21 08:04:23.640331',2,21,21),(13,'AR_BENEFITE_13','I can manage partners','(example)','','2020-02-21 08:04:49.108603','2020-02-21 08:04:49.108617',2,21,21);
/*!40000 ALTER TABLE `manage_benefits_armanagebenefits` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manage_epic_capability_ar_epic_capability`
--

DROP TABLE IF EXISTS `manage_epic_capability_ar_epic_capability`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `manage_epic_capability_ar_epic_capability` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Cepic_key` varchar(50) NOT NULL,
  `Cepic_desc` longtext NOT NULL,
  `create_dt` datetime(6) NOT NULL,
  `update_dt` datetime(6) NOT NULL,
  `ORG_ID_id` int(11) DEFAULT NULL,
  `created_by_id` int(11) NOT NULL,
  `update_by_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `manage_epic_capabili_created_by_id_1318fdb5_fk_account_a` (`created_by_id`),
  KEY `manage_epic_capabili_update_by_id_83801d44_fk_account_a` (`update_by_id`),
  KEY `manage_epic_capabili_ORG_ID_id_f6f1bc35_fk_account_a` (`ORG_ID_id`),
  CONSTRAINT `manage_epic_capabili_ORG_ID_id_f6f1bc35_fk_account_a` FOREIGN KEY (`ORG_ID_id`) REFERENCES `account_ar_organization` (`id`),
  CONSTRAINT `manage_epic_capabili_created_by_id_1318fdb5_fk_account_a` FOREIGN KEY (`created_by_id`) REFERENCES `account_ar_user` (`id`),
  CONSTRAINT `manage_epic_capabili_update_by_id_83801d44_fk_account_a` FOREIGN KEY (`update_by_id`) REFERENCES `account_ar_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manage_epic_capability_ar_epic_capability`
--

LOCK TABLES `manage_epic_capability_ar_epic_capability` WRITE;
/*!40000 ALTER TABLE `manage_epic_capability_ar_epic_capability` DISABLE KEYS */;
INSERT INTO `manage_epic_capability_ar_epic_capability` VALUES (11,'None','None','2020-03-04 14:40:49.705716','2020-03-04 14:40:49.705734',1,1,1),(12,'Capability-C1 (example)','Capabilities are actions that a product can perform to meet the needs of the business or the marketplace and thus expressing business value.','2020-02-21 07:40:00.822239','2020-03-04 15:21:31.964575',1,14,1),(13,'Capability-C2 (example)','Enter a description in this field of what new or changed behaviors in the product you expect this capability to provide. Use a narrative story style or simply list the expected new functionality or features this capability will deliver when implemented.','2020-02-21 07:40:37.908293','2020-02-21 07:40:37.908306',1,14,14),(14,'Phone ID Plus (example)','Phone ID Plus provides the BestEverMortgage product new functionality for storing and retrieving customer data using the customer\'s phone number instead of the system assigned customer-id. This will improve the customer experience and is a major component of Product-P1\'s upgrade for this coming year.','2020-02-21 07:41:13.355549','2020-02-21 07:41:13.355567',1,14,14),(15,'BestEverAPI Pilot (example)','BestEverAPI pilot is rebuild of the current BestEver API to meet new Federal Reserve reporting rules for our business partners. This will allow the Finance Division to on-board new partners who will now not incur manual reporting costs.','2020-02-21 07:41:39.934972','2020-02-21 07:41:39.934984',1,14,14),(17,'None','None','2020-03-05 00:59:18.215739','2020-03-05 00:59:18.215754',2,21,21),(18,'Capability-C1 (example)','Capabilities are actions that a product can perform to meet the needs of the business or the marketplace and thus expressing business value.','2020-02-21 07:40:00.822239','2020-02-21 07:40:00.822260',2,21,21),(19,'Capability-C2 (example)','Enter a description in this field of what new or changed behaviors in the product you expect this capability to provide. Use a narrative story style or simply list the expected new functionality or features this capability will deliver when implemented.','2020-02-21 07:40:37.908293','2020-02-21 07:40:37.908306',2,21,21),(20,'Phone ID Plus (example)','Phone ID Plus provides the BestEverMortgage product new functionality for storing and retrieving customer data using the customer\'s phone number instead of the system assigned customer-id. This will improve the customer experience and is a major component of Product-P1\'s upgrade for this coming year.','2020-02-21 07:41:13.355549','2020-02-21 07:41:13.355567',2,21,21),(21,'BestEverAPI Pilot (example)','BestEverAPI pilot is rebuild of the current BestEver API to meet new Federal Reserve reporting rules for our business partners. This will allow the Finance Division to on-board new partners who will now not incur manual reporting costs.','2020-02-21 07:41:39.934972','2020-02-21 07:41:39.934984',2,21,21);
/*!40000 ALTER TABLE `manage_epic_capability_ar_epic_capability` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manage_epic_capability_ar_epic_capability_PROJECT_ID`
--

DROP TABLE IF EXISTS `manage_epic_capability_ar_epic_capability_PROJECT_ID`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `manage_epic_capability_ar_epic_capability_PROJECT_ID` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ar_epic_capability_id` int(11) NOT NULL,
  `ar_product_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `manage_epic_capability_a_ar_epic_capability_id_ar_938ba088_uniq` (`ar_epic_capability_id`,`ar_product_id`),
  KEY `manage_epic_capabili_ar_product_id_e1a7d8fa_fk_manage_pr` (`ar_product_id`),
  CONSTRAINT `manage_epic_capabili_ar_epic_capability_i_85e04e19_fk_manage_ep` FOREIGN KEY (`ar_epic_capability_id`) REFERENCES `manage_epic_capability_ar_epic_capability` (`id`),
  CONSTRAINT `manage_epic_capabili_ar_product_id_e1a7d8fa_fk_manage_pr` FOREIGN KEY (`ar_product_id`) REFERENCES `manage_product_ar_product` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manage_epic_capability_ar_epic_capability_PROJECT_ID`
--

LOCK TABLES `manage_epic_capability_ar_epic_capability_PROJECT_ID` WRITE;
/*!40000 ALTER TABLE `manage_epic_capability_ar_epic_capability_PROJECT_ID` DISABLE KEYS */;
INSERT INTO `manage_epic_capability_ar_epic_capability_PROJECT_ID` VALUES (3,15,9),(5,21,13);
/*!40000 ALTER TABLE `manage_epic_capability_ar_epic_capability_PROJECT_ID` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manage_features_ar_feature`
--

DROP TABLE IF EXISTS `manage_features_ar_feature`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `manage_features_ar_feature` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Feature_key` varchar(50) NOT NULL,
  `Feature_desc` longtext NOT NULL,
  `create_dt` datetime(6) NOT NULL,
  `update_dt` datetime(6) NOT NULL,
  `CE_ID_id` int(11) DEFAULT NULL,
  `ORG_ID_id` int(11) DEFAULT NULL,
  `create_by_id` int(11) NOT NULL,
  `update_by_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `manage_features_ar_f_create_by_id_f76852b9_fk_account_a` (`create_by_id`),
  KEY `manage_features_ar_f_update_by_id_231c8bb8_fk_account_a` (`update_by_id`),
  KEY `manage_features_ar_f_ORG_ID_id_2ab83274_fk_account_a` (`ORG_ID_id`),
  KEY `manage_features_ar_f_CE_ID_id_caced5f3_fk_manage_ep` (`CE_ID_id`),
  CONSTRAINT `manage_features_ar_f_CE_ID_id_caced5f3_fk_manage_ep` FOREIGN KEY (`CE_ID_id`) REFERENCES `manage_epic_capability_ar_epic_capability` (`id`),
  CONSTRAINT `manage_features_ar_f_ORG_ID_id_2ab83274_fk_account_a` FOREIGN KEY (`ORG_ID_id`) REFERENCES `account_ar_organization` (`id`),
  CONSTRAINT `manage_features_ar_f_create_by_id_f76852b9_fk_account_a` FOREIGN KEY (`create_by_id`) REFERENCES `account_ar_user` (`id`),
  CONSTRAINT `manage_features_ar_f_update_by_id_231c8bb8_fk_account_a` FOREIGN KEY (`update_by_id`) REFERENCES `account_ar_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manage_features_ar_feature`
--

LOCK TABLES `manage_features_ar_feature` WRITE;
/*!40000 ALTER TABLE `manage_features_ar_feature` DISABLE KEYS */;
INSERT INTO `manage_features_ar_feature` VALUES (19,'None','None','2020-03-04 14:40:49.715183','2020-03-04 14:40:49.715204',NULL,1,1,1),(20,'Feature-F1 (example)','A feature is a persistent service or function of a product giving it an ability to meet business needs thus delivering value.','2020-02-21 07:42:24.748925','2020-02-21 07:42:24.748925',12,1,14,14),(21,'Feature-F2 (example)','Enter a description in this field of what feature will do and/or what value it will provide. Use a narrative story style or simply list the expected new or changed functions or behaviors once implemented.','2020-02-21 07:45:08.893806','2020-02-21 07:45:08.893806',13,1,14,14),(22,'Feature-F3 (example)','This is the third feature of capability C1','2020-02-21 07:47:06.231721','2020-02-21 07:47:06.231721',11,1,14,14),(23,'Store Customer Phone # (example)','Storing the customer phone number during the customer capture process is a new feature of Product P1.','2020-02-21 07:47:43.514858','2020-02-21 07:47:43.514858',14,1,14,14),(24,'Retrieve Customer Phone # (example)','Retrieving the customer phone number during the customer servicing process is a new feature of Product P1.','2020-02-21 07:48:20.195480','2020-02-21 07:48:20.195480',14,1,14,14),(25,'Enroll Partner (example)','Allow a qualified business partner to enroll into our data repository.','2020-02-21 07:49:08.598871','2020-02-21 07:49:08.598871',15,1,14,14),(26,'Disenroll Partner # (example)','Allow a qualified business partner to disenroll into our data repository.','2020-02-21 07:49:53.137382','2020-02-21 07:49:53.137382',15,1,14,14),(27,'Submit FedRes ReportType1 (example)','Allow an enrolled business partner to submit Report Type 1 to the Federal Reserve','2020-02-21 07:50:20.570045','2020-02-21 07:50:20.570045',15,1,14,14),(29,'None','None','2020-03-05 00:59:18.234791','2020-03-05 00:59:18.234809',NULL,2,21,21),(30,'Feature-F1 (example)','A feature is a persistent service or function of a product giving it an ability to meet business needs thus delivering value.','2020-02-21 07:42:24.748925','2020-02-21 07:42:24.748925',18,2,21,21),(31,'Feature-F2 (example)','Enter a description in this field of what feature will do and/or what value it will provide. Use a narrative story style or simply list the expected new or changed functions or behaviors once implemented.','2020-02-21 07:45:08.893806','2020-02-21 07:45:08.893806',19,2,21,21),(32,'Feature-F3 (example)','This is the third feature of capability C1','2020-02-21 07:47:06.231721','2020-02-21 07:47:06.231721',17,2,21,21),(33,'Store Customer Phone # (example)','Storing the customer phone number during the customer capture process is a new feature of Product P1.','2020-02-21 07:47:43.514858','2020-02-21 07:47:43.514858',20,2,21,21),(34,'Retrieve Customer Phone # (example)','Retrieving the customer phone number during the customer servicing process is a new feature of Product P1.','2020-02-21 07:48:20.195480','2020-02-21 07:48:20.195480',20,2,21,21),(35,'Enroll Partner (example)','Allow a qualified business partner to enroll into our data repository.','2020-02-21 07:49:08.598871','2020-02-21 07:49:08.598871',21,2,21,21),(36,'Disenroll Partner # (example)','Allow a qualified business partner to disenroll into our data repository.','2020-02-21 07:49:53.137382','2020-02-21 07:49:53.137382',21,2,21,21),(37,'Submit FedRes ReportType1 (example)','Allow an enrolled business partner to submit Report Type 1 to the Federal Reserve','2020-02-21 07:50:20.570045','2020-02-21 07:50:20.570045',21,2,21,21);
/*!40000 ALTER TABLE `manage_features_ar_feature` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manage_features_ar_feature_User_story`
--

DROP TABLE IF EXISTS `manage_features_ar_feature_User_story`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `manage_features_ar_feature_User_story` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ar_feature_id` int(11) NOT NULL,
  `ar_user_story_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `manage_features_ar_featu_ar_feature_id_ar_user_st_24d0a840_uniq` (`ar_feature_id`,`ar_user_story_id`),
  KEY `manage_features_ar_f_ar_user_story_id_99d0b7f4_fk_user_stor` (`ar_user_story_id`),
  CONSTRAINT `manage_features_ar_f_ar_feature_id_eff60adc_fk_manage_fe` FOREIGN KEY (`ar_feature_id`) REFERENCES `manage_features_ar_feature` (`id`),
  CONSTRAINT `manage_features_ar_f_ar_user_story_id_99d0b7f4_fk_user_stor` FOREIGN KEY (`ar_user_story_id`) REFERENCES `user_story_view_ar_user_story` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manage_features_ar_feature_User_story`
--

LOCK TABLES `manage_features_ar_feature_User_story` WRITE;
/*!40000 ALTER TABLE `manage_features_ar_feature_User_story` DISABLE KEYS */;
/*!40000 ALTER TABLE `manage_features_ar_feature_User_story` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manage_goals_armanagegoals`
--

DROP TABLE IF EXISTS `manage_goals_armanagegoals`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `manage_goals_armanagegoals` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Goal_id` varchar(50) DEFAULT NULL,
  `Goal_title` varchar(50) DEFAULT NULL,
  `Gole_description` longtext NOT NULL,
  `Use_in` longtext NOT NULL,
  `created_dt` datetime(6) NOT NULL,
  `updated_dt` datetime(6) NOT NULL,
  `ORG_ID_id` int(11) DEFAULT NULL,
  `created_by_id` int(11) NOT NULL,
  `updated_by_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `manage_goals_armanag_ORG_ID_id_b7bbad85_fk_account_a` (`ORG_ID_id`),
  KEY `manage_goals_armanag_created_by_id_4bb58f4c_fk_account_a` (`created_by_id`),
  KEY `manage_goals_armanag_updated_by_id_5bcbb9c2_fk_account_a` (`updated_by_id`),
  CONSTRAINT `manage_goals_armanag_ORG_ID_id_b7bbad85_fk_account_a` FOREIGN KEY (`ORG_ID_id`) REFERENCES `account_ar_organization` (`id`),
  CONSTRAINT `manage_goals_armanag_created_by_id_4bb58f4c_fk_account_a` FOREIGN KEY (`created_by_id`) REFERENCES `account_ar_user` (`id`),
  CONSTRAINT `manage_goals_armanag_updated_by_id_5bcbb9c2_fk_account_a` FOREIGN KEY (`updated_by_id`) REFERENCES `account_ar_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manage_goals_armanagegoals`
--

LOCK TABLES `manage_goals_armanagegoals` WRITE;
/*!40000 ALTER TABLE `manage_goals_armanagegoals` DISABLE KEYS */;
INSERT INTO `manage_goals_armanagegoals` VALUES (9,'AR_ROLE_9','select','(example)','','2020-02-21 07:54:12.885813','2020-02-21 07:54:12.885830',1,14,14),(10,'AR_ROLE_10','display','(example)','','2020-02-21 07:55:14.306073','2020-02-21 07:55:14.306084',1,14,14),(11,'AR_ROLE_11','view','(example)','','2020-02-21 07:56:08.171204','2020-02-21 07:56:08.171210',1,14,14),(12,'AR_ROLE_12','glide','(example)','','2020-02-21 08:03:27.322501','2020-02-21 08:03:27.322511',1,14,14),(13,'AR_GOAL_13','nhmg','gfhfh','','2020-03-04 15:43:10.159746','2020-03-04 15:43:10.159756',1,1,1),(14,'AR_ROLE_14','select','(example)','','2020-02-21 07:54:12.885813','2020-02-21 07:54:12.885830',2,21,21),(15,'AR_ROLE_15','display','(example)','','2020-02-21 07:55:14.306073','2020-02-21 07:55:14.306084',2,21,21),(16,'AR_ROLE_16','view','(example)','','2020-02-21 07:56:08.171204','2020-02-21 07:56:08.171210',2,21,21),(17,'AR_ROLE_17','glide','(example)','','2020-02-21 08:03:27.322501','2020-02-21 08:03:27.322511',2,21,21);
/*!40000 ALTER TABLE `manage_goals_armanagegoals` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manage_iterations_ariterations`
--

DROP TABLE IF EXISTS `manage_iterations_ariterations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `manage_iterations_ariterations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `IterationName` varchar(50) NOT NULL,
  `owner_id` int(11) DEFAULT NULL,
  `IterationId` longtext NOT NULL,
  `StartDate` date NOT NULL,
  `EndDate` date NOT NULL,
  `Description` longtext NOT NULL,
  `IterationScore` double DEFAULT NULL,
  `IterationSize` int(11) DEFAULT NULL,
  `create_dt` datetime(6) NOT NULL,
  `update_dt` datetime(6) NOT NULL,
  `Backlog_id` int(11) DEFAULT NULL,
  `ORG_ID_id` int(11) DEFAULT NULL,
  `Product_id` int(11) DEFAULT NULL,
  `Team_id` int(11) DEFAULT NULL,
  `create_by_id` int(11) NOT NULL,
  `update_by_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `manage_iterations_ar_create_by_id_bd0c9fd3_fk_account_a` (`create_by_id`),
  KEY `manage_iterations_ar_update_by_id_6f407fe8_fk_account_a` (`update_by_id`),
  KEY `manage_iterations_ar_Backlog_id_d9e9dc12_fk_manage_ba` (`Backlog_id`),
  KEY `manage_iterations_ar_ORG_ID_id_c79673bf_fk_account_a` (`ORG_ID_id`),
  KEY `manage_iterations_ar_Product_id_9fbccbbd_fk_manage_pr` (`Product_id`),
  KEY `manage_iterations_ar_Team_id_bc7cc538_fk_manage_pr` (`Team_id`),
  KEY `manage_iterations_ariterations_owner_id_1b5e37f7` (`owner_id`),
  CONSTRAINT `manage_iterations_ar_Backlog_id_d9e9dc12_fk_manage_ba` FOREIGN KEY (`Backlog_id`) REFERENCES `manage_backlogs_ar_backlog` (`id`),
  CONSTRAINT `manage_iterations_ar_ORG_ID_id_c79673bf_fk_account_a` FOREIGN KEY (`ORG_ID_id`) REFERENCES `account_ar_organization` (`id`),
  CONSTRAINT `manage_iterations_ar_Product_id_9fbccbbd_fk_manage_pr` FOREIGN KEY (`Product_id`) REFERENCES `manage_product_ar_product` (`id`),
  CONSTRAINT `manage_iterations_ar_Team_id_bc7cc538_fk_manage_pr` FOREIGN KEY (`Team_id`) REFERENCES `manage_product_ar_team` (`id`),
  CONSTRAINT `manage_iterations_ar_create_by_id_bd0c9fd3_fk_account_a` FOREIGN KEY (`create_by_id`) REFERENCES `account_ar_user` (`id`),
  CONSTRAINT `manage_iterations_ar_owner_id_1b5e37f7_fk_account_a` FOREIGN KEY (`owner_id`) REFERENCES `account_ar_user` (`id`),
  CONSTRAINT `manage_iterations_ar_update_by_id_6f407fe8_fk_account_a` FOREIGN KEY (`update_by_id`) REFERENCES `account_ar_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manage_iterations_ariterations`
--

LOCK TABLES `manage_iterations_ariterations` WRITE;
/*!40000 ALTER TABLE `manage_iterations_ariterations` DISABLE KEYS */;
INSERT INTO `manage_iterations_ariterations` VALUES (5,'Iteration 1 for Product P1',18,'AR_ITER_5','2020-02-03','2020-02-14','An iteration (sprint) is a time interval or timebox that an agile team uses to perform software development work.',0,0,'2020-03-04 14:40:54.815295','2020-03-04 14:40:54.815311',NULL,1,NULL,13,14,14),(6,'Iteration 2 for Product',14,'AR_ITER_6','2020-02-17','2020-02-28','This is an example iteration for training purposes',0,0,'2020-03-04 14:40:54.847836','2020-03-04 14:40:54.847850',22,1,8,12,14,14),(7,'Iteration 1 for Product P1',21,'AR_ITER_7','2020-02-03','2020-02-14','An iteration (sprint) is a time interval or timebox that an agile team uses to perform software development work.',0,0,'2020-03-05 00:59:19.278756','2020-03-05 00:59:19.278772',NULL,2,NULL,19,21,21),(8,'Iteration 2 for Product P1',21,'AR_ITER_8','2020-02-17','2020-02-28','This is an example iteration for training purposes',0,0,'2020-03-05 00:59:19.306445','2020-03-05 00:59:19.306460',33,2,12,18,21,21);
/*!40000 ALTER TABLE `manage_iterations_ariterations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manage_iterations_ariterations_UserStory`
--

DROP TABLE IF EXISTS `manage_iterations_ariterations_UserStory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `manage_iterations_ariterations_UserStory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ariterations_id` int(11) NOT NULL,
  `ar_user_story_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `manage_iterations_ariter_ariterations_id_ar_user__7d4d86a8_uniq` (`ariterations_id`,`ar_user_story_id`),
  KEY `manage_iterations_ar_ar_user_story_id_fc40c1cb_fk_user_stor` (`ar_user_story_id`),
  CONSTRAINT `manage_iterations_ar_ar_user_story_id_fc40c1cb_fk_user_stor` FOREIGN KEY (`ar_user_story_id`) REFERENCES `user_story_view_ar_user_story` (`id`),
  CONSTRAINT `manage_iterations_ar_ariterations_id_f1344379_fk_manage_it` FOREIGN KEY (`ariterations_id`) REFERENCES `manage_iterations_ariterations` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manage_iterations_ariterations_UserStory`
--

LOCK TABLES `manage_iterations_ariterations_UserStory` WRITE;
/*!40000 ALTER TABLE `manage_iterations_ariterations_UserStory` DISABLE KEYS */;
/*!40000 ALTER TABLE `manage_iterations_ariterations_UserStory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manage_product_ar_product`
--

DROP TABLE IF EXISTS `manage_product_ar_product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `manage_product_ar_product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Product_name` varchar(50) NOT NULL,
  `Product_description` longtext NOT NULL,
  `Business_unit` varchar(100) NOT NULL,
  `Product_size` int(11) NOT NULL,
  `Product_score` int(11) NOT NULL,
  `US_quality_threshold` int(11) NOT NULL,
  `create_dt` datetime(6) NOT NULL,
  `update_dt` datetime(6) NOT NULL,
  `ORG_ID_id` int(11) DEFAULT NULL,
  `create_by_id` int(11) NOT NULL,
  `update_by_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `manage_product_ar_pr_create_by_id_ef0f6749_fk_account_a` (`create_by_id`),
  KEY `manage_product_ar_pr_update_by_id_8fd3ed30_fk_account_a` (`update_by_id`),
  KEY `manage_product_ar_pr_ORG_ID_id_fe4e8906_fk_account_a` (`ORG_ID_id`),
  CONSTRAINT `manage_product_ar_pr_ORG_ID_id_fe4e8906_fk_account_a` FOREIGN KEY (`ORG_ID_id`) REFERENCES `account_ar_organization` (`id`),
  CONSTRAINT `manage_product_ar_pr_create_by_id_ef0f6749_fk_account_a` FOREIGN KEY (`create_by_id`) REFERENCES `account_ar_user` (`id`),
  CONSTRAINT `manage_product_ar_pr_update_by_id_8fd3ed30_fk_account_a` FOREIGN KEY (`update_by_id`) REFERENCES `account_ar_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manage_product_ar_product`
--

LOCK TABLES `manage_product_ar_product` WRITE;
/*!40000 ALTER TABLE `manage_product_ar_product` DISABLE KEYS */;
INSERT INTO `manage_product_ar_product` VALUES (7,'None','None','',0,0,0,'2020-03-04 14:40:49.677252','2020-03-04 14:40:49.677269',1,1,1),(8,'Product-P2 (example)','This is the second product provided for tutorial purposes','Internal Business-Unit-Name or External Business Customer',0,0,9,'2020-02-21 07:23:16.453939','2020-02-21 07:23:16.453956',1,1,1),(9,'BestEverMortgage 2020 Enhancements (example)','Best Ever Mortgage is upending the antiquated mortgage application process with AI algorithms and good old fashioned customer service.','Finance Division',0,0,13,'2020-02-21 07:23:48.229036','2020-02-21 07:23:48.229061',1,1,1),(11,'None','None','',0,0,0,'2020-03-05 00:59:18.187381','2020-03-05 00:59:18.187399',2,21,21),(12,'Product-P2 (example)','This is the second product provided for tutorial purposes','Internal Business-Unit-Name or External Business Customer',0,0,0,'2020-02-21 07:23:16.453939','2020-02-21 07:23:16.453956',2,21,21),(13,'BestEverMortgage 2020 Enhancements (example)','Best Ever Mortgage is upending the antiquated mortgage application process with AI algorithms and good old fashioned customer service.','Finance Division',0,0,0,'2020-02-21 07:23:48.229036','2020-02-21 07:23:48.229061',2,21,21);
/*!40000 ALTER TABLE `manage_product_ar_product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manage_product_ar_product_Team_parent`
--

DROP TABLE IF EXISTS `manage_product_ar_product_Team_parent`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `manage_product_ar_product_Team_parent` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ar_product_id` int(11) NOT NULL,
  `ar_team_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `manage_product_ar_produc_ar_product_id_ar_team_id_fd4965fe_uniq` (`ar_product_id`,`ar_team_id`),
  KEY `manage_product_ar_pr_ar_team_id_5b725721_fk_manage_pr` (`ar_team_id`),
  CONSTRAINT `manage_product_ar_pr_ar_product_id_bf862959_fk_manage_pr` FOREIGN KEY (`ar_product_id`) REFERENCES `manage_product_ar_product` (`id`),
  CONSTRAINT `manage_product_ar_pr_ar_team_id_5b725721_fk_manage_pr` FOREIGN KEY (`ar_team_id`) REFERENCES `manage_product_ar_team` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manage_product_ar_product_Team_parent`
--

LOCK TABLES `manage_product_ar_product_Team_parent` WRITE;
/*!40000 ALTER TABLE `manage_product_ar_product_Team_parent` DISABLE KEYS */;
/*!40000 ALTER TABLE `manage_product_ar_product_Team_parent` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manage_product_ar_team`
--

DROP TABLE IF EXISTS `manage_product_ar_team`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `manage_product_ar_team` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Team_name` varchar(100) NOT NULL,
  `Team_description` longtext NOT NULL,
  `create_dt` datetime(6) NOT NULL,
  `update_dt` datetime(6) NOT NULL,
  `ORG_id_id` int(11) DEFAULT NULL,
  `create_by_id` int(11) NOT NULL,
  `update_by_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `manage_product_ar_team_Team_name_ORG_id_id_e936f5e8_uniq` (`Team_name`,`ORG_id_id`),
  KEY `manage_product_ar_te_create_by_id_7f636dc8_fk_account_a` (`create_by_id`),
  KEY `manage_product_ar_te_update_by_id_55d07108_fk_account_a` (`update_by_id`),
  KEY `manage_product_ar_te_ORG_id_id_3c6ddae3_fk_account_a` (`ORG_id_id`),
  CONSTRAINT `manage_product_ar_te_ORG_id_id_3c6ddae3_fk_account_a` FOREIGN KEY (`ORG_id_id`) REFERENCES `account_ar_organization` (`id`),
  CONSTRAINT `manage_product_ar_te_create_by_id_7f636dc8_fk_account_a` FOREIGN KEY (`create_by_id`) REFERENCES `account_ar_user` (`id`),
  CONSTRAINT `manage_product_ar_te_update_by_id_55d07108_fk_account_a` FOREIGN KEY (`update_by_id`) REFERENCES `account_ar_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manage_product_ar_team`
--

LOCK TABLES `manage_product_ar_team` WRITE;
/*!40000 ALTER TABLE `manage_product_ar_team` DISABLE KEYS */;
INSERT INTO `manage_product_ar_team` VALUES (11,'None','None','2020-03-04 14:40:49.674122','2020-03-04 14:40:49.674139',1,1,1),(12,'Team-T1 (example)','Agile teams build software products.','2020-02-21 07:16:17.705074','2020-02-21 07:16:17.705082',1,14,14),(13,'FlexTeam (example)','This vendor provided team supplements all existing teams','2020-02-21 07:20:58.849623','2020-02-21 07:20:58.849628',1,14,14),(14,'Ticket Masters Kanban (example)','This team handles all production support tickets for all business units. This is a Kanban Team.','2020-02-21 07:21:26.179250','2020-02-21 07:21:26.179255',1,14,14),(15,'Mechanic Masters (example)','This team implements key strategic initiatives','2020-02-21 07:21:48.049098','2020-02-21 07:21:48.049103',1,14,14),(17,'None','None','2020-03-05 00:59:18.162406','2020-03-05 00:59:18.162422',2,21,21),(18,'Team-T1 (example)','Agile teams build software products.','2020-02-21 07:16:17.705074','2020-02-21 07:16:17.705082',2,21,21),(19,'FlexTeam (example)','This vendor provided team supplements all existing teams','2020-02-21 07:20:58.849623','2020-02-21 07:20:58.849628',2,21,21),(20,'Ticket Masters Kanban (example)','This team handles all production support tickets for all business units. This is a Kanban Team.','2020-02-21 07:21:26.179250','2020-02-21 07:21:26.179255',2,21,21),(21,'Mechanic Masters (example)','This team implements key strategic initiatives','2020-02-21 07:21:48.049098','2020-02-21 07:21:48.049103',2,21,21);
/*!40000 ALTER TABLE `manage_product_ar_team` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manage_product_ar_team_Team_member_list`
--

DROP TABLE IF EXISTS `manage_product_ar_team_Team_member_list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `manage_product_ar_team_Team_member_list` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ar_team_id` int(11) NOT NULL,
  `ar_user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `manage_product_ar_team_T_ar_team_id_ar_user_id_55f03599_uniq` (`ar_team_id`,`ar_user_id`),
  KEY `manage_product_ar_te_ar_user_id_a3bc44b1_fk_account_a` (`ar_user_id`),
  CONSTRAINT `manage_product_ar_te_ar_team_id_1a6fb798_fk_manage_pr` FOREIGN KEY (`ar_team_id`) REFERENCES `manage_product_ar_team` (`id`),
  CONSTRAINT `manage_product_ar_te_ar_user_id_a3bc44b1_fk_account_a` FOREIGN KEY (`ar_user_id`) REFERENCES `account_ar_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manage_product_ar_team_Team_member_list`
--

LOCK TABLES `manage_product_ar_team_Team_member_list` WRITE;
/*!40000 ALTER TABLE `manage_product_ar_team_Team_member_list` DISABLE KEYS */;
/*!40000 ALTER TABLE `manage_product_ar_team_Team_member_list` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manage_role_arrole`
--

DROP TABLE IF EXISTS `manage_role_arrole`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `manage_role_arrole` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `role_id` varchar(50) NOT NULL,
  `title` varchar(50) NOT NULL,
  `desc` longtext NOT NULL,
  `create_dt` datetime(6) NOT NULL,
  `update_dt` datetime(6) NOT NULL,
  `create_by_id` int(11) NOT NULL,
  `update_by_id` int(11) NOT NULL,
  `ORG_ID_id` int(11) DEFAULT NULL,
  `use` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `manage_role_arrole_create_by_id_c27ab508_fk_account_ar_user_id` (`create_by_id`),
  KEY `manage_role_arrole_update_by_id_45d9c613_fk_account_ar_user_id` (`update_by_id`),
  KEY `manage_role_arrole_ORG_ID_id_1d6dbcfb_fk_account_a` (`ORG_ID_id`),
  CONSTRAINT `manage_role_arrole_ORG_ID_id_1d6dbcfb_fk_account_a` FOREIGN KEY (`ORG_ID_id`) REFERENCES `account_ar_organization` (`id`),
  CONSTRAINT `manage_role_arrole_create_by_id_c27ab508_fk_account_ar_user_id` FOREIGN KEY (`create_by_id`) REFERENCES `account_ar_user` (`id`),
  CONSTRAINT `manage_role_arrole_update_by_id_45d9c613_fk_account_ar_user_id` FOREIGN KEY (`update_by_id`) REFERENCES `account_ar_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manage_role_arrole`
--

LOCK TABLES `manage_role_arrole` WRITE;
/*!40000 ALTER TABLE `manage_role_arrole` DISABLE KEYS */;
INSERT INTO `manage_role_arrole` VALUES (7,'AR_ROLE_7','Partner Manager','(example)','2020-02-21 07:51:19.759523','2020-02-21 07:51:19.759538',14,14,1,''),(8,'AR_ROLE_8','proxy-test-partner-user','(example)','2020-02-21 07:53:12.405115','2020-02-21 07:53:12.405124',14,14,1,''),(9,'AR_ROLE_9','Eagle','(example)','2020-02-21 07:53:28.673501','2020-02-21 07:53:28.673517',14,14,1,''),(11,'AR_ROLE_11','Partner Manager','(example)','2020-02-21 07:51:19.759523','2020-02-21 07:51:19.759538',21,21,2,''),(12,'AR_ROLE_12','proxy-test-partner-user','(example)','2020-02-21 07:53:12.405115','2020-02-21 07:53:12.405124',21,21,2,''),(13,'AR_ROLE_13','Eagle','(example)','2020-02-21 07:53:28.673501','2020-02-21 07:53:28.673517',21,21,2,'');
/*!40000 ALTER TABLE `manage_role_arrole` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_story_points_aruserstorypoints`
--

DROP TABLE IF EXISTS `user_story_points_aruserstorypoints`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_story_points_aruserstorypoints` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Point_Key` varchar(50) NOT NULL,
  `Point_Description` longtext NOT NULL,
  `Point_score` bigint(20) NOT NULL,
  `create_dt` datetime(6) NOT NULL,
  `update_dt` datetime(6) NOT NULL,
  `create_by_id` int(11) NOT NULL,
  `update_by_id` int(11) NOT NULL,
  `ORG_ID_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_story_points_ar_ORG_ID_id_a46634cd_fk_account_a` (`ORG_ID_id`),
  KEY `user_story_points_ar_create_by_id_7ae35774_fk_account_a` (`create_by_id`),
  KEY `user_story_points_ar_update_by_id_46eaec5e_fk_account_a` (`update_by_id`),
  CONSTRAINT `user_story_points_ar_ORG_ID_id_a46634cd_fk_account_a` FOREIGN KEY (`ORG_ID_id`) REFERENCES `account_ar_organization` (`id`),
  CONSTRAINT `user_story_points_ar_create_by_id_7ae35774_fk_account_a` FOREIGN KEY (`create_by_id`) REFERENCES `account_ar_user` (`id`),
  CONSTRAINT `user_story_points_ar_update_by_id_46eaec5e_fk_account_a` FOREIGN KEY (`update_by_id`) REFERENCES `account_ar_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_story_points_aruserstorypoints`
--

LOCK TABLES `user_story_points_aruserstorypoints` WRITE;
/*!40000 ALTER TABLE `user_story_points_aruserstorypoints` DISABLE KEYS */;
INSERT INTO `user_story_points_aruserstorypoints` VALUES (21,'None','None',0,'2020-03-04 14:40:49.724600','2020-03-04 14:40:49.724617',1,1,1),(22,'1','tiny',1,'2020-02-21 08:06:05.749018','2020-02-21 08:06:05.749037',14,14,1),(23,'2','small',3,'2020-02-21 08:06:34.839507','2020-02-21 08:06:34.839522',14,14,1),(24,'5','medium-medium',5,'2020-02-21 08:07:03.792424','2020-02-21 08:07:03.792434',14,14,1),(25,'8','medium-large',8,'2020-02-21 08:07:24.648819','2020-02-21 08:07:24.648841',14,14,1),(26,'3','medium-small',3,'2020-02-21 08:08:06.821177','2020-02-21 08:08:06.821192',14,14,1),(27,'13','large',13,'2020-02-21 08:09:06.246366','2020-02-21 08:09:06.246372',14,14,1),(28,'20','XL',20,'2020-02-21 08:49:58.937723','2020-02-21 08:49:58.937746',14,14,1),(29,'40','XX Large',40,'2020-02-21 08:51:54.862068','2020-02-21 08:51:54.862079',14,14,1),(30,'100','XXX Large',100,'2020-02-21 08:52:21.333485','2020-02-21 08:52:21.333497',14,14,1),(32,'None','None',0,'2020-03-05 00:59:18.244105','2020-03-05 00:59:18.244120',21,21,2),(33,'1','tiny',1,'2020-02-21 08:06:05.749018','2020-02-21 08:06:05.749037',21,21,2),(34,'2','small',3,'2020-02-21 08:06:34.839507','2020-02-21 08:06:34.839522',21,21,2),(35,'5','medium-medium',5,'2020-02-21 08:07:03.792424','2020-02-21 08:07:03.792434',21,21,2),(36,'8','medium-large',8,'2020-02-21 08:07:24.648819','2020-02-21 08:07:24.648841',21,21,2),(37,'3','medium-small',3,'2020-02-21 08:08:06.821177','2020-02-21 08:08:06.821192',21,21,2),(38,'13','large',13,'2020-02-21 08:09:06.246366','2020-02-21 08:09:06.246372',21,21,2),(39,'20','XL',20,'2020-02-21 08:49:58.937723','2020-02-21 08:49:58.937746',21,21,2),(40,'40','XX Large',40,'2020-02-21 08:51:54.862068','2020-02-21 08:51:54.862079',21,21,2),(41,'100','XXX Large',100,'2020-02-21 08:52:21.333485','2020-02-21 08:52:21.333497',21,21,2);
/*!40000 ALTER TABLE `user_story_points_aruserstorypoints` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_story_view_ar_us_status`
--

DROP TABLE IF EXISTS `user_story_view_ar_us_status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_story_view_ar_us_status` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `status_key` varchar(50) NOT NULL,
  `status_desc` longtext NOT NULL,
  `status_shortcode` varchar(50) NOT NULL,
  `create_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  `create_by_id` int(11) DEFAULT NULL,
  `update_by_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `status_key` (`status_key`),
  UNIQUE KEY `status_shortcode` (`status_shortcode`),
  KEY `user_story_view_ar_u_create_by_id_5e792f8b_fk_auth_user` (`create_by_id`),
  KEY `user_story_view_ar_u_update_by_id_3bf719fa_fk_auth_user` (`update_by_id`),
  CONSTRAINT `user_story_view_ar_u_create_by_id_5e792f8b_fk_auth_user` FOREIGN KEY (`create_by_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `user_story_view_ar_u_update_by_id_3bf719fa_fk_auth_user` FOREIGN KEY (`update_by_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_story_view_ar_us_status`
--

LOCK TABLES `user_story_view_ar_us_status` WRITE;
/*!40000 ALTER TABLE `user_story_view_ar_us_status` DISABLE KEYS */;
INSERT INTO `user_story_view_ar_us_status` VALUES (1,'None','None user story','None','2020-03-04 11:18:45.000000','2020-03-04 11:18:45.000000',1,1),(2,'Not Ready','A user story is available to being worked on (edited and reviewed) by one or more authors (system assigned or Human Input)','NR','2020-03-04 11:19:25.000000','2020-03-04 11:19:25.000000',1,1),(3,'Ideation','A user story is created with a title only and other  information (system assigned)','ID','2020-03-04 11:19:54.000000','2020-03-04 11:19:54.000000',1,1),(4,'Pending','Desc','PD','2020-03-04 11:20:22.000000','2020-03-04 11:20:22.000000',1,1),(5,'Active','desc','AC','2020-03-04 11:21:00.000000','2020-03-04 11:21:00.000000',1,1);
/*!40000 ALTER TABLE `user_story_view_ar_us_status` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_story_view_ar_us_type`
--

DROP TABLE IF EXISTS `user_story_view_ar_us_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_story_view_ar_us_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type_key` varchar(50) NOT NULL,
  `type_desc` longtext NOT NULL,
  `type_short_code` varchar(50) NOT NULL,
  `create_dt` datetime(6) NOT NULL,
  `update_dt` datetime(6) NOT NULL,
  `create_by_id` int(11) DEFAULT NULL,
  `update_by_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `type_key` (`type_key`),
  UNIQUE KEY `type_short_code` (`type_short_code`),
  KEY `user_story_view_ar_us_type_create_by_id_904e1644_fk_auth_user_id` (`create_by_id`),
  KEY `user_story_view_ar_us_type_update_by_id_5c5e2f06_fk_auth_user_id` (`update_by_id`),
  CONSTRAINT `user_story_view_ar_us_type_create_by_id_904e1644_fk_auth_user_id` FOREIGN KEY (`create_by_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `user_story_view_ar_us_type_update_by_id_5c5e2f06_fk_auth_user_id` FOREIGN KEY (`update_by_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_story_view_ar_us_type`
--

LOCK TABLES `user_story_view_ar_us_type` WRITE;
/*!40000 ALTER TABLE `user_story_view_ar_us_type` DISABLE KEYS */;
INSERT INTO `user_story_view_ar_us_type` VALUES (1,'None','None','None','2020-03-04 11:21:43.000000','2020-03-04 11:21:43.000000',1,1),(2,'Non-Functional Requirement','A User Story of type [Non-Functional Requirement] where the role, goal and benefit fulfillment is aimed at meeting a technology objective to support functional user story fulfillment.','NFR','2020-03-04 11:22:12.000000','2020-03-04 11:22:12.000000',1,1),(3,'Discovery','An User Story of type [discovery or spike] where the role, goal and benefit fulfillment is aimed at meeting a research objective to support functional user story creation.','DISC','2020-03-04 11:22:37.000000','2020-03-04 11:22:37.000000',1,1),(4,'Functional','A User Story of type [functional] where the role, goal and benefit fulfillment is aimed at meeting a functional objective to support business value generation.','FUNC','2020-03-04 11:23:09.000000','2020-03-04 11:23:09.000000',1,1);
/*!40000 ALTER TABLE `user_story_view_ar_us_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_story_view_ar_user_story`
--

DROP TABLE IF EXISTS `user_story_view_ar_user_story`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_story_view_ar_user_story` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `owner_id` int(11) DEFAULT NULL,
  `title` varchar(80) NOT NULL,
  `story_tri_part_text` longtext NOT NULL,
  `acceptance_criteria` longtext NOT NULL,
  `ac_readability_score` bigint(20) NOT NULL,
  `conversation` longtext NOT NULL,
  `convo_readability_score` bigint(20) NOT NULL,
  `attachments` varchar(100) DEFAULT NULL,
  `autoscoring_on` tinyint(1) NOT NULL,
  `archive_indicator` tinyint(1) NOT NULL,
  `readiness_quality_score` bigint(20) NOT NULL,
  `updated_dt` datetime(6) NOT NULL,
  `created_dt` datetime(6) NOT NULL,
  `ORG_id_id` int(11) DEFAULT NULL,
  `UST_ID_id` int(11) DEFAULT NULL,
  `ar_user_id` int(11) DEFAULT NULL,
  `backlog_parent_id` int(11) DEFAULT NULL,
  `created_by_id` int(11) NOT NULL,
  `story_points_id` int(11) DEFAULT NULL,
  `updated_by_id` int(11) NOT NULL,
  `user_story_status_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_story_view_ar_u_created_by_id_35dd9c90_fk_account_a` (`created_by_id`),
  KEY `user_story_view_ar_u_updated_by_id_2aede9c1_fk_account_a` (`updated_by_id`),
  KEY `user_story_view_ar_u_ORG_id_id_2168fedb_fk_account_a` (`ORG_id_id`),
  KEY `user_story_view_ar_u_UST_ID_id_fcde65db_fk_user_stor` (`UST_ID_id`),
  KEY `user_story_view_ar_u_user_story_status_id_7a48e6b8_fk_user_stor` (`user_story_status_id`),
  KEY `user_story_view_ar_u_story_points_id_6ecabd92_fk_user_stor` (`story_points_id`),
  KEY `user_story_view_ar_u_ar_user_id_c17ee31d_fk_account_a` (`ar_user_id`),
  KEY `user_story_view_ar_user_story_owner_id_5785bb4f` (`owner_id`),
  KEY `user_story_view_ar_u_backlog_parent_id_f238d060_fk_manage_ba` (`backlog_parent_id`),
  CONSTRAINT `user_story_view_ar_u_ORG_id_id_2168fedb_fk_account_a` FOREIGN KEY (`ORG_id_id`) REFERENCES `account_ar_organization` (`id`),
  CONSTRAINT `user_story_view_ar_u_UST_ID_id_fcde65db_fk_user_stor` FOREIGN KEY (`UST_ID_id`) REFERENCES `user_story_view_ar_us_type` (`id`),
  CONSTRAINT `user_story_view_ar_u_ar_user_id_c17ee31d_fk_account_a` FOREIGN KEY (`ar_user_id`) REFERENCES `account_ar_user` (`id`),
  CONSTRAINT `user_story_view_ar_u_backlog_parent_id_f238d060_fk_manage_ba` FOREIGN KEY (`backlog_parent_id`) REFERENCES `manage_backlogs_ar_backlog` (`id`),
  CONSTRAINT `user_story_view_ar_u_created_by_id_35dd9c90_fk_account_a` FOREIGN KEY (`created_by_id`) REFERENCES `account_ar_user` (`id`),
  CONSTRAINT `user_story_view_ar_u_owner_id_5785bb4f_fk_account_a` FOREIGN KEY (`owner_id`) REFERENCES `account_ar_user` (`id`),
  CONSTRAINT `user_story_view_ar_u_story_points_id_6ecabd92_fk_user_stor` FOREIGN KEY (`story_points_id`) REFERENCES `user_story_points_aruserstorypoints` (`id`),
  CONSTRAINT `user_story_view_ar_u_updated_by_id_2aede9c1_fk_account_a` FOREIGN KEY (`updated_by_id`) REFERENCES `account_ar_user` (`id`),
  CONSTRAINT `user_story_view_ar_u_user_story_status_id_7a48e6b8_fk_user_stor` FOREIGN KEY (`user_story_status_id`) REFERENCES `user_story_view_ar_us_status` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_story_view_ar_user_story`
--

LOCK TABLES `user_story_view_ar_user_story` WRITE;
/*!40000 ALTER TABLE `user_story_view_ar_user_story` DISABLE KEYS */;
INSERT INTO `user_story_view_ar_user_story` VALUES (5,NULL,'None','','',0,'',0,'None',0,0,0,'2020-03-04 14:40:49.696348','2020-03-04 14:40:49.696359',1,NULL,NULL,NULL,1,NULL,1,NULL),(6,18,'Enroll Partner jfgjfj','As a Partner Manager I want to enroll a qualified partner','',0,'',0,'None',0,0,63,'2020-03-05 05:17:28.891225','2020-03-04 14:40:54.642900',1,3,18,26,14,NULL,1,4),(7,NULL,'None','','',0,'',0,'None',0,0,0,'2020-03-05 00:59:18.206078','2020-03-05 00:59:18.206088',2,NULL,NULL,NULL,21,NULL,21,NULL),(8,21,'Enroll Partner','As a Partner Manager I want to enroll a qualified partner','',0,'',0,'None',0,0,63,'2020-03-05 00:59:19.115337','2020-03-05 00:59:19.115347',2,3,NULL,37,21,NULL,21,4);
/*!40000 ALTER TABLE `user_story_view_ar_user_story` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-03-07 13:55:44
