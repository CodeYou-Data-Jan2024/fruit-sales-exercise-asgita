import pandas as pd

data = {"Apples":[35,41], "Bananas":[21,34], "Index":["2017 Sales","2018 Sales"]}
df = pd.DataFrame(data, columns=["Apples","Bananas"], index=data["Index"])
print(df)

df.to_csv("fruit.csv", sep=',')
#df = pd.read_csv('fruit.csv')
#print(df.to_string()) 
