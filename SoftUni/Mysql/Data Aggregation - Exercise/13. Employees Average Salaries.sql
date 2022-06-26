CREATE table `hpe` AS
select * from employees
where salary > 30000 and manager_id != 42;
UPDATE `hpe`
set `salary` = `salary` + 5000
where `department_id` = 1;

select `department_id`, avg(salary) as `avg_salary`
from `hpe`
group by department_id
ORDER BY department_id