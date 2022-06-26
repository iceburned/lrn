SELECT
    department_id, ROUND(MIN(salary), 2) as e
FROM
    employees
GROUP BY department_id
having e > 800;