SELECT
    CAST(T1.obsdate AS DATE) AS dateob,
    ROUND(T1.phase, 4) AS phase_zr,
    ROUND(T1.vmag, 4) AS vmag_zr,
    ROUND(T2.phase, 4) AS phase_zg,
    ROUND(T2.vmag, 4) AS vmag_zg,
    ROUND((T2.vmag - T1.vmag), 4) AS color_index
FROM
    'table_122695-2000-SY1320122695.csv' AS T1
JOIN
    'table_122695-2000-SY1320122695.csv' AS T2 ON T1.obsdate = T2.obsdate
WHERE
    T1.filtercode = 'zr'
    AND T2.filtercode = 'zg'
	AND (T2.obsdate - T1.obsdate) BETWEEN INTERVAL '-10 minutes' AND INTERVAL '10 minutes';
