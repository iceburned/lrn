select
       c.id as driver_id,
       v.vehicle_type,
       concat(first_name, ' ', last_name)
from campers as c
join vehicles as v
on v.driver_id = c.id