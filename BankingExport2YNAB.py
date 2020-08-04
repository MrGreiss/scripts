import csv
import sys


def try_to_match_Payee(memo):
    known_payees = \
        {"BENZINA*": "Beznina",
         "NETFLIX.COM": "Netflix",
         "VODAFONE CZECH REP": "Vodafon",
         "Alza.cz a.s": "Alza.cz",
         "VOYO": "Voyo.sk",
         }
    payee_found = None
    for payee in known_payees:
        if payee in memo:
            payee_found = known_payees[payee]
            if payee_found is not None:
                return payee_found

    if payee_found is None:
        raise KeyError("Missing match Payee")


def trimIntro(filename, encoding):
    with open(filename, 'r', encoding=encoding) as file:
        lines = file.readlines()
        for index, line in enumerate(lines):
            if line.startswith("číslo účtu"):
                break
    with open(filename, 'w', encoding=encoding) as file:
        file.writelines(lines[index:])


if sys.argv[1].startswith("airbank"):
    columnMapping = (("Datum provedení", "Date"), ("Částka v měně účtu", "Inflow"), ("Částka v měně účtu", "Outflow"),
                     ("Název protistrany", "Payee"), ("Poznámka k úhradě", "Memo"))
    inputFileEncoding = "cp1250"
    outputFileName = "ynab_airbank.csv"
elif "pohyby" in sys.argv[1]:
    columnMapping = (
    ("datum zaúčtování", "Date"), ("částka", "Outflow"), ("částka", "Inflow"), ("název účtu protiúčtu", "Payee"),
    ("poznámka", "Memo"))
    inputFileEncoding = "cp1250"
    outputFileName = "ynab_csob.csv"
    trimIntro(sys.argv[1], inputFileEncoding)
else:
    print(
        "Unknown bank export file. Should start with: \"airbank\" (for AirBank export file) or \"pohyby\" (for CSOB export file).")
    exit()

with open(sys.argv[1], 'r', encoding=inputFileEncoding) as infile, open(outputFileName, 'w',
                                                                        encoding='utf-8') as outfile:
    reader = csv.DictReader(infile, delimiter=';', )
    writer = csv.DictWriter(outfile, fieldnames=("Date", "Payee", "Memo", "Outflow", "Inflow"), lineterminator='\n',
                            quoting=csv.QUOTE_ALL)
    writer.writeheader()
    for row in reader:
        outrow = {}
        for inkey, outkey in columnMapping:
            if outkey is "Payee":
                outrow.update({outkey: try_to_match_Payee(row["poznámka"])})
            else:
                outrow.update({outkey: row[inkey]})
        writer.writerow(outrow)
