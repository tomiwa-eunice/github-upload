# 1 Provide background info here"

# 2
# country_list = ["Albania", ]
# energy_region_list = []
renewableE = zip(country_list, energy_region_list)
renewableE["Albania"]=(37,"nonEU")
renewableE["Austria"]=(34,"EU")
renewableE["Belgium"]=(9,"EU")
renewableE["Bulgaria"]=(19,"EU")
renewableE["Croatia"]=(28,"EU")
renewableE["Cyprus"]=(9,"EU")
renewableE["Czech Republic"]=(15,"EU")
renewableE["Denmark"]=(32,"EU")
renewableE["Estonia"]=(29,"EU")
renewableE["Finland"]=(39,"EU")
renewableE["France"]=(16,"EU")
renewableE["FYROM"]=(18,"nonEU")
renewableE["Germany"]=(15,"EU")
renewableE["Greece"]=(15,"EU")
renewableE["Hungary"]=(14,"EU")
renewableE["Iceland"]=(73,"nonEU")
renewableE["Ireland"]=(10,"EU")
renewableE["Italy"]=(17,"EU")
renewableE["Latvia"]=(37,"EU")
renewableE["Lithuania"]=(26,"EU")
renewableE["Luxembourg"]=(5,"EU")
renewableE["Malta"]=(6,"EU")
renewableE["Montenegro"]=(42,"nonEU")
renewableE["Netherlands"]=(6,"EU")
renewableE["Norway"]=(69,"nonEU")
renewableE["Poland"]=(11,"EU")
renewableE["Portugal"]=(29,"EU")
renewableE["Romania"]=(25,"EU")
renewableE["Serbia"]=(21,"nonEU")
renewableE["Slovakia"]=(12,"EU")
renewableE["Slovenia"]=(21,"EU")
renewableE["Spain"]=(17,"EU")
renewableE["Sweden"]=(54,"EU")
renewableE["United Kingdom"]=(9,"EU")

for country in renewableE:
    print(country,"(",renewableE[country][1],")","->",renewableE[country][0],)

# 3.
i = str(input("Write the name of a country from the dictionary :"))
if renewableE[i][0] <= 20:
    print(i, "has small share of renewable energy")
elif renewableE[i][0] > 60:
    print(i, "has large share of renewable energy")
else:
    print(i, "has medium share of renewable energy")

# 4
non_eu_countries = 0
for value in renewableE.values():
    if 'nonEU' in value:
        non_eu_countries += 1
print(non_eu_countries)

# 5
for key in renewableE.keys():
    if "nonEU" in renewableE[key]:
        print(key)

# 6
count = 0
for i in renewableE:
    if renewableE[i][0] == 100:
        count += 1
if count == 0:
        print("write something here")
else:
    print("write something else here")

# 7
x = min(renewableE.values())[0]
print(x)

# 8
x = max(renewableE.values())[0]
print(x)

# 9
the_sum = 0
for i in renewableE:
    if renewableE[i][0]:
        the_sum += renewableE [i][0]
print ((the_sum/ len(renewableE.keys())))

