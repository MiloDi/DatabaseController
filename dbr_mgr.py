



class dbr_mgr:
    """manages the queries""""
    def __init__(self, csv_read_loc):
        self.csv_read_loc = csv_read_loc  
        self.data = []
        self.header = None
        
    def create_tbl(table_name, column_names ={}):
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
            'delete' : """DROP TABLE chroma;""",
            'insert' : """INSERT INTO chroma (tote_id, PHs, PHx, PHsp) VALUES (2, 0.0, 2.2, 3.3);"""            
        return create

    def insert_tbl():
        return "INSERT INTO {} VALUES (%s)").format(table_name), values_list)