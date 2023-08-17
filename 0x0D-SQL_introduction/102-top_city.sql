--Import in hbtn_0c_0 database this table dump:
--download (same as Temperatures #0)
SELECT city, AVG(temperature) AS avg_temp
FROM your_table_name
WHERE month IN ('July', 'August')
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
