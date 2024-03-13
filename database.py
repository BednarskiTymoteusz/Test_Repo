import sqlite3
import global_variables
import pandas as pd

db_file_path = "E:/PYTHON PROJECTS/FileSelector/db/Transactions_db.db"

def saveTradesIntoDb(trade_list):
    conn = sqlite3.connect(db_file_path)
    cursor = conn.cursor()

    for trans in trade_list:
        params = (float(trans.ProductPrice),
                    trans.ProductName,
                    float(trans.Amount),
                    trans.TransactionDate,
                    trans.Group,
                    trans.ProductColor,
                    trans.ProducMaterial,
                    trans.CountryProducer)

        cursor.execute("INSERT INTO transactions VALUES(?,?,?,?,?,?,?,?)", params)
        conn.commit()

    conn.close()

def saveInputDfIntoDb(df_input):

    df_temp = df_input[global_variables.inputHeaderList]
    mapping = {'Price': 'product_price', 'Product': 'product_name', 'Amount': 'amount', 'Date': 'trans_date', 'Group': 'group', 'Color': 'product_color', 'Material': 'product_material', 'Country': 'country_producer'}
    df_temp.rename(columns=mapping, inplace=True)
    conn = sqlite3.connect(db_file_path)
    df_temp.to_sql('transactions', conn, if_exists='append', index=False)