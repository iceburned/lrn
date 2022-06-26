select c.country_code, count(m.mountain_range) as 'mountain_range'
from mountains_countries c
         join mountains as m
              on c.mountain_id = m.id
where c.country_code in ('BG', 'RU', 'US')
group by c.country_code
order by mountain_range desc;