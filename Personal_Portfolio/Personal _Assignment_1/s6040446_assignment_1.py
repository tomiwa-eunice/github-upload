# 1 Dictionary containing the data from Eurostat on the share (%)
#   of renewable energy consumption among the European countries.


# 2
# different approach that creates a dictionary with the named variable "renewableE"
renewableE = {"Albania": (37, "nonEU"), "Austria": (34, "EU"), "Belgium": (9, "EU"), "Bulgaria": (19, "EU"),
              "Croatia": (28, "EU"), "Cyprus": (9, "EU"), "Czech Republic": (15, "EU"), "Denmark": (32, "EU"),
              "Estonia": (29, "EU"), "Finland": (39, "EU"), "France": (16, "EU"), "FYROM": (18, "nonEU"),
              "Germany": (15, "EU"), "Greece": (15, "EU"), "Hungary": (14, "EU"), "Iceland": (73, "nonEU"),
              "Ireland": (10, "EU"), "Italy": (17, "EU"), "Latvia": (37, "EU"), "Lithuania": (26, "EU"),
              "Luxembourg": (5, "EU"), "Malta": (6, "EU"), "Montenegro": (42, "nonEU"), "Netherlands": (6, "EU"),
              "Norway": (69, "nonEU"), "Poland": (11, "EU"), "Portugal": (29, "EU"), "Romania": (25, "EU"),
              "Serbia": (21, "nonEU"), "Slovakia": (12, "EU"), "Slovenia": (21, "EU"), "Spain": (17, "EU"),
              "Sweden": (54, "EU"), "United Kingdom": (9, "EU")}

for country in renewableE:      # iterates over the dictionary

    # itemize the content of the dictionary using "->" as a separator.
    print(country, "(", renewableE[country][1], ")", "->", renewableE[country][0],)


# 3.
# categorizing the content of the dictionary according to the share value
i = str(input("Write the name of a country from the dictionary: "))

if renewableE[i][0] <= 20:      # checks if country has a share value of less than or 20%

    print(i, "has small share of renewable energy")

elif renewableE[i][0] > 60:     # checks if country has a share value of greater than 60%

    print(i, "has large share of renewable energy")

else:
    # prints the category of the share of renewable energy, which the specified country belongs to
    print(i, "has medium share of renewable energy")


# 4
non_eu_countries = 0
for value in renewableE.values():   # iterates over each value in the dictionary
    if 'nonEU' in value:
        non_eu_countries += 1

# prints the total number of non-European countries in the dictionary
print(non_eu_countries)


# 5
for key in renewableE.keys():   # iterates over each key in the dictionary
    if "nonEU" in renewableE[key]:
        print(key)      # itemize the non-European countries in the dictionary


# 6
count = 0
for i in renewableE:
    if renewableE[i][0] == 100:      # checks if any country in the dictionary has a share value of 100%
        count += 1
if count == 0:
        print("No country from the dictionary has a 100% share of renewable energy")
else:
    print(count, "country from the dictionary has a share of 100 renewable energy")


# 7
x = min(renewableE.values())[0]     # checks country with the minimum share value

# print the value
print("Value of the country with the minimum share of renewable energy is", x)


# 8
x = max(renewableE.values())[0]      # checks country with the maximum share value

# print the value
print("Value of the country with the maximum share of renewable energy is", x)


# 9
# calculates the mean share for all countries in the dictionary
the_sum = 0
for i in renewableE:        # iterates over items in the dictionary
    if renewableE[i][0]:
        the_sum += renewableE[i][0]

# prints the mean value of the total share and rounds up to the nearest integer
print("Mean share value", "=", round(the_sum / len(renewableE.keys())))


# 10
# calculates the mean share of EU and non-EU countries respectively
sum_non_eu, sum_eu = 0, 0
count_non_eu, count_eu = 0, 0
for i in renewableE.values():        # iterates over values in the dictionary
    if i[1] == 'nonEU':              # checks if country is non-EU
        count_non_eu += 1
        sum_non_eu += i[0]
    else:
        count_eu += 1
        sum_eu += i[0]

mean_non_eu = round(sum_non_eu / count_non_eu)
mean_eu = round(sum_eu / count_eu)

print("Mean share of EU and non-EU countries are {} and {} respectively.".format(mean_eu, mean_non_eu))
print("Warning !!!: The mean is affected by extreme values either too high or too low")







