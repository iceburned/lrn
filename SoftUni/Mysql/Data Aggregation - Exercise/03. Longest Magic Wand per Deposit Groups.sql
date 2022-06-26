SELECT
    deposit_group, MAX(magic_wand_size) AS 'm_wand'
FROM
    wizzard_deposits
GROUP BY deposit_group
ORDER BY m_wand , deposit_group;