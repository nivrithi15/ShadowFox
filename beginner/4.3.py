Australia = ["Sydney","Melbourne","Brisbane","Perth"]
UAE = ["Dubai","Abu Dhabi","Sharjah","Ajman"]
India = ["Mumbai","Bangalore","Chennai","Delhi"]
name1=input("Enter name of a city:")
name2=input("Enter name of a city:")
if name1 in Australia and name2 in Australia:
    print("Both cities are in Australia")
elif name1 in UAE and name2 in UAE:
    print("Both cities are in UAE")
elif name1 in India and name2 in India:
    print("Both cities are in India")
else:
    print("They don't belong to the same country")