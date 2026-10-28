celcius=float(input("Enter a temperature in celcius: "))
while celcius<-100 or celcius>100:
    print("Invalid temperature. Please enter a temperature between -100 to 100.")
    celcius=float(input("Enter a temperature in celcius: "))

fahrenheit=((9/5)*celcius)+32
print(f"{fahrenheit:.2f}")
