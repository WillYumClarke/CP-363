SELECT m.memberSurname, m.memberForename, p.pubTitle,
CASE 
	WHEN p.pubPubType = 'a' THEN 'article'
	WHEN p.pubPubType = 'p' THEN 'paper'
	WHEN p.pubPubType = 'b' THEN 'book'
END AS pubPubType
FROM member AS m, pub AS p
WHERE p.pubPubType = 'a' AND p.pubTitle LIKE 'd%'
ORDER BY m.memberSurname, m.memberForename, p.pubTitle
