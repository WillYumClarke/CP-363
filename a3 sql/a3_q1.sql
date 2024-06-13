SELECT m.memberSurname, m.memberForename,
(SELECT COUNT(*) FROM pub AS p
WHERE p.pubMemberId = m.memberId AND p.pubPubType LIKE 'a') AS articles,
(SELECT COUNT(*) FROM pub AS p
WHERE p.pubMemberId = m.memberId AND p.pubPubType LIKE 'p') AS papers,
(SELECT COUNT(*) FROM pub AS p
WHERE p.pubMemberId = m.memberId AND p.pubPubType LIKE 'b') AS books
FROM member AS m
ORDER BY m.memberSurname, m.memberForename