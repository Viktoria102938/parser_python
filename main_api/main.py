import requests

url = "https://restcountries.com/v3.1/all"
response = requests.get(url)
data = response.json()

print("******* This is a python program to fetch data from rest country api ******* ")
print(" ")
print("List of countries:")
for country in data:
    print(country["name"]["common"])

chosen_country = input("Enter the name of the country you want to know about: ").title()
found = False

for country in data:
    if country["name"]["common"] == chosen_country:
        found = True
        print("""\n**** Congratulations, your country is present in our database ****
            o> Press 0 to exit
            o> Press 1 to view capital of this nation
            o> Press 2 to view region of this nation
            o> Press 3 to view subregion of this nation
            o> Press 4 to view total population of this nation
            o> Press 5 to view total area of this nation in km square
            o> Press 6 to view timezone of this nation
            o> Press 7 to view share border of this nation
            o> Press 8 to view currency of this nation
            o> Press 9 to view languages spoken in this nation
                                                                """)

        choice = -1
        attempts = 0
        while choice not in range(13) and attempts < 3:
            choice = int(input("\nEnter your choice: "))
            attempts += 1
            if choice not in range(13) and attempts < 3:
                print("Invalid input. Please try again.")

        if choice == 0:
            exit()
        elif choice == 1:
            print("Capital of {} is: {}".format(chosen_country, country["capital"][0]))
        elif choice == 2:
            print("Region of {} is: {}".format(chosen_country, country["region"]))
        elif choice == 3:
            print("Subregion of {} is: {}".format(chosen_country, country["subregion"]))
        elif choice == 4:
            print("Population of {} is: {}".format(chosen_country, country["population"]))
        elif choice == 5:
            print("The total area of {} is: {}".format(chosen_country,country["area"]))
        elif choice == 6:
            print("The Timezone of the country is: {}".format(chosen_country, country["timezones"]))
        elif choice == 7:
            print("Sharing borders {} is: {}".format(chosen_country,country["borders"]))
        elif choice == 8:
            print("Currency of {} is:{}".format(chosen_country, country["currencies"]))
        elif choice == 9:
            print("Language spoken in {} is:{}".format(chosen_country,country["languages"]))






