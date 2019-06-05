import pymysql
import sys

REGION = 'us-west-2'

rds_host  = "test.cnsof36yhl8s.us-west-2.rds.amazonaws.com"
name = "test"
password = "test1234"
db_name = "test"

def save_events(event):
    """
    This function fetches content from mysql RDS instance
    """
    result = []
    conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
    with conn.cursor() as cur:
        cur.execute("""insert into Employee (EmpID, Name) values( %s, '%s')""" % (event['EmpID'], event['Name']))
        cur.execute("""select * from Employee""")
        conn.commit()
        cur.close()
        for row in cur:
            result.append(list(row))
        print ("Data from RDS...")
        print (result)

def main(event, context):
    save_events(event)
        


# event = {
#   "id": 777,
#   "name": "appychip"
# }
# context = ""
# main(event, context)
