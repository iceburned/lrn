SELECT
    department_id, MAX(salary) AS 'max_salary'
FROM
    employees
WHERE
    NOT salary BETWEEN 30000 AND 70000
GROUP BY department_id
ORDER BY department_id