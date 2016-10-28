--
-- .print Option 1
-- select chart_id
-- from charts c, patients p
-- where p.hcno = c.hcno
--
--
-- select * from
-- medications m, charts c
-- where m.hcno = c.hcno
-- union
-- select * from
-- medications m, charts c
-- where m.hcno = c.hcno
-- union
-- select * from
-- medications m, charts c
-- where m.hcno = c.hcno
-- union
-- select * from



SELECT c.chart_id, c.adate, c.edate, CASE WHEN (c.edate is NULL) THEN 'open' ELSE 'closed' END status
FROM charts c
WHERE c.hcno = '15384'
ORDER BY c.adate DESC;
.print
-- SELECT
-- FROM charts c, symptoms s, diagnoses d, medications m
-- WHERE c.chart_id = s.chart_id
-- AND c.chart_id = d.chart_id
-- AND c.chart_id = m.chart_id


SELECT type, cdate, value
FROM (
  SELECT 'Symptom' as type, s.obs_date as cdate, s.symptom as value
  FROM charts c, symptoms s
  WHERE c.chart_id = s.chart_id
  AND c.chart_id = '10056'
  UNION
  SELECT 'Diagnosis' as type, d.ddate as cdate, d.diagnosis as value
  FROM charts c, diagnoses d
  WHERE c.chart_id = d.chart_id
  AND c.chart_id = '10056'
  UNION
  SELECT 'Medication' as type, m.mdate as cdate, m.drug_name as value
  FROM charts c, medications m
  WHERE c.chart_id = m.chart_id
  AND c.chart_id = '10056'
)
ORDER BY cdate ASC;
