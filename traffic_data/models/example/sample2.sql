select *
from {{ ref('sample1') }}
where id = 1
