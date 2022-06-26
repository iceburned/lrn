select c.country_name, r.river_name from countries c
left join countries_rivers as cr
using (country_code)
left join rivers as r
on cr.river_id = r.id
where c.continent_code in (
    select cc.continent_code from continents as cc
    where cc.continent_name = 'Africa'
    )
order by c.country_name limit 5;