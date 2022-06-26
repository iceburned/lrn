select peak_name, river_name,
lower(concat(left(peak_name, length(peak_name) -1), river_name)) as 'mix'
from peaks, rivers
where right(peak_name, 1) = left(river_name, 1)
 order by 'mix';