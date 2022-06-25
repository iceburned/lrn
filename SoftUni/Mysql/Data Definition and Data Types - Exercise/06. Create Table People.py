CREATE TABLE `people`(
`id` INT PRIMARY KEY AUTO_INCREMENT,
`name` VARCHAR(200) NOT NULL,
`picture` BLOB,
`height` FLOAT(5, 2),
`weight` FLOAT(5, 2),
`gender` CHAR(1) NOT NULL,
`birthday` DATE NOT NULL,
`biography` TEXT
);

INSERT INTO `people`
VALUES
(1, 'Teol', 'a2w', 123.22, 23.23, 'm', '21-11-11', 'asdasdad'),
(2, 'Beol', 'a2w', 123.22, 23.23, 'm', '21-11-11', 'asdssxasdad'),
(3, 'Aeol', 'a2w', 123.22, 23.23, 'm', '21-11-11', 'asdssxasdad'),
(4, 'Zeol', 'a2w', 123.22, 23.23, 'm', '21-11-11', 'asdssxasdad'),
(5, 'Veol', 'a2w', 123.22, 23.23, 'm', '21-11-11', 'asdssxasdad');