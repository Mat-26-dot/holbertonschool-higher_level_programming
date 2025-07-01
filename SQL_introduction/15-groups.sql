-- lists the number of records with the same score in the table

SELECT score
FROM second_table
WHERE score = value
ORDER BY score DESC;