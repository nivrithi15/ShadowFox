Australia = ["Sydney","Melbourne","Brisbane","Perth"]
UAE = ["Dubai","Abu Dhabi","Sharjah","Ajman"]
India = ["Mumbai","Bangalore","Chennai","Delhi"]
name=input("Enter name of a city:")
if name in Australia:
    print(f"{name} is in Australia")
elif name in UAE:
    print(f"{name} is in UAE")
elif name in India:
    print(f"{name} is in India")
else:
    print(f"{name} is not found in any of the lists.")
