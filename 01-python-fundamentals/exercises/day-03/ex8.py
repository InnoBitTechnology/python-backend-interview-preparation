details = { 'name': 'Manoj',
           'age': 27,
           'city': 'Agra',
           'role': 'Backend Engineering',
           'experience': 4}
print(details['name'])
details['age'] = 25
print(details['age'])
details["salary"] = 100000
print("="*20)
for key in details:
    print(key)
for value in details.values():
    print(value)
for key,value in details.items():
    print(key, value)
