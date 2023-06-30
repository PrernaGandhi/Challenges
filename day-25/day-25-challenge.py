# with open("weather_data.csv") as file:
#     data = file.readlines()
#     print(data)

# import csv
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         # print(row)
#         if row[1] == 'temp':
#             continue
#         temperatures.append(int(row[1]))
#     print(temperatures)


import pandas

data = pandas.read_csv("weather_data.csv")
# print(data)
temperatures = data["temp"]
# print(temperatures)

# avg temperatures
temperatures_list = temperatures.to_list()
avg = round(sum(temperatures_list) / len(temperatures_list), 2)
# print(avg)
# print(temperatures.mean())

# get max temp
# print(temperatures.max())


# get data in row where day is monday
# print(data[data["day"] == "Monday"])
# print(data[data.day == "Monday"])

# find row of data with the max temperature
max_temp = data["temp"].max()
# print(data[data["temp"] == max_temp])
# or
max_temp = data.temp.max()
# print(data[data.temp == max_temp])


# convert monday's temp to Fahrenheit
monday = data[data.day == "Monday"]
# FutureWarning: Calling int on a single element Series is deprecated and will raise a TypeError in the future.
# Use int(ser.iloc[0]) instead monday_temp = int(monday.temp)
# monday_temp = int(monday.temp)
monday_temp = monday.iloc[0, 1]
# or
# monday_temp = monday.temp
monday_temp_F = monday_temp * (9 / 5) + 32
# print(monday_temp_F)


# create dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Lily"],
    "scores": [80, 40, 90]
}

data_frame = pandas.DataFrame(data_dict)
new_data_csv = data.to_csv("new_data_csv.csv")
