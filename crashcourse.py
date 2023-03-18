

def lowestPoint():
    return "hoi"

antwoord = lowestPoint()

antwoord == "hoi" #True

list = ["appel","peer",3,4,6,7]
dictionary = {"appel": 30, "peer": 40, 0: 50}
tuple = ("appel", "peer")

type(list) == "List"
item1, item2 = tuple

list.append("kiwi")

list[0] == "appel" #True
list[1] == "peer" 
list[2] == 3 
#key, value pair

dictionary["appel"] += 1

items_op_voorraad = ["appel", "peer", "kiwi"]

if "appel" in items_op_voorraad:
    items_op_voorraad.remove("appel")

if "appel" in dictionary.keys():
    dictionary["appel"] = 0

dictionary["appel"] == 30 
dictionary["peer"] == 40

dictionary[0] == 50

for item in list:
    print(item)

dictionary.keys() == ["appel", "peer", 0]

dictionary.items() == [("appel", 30), (), ()]


for key, value in dictionary.items():
    print(key, value)

#def max(df):
#     max_value = 0 
#     for item in list:
#         if item > max_value:
#             max_value = item
#     return max_value


["appel", "peer", "banaan"] - ["appel", "banaan"]  == ["peer"]
"ik ben hassen je weet zelf".replace("e", "i")
