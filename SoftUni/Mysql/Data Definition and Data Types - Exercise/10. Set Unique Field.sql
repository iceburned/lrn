ALTER TABLE `minions`.`users`
DROP PRIMARY KEY,
ADD PRIMARY KEY (`id`),
ADD UNIQUE (`username`);
;