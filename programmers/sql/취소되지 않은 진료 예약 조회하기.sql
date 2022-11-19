-- 코드를 입력하세요
select
    a.APNT_NO,
    p.PT_NAME,
    p.PT_NO,
    d.MCDP_CD,
    d.DR_NAME,
    a.APNT_YMD
from appointment as a
join patient as p
on a.PT_NO = p.PT_NO
join doctor as d
on a.MDDR_ID = d.DR_ID
where a.APNT_CNCL_YN = 'N'
and date_format(a.APNT_YMD, '%Y-%m-%d') = '2022-04-13'
order by a.APNT_YMD