create table people(
    `person_id` int primary key auto_increment,
    `first_name` varchar(20),
    `salary` decimal(10, 2),
    passport_id int
);
create table `passports`(
    `passport_id` int primary key auto_increment,
    `passport_number` varchar(20) unique
)auto_increment = 101;

alter table `people`
add constraint fk_people_passports
foreign key (passport_id)
references passports(passport_id);

insert into `passports` (passport_number)
value
('N34FG21B'),
('K65LO4R7'),
('ZE657QP2');

insert into people
values
(1, 'Roberto', 43300.00, 102),
(2, 'Tom', 56100.00, 103),
(3, 'Yana', 60200.00, 101);