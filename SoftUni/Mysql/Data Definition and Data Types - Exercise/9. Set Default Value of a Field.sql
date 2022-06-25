ALTER TABLE `minions`.`users`
CHANGE COLUMN `last_login_time` `last_login_time` DATETIME NULL DEFAULT CURRENT_TIMESTAMP;