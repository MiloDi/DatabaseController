import csv
import psycopg2
import sys
import getpass
import db_context_mgr

class csv_mgr:     
    """csv"""
    def __init__(self, csv_read_loc):
        self.csv_read_loc = csv_read_loc  
        self.data = []
        self.headers = None
        
    def get_data(self):
        """gets the data from csv file"""
        with open(self.csv_read_loc, mode='r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for i in csv_reader: 
                self.data.append(i)
        self.headers - self.data.pop(0)
    
    def write_data(self):
        return False



    
