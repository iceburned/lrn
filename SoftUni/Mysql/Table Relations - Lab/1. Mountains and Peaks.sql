create table `mountains` (
    id int auto_increment primary key ,
    `name` varchar(50)
);
create table `peaks` (
    id int auto_increment primary key,
    `name` varchar(50),
    `mountain_id` int
);
alter table peaks
add constraint `fk_peaks_mountains`
foreign key (mountain_id)
references mountains(id);