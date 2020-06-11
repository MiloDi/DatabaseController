import psycopg2

class postgres_connection(object):
    """postgres db connection"""
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.con = None
        
    def exec_transact(self, sql):
        self.conn = psycopg2.connect(self.connection_string)
        with self.conn:
            with self.conn.cursor() as curs:
                curs.execute(sql)
        self.conn.close()


class dbr_mgr:
    """manages the queries""""
    def __init__(self, csv_read_loc):
        self.csv_read_loc = csv_read_loc  
        self.data = []
        self.header = None
        
    def create_tbl(self, table_name, column_names ={}):
        # PHS = peak height (mm) of standard
        # PHx = peak height (mm) of analyte in unspiked aliquot of unknown
        # PHsp = peak height (mm) of analyte in spiked aliquot of unknown
        # Csp = output
        create = """ CREATE TABLE {} (
                _id SERIAL PRIMARY KEY,
                FLOAT(10),
                FLOAT(10),
                 FLOAT(10),
                FLOAT(10)); """,       
        return create

    def insert_tbl(self, tbl_name, values):
    # """INSERT INTO chroma (tote_id, PHs, PHx, PHsp) VALUES (2, 0.0, 2.2, 3.3);""" 
        return "INSERT INTO {} VALUES (%s);").format(tbl_name), values)
        
    def drop_tble(self, tbl_name):
        return """DROP TABLE {};""".format(tbl_name)