-- script that lists all records of the table second_table of the database hbtn_0c_0
SELECT score, name
WHERE name IS NOT null
FROM second_table
ORDER BY second_table DESC;