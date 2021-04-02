CREATE SCHEMA IF NOT EXISTS `meli` DEFAULT CHARACTER SET utf8 ;
use meli;

CREATE TABLE `meli`.`item` (
  `site` varchar(4) NOT NULL,
  `id` varchar(12) NOT NULL,
  `price` float(14,2) DEFAULT NULL,
  `start_time` varchar(30) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `description` varchar(80) DEFAULT NULL,
  `nickname` varchar(40) DEFAULT NULL,
  `Timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`site`,`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;