import pandas as pd

loc = "C:/Users/UserName/Downloads/1270_2296_bundle_archive/"
Neg = open(loc+"processedNegative.csv", "r").read()
Neut = open(loc+"processedNegative.csv", "r").read()
Pos = open(loc+"processedPositive.csv", "r").read()

# print(type(Neg))
NegArr = Neg.split(",")
# for i in range(10):
#     print(NegArr[i])
NeutArr = Neut.split(",")
PosArr = Pos.split(",")

arr = NegArr+NeutArr+PosArr
df1 = pd.DataFrame(NegArr,columns = ['Text'])
df1 = df1.assign(Sent="-1")

df2 = pd.DataFrame(NeutArr,columns = ['Text'])
df2 = df2.assign(Sent="0")

df3 = pd.DataFrame(PosArr,columns = ['Text'])
df3 = df3.assign(Sent="1")

df = pd.concat([df1, df2, df3])
