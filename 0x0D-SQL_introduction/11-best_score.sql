-- listing records with condition that score>= 10 in thesecond_table.
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY score DESC;
