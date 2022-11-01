-- selects score and and count of score as number grouping by score and ordering count in descending order
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY number DESC;
