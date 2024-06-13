"""
-------------------------------------------------------
Author:  William Clarke
ID:      190524800
Email:   clar5248@mylaurier.ca
-------------------------------------------------------
"""

def get_member_publications(cursor, pubTitle=None, pubType=None):
    """
    -------------------------------------------------------
    Queries the pub and member tables.
    Use: rows = get_member_publications(cursor)
    Use: rows = get_member_publications(cursor, pubTitle=v1)
    Use: rows = get_member_publications(cursor, pubType=v2)
    Use: rows = get_member_publications(cursor, pubTitle=v1, pubType=v2)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        pubTitle - a partial pubTitle (str)
        pubType - a publication type (str)
    Returns:
        rows - (list of member's last name, member's first
            name, the title of a publication, and the full publication
            type (i.e. 'article' rather than 'a') data)
            if pubTitle and/or pubType are not None:
                rows containing pubTitle and/or pubType
            else:
                all member and publication rows
            Sorted by last name, first name, publication title
    -------------------------------------------------------
    """
    if pubTitle == None and pubType == None:
        sql = """      
        SELECT m.memberSurname, m.memberForename, p.pubTitle,
        CASE 
            WHEN p.pubPubType = 'a' THEN 'article'
            WHEN p.pubPubType = 'p' THEN 'paper'
            WHEN p.pubPubType = 'b' THEN 'book'
        END AS pubPubType
        FROM member AS m, pub AS p
        ORDER BY m.memberSurname, m.memberForename, p.pubTitle
        """
        cursor.execute(sql)
        rows = cursor.fetchall()
    elif pubTitle == None and pubType != None:
        sql = """           
        SELECT m.memberSurname, m.memberForename, p.pubTitle,
        CASE 
            WHEN p.pubPubType = 'a' THEN 'article'
            WHEN p.pubPubType = 'p' THEN 'paper'
            WHEN p.pubPubType = 'b' THEN 'book'
        END AS pubPubType
        FROM member AS m, pub AS p
        WHERE p.pubPubType = %(pubType)s
        ORDER BY m.memberSurname, m.memberForename, p.pubTitle
        """
        params = {'pubType': pubType}
        cursor.execute(sql, params)
        rows = cursor.fetchall()
    elif pubTitle != None and pubType == None:
        pubTitle += '%'
        sql = """        
        SELECT m.memberSurname, m.memberForename, p.pubTitle,
        CASE 
            WHEN p.pubPubType = 'a' THEN 'article'
            WHEN p.pubPubType = 'p' THEN 'paper'
            WHEN p.pubPubType = 'b' THEN 'book'
        END AS pubPubType
        FROM member AS m, pub AS p
        WHERE p.pubTitle LIKE %(pubTitle)s
        ORDER BY m.memberSurname, m.memberForename, p.pubTitle
        """
        params = {'pubTitle': pubTitle}
        cursor.execute(sql, params)
        rows = cursor.fetchall()
    elif pubTitle != None and pubType != None:
        pubTitle += '%'
        sql = """
        SELECT m.memberSurname, m.memberForename, p.pubTitle,
        CASE 
            WHEN p.pubPubType = 'a' THEN 'article'
            WHEN p.pubPubType = 'p' THEN 'paper'
            WHEN p.pubPubType = 'b' THEN 'book'
        END AS pubPubType
        FROM member AS m, pub AS p
        WHERE p.pubTitle LIKE %(pubTitle)s AND p.pubPubType = %(pubType)s
        ORDER BY m.memberSurname, m.memberForename, p.pubTitle
        """
        params = {'pubTitle': pubTitle, 'pubType': pubType}
        cursor.execute(sql, params)
        rows = cursor.fetchall()
    return rows


