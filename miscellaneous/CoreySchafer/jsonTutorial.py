# https://www.youtube.com/watch?v=9N6a-VLBa2I JSON tutorial
# practically DAT1

import json  # pretty much every language has libararies for parsing JSON data
from urllib.request import urlopen

# # rn just a multiline python string that happens to be valid JSON ~ looks almost like python dictionary
# # key called states and a value of people is an array of four more objects, each object having further keys
# states_string = """
# {
#   "states": [
#     {
#       "name": "Alabama",
#       "abbreviation": "AL",
#       "area_codes": ["205", "251", "256", "334", "938"]
#     },
#     {
#       "name": "Alaska",
#       "abbreviation": "AK",
#       "area_codes": ["907"]
#     },
#     {
#       "name": "Arizona",
#       "abbreviation": "AZ",
#       "area_codes": ["480", "520", "602", "623", "928"]
#     },
#     {
#       "name": "Arkansas",
#       "abbreviation": "AR",
#       "area_codes": ["479", "501", "870"]
#     }
#   ]
# }
# """
#
# data = json.loads(states_string)  # converting into python object of <class "dict"> as type(object) would inform us
# # so we can work with data more easily (translates by default JSON to Python: object to dict, array to list, string to
# # str, number (int) to int, number (real) to float, true to True, false to False, null to None)
# for datum in data["states"]:
#     print(datum["name"])  # printing all names of states in json string
#
# # now doing the reverse: dumping the python object into json string
# # lets say we want to remove the area_codes from each state cuz postal services having an uphaul and convert this back to json string
#
# for datum in data["states"]:
#     del datum["area_codes"]
# new_states_string = json.dumps(data, indent=2, sort_keys=True)  # sort_keys sorts the keys alphabetically if you so wish to do
# # since long string would be easier on eyes to format it with an indent arguemnt, and it indents every item by that indent arguemnet amaount
# print(new_states_string)
#
# new_states_string = """
# {
#   "states": [
#     {
#       "name": "Alabama",
#       "abbreviation": "AL"
#     },
#     {
#       "name": "Alaska",
#       "abbreviation": "AK"
#     },
#     {
#       "name": "Arizona",
#       "abbreviation": "AZ"
#     },
#     {
#       "name": "Arkansas",
#       "abbreviation": "AR"
#     }
#   ]
# }
# """


# # now if we want to access a json file in the same directory, first open it
# with open("states.json") as f:  # open("states.json", "r") is the same - default read only
#     data = json.load(f)["states"]  # used for loading data from json file into python object
#     # note the confusion list in dico before accessing
#     print(data)
#
# for datum in data:
#     print(datum["abbreviation"], datum["area_codes"])
#     del datum["name"]
#
# with open("new_states.json", "w") as g:
#     json.dump(data, g, indent=2, sort_keys=True)
# # creates new json file with only abbreviation and area_codes


# real world example of using json on data using yahoo finance https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json
with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as response:
    source = response.read()  # not very readbale rn just prints all webpage content out -just a very long string

data = json.loads(source)  # converting long string into python object
print(json.dumps(data, indent=2))  # prinitng in readable format - we see meta data
print(data["list"]["meta"]["count"] == len(data["list"]["resources"]))# checking if the count in the meta data is indeed correct

gbp_rates = dict()  # creating dict so the conversions can be accessed quicker

for item in data["list"]["resources"]:
    name = item["resource"]["fields"]["name"]  # when working with real data you have to dig down a but till you get exactly what you're looking foe, hum
    price = item["resource"]["fields"]["price"]
    gbp_rates[name] = price  # stores name of conversion and the actual price of the conversion

print("USD/EUR")  # prints approx 846500
print(50 * float(gbp_rates["GBP/PKR"]))  # if you wanna convert 50 GBP to Pakistani Rupees ~ first convert from string to float
# if you want to you could take down and convert to data from API's json once a day and save into local json file, and write a function that accesses the data in a more repeatable way
# we see how benefical parsing json is for getting out information and suiting our needs

