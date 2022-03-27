import csv
import sys


def try_to_match_Payee(memo):
    known_payees = \
        {"BENZINA*": "Beznina",
         "NETFLIX.COM": "Netflix",
         "CSOB": "CSOB",
         "Vodafone Czech": "Vodafon",
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
         "CANDYBULL": "Candy Bull",
         "Tesco": "Tesco",
         "YouTubePremium": "Youtube",
         "TEDOS Mikulov": "Parkovani",
         "Aquapark Moravia": "Aqualand Moravia",
         "AQUALAND": "Aqualand Moravia",
         "ALBERT": "Albert",
         "GENTLEMAN BROTHERS": "Gentleman Brothers",
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
         "Cup And Cake": "Cup&Cake",
         "RESTAURANT JESTED": "Restaurace Jested",
         "czc.cz": "CZC.cz",
         "www.speedlo.cz": "Speedlo.cz",
         "DECATHLON PRAHA": "Decathlon",
         "FORBES.CZ": "Forbes",
         "Operator ICT": "Ropid",
         "EDALNICE": "E-Dalnice",
         "CD LIBEREC": "Jested lanovka",
         "NFPOMOCI.CZ": "Nfpomoci.cz",
         "Zabka": "Zabka",
         "CESKA POSTA": "Ceska Posta",
         "ready2wash" : "AS Superwash",
         "MYCKA KLADNO": "Mycka Kladno",
         "www.madmonq.gg": "Madmonq",
         "STATUTAR": "Czech Point",
         "PARKING CENTRUM, PRAHA 2": "Parking Hlavni Nadrazi",
         "ROBIN OIL": "Robin Oil",
         "LIDL DEKUJE ZA NAKUP": "Lidl",
         "Benzina": "Beznina",
         "ZKONTROLUJSIAU": "Cebia",
         "KVETINY NOVAK": "Kvetniny Novak",
         "Eshop ZOO Zlin": "Zoo Zlin",
         "SHELL": "Shell",
         "STARBUCKS": "Starbucks",
         "Gaijin Games": "Gaijin games",
         "Gentleman Store": "Gentleman Store",
         "ROSSMANN": "Rossmann",
         "PARKOVISTE 1, MODRAVA": "Parkoviste modrava",
         "CS EUROOIL": "Eurooil",
         "HBO": "HBO",
         "AUTO SERVIS DEJVICE": "Volvo servis",
         "CUKRARNA PEKNY KASTANY": "Creme de la Creme",
         "Nintendo": "Nintendo",
         "www.bazos.cz": "Bazos",
         "JetBrains, Prague": "JetBrains",
         "SUPER ZOO": "Super Zoo",
         "surteesstudios": "SurteesStudios",
         "MO BOOST": "Mmo Boost",
         "PLYN s.r.o": "EuroDily.cz",
         "MALL.CZ": "Mall.cz",
         "M RESTAURANT": "McDonalds",
         "GIBON UPOMINKOVE": "Gitft Shop Liberec Zoo",
         "DARUJME.CZ": "Darujme.cz",
         "LEKARNA DR.MAX": "Dr.Max",
         "TAIKO": "Taiko",
         "MICROSOFT": "Microsoft",
         "POTRAVINY NA KOVARNE": "Potraviny na Kovarne",
         "LAZENSKA KAVA": "Lazenska kava luhacovice",
         "TRAVELLAB": "TravelLab",
         "U Provaznice": "U Provaznice",
         "GOPAY  *TAMAZPET.COM, tamazpet.com": "Tam a Zpet",
         "NC KVILDA PARKOVISTE": "NC Kvilda Parkoviste",
         "REKOLA": "Rekola",
         "GASTRO - WC MEDVEDIN": "WC Medvedin",
         "IGLOO BAR": "Igloo bar",
         "Lanova draha Hromovka": "Lanova draha Hromovka",
         "SP.M. PARKING": "Parking Hromovka",
         "POKLADNA UVN": "UVN",
         "Qerko": "Qerko",
         "FAME STYLE AGENCY": "Institut zdravych vlasu",
         "PIVOVAR LADVI COBOLIS": "Pivovar cobolis",
         "GOPAY * O2": "O2",
         "Alza, Prague": "Alza.cz",
         "GELATO CAFE": "Gelato cafe",
         "PLZENSKA 233/8": "Plzenska 238/8",
         "FreshCup": "Mamas bakery",
         "LA ZmrZka": "La Zmrzka",
         "gopass": "GoPass",
         "Foot Locker": "Foot Locker",
         "SKYLINK": "Skylink.cz",
         "ANTONINOVO PEKARSTVI": "Antoninovo Pekarstvi",
         "Mc Donald": "McDonalds",
         "CSAD KLADNO": "CSAD Kladno",
         "PARKOVANI FN MOTOL": "Parkovani FN Motol",
         "MOTOL CAFE": "Motol Cafe",
         "www.cd.cz": "Ceske Drahy",
         "Decathlon": "Decathlon",
         "Intersport": "Intersport",
         "BK Praha ": "Burger King",
         "SANI": "Sani",
         "KAFE U ZLABU": "Kafe u Zlabu",
         "TENISOVY KLUB SPORT": "Tenisovy klub luziny",
         "SENYUM CLINIC": "Senyum clinic",
         "KE KOPANINE, TUCHOMERICE": "Go Tank",
         "PLAYSTATIONNETWORK": "Playstation e-shop",
         "BEZKEMPU.CZ": "BezKempu.cz",
         "KB ATM": "KB",
         "T-MOBILE": "T-Mobile",
         "KYTKY U ANDELA": "Kytky od Pepy",
         "360PIZZA": "360 Pizza",
         "www.liftago.com": "Lifttago",
         "LEGENDA RESTAURACE": "Legenda",
         "LEGENDA MUSIC": "Legenda",
         "VERY GOODIES": "Very Goodies",
         "Lidl": "Lidl",
         "PAUL": "Paul",
         "AUTO STODULKY": "Volvo servis",
         "UBER": "Uber",
         "PARKOVACI DUM RYCHTAR, PLZEN": "Parkovaci dum rychtar, Plzen",
         "CROSSWALK BARBER": "Crosswalk barber",
         "CHATA U SLONA": "Chata u Slona",
         "CINEMA CITY": "CinemaCity",
         "GLOBUS": "Globus",
         "Ptakoviny": "Ptakoviny",
         "KNEDLIN": "Knedlin",
         "AOS CZECH": "Apple",
         "WWW.ISPACE.CZ": "Samsung",
         "amazingplaces": "Amazing Places",
         "DISKARD": "STK-Diskard",
         "Cre8shop": "Cre8",
         "Globus": "Globus",
         "Creative cut": "Creative cut",
         "CZC.CZ": "CZC.cz",
         "KARLOK SRO": "Lokal",
         "THE PUB": "The Pub",
         "ASPIRA": "Aspira Cafe",
         "GOODSAILORS": "Ceske parky",
         "SB Avion Park": "Starbucks",
         "Penny": "Penny",
         "OPTIKSTUDIOJANACIZKOV": "Optik Studio Jana Cizkova",
         "CS, CERNOHORSKA": "Ceska Sporitelna",
         "go.ticketportal": "TicketPortal",
         "PARKOVISTE SLUNECNA": "Parkoviste slunecna (Prasily)",
         "PIZZERIA PALATINO": "Pizzeria Palatino",
         "cinemacity.cz": "CinemaCity",
         "PRODEJNA ARKO": "Arko",
         "Fresh Point": "Sklizeno",
         "PARKOVISTE KLD 2": "Skiareal Cerna Hora",
         "MEGA PLUS SPODNI STA, JANSKE LAZNE": "Skiareal Cerna Hora",
         "Cup and Cake": "Cup&Cake",
         "RESTAURACE TRIFOT": "Trifot",
         "Amitabh Enterprises": "Bombay Express",
         "SBX Praha": "Starbucks",
         "NC SRNI PARKOVISTE": "Parkoviste Srni",
         "OH DEER BAKERY": "Oh Deer Bakery",
         "SV KATERINA": "Shell",
         "AMLOK, LOKAL": "Lokal",
         "MARTHYpyro": "MarthyPyro",
         "PARKOVISTE  KAPKA, BOZI DAR": "Parkoviste Bozi Dar",
         "Pivovar Ladvi COBOLIS": "Pivovar cobolis",
         "bezrealitky": "Bezrealitky.cz",
         "Restaurace Stadion": "Restaurace stadion",
         "School Svaty Petr": "SkolMax",
         "Shop/rental LD Svaty": "Pujcovna sv. Petr",
         "Senyum clinic": "Senyum clinic",
         "Ruzyne SAL": "Salomon",
         "nextbike": "Nextbike",
         "RIP CURL": "RipCurl",
         "2P33 PEAK PERFORMANC": "Peak Performance",
         "AQUAPALACE PRAHA": "Aquapalace",
         "RPM SERVICE": "RPM Service"





































































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
