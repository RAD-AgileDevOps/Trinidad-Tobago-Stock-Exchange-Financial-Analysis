class ttse_data_analysis:
        """
        Developer: Roger De Four
        Date: 2020-06-15
        Description: a class object designed to encapusale the business logic in relation to perfoming
        rudimentary data analysis on publicly available datasets from the TTSE


        """

        def __init__(self , co_name):

            self.co_name = co_name
            print(self.co_name)  # oututs to the command line the company being analysed
        
        def data_frame(self):
            
            import pandas as pd
            import psycopg2 as pg2
            import numpy as np
            import matplotlib as mp
            from matplotlib import pyplot as plt


            self.conn = pg2.connect("password='pEfr8mER' user='postgres' dbname='ttse_stocks'")
            self.cur = self.conn.cursor()
            self.sql = 'select * from angostura_stock_data'
            self.cur.execute(self.sql)
            self.data = self.cur.fetchall()
            self.df_ttse = pd.DataFrame(self.data)

            print(self.df_ttse)
            
        def data_analysis(self):
        
            print(self.df_ttse.describe())
            
            
co_stat = ttse_data_analysis('Angostura')
co_stat.data_frame()
co_stat.data_analysis()


            

        
            
            