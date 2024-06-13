SELECT b.broadDesc,
(SELECT COUNT(*) FROM member AS m, memberBroad AS mb
WHERE b.broadID = mb.memberBroadBroadID
AND mb.memberBroadMemberID = m.memberID) AS memberCount
FROM broad AS b
ORDER BY broadDesc