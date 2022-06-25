CREATE TABLE `users`(
`id` INT(63) PRIMARY KEY AUTO_INCREMENT,
`username` VARCHAR(60) NOT NULL,
`password` VARCHAR(52) NOT NULL,
`profile_picture` BLOB,
`last_login_time` DATETIME,
`is_deleted` BOOL
);

INSERT INTO `users`
VALUES
(1, 'sas', 'ASDQ233', 'ASD', '11.2.2', True),
(2, 'qas', 'ASDQ233', 'ASD', '11.2.2', True),
(3, 'zas', 'ASDQ233', 'ASD', '11.2.2', True),
(4, 'cas', 'ASDQ233', 'ASD', '11.2.2', True),
(5, 'bas', 'ASDQ233', 'ASD', '11.2.2', True);