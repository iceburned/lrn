SELECT
    CONCAT_WS(' ', first_name, last_name) AS Full_name,
    TIMESTAMPDIFF(DAY, born, died) AS DaysLived
FROM
    authors;