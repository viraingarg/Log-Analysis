create or replace view errno21 as select time::timestamp::date as td,
count(case when status like '%200%' then 1 end) as done,
count(case when status like '%404%' then 1 end) as abcd,
count(method) as al from log group by td;

-------------------------------------------------------------------------------

create or replace view articlespopular as select articles.title,
count(case when log.status like '%200%' then 1 end) as data from
articles left join log on log.path like '%' || articles.slug
group by articles.title;

------------------------------------------------------------------------------

create or replace view loc_pop as select substring(path,10)
as location from log where path like '/arti%';

--------------------------------------------------------------------------------

create or replace view countall as select articles.author,count(*)
from articles join loc_pop on articles.slug = loc_pop.location
group by articles.author order by count(*) desc;

--------------------------------------------------------------------------------
create or replace view authpopular as select authors.name, authors.id
from authors join articles on  articles.author = authors.id group by
authors.id;
