select t.town_id, t.name as 'town_name', a.address_text from towns as t
join addresses as a
on a.town_id = t.town_id
where t.name in ('San Francisco', 'Sofia', 'Carnation')
order by t.town_id, a.address_id;
