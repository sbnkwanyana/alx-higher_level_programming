-- selects the city and average from temperatures, grouping by city and ordered by average temperature from hottest to coldest
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
