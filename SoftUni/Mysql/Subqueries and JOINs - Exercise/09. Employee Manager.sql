select e.employee_id, e.first_name, e.manager_id, em.first_name as 'manager_name'
from employees as e
join employees as em
on e.manager_id = em.employee_id
where e.manager_id in (3, 7)
order by e.first_name;