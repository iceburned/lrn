select e.first_name, e.last_name, t.name as town, a.address_text from employees e
join addresses a
using (address_id)
join towns t
using (town_id)
order by e.first_name, e.last_name limit 5;