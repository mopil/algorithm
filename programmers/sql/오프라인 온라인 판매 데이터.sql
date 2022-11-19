select
    date_format(t.sales_date, '%Y-%m-%d') sales_date,
    t.product_id,
    t.user_id,
    t.sales_amount
from (
    select online_sale_id, user_id, product_id, sales_amount, sales_date from online_sale
    union
    select offline_sale_id, NULL, product_id, sales_amount, sales_date from offline_sale) t
where t.sales_date like '2022-03%'
order by t.sales_date, t.product_id, t.user_id