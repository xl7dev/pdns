CREATE DATABASE IF NOT EXISTS pdns;
USE pdns;
CREATE TABLE IF NOT EXISTS pdns(
  id int(11) NOT NULL AUTO_INCREMENT,
  name varchar(255)          NOT NULL DEFAULT '',
  type varchar(10)           NOT NULL DEFAULT '',
  value varchar(255)         NOT NULL DEFAULT '',
  count BIGINT(20) UNSIGNED  NOT NULL DEFAULT '1',
  first DATETIME             NOT NULL,
  last DATETIME              NOT NULL ,
  PRIMARY KEY (ID),
  UNIQUE KEY (name,type,value),
  KEY name_idx (name),
  KEY value_idx (value)
)