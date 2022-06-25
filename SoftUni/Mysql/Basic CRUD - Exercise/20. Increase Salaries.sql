update employees
set salary = salary + (salary * 0.12)
where department_id in (1, 2, 4, 11);
select salary from employees