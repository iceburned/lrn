SELECT
    first_name, last_name
FROM
    employees
WHERE
    NOT job_title LIKE '%engineer%';