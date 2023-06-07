import csv
import random
from datetime import datetime, timedelta

def generate_csv_file(num_rows):
    columns = [
        "id_date", "dn", "date_debut", "type_even", "nombre_even", "even_minutes", "direction_appel",
        "termination_type", "type_reseau", "type_destination", "operator", "country",
        "profile_id", "city", "gamme", "marche", "segment", "billing_type", "contract_id", "date_fin"
    ]
    start_date = datetime(2022, 1, 1)
    end_date = datetime(2023, 3, 1)

    rows = []
    for _ in range(num_rows):
        row = []
        # id_date
        id_date = start_date + timedelta(seconds=random.randint(0, int((end_date - start_date).total_seconds())))
        row.append(id_date.strftime("%Y%m%d"))
        # dn
        dn = generate_dn()
        row.append(dn)
        # date_debut
        row.append(id_date.strftime("%d/%m/%Y %H:%M"))
        # type_even
        type_even = random.choice(["voice", "sms"])
        row.append(type_even)
        # nombre_even
        row.append(random.randint(1, 10))
        # even_minutes
        if type_even == "sms":
            row.append(None)
            date_fin = id_date + timedelta(minutes=random.randint(1, 60))
        else:
            even_minutes = random.randint(1, 60)
            row.append(even_minutes)
            date_fin = id_date + timedelta(minutes=even_minutes)
        # direction_appel
        row.append(random.choice(["IN", "OUT"]))
        # termination_type
        row.append(random.choice(["on-net", "off-net"]))
        # type_reseau
        type_reseau = random.choice(["mobile", "fix"])
        row.append(type_reseau)
        # type_destination
        type_destination = random.choices(["national", "international"], [0.8, 0.2])[0]
        row.append(type_destination)
        # operator
        if type_destination == "national":
            row.append(random.choices(["INWI", "IAM", "ORANGE"], [0.6, 0.2, 0.2])[0])
            row.append("Morocco")
        elif type_destination == "international":
            row.append("International")
            row.append(random.choice(["France", "Spain", "USA"]))
        # profile_id
        row.append(str(random.randint(1000, 9999)))
        # city
        if type_destination == "national":
            row.append(random.choice(["Casablanca", "Rabat", "Marrakech", "Fes", "Tangier"]))
        else:
            row.append("international city")
        # gamme
        gamme = ""
        if type_reseau == "fix":
            gamme = random.choice(["ADSL", "Fibre optique"])
        elif type_reseau == "mobile":
            if type_destination == "national":
                gamme = random.choice(["MRE", "Data Prepaid", "Data Postpaid", "Forfaits 99 dhs", "Forfaits 49 dhs", "Forfaits 149 dhs", "Forfaits 199 dhs", "Forfaits 249 dhs"])
            else:
                gamme = "Autres"
        row.append(gamme)

        # marche
        marche = ""
        if gamme == "Data Prepaid" :
            marche = "Mobile Prepaid"
        elif gamme == "Data Postpaid":
            marche = "Mobile Postpaid"
        elif gamme == "ADSL" or gamme == "Fibre optique":
            marche = "Home"
        elif gamme == "Forfaits 49 dhs" or gamme == "Forfaits 149 dhs"or gamme == "Forfaits 199 dhs"or gamme == "Forfaits 99 dhs"or gamme == "Forfaits 249 dhs":
            marche = "Mobile Postpaid"
        else:
            marche = "Autres"
        row.append(marche)

        # segment
        if marche == "Mobile Prepaid":
            row.append(random.choices(["B2C", "Autres"], [0.9, 0.1])[0])
        elif marche == "Mobile Postpaid":
            row.append(random.choices(["B2B", "Autres"], [0.9, 0.1])[0])
        else:
            row.append(random.choice(["B2B", "B2C", "Autres"]))

        # billing_type
        if marche == "Mobile Prepaid":
            row.append("prepaid")
        elif marche == "Mobile Postpaid":
            row.append("postpaid")
        else:
            row.append("Autres")

        # contract_id
        row.append("ABC" + str(random.randint(100000, 999999)))
        # date_fin
        row.append(date_fin.strftime("%d/%m/%Y %H:%M"))

        rows.append(row)

    with open("data.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(columns)
        writer.writerows(rows)




def generate_dn():
    prefix = "2125" if random.random() < 0.5 else "2126"
    suffix = str(random.randint(10000000, 99999999))
    return prefix + suffix


# Exemple d'utilisation
generate_csv_file(1000)  # Génère un fichier CSV avec 1000 lignes
