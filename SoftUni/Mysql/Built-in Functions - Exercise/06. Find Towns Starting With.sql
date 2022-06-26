select town_id, name from towns
WHERE left(name, 1) = 'm' or left(name, 1) = 'k' or left(name, 1) = 'B'
or left(name, 1) = 'E'
order by `name`;