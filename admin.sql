-- , sum(m.amount* (julianday(m.start_date) - julianday(m.end_date)))
-- AND m.mdate between date('2013') and  date('2016')
-- SELECT s.name, m.drug_name, sum(m.amount* (cast(julianday(m.end_med) as int) - cast(julianday(m.start_med) as int)))
-- FROM staff s, medications m
-- WHERE m.staff_id = s.staff_id
-- AND m.mdate between date('2010-01-01') and date('2016-01-01')
-- GROUP BY s.name, m.drug_name
-- HAVING s.role = 'D'
-- ORDER BY s.name;
--
--
-- SELECT d.category, m.drug_name, sum(m.amount* (cast(julianday(m.end_med) as int) - cast(julianday(m.start_med) as int))),
--   (SELECT sum(m1.amount* (cast(julianday(m1.end_med) as int) - cast(julianday(m1.start_med) as int))) as total
--   FROM medications m1
--   WHERE m1.drug_name = m.drug_name)
-- FROM drugs d, medications m
-- WHERE d.drug_name = m.drug_name
-- AND m.mdate between date('2010-01-01') and  date('2016-01-01')
-- GROUP BY d.category, m.drug_name
-- ORDER BY d.category;


SELECT d.diagnosis
FROM charts c, diagnoses d,medications m
WHERE c.chart_id = d.chart_id
AND m.chart_id = c.chart_id
AND m.drug_name = 'Retrovir'
AND m.mdate > d.ddate
GROUP BY d.diagnosis
ORDER BY (select  (SUM(CASE WHEN m1.drug_name = m.drug_name THEN 1 ELSE 0 END)/count(*))
  FROM medications m1, diagnoses d1
  WHERE m1.chart_id = d1.chart_id
  AND m1.hcno = d1.hcno
  AND d1.diagnosis = d.diagnosis) DESC;
