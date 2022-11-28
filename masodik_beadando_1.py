import pandas as pd

# adatok beolvasása
dataFrame = pd.read_csv("orders.tsv", sep="\t", header=0)

# item_price oszlop átalaklítása
dataFrame['item_price'] = dataFrame["item_price"].replace("[\$]", '', regex=True).astype(float)

# sum oszlop
dataFrame["Sum"] = dataFrame["item_price"]*dataFrame["quantity"]

# átlagos érték
df = dataFrame.groupby('order_id')['Sum'].sum()
mean = df.sum()/df.count()
print("Átlagos rendelés értéke: " + str(mean))

# ételek szerinti csoportosítás és rendezés
df1 = dataFrame.groupby("item_name")["quantity"].sum().sort_values(ascending=True)
print(df1)

# dobozos üdítők
canned_drinks = dataFrame[dataFrame["item_name"].isin(["Canned Soda" , "Canned Soft Drink"])]
print(canned_drinks)

# egyes üdítők
canned_drinks_by_choice = canned_drinks.groupby('choice_description')["quantity"].sum()
print(canned_drinks_by_choice)