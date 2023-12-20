select *
from {{ ref('sample2') }}
where id = 1