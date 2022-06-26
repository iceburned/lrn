select count(salary) from employees
where salary > (select avg(salary) from employees);