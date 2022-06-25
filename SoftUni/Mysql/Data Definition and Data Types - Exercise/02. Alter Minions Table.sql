ALTER TABLE `minions`
ADD `town_id` int
;

alter table `minions`
add constraint `fk_minions_towns`
FOREIGN KEY (town_id) REFERENCES towns(id)
;