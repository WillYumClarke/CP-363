SELECT DISTINCT m.memberSurname, m.memberForename,
(SELECT COUNT(*) FROM pub AS p WHERE p.pubMemberID = m.memberID AND m.memberID = 49 AND  p.pubPubType = 'a') AS pubCount
FROM member AS m, pub AS p
WHERE m.memberID = 49 AND p.pubPubType = 'a'
ORDER BY m.memberSurname, m.memberForename