-- selects the state with the highest temperature
SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state ORDER BY state;
