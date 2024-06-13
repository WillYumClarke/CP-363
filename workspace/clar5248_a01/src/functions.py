"""
-------------------------------------------------------
Author:  William Clarke
ID:      190524800
Email:   clar5248@mylaurier.ca
__updated__ = "2022-10-10"
-------------------------------------------------------
"""


def get_broad(cursor, broadId=None):
    """
    -------------------------------------------------------
    Queries the broad table.
    Use: rows = get_broad(cursor)
    Use: rows = get_broad(cursor, broadId=v)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        broadId - a broad ID (int)
    Returns:
        rows - (list of broad table data)
            if broadId is not None:
                rows matching broadId
            else:
                the entire broad table
            Sorted by broad description
    -------------------------------------------------------
    """
    if broadId == None:
        sql = "SELECT * FROM broad ORDER BY broadDesc"
        cursor.execute(sql)
        rows = cursor.fetchall()
    else:
        sql = "Select * FROM broad WHERE broadId = %(broadId)s ORDER BY broadDesc"
        params = {'broadId': broadId}
        cursor.execute(sql, params)
        rows = cursor.fetchall()
    return rows

    
def get_publications(cursor, memberId=None, pubPubType=None):
    """
    -------------------------------------------------------
    Queries the pub table.
    Use: rows = get_publications(cursor)
    Use: rows = get_publications(cursor, memberId=v1)
    Use: rows = get_publications(cursor, pubPubType=v2)
    Use: rows = get_publications(cursor, memberId=v1, pubPubType=v2)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        memberId - a member ID number (int)
        pubPubType - a publication type (str)
    Returns:
        rows - (list of pub table data)
            if memberId and/or pubPubType are not None:
                rows matching memberId and/or pubPubType
            else:
                the entire pub table
            Sorted by publication title
    -------------------------------------------------------
    """
    if memberId == None or pubPubType == None:
        sql = "SELECT * FROM pub ORDER BY pubTitle"
        cursor.execute(sql)
        rows = cursor.fetchall()
    else:
        sql = "Select * FROM pub WHERE pubPubType = %(pubType)s OR pubMemberId = %(memberId)s ORDER BY pubTitle"
        params = {'pubType': pubPubType, 'memberId': memberId}
        cursor.execute(sql, params)
        rows = cursor.fetchall()
    return rows
        
    
def get_member_broad(cursor, memberId=None, broadId=None):
    """
    -------------------------------------------------------
    Queries the vMemberBroad view.
    Use: rows = get_member_broad(cursor)
    Use: rows = get_member_broad(cursor, memberId=v1)
    Use: rows = get_member_broad(cursor, broadId=v2)
    Use: rows = get_member_broad(cursor, memberId=v1, broadId=v2)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        memberId - a member ID number (int)
        broadId - a broad ID number (int)
    Returns:
        rows - (list of vMemberBroad view data)
            if memberId and/or broadId are not None:
                rows matching memberId and/or broadId
            else:
                the entire vMemberBroad view
            Sorted by member last name, first name, and broad description
    -------------------------------------------------------
    """
    if memberId == None or broadId == None:
        sql = "SELECT * FROM vMemberBroad ORDER BY memberSurname, memberForename, broadDesc"
        cursor.execute(sql)
        rows = cursor.fetchall()
    else:
        sql = "SELECT * FROM vMemberBroad WHERE memberId = %(memberId)s OR broadId = %(broadId)s ORDER BY memberSurname, memberForename, broadDesc"
        params = {'memberId': memberId, 'broadId': broadId}
        cursor.execute(sql, params)
        rows = cursor.fetchall()
    return rows

            
def get_expertises(cursor, broad=None, narrow=None):
    """
    -------------------------------------------------------
    Queries the vBroadNarrow view.
    Use: rows = get_expertises(cursor)
    Use: rows = get_expertises(cursor, broad=v1)
    Use: rows = get_expertises(cursor, narrow=v2)
    Use: rows = get_expertises(cursor, broad=v1, narrow=v2)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        broad - a partial broad expertise description (str)
        narrow - a partial narrow expertise description (str)
    Returns:
        rows - (list of vBroadNarrow view data)
            if broad and/or narrow are not None:
                rows containing broad and/or narrow
            else:
                the entire vBroadNarrow view
            Sorted by broad description, narrow broad description
    -------------------------------------------------------
    """
    if broad == None or narrow == None:
        sql = "SELECT * FROM vBroadnarrow ORDER BY broadDesc, narrowDesc"
        cursor.execute(sql)
        rows = cursor.fetchall()
    else:
        sql = "SELECT * FROM vBroadNarrow WHERE broadDesc LIKE %(broad)s OR narrowDesc LIKE %(narrow)s ORDER BY broadDesc, narrowDesc"
        params = {'broad': broad, 'narrow': narrow}
        cursor.execute(sql, params)
        rows = cursor.fetchall()
    return rows
        
