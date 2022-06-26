SELECT
    first_name, last_name
FROM
    employees
WHERE
    first_name LIKE '%ei%'
        OR last_name LIKE '%ei%';