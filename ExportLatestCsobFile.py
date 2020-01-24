import glob, os
files = glob.glob("pohyby*.csv")
files.sort()
os.system("BankingExport2YNAB.py \"" + files[-1] + "\"")