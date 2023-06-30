# count the number of gray, cinnamon, black squirrel and put it in a file
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# gray = data[data["Primary Fur Color"] == "Gray"]["Primary Fur Color"].count()
gray_count = len(data[data["Primary Fur Color"] == "Gray"])
# black = data[data["Primary Fur Color"] == "Black"]["Primary Fur Color"].count()
black_count = len(data[data["Primary Fur Color"] == "Black"])
# cinnamon = data[data["Primary Fur Color"] == "Cinnamon"]["Primary Fur Color"].count()
cinnamon_count = len(data[data["Primary Fur Color"] == "Cinnamon"])

new_data_dict = {
    "Fur Color": ["gray", "black", "red"],
    "count": [gray_count, black_count, cinnamon_count]
}
print(new_data_dict)
new_data = pandas.DataFrame(new_data_dict)
print(new_data)
new_data_csv = new_data.to_csv("new_data_csv.csv")
