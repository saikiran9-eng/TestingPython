
names = ("Navin", "saikiran", "Tendulkar", "saikiran")
company = ("Microsoft", "Infosys", "cognizant", "Wipro")
location = ("Chennai", "Banglore", "Delhi", "Hyderabad")

zipped = zip(names, company, location)

for (a,b,c) in zipped:
    print(a,b,c)