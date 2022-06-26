select avg(salary) as 'min_average_salary'
from employees as e
group by department_id
order by min_average_salary
limit 1;