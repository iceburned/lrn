select e.employee_id,
       concat(e.first_name, ' ', e.last_name) as 'employee_name',
       concat(em.first_name, ' ', em.last_name) as 'manager_name',
       d.name        as 'department_name'
from employees as e
         join employees as em
              on e.manager_id = em.employee_id
         join departments as d
              on e.department_id = d.department_id
order by e.employee_id
limit 5;