import pandas as pd

def getcredit(marks):
    if marks >= 90:
        convert = 10
    elif 75<= marks <= 89:
        convert = 9
    elif 65 <= marks <= 74:
        convert = 8
    elif 55<= marks <=64:
        convert = 7
    elif 50<=marks<=54:
        convert = 6
    elif 45<=marks<=49:
        convert = 5
    elif 40<=marks <=44:
        convert = 4
    else:
        convert = 0
    return convert
    

df = pd.read_excel("CSE CGPA.xlsx")

totalcredit = 0
cg = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

print(df.columns)
for i,r in df.iterrows():
    totalcredit += r['CREDIT']
    for j in range(1,9):
        print(r[j])
        convert = getcredit(r[j])
        cg[j-1] += convert*r['CREDIT']

for i in range(0,8):
    print(round(cg[i]/totalcredit,3))