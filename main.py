import pandas as pd

# pd.set_option('display.max_columns', 500)
# pd.set_option('display.width', 1000)

df = pd.read_csv('tehetsegpont.csv')
df["addSpace"] = df["name"] = " " + df["name"]
df["replaceDr"] = df["addSpace"].str.replace(' Dr.', 'Dr.')
df["removeSpaceDr"] = df["replaceDr"].str.replace(' dr.', 'dr.')
df[['title', 'firstName', 'lastName']] = df["removeSpaceDr"].str.split(' ', n=2, expand=True)


df.to_csv("kesz.csv", index=False)
print(df.head(10))
