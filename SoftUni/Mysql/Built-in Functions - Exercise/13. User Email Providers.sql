SELECT
    user_name,
    REGEXP_SUBSTR(`email`, '[a-zA-Z]+.[a-z]+$') AS email_provider
FROM
    users
ORDER BY email_provider , user_name;