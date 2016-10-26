-- , sum(m.amount* (julianday(m.start_date) - julianday(m.end_date)))
SELECT s.name, m.drug_name, sum(m.amount* (julianday(m.start_med) - julianday(m.end_med)))
FROM staff s, medications m
WHERE m.staff_id = s.staff_id
AND m.mdate between date('2013') and  date('2016')
GROUP BY s.name, m.drug_name
HAVING s.role = 'D'
ORDER BY s.name;
