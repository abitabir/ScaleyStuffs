def wildcard_pattern(string, wildcard):
    def _possible_combinations(string, wildcard, possible_combos):
        if set(string) == {'1', '0'} or set(string) == {'1'} or set(string) == {'0'} or set(string.strip()) == set(): #base case
            possible_combos.add(string)
        else:
            string1 = string.replace(wildcard, '1', 1)
            _possible_combinations(string1, wildcard, possible_combos)
            string2 = string.replace(wildcard, '0', 1)
            _possible_combinations(string2, wildcard, possible_combos)
        return possible_combos
    output = set()
    _possible_combinations(string, wildcard, output)
    return output


def fill_bag(values, weights, max_weight):
    if max_weight == 0:
        return 0
    else:
        output = {}
        _possible_valid_combos(values, weights, max_weight, output, 0, 0)
        return output

def _possible_valid_combos(remaining_values, remaining_weights, max_weight, possible_combos, current_value, current_weight):
    _add_item(remaining_values, remaining_weights, max_weight, possible_combos, current_value, current_weight)
    _skip_item(remaining_values, remaining_weights, max_weight, possible_combos, current_value, current_weight)


def _add_item(remaining_values, remaining_weights, max_weight, possible_combos, previous_value, previous_weight):
    current_value = previous_value + remaining_values.pop(0)
    current_weight = previous_value + remaining_weights.pop(0)
    if remaining_values == [] or current_weight > max_weight:
        possible_combos[previous_value] = previous_weight
        return possible_combos
    else:
        _possible_valid_combos(remaining_values, remaining_weights, max_weight, possible_combos, current_value, current_weight)
        print(remaining_values, remaining_weights, possible_combos, previous_value, previous_weight, current_value, current_weight)
        return remaining_values, remaining_weights, possible_combos, previous_value, previous_weight, current_value, current_weight

def _skip_item(remaining_values, remaining_weights, max_weight, possible_combos, current_value, current_weight):
    _add_item(remaining_values[1:], remaining_weights[1:], max_weight, possible_combos, current_value, current_weight)

print(fill_bag([20, 5, 5, 10, 40, 15, 25], [1, 2, 2, 3, 8, 7, 4], 10))

btree = [8, [3, [1,[],[]],[6,[4,[],[]],[7,[],[]]]],[10,[],[14,[13,[],[]],[]]]]


def pre_order(treeset, output):
    if treeset != []:
        output += str(treeset[0]) + " ";
        output = pre_order(treeset[2], output);
        output = pre_order(treeset[1], output);
    return output;
print(pre_order(btree, ""));

def in_order(treeset, output):
    if treeset != []:
        output = in_order(treeset[2], output); #descending - if you want ascending swap 2 and 1 (your left/lesser first)
        output += str(treeset[0]) + " ";
        output = in_order(treeset[1], output);
    return output;
print(in_order(btree, ""));

def post_order(treeset, output):
    if treeset != []:
        output = post_order(treeset[1], output);
        output = post_order(treeset[2], output);
        output += str(treeset[0]) + " ";
    return output;
print(post_order(btree, ""));

