SELECT m.memberSurname, m.memberForename,
(SELECT COUNT(*) FROM broad AS b, memberBroad AS mb 
WHERE b.broadID = mb.memberBroadBroadID 
AND mb.memberBroadMemberID = m.memberID)
FROM member AS m
ORDER BY m.memberSurname, m.memberForename