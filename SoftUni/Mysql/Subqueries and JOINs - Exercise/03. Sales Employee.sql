select e.employee_id, e.first_name, e.last_name, d.name as department_name from employees e
join departments d
using (department_id)
where d.name = 'Sales'
order by e.employee_id desc;