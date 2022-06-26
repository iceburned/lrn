select
       e.employee_id,
       concat(first_name, ' ', last_name) as full_name,
       d.department_id,
       d.name as 'department_name'
       from employees as e
join departments as d
on e.employee_id = d.manager_id
order by e.employee_id limit 5;