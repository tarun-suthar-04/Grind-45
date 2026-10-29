import json
# json_str='{"id": null,"name": "Aarav Sharma","is_age_18+": true}'
# print(type(json_str))
# print(json_str)

# data=json.loads(json_str)

# print(type(data)) 
# print(data) 

# json_str1=json.dumps(data)
# print(type(json_str1))
# print(json_str1)

# with open("sample.json","r",encoding="utf-8") as f:
#     py_obj=json.load(f)

#     print(type(py_obj))
#     print(py_obj)

    
# d={'id': 1, 'name': 'Aarav Sharma', 'age': 24, 'address': {'house_no': '12A', 'street': 'Vijay Nagar', 'city': 'Indore', 'state': 'Madhya Pradesh', 'pincode': '452010'}, 'hobbies': ['cricket', 'coding', 'reading'], 'contact': {'email': 'aarav@example.com', 'phone': '+91-9000000001'}, 'education': {'degree': 'B.Tech', 'graduated': True}}
# with open("dumpdata.json","w",encoding="utf-8") as f:
#     json.dump(d,f,indent=3,sort_keys=False)

# with open("dumpdata.json","r",encoding="utf-8") as f:
#     print(f.read())

# cities=[{'name':"indore" , "population":1000000 },{'name':"Jhalawar" , "population":1000000 },{'name':"Bhopal" , "population":1000000 }]

try:
    with open("cities.json","r") as f:
        cities=json.load(f)

    for city in cities:
        print(f"city : {city['name']}\n populaiton : {city['population']}")

    new_city=input("enter city name : ").strip()
    new_population=int(input("Enter population : "))

    cities.append({"name":new_city,"population":new_population})

    with open("cities.json", "w") as f :
        json.dump(cities,f,indent=3)


except FileNotFoundError:
    print("Error: cities.json was not found.")

except json.JSONDecodeError:
    print("Error: cities.json contains invalid JSON.")

except ValueError:
    print("Error: Population must be a valid integer.")

