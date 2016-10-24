
.print Option 1
select chart_id 
from charts c, patients p
where p.hcno = c.hcno


select * from
medications m, charts c
where m.hcno = c.hcno
union
select * from
medications m, charts c
where m.hcno = c.hcno
union
select * from
medications m, charts c
where m.hcno = c.hcno
union
select * from 


