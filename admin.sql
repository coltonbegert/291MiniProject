-- , sum(m.amount* (julianday(m.start_date) - julianday(m.end_date)))
-- AND m.mdate between date('2013') and  date('2016')
SELECT s.name, m.drug_name, sum(m.amount* (cast(julianday(m.end_med) as int) - cast(julianday(m.start_med) as int)))
FROM staff s, medications m
WHERE m.staff_id = s.staff_id
AND m.mdate between date('2015-01-01') and date('2016-01-01')
GROUP BY s.name, m.drug_name
HAVING s.role = 'D'
ORDER BY s.name;
