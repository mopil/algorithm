select j.flavor
from july as j
inner join first_half as fh
on fh.flavor = j.flavor
group by j.flavor
order by (sum(fh.total_order) + sum(j.total_order)) desc
limit 3