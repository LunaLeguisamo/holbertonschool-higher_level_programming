-- Script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0
SELECT COUNT(*) FROM second_table
WHERE score = number
ORDER BY second_table DESC;