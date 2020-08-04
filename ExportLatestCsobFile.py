import glob, os
files = glob.glob("pohyby*.csv")
files.sort()
os.system("/Users/i332916/Developer/scripts/BankingExport2YNAB.py \"" + files[-1] + "\"")