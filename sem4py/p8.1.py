# Import the Util module
import Util

if __name__ == "__main__":
    # Convert Celsius to Fahrenheit
    celsius_temp = 25
    fahrenheit_temp = Util.celsius_to_fahrenheit(celsius_temp)
    print(f"{celsius_temp} degrees Celsius is equal to {fahrenheit_temp:.2f} degrees Fahrenheit")

    # Convert Fahrenheit to Celsius
    fahrenheit_temp = 77
    celsius_temp = Util.fahrenheit_to_celsius(fahrenheit_temp)
    print(f"{fahrenheit_temp} degrees Fahrenheit is equal to {celsius_temp:.2f} degrees Celsius")
