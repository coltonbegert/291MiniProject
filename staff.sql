

create view report(name, drug_name,


select name, total(amount), drug_name, mdate
from medications, staff
where m. hcno = s.staff_id
group by drug_name, mdate;


select total(amount), drug_name
from medications, drugs
where d.drug_name = m.drug_name
group by category, mdate;

select drug_name
from medications, diagnoses
where d.hcno = m.hcno



select d.diagnosis
from diagnoses, medications, drugs dr
where d.hcno = m.hcno, dr = 'asdfasd', dr.drug_name = m.drug_name
order by avg(amount)
