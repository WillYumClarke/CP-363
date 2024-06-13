SELECT b.broadDesc, n.narrowDesc,
(SELECT COUNT(*) FROM member AS m, memberNarrow AS mn
WHERE m.memberID = mn.memberNarrowMemberID
AND mn.memberNarrowNarrowID = n.narrowID) AS memberCount
FROM broad AS b, narrow AS n
ORDER BY b.broadDesc, n.narrowDesc