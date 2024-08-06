# Copyright (c) Meta Platforms, Inc. and affiliates.
# This software may be used and distributed according to the terms of the Llama 2 Community License Agreement.

import sqlite3
import csv

# Define the input CSV file and the SQLite database file
input_csv = r'C:\Users\Kritika\Downloads\NPCI Python LLM\npci.csv'
database_file = r'C:\Users\Kritika\Downloads\NPCI Python LLM\npci.db'



# Connect to the SQLite database
conn = sqlite3.connect(database_file)
cursor = conn.cursor()

# Create a table to store the data
cursor.execute('''CREATE TABLE IF NOT EXISTS npci_table (
"Bank Category"                                                                TEXT,
"Bank Name"                                                                    TEXT,
"ATM & CRM Onsite"                                                              INT,
"ATM & CRM Offsite"                                                             INT,
"PoS"                                                                           INT,
"Micro ATM"                                                                     INT,
"Bharat QR Codes"                                                               INT,
"UPI QR Codes"                                                                  INT,
"Credit Cards"                                                                 INT,
"Debit Cards"                                                                   INT,
"CreditCard Card Payments Transactions PoS  Volume (in actuals)"               INT,
"Credit Card Card Payments Transactions PoS  Value (in Rs 000)"                 INT,
"Credit Card Card Payments Transactions Online(e-com)  Volume (in actuals)"     INT,
"Credit Card Card Payments Transactions Online(e-com)  Value (in Rs 000)"       INT,
"Credit Card Card Payments Transactions Others  Volume (in actuals)"            INT,
"Credit Card Card Payments Transactions Others  Value (in Rs 000)"              INT,
"Credit Card Cash Withdrawal At ATM Volume (in actuals)"                        INT,
"Credit Card Cash Withdrawal At ATM Value (in Rs 000)"                          INT,
"Debit Card Card Payments Transactions PoS  Volume (in actuals)"                INT,
"Debit Card Card Payments Transactions PoS  Value (in Rs 000)"                  INT,
"Debit Card Card Payments Transactions Online(e-com)  Volume (in actuals)"      INT,
"Debit Card Card Payments Transactions Online(e-com)  Value (in Rs 000)"        INT,
"Debit Card Card Payments Transactions Others  Volume (in actuals)"             INT,
"Debit Card Card Payments Transactions Others  Value (in Rs 000)"               INT,
"Debit Card Cash Withdrawal ATM Volume (in actuals)"                            INT,
"Debit Card Cash Withdrawal ATM Value (in Rs 000)"                              INT,
"Debit Card Cash Withdrawal PoS Volume (in actuals)"                            INT,
"Debit Card Cash Withdrawal PoS Value (in Rs 000)"                              INT            
                )''')

# Read data from the CSV file and insert it into the SQLite table
with open(input_csv, 'r', newline='') as npci:
    csv_reader = csv.reader(npci)
    next(csv_reader)  # Skip the header row
    
    for row in csv_reader:
        cursor.execute('INSERT INTO npci_table VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', row)
        #for row in rows:
        #if len(row) != 28:
           # print(f"Incorrect number of elements in row: {row}")
        #else:
           # cursor.execute('INSERT INTO npci_table VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', row)



# Commit the changes and close the database connection
conn.commit()
conn.close()

print(f'Data from {input_csv} has been successfully imported into {database_file}')

