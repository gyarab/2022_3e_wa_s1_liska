import httpx
from pprint import pprint

url = "https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-ostatnich-men/kurzy-ostatnich-men/kurzy.txt;jsessionid=E298623F3DBF7339EC6C794C7A7D982F"
res = httpx.get(url)
rows = res.text.split("\n")

rows = rows[1:-1]

'''
data = {
    "Eur": 23.858,
    "USD": 21.872,
    ...
}
'''
data = {}
for r in rows:
    cols = r.split
pprint(rows)

'''
ja jsem viceradkovy koment
^^
'''