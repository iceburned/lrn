select
e.first_name, e.last_name, e.department_id
from employees as e
where e.salary >
(
select avg(e2.salary) from employees as e2
where e2.department_id = e.department_id
)
order by department_id, employee_id
limit 10;