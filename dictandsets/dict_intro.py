vehicles = {
    "dream": "Honda 250T",
    "roadster": "BMW R110",
    "er5": "Kawasaki ER5"
}

vehicles["starfighter"] = "lockhedd f-104"
vehicles["learjet"] = "bombardier learjet 75"
vehicles["toy"] = "glider"

#Upgrade the virago

vehicles['dream'] = "yamaha xv35"

for key, value in vehicles.items():
    print(key, value)

del vehicles["er5"]
result = vehicles.pop("f1", None)
print(result)
plane = vehicles.pop("dream")
print(plane)
print()

for key, value in vehicles.items():
    print(key)
    