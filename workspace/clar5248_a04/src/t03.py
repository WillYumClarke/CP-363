"""
-------------------------------------------------------
Author:  William Clarke
ID:      190524800
Email:   clar5248@mylaurier.ca
-------------------------------------------------------
"""
from Connect import  Connect
from Tunnel import Tunnel
from functions import get_constraint_info

constraintType = 'FOREIGN KEY'
tableSchema = 'information_schema'

try:
    tunnel = Tunnel("hopper.txt")
    with tunnel.tunnel:
        conn = Connect("dcris.txt")
    cursor = conn.cursor
    rows = get_constraint_info(cursor, tableSchema, constraintType)
    
    print("Columns:")
    print(conn.cursor.column_names)
    print("Data:")
    
    #print(rows)
    for row in rows:
        print(row)
        
    conn.close()
except BaseException as e:
        print(str(e))