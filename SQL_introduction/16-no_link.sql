--  lists all records of the table second_table

SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND NOT ""
ORDER BY score DESC;