SELECT  m.memberSurname, m.memberForename, b.broadDesc, n.narrowDesc
FROM member AS m, broad as b, narrow as n
WHERE m.memberId = 49
ORDER BY m.memberSurname, m.memberForename, b.broadDesc, n.narrowDesc;