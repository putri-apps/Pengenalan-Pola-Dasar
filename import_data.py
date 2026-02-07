# Membaca data dari file dengan format CSV
import pandas as pd
data = pd.read_csv("Data.csv", sep=";")
print(data)
# Membaca data dari file dengan format text (delimeter)
print("\n read text data with tab delimiter")
with open ('Data.txt') as data:
    print(data.read())
# Membaca data dari URL
import pandas as pd
f = pd.read_csv('http://www.exploredata.net/ftp/Spellman.csv')
print(f)