temp = int(input("Enter a temperature in celcius: "))
temp_celcius = 0

def fahrenheit_to_celcius(temp):
     temp_celcius = ((temp - 32) * (5/9))
     return temp_celcius


temp_celcius = fahrenheit_to_celcius(temp)
print("{} degrees fahrenheit is equal to {:.2f} degrees celcius".format(temp,temp_celcius))
