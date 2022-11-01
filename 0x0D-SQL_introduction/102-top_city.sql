-- selects a limit of 3 records, the city name and average calcu;ated by city in the months of july and august ordered from hottest to coldest
SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month = 7 OR month = 8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
