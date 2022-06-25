SELECT
    title
FROM
    books
WHERE
    SUBSTR(title, 1, 12) = 'Harry Potter';