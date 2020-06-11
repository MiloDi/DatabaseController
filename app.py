import csv_mgr
import db_context_mgr
import dbr_mgr
import getpass



def get_congif():
    configs = ['postgres', 'postgres', 'localhost', pas, 1]   
    connnection_string = """
        dbname='{}'
        user='{}'
        host='{}'
        password='{}'
        connect_timeout='{}'
        """.format(dbname, user, host, secret, connect_timeout)
    try:
        with open('postgrespas.txt', 'r') as secret:
                pasw = secret.read()
    except FileNotFoundError:
        pas = getpass.getpass("Enter database password: ")
        



def do_math(a, b, c, constant):
    return ((a-b)/c)*constant 

def main():
    
    with postgres_connection() as conn:
        data =  pd.read_sql(sql, conn.connector)
        
    
    data = get_data()
    data.pop(0)
    queries = create_queries()
    exec_queries(queries, configs, data)
    

    
if __name__ == "__main__":
    main()

