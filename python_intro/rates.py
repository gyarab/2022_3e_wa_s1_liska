import httpx
##from pprint import pprint

url = "https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-ostatnich-men/kurzy-ostatnich-men/kurzy.txt;jsessionid=E298623F3DBF7339EC6C794C7A7D982F"
res = httpx.get(url)
rows = res.text.split("\n")

rows = rows[2:-1]


data = {}
data.update({"CZK" : 1})

for r in rows:
    cols = r.split("|")
    data.update({cols[3] : float(cols[4].replace(",", ".")) / float(cols[2])})

print("Zadejte značku převáděné měny ...")
mena1 = input()
print("")

print("Zadejte množství převáděné měny ...")
mnozstvi = float(input())
print("")

print("Zadejte značku měny na níž si přejete převést ...")
mena2 = input()
print("---------------")

print("= ", end= "")
print(round(mnozstvi * data[mena2] / data[mena1], 2), end="")
print(" " + mena2)



'''
ja jsem viceradkovy koment
^^
'''
