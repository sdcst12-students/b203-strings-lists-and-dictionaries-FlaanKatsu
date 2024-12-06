inv = {
    "0" : 5,
    "1" : 3,
    "2" : 2
}

items = {
    "English" : ['food','water','money'],
    "French" : ['mange','eau','cashola']
}

locale = "English"

word = "food"
indx = items[locale].index(word)
print (indx)
print(inv[str(indx)])
"""
inv = {
    "1" : 0,
    "2" : 0,
    "3" : 0
}


if locale == en:
    items = {
        1 : "orange"
        2 : "shoes"
    }
elif locale == jp:
    items = {
        1 : みかん
        ２：
    }

    """