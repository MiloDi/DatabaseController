import csv
import psycopg2
import sys
import getpass


def get_pasw():
    return getpass.getpass("Enter database password: ")

def get_secret():
    with open('postgrespas.txt', 'r') as secret:
        pasw = secret.read()
    return str(pasw)

        
def postgres(dbname, user, host, secret, connect_timeout):   
    try:
        conn = psycopg2.connect("dbname='{}' user='{}' host='{}' password='{}' connect_timeout={}".format(dbname, user, host, secret, connect_timeout))
        print("Connection successfull") 
        return conn
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise  
    
def get_data():
    data = []
    with open('paper_data.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for i in csv_reader: 
            data.append(i)
    return data

def create_queries():
    # PHS = peak height (mm) of standard
    # PHx = peak height (mm) of analyte in unspiked aliquot of unknown
    # PHsp = peak height (mm) of analyte in spiked aliquot of unknown
    queries = {
        'create' : """ CREATE TABLE chroma (
            tote_id SERIAL PRIMARY KEY,
            PHs FLOAT(10),
            PHx FLOAT(10),
            PHsp FLOAT(10),
            Csp FLOAT(10)); """,
        'delete' : """DROP TABLE chroma;""",
        'insert' : """INSERT INTO chroma (tote_id, PHs, PHx, PHsp) VALUES (2, 0.0, 2.2, 3.3);"""
        
        }
    return queries

def exec_queries(queries, configs, data):
    dbname, user, host, secret, connect_timeout = [i for i in configs]
    conn = postgres(dbname, user, host, secret, connect_timeout)
    cur = conn.cursor()
    cur.execute(queries['delete'])
    cur.execute(queries['create'])
    for i in range(len(data)):
        cur.execute("""INSERT INTO chroma (tote_id, PHs, PHx, PHsp) VALUES ({}, {}, {}, {});""".format(i+1, data[i][0], data[i][1], data[i][2]))
    conn.commit()
        
    cur.execute('select * from chroma;')
    conn.commit()
    for i in cur:
        print(i) 
    # for i in cur:
        calc = do_math(i[1], i[2], i[3], 165.87)
        cur.execute("""UPDATE chroma SET Csp = {} WHERE tote_id = '{}';""".format(calc, i[0]))

    cur.execute('select * from chroma;')
    conn.commit()
    for i in cur:
        print(i) 
        
    conn.close()

def do_math(a, b, c, constant):
    return ((a-b)/c)*constant 
    
def main():
    try:
        pas = get_secret()
    except FileNotFoundError:
        pas = get_pasw()
    configs = ['postgres', 'postgres', 'localhost', pas, 1]    
    data = get_data()
    data.pop(0)
    queries = create_queries()
    exec_queries(queries, configs, data)
    

    
if __name__ == "__main__":
    main()

