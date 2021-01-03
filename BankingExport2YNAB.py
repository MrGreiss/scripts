import csv
import sys


def try_to_match_Payee(memo):
    known_payees = \
        {"BENZINA*": "Beznina",
         "NETFLIX.COM": "Netflix",
         "CSOB": "CSOB",
         "VODAFONE CZECH REP": "Vodafon",
         "Alza.cz a.s": "Alza.cz",
         "VOYO": "Voyo.sk",
         "Revolut": "Revolut",
         "MPLA.CZ": "MPLA (Parkovani)",
         "OMV": "OMV",
         "NESPRESSO": "Nespresso",
         "GENTLEMAN STORE": "Gentleman Store",
         "NOTINO": "Notino",
         "sazka.cz": "Sazka",
         "MCDONALD": "McDonalds",
         "GROSSETO": "Grosseto",
         "BISTRO SLECHTOVKA": "Bistro Slechtovka",
         "Parkovaci kasy": "Parkovani",
         "BENZINA": "Benzina",
         "SHZ CESKY KRUMLOV": "Hrad Cesky Krumlov",
         "APPLE": "Apple",
         "KFC": "KFC",
         "GELATO PRAGA": "Gelato Praga",
         "PH": "Pizza Hut",
         "Candy Bull": "Candy Bull",
         "Tesco": "Tesco",
         "YouTubePremium": "Youtube",
         "TEDOS Mikulov": "Parkovani",
         "Aquapark Moravia": "Aqualand Moravia",
         "AQUALAND": "Aqualand Moravia",
         "ALBERT": "Albert",
         "GENTLEMEN BROTHERS": "Gentleman Brothers",
         "NOVY SMICHOV": "OC Novy Smichov",
         "MC DONALDS": "McDonalds",
         "PARKING MEDVEDI": "Parkovani",
         "FABERA SYSTEMS": "Fabera Systems",
         "AQUA PARK SPINDLERUV": "Aquapark Spindleruv mlyn",
         "Lanova draha Svaty Pet": "Lanovka Spindleruv Mlyn",
         "TWISTO": "Twisto",
         "McDonald": "McDonalds",
         "Kytky od Pepy": "Kytky od Pepy",
         "RBCZ": "Raiffeisenbank",
         "Transakcni poplatek": "CSOB",
         "HOTEL SKALNI MLYN": "Hotel Skalni Mlyn",
         "KAVARNA V MYSLIVNE": "Kavarna v Myslivne",
         "Billa": "Billa",
         "YOUTUBEPREMIUM": "Youtube Premium",
         "CENTRUM STROMOVKA": "Centrum Stromovka",
         "PVA": "PVA expo",
         "Damejidlo": "Damejidlo",
         "Amazon Video": "Amazon",
         "SPRAVA JESKYNI": "Sprava Jenskyni CR",
         "HOTEL INTERNATIO": " Hotel International",
         "BEER TRUCK": "Beer Truck",
         "MESTSKA PLOVARNA": "Mestska Plovarna Luhacovice",
         "RESTAURACE - PIZZERIE, LUHACOVICE": "Rimini",
         "BUFET POD VYHLIDKOU": "Bufet pod Vyhlidkou",
         "MIRONET": "Mironet",
         "Booking.com": "Booking.com",
         "damejidlo": "Damejidlo",
         "SUNNYSOFT": "Sunny soft",
         "RESTAURACE SOKOLI": "Restaurace Sokoli",
         "EZUP": "Ezup",
         "RELAY": "Relay",
         "EMOTION PARK": "E-motion",
         "DM DROGERIE": "Dm Drogerie",
         "adidas": "Adidas",
         "MAKRO": "Makro",
         "FOOT LOCKER": "Foot Locker",
         "KYTKY EVROPSKA": "Kytky od Pepi",
         "DATART": "Datart",
         "IKEA": "Ikea",
         "MOL": "Mol",
         "Pizza Bustehrad": "Pizza Bustehrad",
         "PRAGUE ON STREET PARKING": "MPLA (Parkovani)",
         "Alza, Praha": "Alza.cz",
         "GETBIZODNE.COM, DECIN": "GETBIZODNE.COM",
         "EPIC GAMES STORE": "Epic Game store",
         "BOZI DAR 199": "Parkoviste Bozi Dar",
         "CUP AND CAKE": "Cup&Cake",
         "RESTAURANT JESTED": "Restaurace Jested",
         "CZC": "CZC.cz",




















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
            if outkey is "Payee" and len(row['poznámka']) > 0 and len(row['číslo účtu protiúčtu']) == 0:
                outrow.update({outkey: try_to_match_Payee(row["poznámka"])})
            else:
                if outkey is "Memo" and len(row['poznámka']) > 0:
                    memo = row[inkey]
                    if "Místo" in memo:
                        memo = memo.split("Místo:", 2)[1]
                        outrow.update({outkey: memo})
                    else:
                        outrow.update({outkey: row[inkey]})
                else:
                    outrow.update({outkey: row[inkey]})
        writer.writerow(outrow)
