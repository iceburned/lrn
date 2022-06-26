select e.employee_id, e.first_name, p.name
from employees as e
         join employees_projects as ep
              using (employee_id)
         join projects as p
              using (project_id)
where DATE(p.start_date) > '2002-08-13'
  and p.end_date is null
order by e.first_name, p.name
limit 5;