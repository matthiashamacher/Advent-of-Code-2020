import functions


def get_bag_color(rule):
    rule_parts = get_rule_parts(rule)

    return rule_parts[0]


def get_rule_parts(rule):
    return functions.get_data_from_string(rule, ' bags contain ')


def get_content(content_description):
    contents = []
    content = {}

    if 'no other bags' in content_description:
        return None

    if ', ' in content_description:
        contents = functions.get_data_from_string(content_description, ', ')

    if len(contents) > 1:
        for content_string in contents:
            content_parts = functions.get_data_from_string(content_string, ' ')
            color = ' '.join([content_parts[1], content_parts[2]])

            content[color] = int(content_parts[0])
    else:
        content_parts = functions.get_data_from_string(content_description, ' ')
        color = ' '.join([content_parts[1], content_parts[2]])

        content[color] = int(content_parts[0])

    return content


def get_bags(bag_color, bag_rules):
    bags = 0
    current_bag_rule = bag_rules[bag_color]

    if current_bag_rule is None:
        return 1

    for content_bag in current_bag_rule:
        count = current_bag_rule[content_bag]

        if bag_rules[content_bag] is None:
            bags += count
            continue

        bags += count
        bags += (get_bags(content_bag, bag_rules) * count)

    return bags
