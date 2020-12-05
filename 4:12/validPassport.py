import re
with open('input', 'r') as file:
    user_input = file.readlines()


def pass_test(key, val):
    if key == 'byr':
        try:
            return len(val) == 4 and 1920 <= int(val) <= 2002
        except TypeError:
            return False
    if key == 'iyr':
        try:
            return len(val) == 4 and 2010 <= int(val) <= 2020
        except TypeError:
            return False
    if key == 'eyr':
        try:
            return len(val) == 4 and 2020 <= int(val) <= 2030
        except TypeError:
            return False
    if key == 'hgt':
        try:
            number = int(val[:-2])
        except ValueError:
            return False
        unit = val[-2:]
        if unit == 'cm':
            return 150 <= number <= 193
        elif unit == 'in':
            return 59 <= number <= 76
        else:
            return False
    if key == 'hcl':
        return val[0] == '#' and len(val) == 7 and len(re.findall('[a-f0-9]', val[1:])) == 6
    if key == 'ecl':
        return ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'].count(val) == 1
    if key == 'pid':
        if len(val) == 9:
            try:
                number = int(val)
                return True
            except ValueError:
                return False
        return False


def build_dic(obj_string, dict_keys, pass_test_bool=False):
    '''obj_string == "key:value key:value key:value..."'''
    dict_build = {}
    for key_val_str in obj_string.split():
        key_val_list = key_val_str.split(':')
        key = key_val_list[0]
        val = key_val_list[1]
        if key in dict_keys:
            if pass_test_bool:
                if pass_test(key, val):
                    dict_build[key] = val
            else:
                dict_build[key] = val
    return dict_build


def find_passports(pass_test_bool, indata):
    dict_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    obj = ''
    dict_list = []
    for data in indata:
        match_test = re.match("[a-zA-Z0-9#:]", data) != None
        end_test = data == indata[-1]
        if match_test and not end_test:
            obj += re.sub("[^a-zA-Z0-9#:]", ' ', data)
        elif match_test and end_test:
            obj += re.sub("[^a-zA-Z0-9#:]", ' ', data)
            passport = build_dic(obj, dict_keys, pass_test_bool)
            dict_list.append(passport)
        else:
            passport = build_dic(obj, dict_keys, pass_test_bool)
            dict_list.append(passport)
            obj = ''
    correct_passports = 0
    for passport in dict_list:
        if len(dict_keys) == len(list(passport.keys())):
            correct_passports += 1
    return correct_passports


part1 = find_passports(pass_test_bool=False, indata=user_input)
part2 = find_passports(pass_test_bool=True, indata=user_input)

print('Solution part one:', part1, 'Solution part two:', part2)
