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