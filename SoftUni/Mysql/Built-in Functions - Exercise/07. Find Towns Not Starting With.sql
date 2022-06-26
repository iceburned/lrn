SELECT
    town_id, `name`
FROM
    towns
WHERE
    LEFT(name, 1) NOT IN ('r' , 'b', 'd')
ORDER BY `name`;