"""
-------------------------------------------------------
Author:  William Clarke
ID:      190524800
Email:   clar5248@mylaurier.ca
-------------------------------------------------------
"""


def get_all_pub_counts(cursor, memberId=None):
    """
    -------------------------------------------------------
    Queries the pub and member tables.
    Use: rows = pub_counts(cursor)
    Use: rows = pub_counts(cursor, memberId=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        memberId - a member ID (int)
    Returns:
        rows - (list of member's last name, a member's first
            name, and the numbers of publications of each type data.
            Name these three fields "articles", "papers", and "books")
            if memberId is not None:
                rows containing memberId
            else:
                all member and publication rows
            Sorted by last name, first name
    -------------------------------------------------------
    """
    if memberId == None:
        sql = """
        SELECT m.memberSurname, m.memberForename,
        (SELECT COUNT(*) FROM pub AS p
        WHERE p.pubMemberId = m.memberId AND p.pubPubType LIKE 'a') AS articles,
        (SELECT COUNT(*) FROM pub AS p
        WHERE p.pubMemberId = m.memberId AND p.pubPubType LIKE 'p') AS papers,
        (SELECT COUNT(*) FROM pub AS p
        WHERE p.pubMemberId = m.memberId AND p.pubPubType LIKE 'b') AS books
        FROM member AS m
        ORDER BY m.memberSurname, m.memberForename
        """
        cursor.execute(sql)
        rows = cursor.fetchall()
    else:
        sql = """
        SELECT m.memberSurname, m.memberForename,
        (SELECT COUNT(*) FROM pub AS p
        WHERE p.pubMemberId = m.memberId AND p.pubPubType LIKE 'a') AS articles,
        (SELECT COUNT(*) FROM pub AS p
        WHERE p.pubMemberId = m.memberId AND p.pubPubType LIKE 'p') AS papers,
        (SELECT COUNT(*) FROM pub AS p
        WHERE p.pubMemberId = m.memberId AND p.pubPubType LIKE 'b') AS books
        FROM member AS m
        WHERE m.memberId = %(memberId)s
        ORDER BY m.memberSurname, m.memberForename
        """
        params = {'memberId': memberId}
        cursor.execute(sql, params)
        rows = cursor.fetchall()
    return rows


def get_expertise_counts(cursor, memberId=None):
    """
    -------------------------------------------------------
    Use: rows = get_expertise_counts(cursor)
    Use: rows = get_expertise_counts(cursor, memberId=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        memberId - a member ID number (int)
    Returns:
        rows - (list of member's last name, a member's first
            name, and the number of broad and narrow expertises
            for the member data. Name these fields "broadCount" and "narrowCount")
            if memberId is not None:
                rows containing memberId
            else:
                all member, broad, and narrow expertise rows
            Sorted by last name, first name
    -------------------------------------------------------
    """
    if memberId == None:
        sql = """
        SELECT m.memberSurname, m.memberForename,
        (SELECT COUNT(*) FROM broad AS b, memberBroad AS mb
        WHERE b.broadID = mb.memberBroadBroadID 
        AND mb.memberBroadMemberID = m.memberID) AS broadCount,
        (SELECT COUNT(*) FROM narrow AS n, memberNarrow AS mn
        WHERE n.narrowID = mn.memberNarrowNarrowID
        AND mn.memberNarrowMemberID = m.memberID) AS narrowCount
        FROM member AS m
        ORDER BY m.memberSurname, m.memberForename
        """
        cursor.execute(sql)
        rows = cursor.fetchall()
    else:
        sql = """
        SELECT m.memberSurname, m.memberForename,
        (SELECT COUNT(*) FROM broad AS b, memberBroad AS mb
        WHERE b.broadID = mb.memberBroadBroadID 
        AND mb.memberBroadMemberID = m.memberID) AS broadCount,
        (SELECT COUNT(*) FROM narrow AS n, memberNarrow AS mn
        WHERE n.narrowID = mn.memberNarrowNarrowID
        AND mn.memberNarrowMemberID = m.memberID) AS narrowCount
        FROM member AS m
        WHERE m.memberID = %(memberId)s
        ORDER BY m.memberSurname, m.memberForename
        """
        params = {'memberId': memberId}
        cursor.execute(sql, params)
        rows = cursor.fetchall()
    return rows


