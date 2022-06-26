select
       e.employee_id, e.first_name, e.salary, d.name 'department_name'
from employees e
join departments d
using (department_id)
where e.salary > 15000
order by d.department_id desc limit 5;