def get_publication_counts(cursor, memberId=None, pubType=None):
    """
    -------------------------------------------------------
    Queries the pub and member tables.
    Use: rows = get_publication_counts(cursor)
    Use: rows = get_publication_counts(cursor, memberId=v1)
    Use: rows = get_publication_counts(cursor, pubType=v2)
    Use: rows = get_publication_counts(cursor, memberId=v1, pubType=v2)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        memberId - a member ID number (int)
        pubType - a publication type (str)
    Returns:
        rows - (list of member's last name, member's first
            name, and the number of publications of type
            pubType data)
            if memberId or pubType is not None:
                rows containing memberId and/or pubType
            else:
                all member names and publication counts
            Sorted by last name, first name
    -------------------------------------------------------
    """
    if memberId == None and pubType == None:
        sql = """        
        SELECT m.memberSurname, m.memberForename,
        (SELECT COUNT(*) FROM pub AS p WHERE p.pubMemberID = m.memberID) AS pubCount
        FROM member AS m
        ORDER BY m.memberSurname, m.memberForename
        """
        cursor.execute(sql)
        rows = cursor.fetchall()
    elif memberId != None and pubType == None:
        sql = """
        SELECT m.memberSurname, m.memberForename,
        (SELECT COUNT(*) FROM pub AS p WHERE p.pubMemberID = m.memberID AND m.memberID = %(memberID)s) AS pubCount
        FROM member AS m
        WHERE m.memberID = %(memberID)s
        ORDER BY m.memberSurname, m.memberForename
        """
        params = {'memberID': memberId, 'memberID': memberId}
        cursor.execute(sql, params)
        rows = cursor.fetchall()
    elif memberId == None and pubType != None:
        sql = """
        SELECT DISTINCT m.memberSurname, m.memberForename,
        (SELECT COUNT(*) FROM pub AS p WHERE p.pubMemberID = m.memberID AND p.pubPubType = %(pubType)s) AS pubCount
        FROM member AS m, pub AS p
        WHERE p.pubPubType = %(pubPubType)s
        ORDER BY m.memberSurname, m.memberForename
        """
        params = {'pubType': pubType, 'pubType': pubType}
        cursor.execute(sql, params)
        rows = cursor.fetchall()
    elif memberId != None and pubType != None:
        sql = """
        SELECT DISTINCT m.memberSurname, m.memberForename,
        (SELECT COUNT(*) FROM pub AS p WHERE p.pubMemberID = m.memberID 
            AND m.memberID = %(memberID)s 
            AND  p.pubPubType = %(pubType)s) AS pubCount
        FROM member AS m, pub AS p
        WHERE m.memberID = %(memberID)s AND p.pubPubType = %(pubType)s
        ORDER BY m.memberSurname, m.memberForename
        """
        params = {'pubType': pubType, 'memberID':memberId, 'pubType': pubType, 'memberID':memberId}
        cursor.execute(sql, params)
        rows = cursor.fetchall()
    return rows


def get_broad_counts(cursor, memberId=None):
    """
    -------------------------------------------------------
    Queries the member and broad tables.
    Use: rows = get_broad_counts(cursor)
    Use: rows = get_broad_counts(cursor, memberId=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        memberId - a member ID number (int)
    Returns:
        rows - (list of member's last name, member's first
            name, and the number of broad expertises they hold data)
            if memberId is not None:
                rows containing memberId
            else:
                all member and broad expertise rows
            Sorted by last name, first name
    -------------------------------------------------------
    """
    if memberId == None:
        sql = """
        SELECT m.memberSurname, m.memberForename,
        (SELECT COUNT(*) FROM broad AS b, memberBroad AS mb 
        WHERE b.broadID = mb.memberBroadBroadID 
        AND mb.memberBroadMemberID = m.memberID)
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
        AND mb.memberBroadMemberID = 49)
        FROM member AS m
        WHERE m.memberID = 49
        ORDER BY m.memberSurname, m.memberForename
        """
        params = {'memberID': memberId, 'memebrID': memberId}
        cursor.execute(sql, params)
        rows = cursor.fetchall()
    return rows

    
def get_all_expertises(cursor, memberId=None):
    """
    -------------------------------------------------------
    Queries the member, broad, and narrow tables
    Use: rows = get_all_expertises(cursor)
    Use: rows = get_all_expertises(cursor, memberId=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        memberId - a member ID number (int)
    Returns:
        rows - (list of member's last name, member's first
            name, a broad description, and a narrow description data)
            if memberId is not None:
                rows containing memberId
            else:
                all member and expertise rows
            Sorted by last name, first name, broad description, narrow
                description
    -------------------------------------------------------
    """
    
    if memberId == None:
        sql = """
        SELECT m.memberSurname, m.memberForename, b.broadDesc, n.narrowDesc
        FROM member AS m, broad as b, narrow as n
        ORDER BY m.memberSurname, m.memberForename, b.broadDesc, n.narrowDesc
        """
        cursor.execute(sql)
        rows = cursor.fetchall()
    else:
        sql = """
        SELECT m.memberSurname, m.memberForename, b.broadDesc, n.narrowDesc
        FROM member AS m, broad as b, narrow as n
        WHERE m.memberID = %(memberId)s
        ORDER BY m.memberSurname, m.memberForename, b.broadDesc, n.narrowDesc
        """
        params = {'memberID': memberId}
        cursor.execute(sql, params)
        rows = cursor.fetchall()
    return rows
