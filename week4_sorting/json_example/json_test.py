import requests
import json

url = "https://covid-api.mmediagroup.fr/v1/history?country=Germany&status=confirmed"

req1 = requests.get(url)

print(req1.text)


dict1 = json.loads(req1.text)

print(dict1)

key1 = "All"
key2 = "dates"

dates = []
confirmed_cases = []
for date in dict1[key1][key2]:
    # if date <= "2022-08-31":
    print(date, dict1[key1][key2][date])
    dates.append(date)
    confirmed_cases.append(dict1[key1][key2][date])
    
# loop through confirmed cases, subtract each day's confirmed cases value
# from the previous day's confirmed cases value



germany_dict = {}
germany_dict["country"] = "germany"
germany_dict["avg_new_daily"] = 0 # the average new_cases
germany_dict["date_highest"] = "2020-06-15"

print(germany_dict)
json.dump(germany_dict, open("data.json", "w"))


