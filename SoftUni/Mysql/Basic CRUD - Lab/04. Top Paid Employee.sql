CREATE VIEW `hi_salary` AS
    SELECT
        *
    FROM
        `employees`
    ORDER BY salary DESC
    LIMIT 1;

SELECT
    *
FROM
    hi_salary