def get_broad_counts(cursor, broadId=None):
    """
    -------------------------------------------------------
    Use: rows = get_broad_counts(cursor)
    Use: rows = get_broad_counts(cursor, broadId=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        broadId - a keyword ID number (int)
    Returns:
        rows - (list of a broad expertise descriptions and the number of
            narrow expertises that belong to it data. Name the
            second field "narrowCount".)
            if broadId is not None:
                rows containing broadId
            else:
                all broad and narrow rows
            Sorted by broad expertise description
    -------------------------------------------------------
    """
    if broadId == None:
        sql = """
        SELECT b.broadDesc,
        (SELECT COUNT(*) FROM narrow AS n
        WHERE n.narrowBroadID = b.broadID) AS narrowCount
        FROM broad AS b
        ORDER BY b.broadDesc
        """
        cursor.execute(sql)
        rows = cursor.fetchall()
    else:
        sql = """
        SELECT b.broadDesc,
        (SELECT COUNT(*) FROM narrow AS n
        WHERE n.narrowBroadID = b.broadID) AS narrowCount
        FROM broad AS b
        WHERE b.broadID = %(broadId)s
        ORDER BY b.broadDesc
        """
        params = {'broadId': broadId}
        cursor.execute(sql, params)
        rows = cursor.fetchall()
    return rows
    

def get_broad_member_counts(cursor, broadId=None):
    """
    -------------------------------------------------------
    Use: rows = get_broad_memberCounts(cursor)
    Use: rows = get_broad_memberCounts(cursor, broadId=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        broadId - a keyword ID number (int)
    Returns:
        rows - (list of a keyword description and the number of members
            that have it data. Name the second field "memberCount".)
            if broadId is not None:
                rows containing broadId
            else:
                all member and keyword rows
            Sorted by keyword description
    -------------------------------------------------------
    """
    if broadId == None:
        sql = """
        SELECT b.broadDesc,
        (SELECT COUNT(*) FROM member AS m, memberBroad AS mb
        WHERE b.broadID = mb.memberBroadBroadID
        AND mb.memberBroadMemberID = m.memberID) AS memberCount
        FROM broad AS b
        ORDER BY broadDesc
        """
        cursor.execute(sql)
        rows = cursor.fetchall()
    else:
        sql = """
        SELECT b.broadDesc,
        (SELECT COUNT(*) FROM member AS m, memberBroad AS mb
        WHERE b.broadID = mb.memberBroadBroadID
        AND mb.memberBroadMemberID = m.memberID) AS memberCount
        FROM broad AS b
        WHERE b.broadID = %(broadId)s
        ORDER BY broadDesc
        """
        params = {'broadId': broadId}
        cursor.execute(sql, params)
        rows = cursor.fetchall()
    return rows


def get_narrow_member_counts(cursor, narrowId=None):
    """
    -------------------------------------------------------
    Use: rows = get_narrow_memberCounts(cursor)
    Use: rows = get_narrow_memberCounts(cursor, narrowId=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        narrowId - a supp_key ID number (int)
    Returns:
        rows - (list of a broad expertise description, a narrow
            expertise description, and the number of members that have that
            narrow expertise data. Name the last field "memberCount".)
            if narrowId is not None:
                rows containing narrowId
            else:
                all member, broad, and narrow expertises rows
            Sorted by broad description, narrow description
    -------------------------------------------------------
    """
    if narrowId == None:
        sql = """
        SELECT b.broadDesc, n.narrowDesc,
        (SELECT COUNT(*) FROM member AS m, memberNarrow AS mn
        WHERE m.memberID = mn.memberNarrowMemberID
        AND mn.memberNarrowNarrowID = n.narrowID) AS memberCount
        FROM broad AS b, narrow AS n
        ORDER BY b.broadDesc, n.narrowDesc
        """
        cursor.execute(sql)
        rows = cursor.fetchall()
    else:
        sql = """
        SELECT b.broadDesc, n.narrowDesc,
        (SELECT COUNT(*) FROM member AS m, memberNarrow AS mn
        WHERE m.memberID = mn.memberNarrowMemberID
        AND mn.memberNarrowNarrowID = n.narrowID) AS memberCount
        FROM broad AS b, narrow AS n
        WHERE n.narrowID = %(narrowId)s
        ORDER BY b.broadDesc, n.narrowDesc
        """
        params = {'narrowId': narrowId}
        cursor.execute(sql,params)
        rows = cursor.fetchall()
    return rows