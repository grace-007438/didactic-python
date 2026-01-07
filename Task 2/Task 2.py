print("Temperature: Celsius to Fahrenheit")
print("Distance: Kilometers to Miles")
print("Weight: Kilograms to Pounds")
option=int(input("Enter your option (1,2,3): "))

if option==1:
    celsius=float(input("Enter temperature in Celsius:"))
    fahrenheit=(celsius*9/5)+32
    print("Temperature in Fahrenheit:",fahrenheit)

elif option==2:
    kilometers=float(input("Enter distance in Kilometers:"))
    miles=kilometers*0.621371
    print("Distance in Miles:",miles)

elif option==3:
    kilograms=float(input("Enter weight in Kilograms:"))
    pounds=kilograms*2.20462
    print("Weight in Pounds:", pounds)

else:
    print("Invalid option! select 1,2,3.")
