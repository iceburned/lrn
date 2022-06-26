SELECT
    `name`, DATE_format(`start`, '%Y-%m-%d')
FROM
    games
WHERE
    YEAR(start) BETWEEN 2011 AND 2012

ORDER BY start limit 50;