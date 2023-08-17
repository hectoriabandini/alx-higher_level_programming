--Import in hbtn_0c_0 database this table dump: download
SELECT city, AVG(temperature) AS avg_temp
FROM your_table_name
GROUP BY city
ORDER BY avg_temp DESC;
