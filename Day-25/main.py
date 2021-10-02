import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

gray_color = data[data['Primary Fur Color'] == 'Gray']

red_color = data[data['Primary Fur Color'] == 'Cinnamon']

black_color = data[data['Primary Fur Color'] == 'Black']

data_dict = {
    "color": ["Gray", "Cinnamon", "Black"],
    "color_count": [len(gray_color), len(red_color), len(black_color)]

}
data = pandas.DataFrame(data_dict)
data.to_csv('Squirrel Count')



