import csv
with open("todo_app/weather.csv", "r") as file:
    data = list(csv.reader(file))
    # this is an iterable object, so we can iterate over it
    # a list of lists is returned, where each inner list represents a row in the CSV file
    # we can also use the csv.DictReader to read the CSV file as a dictionary
    
city = input("Enter the city name: ")
for row in data:
    if row[0].lower() == city.lower():
        print(f"Weather in {row[0]}: {row[1]}°C, {row[2]}% humidity, {row[3]} km/h wind speed")
        break