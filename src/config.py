import os

current_dir = os.path.dirname(os.path.abspath(__file__))
file_transaction_xlsx = os.path.join(current_dir, "../data", "transactions_excel.xlsx")
file_transaction_csv = os.path.join(current_dir, "../data", "transactions.csv")
file_transaction_json = os.path.join(current_dir, "../data", "transactions.json")
