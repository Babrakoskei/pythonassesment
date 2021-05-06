studentCities = {"Pete": "Los Angeles","Bieber": "Toronto","Colson":"Cleaveland"}
print(studentCities)
print(studentCities["Pete"])
studentCities["Derek"]= "Scotland"
print(studentCities)
studentCities["Bieber"] = "Newyork"
print(studentCities)
studentCities.pop("Colson")
print(studentCities)
print("Pete" in studentCities)
print("Colson" in studentCities)
keys = studentCities.keys()
print(keys)
values = studentCities.values()
print(values)
dancerNumbers = {"Audrey": 50,"Sharlie": 51,"Manny": 52}
print(dancerNumbers["Manny"])
print(dancerNumbers["Audrey"])
dancerNumbers["Sharlie"]= 55
print(dancerNumbers)
dancerNumbers["Hailey"] = 60
print(dancerNumbers)
dancerNumbers.pop("Manny")
print(dancerNumbers)
keys= dancerNumbers.keys()
print(keys)
values= dancerNumbers.values()
print(values)

babra = { "name": "Babra","age":20,"class": "AnitaB"}
sandra= {"name":"Sandra","age":19,"class":"Lovelace"}
janelle= {"name":"Janelle","age": 21,"class": "Lisalab"}
grace= {"name":"grace","age":23,"class":"AnitaB"}



students= [babra,sandra,janelle,grace]
print(students)

for student in students:
    print(student["age"])
    print(student["name"])
    print(student["class"])
    statement = "these Are Akirachix students"
    print(statement)

    name = "Babra"
    age = 21
    profession = "coder"
    city= "Los Angelos"
    sentence ="{} is a {} year old girl {} living in {}".format(name,age,profession,city)
    print(sentence)

firstName = "Maryln"
lastName = "Monroe"
yearOfBirth= 1990
currentYear = 2021
country = "France"
age = currentYear - yearOfBirth
profession = "Actress"

print(f"On this day we celebrate {profession}, {firstName} {lastName} who died at the age of {age} in her home country {country}")

a = {1,2,3,4,5}
print(a)
print(type (a))
s1 ={"a","b","c"}
s2 = {2,5,6,9,3}

a.add("b")
print(a)
s1.update("d","e","j")
print(s1)

print("b" in s2)
print("x" in s1)
print(4 in a)

a.remove(3)
print(a)
s2.discard(10)
print(s2)

m = s1.difference(s2)
print(m)
k = a.difference(s2)
print(k)
o = s2.union(a)
print(o)
s1.union(a)
a.update("a","f")
print(a)
j =s1.union(s2)
print(j)
p = a.union(s2)
print(p)

l = a.union(s2)
print(l)

g = {"23,21,34"}

q = g.intersection(a)
print(q)

countryPresidents = {"Canada": "Justin Trudeau","America": "Joe Biden","Uganda": "Yoweri Museveni"}
print(countryPresidents)
countryPresidents["kenya"] = "Uhuru Kenyatta"
print(countryPresidents)
countryPresidents["America"] = "Kamala Haris"
print(countryPresidents)
countryPresidents.pop("Uganda")
print(countryPresidents)
print(" Justin" in countryPresidents)
print("Justin Trudeau" in countryPresidents)
print("Canada" in countryPresidents)
print("Kamala Haris" in countryPresidents)
print("Uganda" in countryPresidents)
keys = countryPresidents.keys()
print(keys)
values = countryPresidents.values()
print(values)
















