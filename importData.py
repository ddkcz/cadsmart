
def import_data():
    import pandas as pd


    df = pd.read_csv("clients.csv")


    df = df.apply(lambda x: x.str.strip() if x.dtype == "O" else x)
    df['NAZWA'] = df['NAZWA'].str.upper()
    df['E-MAIL'] = df['E-MAIL'].str.lower()
    df['SUPERTYP'] = df['SUPERTYP'].str.lower()
    df['TYP'] = df['TYP'].str.lower()
    df['SUBTYP'] = df['SUBTYP'].str.lower()


    df = df.fillna('')

    df.to_csv('clients_clean.csv', index=False)

    print(df)

