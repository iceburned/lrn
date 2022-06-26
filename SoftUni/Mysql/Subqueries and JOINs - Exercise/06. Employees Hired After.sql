select e.first_name, e.last_name, e.hire_date, d.name as dept_name
from employees as e
         join departments as d
              using (department_id)
where e.hire_date > timestamp('1999/1/1')
  and d.name in ('Sales', 'Finance')
order by e.hire_date;