SELECT m.memberSurname, m.memberForename,
(SELECT COUNT(*) FROM broad AS b, memberBroad AS mb
WHERE b.broadID = mb.memberBroadBroadID 
AND mb.memberBroadMemberID = m.memberID) AS broadCount,
(SELECT COUNT(*) FROM narrow AS n, memberNarrow AS mn
WHERE n.narrowID = mn.memberNarrowNarrowID
AND mn.memberNarrowMemberID = m.memberID) AS narrowCount
FROM member AS m
ORDER BY m.memberSurname, m.memberForename