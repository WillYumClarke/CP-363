"""
-------------------------------------------------------
Author:  William Clarke
ID:      190524800
Email:   clar5248@mylaurier.ca
__updated__ = "2022-10-27"
-------------------------------------------------------
"""
from Connect import  Connect
from Tunnel import Tunnel
from functions import get_broad_counts

memberId = 3
try:
    tunnel = Tunnel("hopper.txt")
    with tunnel.tunnel:
        conn = Connect("dcris.txt")
    cursor = conn.cursor
    rows = get_broad_counts(cursor, memberId)
    
    print("Columns:")
    print(conn.cursor.column_names)
    print("Data:")
    
    #print(rows)
    for row in rows:
        print(row)
        
    conn.close()
except BaseException as e:
        print(str(e))
