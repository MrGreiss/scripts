import glob, os
files = glob.glob("airbank_*.csv")
files.sort()
os.system("BankingExport2YNAB.py " + files[-1])