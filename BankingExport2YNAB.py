import csv
import sys

print(sys.argv[0])
print(sys.argv[1])
if sys.argv[1].startswith("airbank"):
    columnMapping = (("Datum provedení", "Date"), ("Částka v měně účtu", "Inflow"),("Částka v měně účtu","Outflow"),("Název protistrany","Payee"), ("Poznámka k úhradě","Memo"))
elif sys.argv[1].startswith("pohyby"):
    columnMapping = (("datum zaúčtování","částka","částka","název účtu protiúčtu","poznámka"),("Date","Payee","Memo","Outflow","Inflow"))
else:
    print("Unknown bank export file. Should start with: \"airbank\" (for AirBank export file) or \"pohyby\" (for CSOB export file).")
    exit()

with open(sys.argv[1], 'r') as infile, open('ynab.csv', 'w') as outfile:
    # output dict needs a list for new column ordering
    reader = csv.DictReader(infile, delimiter=';',)
    print(reader.fieldnames)
    writer = csv.DictWriter(outfile, fieldnames=("Date","Payee","Memo","Outflow","Inflow"), lineterminator='\n', quoting=csv.QUOTE_ALL)
    writer.writeheader()
    for row in reader:
        outrow = {}
        for inkey, outkey in columnMapping:
            outrow.update({outkey: row[inkey]})
        print(outrow)
        writer.writerow(outrow)
