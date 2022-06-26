select ep.employee_id,
       e.first_name,
       if(year(p.start_date) >= 2005, Null, p.name) as 'project_name'
from employees as e
         join employees_projects as ep
              using (employee_id)
         join projects as p
              using (project_id)
where e.employee_id = 24
order by project_name;