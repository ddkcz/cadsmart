print("Hello there!")

import pandas as pd

columns = [
    'NAZWA',
    'E-MAIL',
    'SUPERTYP',
    'TYP',
    'SUBTYP'
]
df = pd.DataFrame(columns=columns)


qty = int(input("Ile utworzyć?: ") )

for lp in range(0,qty):

    name = input("Nazwa kontaktu: ")
    mail = input("adres e-mail: ")
    supertype = input("supertyp: ")
    typ = input("typ: ")    
    subtype = input("subtyp: ")
    
    new_row = {
        'NAZWA': name,
        'E-MAIL' : mail,
        'SUPERTYP': supertype,
        'TYP': typ,
        'SUBTYP' : subtype,
        }
    df = df._append(new_row, ignore_index=True)

print(df)
df.to_csv('clients.csv', index=False)
