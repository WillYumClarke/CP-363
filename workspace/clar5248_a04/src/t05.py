"""
-------------------------------------------------------
Author:  William Clarke
ID:      190524800
Email:   clar5248@mylaurier.ca
-------------------------------------------------------
"""
from Connect import  Connect
from Tunnel import Tunnel
from functions import get_key_info

tableName = 'pub'
refTableName = 'pubType'
constraintSchema = 'information_schema'

try:
    tunnel = Tunnel("hopper.txt")
    with tunnel.tunnel:
        conn = Connect("dcris.txt")
    cursor = conn.cursor
    rows = get_key_info(cursor, constraintSchema, tableName, refTableName)
    print("Columns:")
    print(conn.cursor.column_names)
    print("Data:")
    
    #print(rows)
    for row in rows:
        print(row)
        
    conn.close()
except BaseException as e:
        print(str(e))