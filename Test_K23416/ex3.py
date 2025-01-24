import csv
import pandas as pd
with open("data/employee.csv","r",newline='',encoding="UTF-8") as f:
    reader = csv.reader(f, delimiter=",", quoting=csv.QUOTE_NONE)
    for row in reader:
        print(f"{row[0]} - {row[1]} >> {row[2]} >> {row[3]}")

#%% Read csv file using pandas
df = pd.read_csv("data/employee.csv")
print(df["Name"])
#HADOOP => SPARK
