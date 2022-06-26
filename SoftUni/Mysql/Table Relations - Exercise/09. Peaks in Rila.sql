select m.mountain_range, p.peak_name, p.elevation from `mountains` as m
join peaks as p
on p.mountain_id = m.id
where m.mountain_range = 'Rila'
order by p.elevation desc ;