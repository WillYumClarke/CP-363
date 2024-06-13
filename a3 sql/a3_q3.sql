SELECT b.broadDesc,
(SELECT COUNT(*) FROM narrow AS n
WHERE n.narrowBroadID = b.broadID) AS narrowCount
FROM broad AS b
ORDER BY b.broadDesc