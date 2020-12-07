import functions
import day7.day_functions


def main(data):
    return function(data.data)


def test(data):
    return function(data.data)


def function(input):
    my_bag = 'shiny gold'
    rules = functions.get_data_from_string(input)
    valid_bags = []

    for rule in rules:
        bag_color = day7.day_functions.get_bag_color(rule)

        if my_bag == bag_color:
            continue

        if my_bag in rule:
            valid_bags.append(bag_color)

    for valid_bag in valid_bags:
        for rule in rules:
            bag_color = day7.day_functions.get_bag_color(rule)

            if valid_bag in rule:
                if bag_color not in valid_bags:
                    valid_bags.append(bag_color)

    return len(valid_bags)
