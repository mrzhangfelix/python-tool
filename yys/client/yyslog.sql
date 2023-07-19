-- 导出 dev 的数据库结构
CREATE DATABASE IF NOT EXISTS `dev` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `dev`;

-- 导出  表 dev.yyslog 结构
CREATE TABLE IF NOT EXISTS `yyslog` (
  `id` int DEFAULT NULL,
  `st` datetime DEFAULT NULL,
  `ut` datetime DEFAULT NULL,
  `type` varchar(50) DEFAULT NULL,
  `count` varchar(50) DEFAULT NULL,
  `remark` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- 正在导出表  dev.yyslog 的数据：~3 rows (大约)
INSERT INTO `yyslog` (`id`, `st`, `ut`, `type`, `count`, `remark`) VALUES
	(1, NULL, NULL, 'jiejie', NULL, NULL),
	(2, '2023-07-19 18:45:22', NULL, 'tansuo', NULL, NULL),
	(3, '2023-07-19 16:30:34', '2023-07-19 17:27:10', 'yaoqi', '70', 'ended');
