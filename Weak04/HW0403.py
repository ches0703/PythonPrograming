dict_nation_capital = {}

while True:
    get_data = input("Input nation and its capital (. to quit) : ")
    if get_data == '.':
        break
    nation, capital = get_data.split(" ")
    dict_nation_capital[nation] = capital

print("dict_nation_capital : ", dict_nation_capital)

while True:
    get_data = input("Input nation to find its capital (. to quit) : ")
    if get_data == '.':
        break
    if get_data in dict_nation_capital:
        print("The capital of {} is {}".format(
            get_data, dict_nation_capital[get_data]))
    else:
        print("No Data...")
