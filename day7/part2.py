import functions
import day7.day_functions


def main(data):
    return function(data.data)


def test(data):
    return function(data.data)


def test_second_data(data):
    return function(data.second_data)


def function(input):
    bags = 0
    my_bag = 'shiny gold'
    rules = functions.get_data_from_string(input)
    bag_rules = {}

    for rule in rules:
        [bag_color, content_description] = day7.day_functions.get_rule_parts(rule)
        content = day7.day_functions.get_content(content_description)
        bag_rules[bag_color] = content

    bags = day7.day_functions.get_bags(my_bag, bag_rules)

    return bags
