from urllib.parse import urlencode, unquote 
import sys
import urllib
import requests
import json

if len(sys.argv) != 4:
    print("argument가 부족합니다.")
    sys.exit()

months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', 10, 11, 12]
rows = sys.argv[1]
start = sys.argv[2]
end = sys.argv[3]
title = start + " ~ " + end

url = "	http://apis.data.go.kr/1400000/forestStusService/getfirestatsservice"

queryString="?"+urlencode(
   {  
       "serviceKey":unquote("zWBN4GdBq7P56bK6Dpi9Zjby6H1XpFDJPMez436%2BCoe8KzV0Wzf0W9Ox7LfLQ%2FRB9m6oFiLxffw8WseX3UPctw%3D%3D"),
       "_type":"json",
       "numOfRows":rows,
       "pageNo":"1", 
       "searchStDt":start+"0101",
       "searchEdDt":end+"1231"
     }
)

queryURL = url + queryString 
response = requests.get(queryURL)
#print(queryURL)
#print(response)  # 200


data = urllib.request.urlopen(queryURL).read()
output_j = json.loads(data)
cases = {}

testArr = output_j["response"]["body"]["items"]["item"]

for m in months:
    fireCause = {}
    for s in testArr:
        if s["startmonth"] == m:
            if s["firecause"] in fireCause:
                fireCause[s["firecause"]] += 1
            else:
                fireCause[s["firecause"]] = 1
    cases[m] = fireCause

cases["totalCnt"] = output_j["response"]["body"]["totalCount"]

result = open(title + ".txt", mode="w", encoding="UTF-8")
result.write(str(cases))

result.close()