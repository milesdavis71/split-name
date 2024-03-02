import pandas as pd

pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
# df = pd.DataFrame({'name': {0: ' Braund', 1: ' Heikkinen', 2: ' Allen', 3: ' Moran', 4: ' McCarthy'}, 'Fullname': {0: ' Mr. Owen Harris ', 1: ' Miss. Laina ', 2: ' Mr. William Henry ', 3: ' Mr. James ', 4: ' Mr. Timothy J '}})
data = pd.read_csv('tehetsegpont.csv')
data.dropna(inplace=True)

new = data["name"].str.split(" ", n = -1, expand = True)
# making seperate title column from new data frame
data["Title"]= new[0]
# making seperate first name column from new data frame
data["First Name"]= new[1]
# making seperate last name column from new data frame
data["Last Name"]= new[2]
print(data)