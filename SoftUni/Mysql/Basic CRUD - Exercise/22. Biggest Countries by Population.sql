SELECT
    country_name, population
FROM
    countries
WHERE
    continent_code = 'EU'
ORDER BY population desc, country_name limit 30;