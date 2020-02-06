def is_str(o):
    return isinstance(o, str)


def trim_array(a):
    ta = []
    for p in a:
        ta.append(p.strip())
    return ta


def clean_array(a):
    ta = []
    for p in a:
        if p != '':
            ta.append(p.strip())
    return ta


def has_brackets(a):
    for i in a:
        if '(' in i:
            return True
    return False


def find_first_index(s, c='('):
    return s.index(c)


def find_last_index(s, c=')'):
    return s.rindex(c)


def find_indexes(s, c1='(', c2=')'):
    return [find_first_index(s, c1), find_last_index(s, c2)]


def find_pair_index(s, i=0, c=')'):
    ts = s[i+1:]
    result = i
    c = 1
    for i in ts:
        result += 1
        if i == '(':
            c += 1
        elif i == ')':
            c -= 1
        if c == 0:
            break
    return result


def split_and_or(s):
    join_keyword = 'or'
    all_split = []
    all_split = s.split(' OR ')
    if len(all_split) == 1:
        join_keyword = 'and'
        all_split = s.split(' AND ')
    return {'keyword': join_keyword, 'array': all_split}


def get_part(s, start_index=0, end_index=0):
    return s[start_index+1:end_index]


def get_part_array(s):
    result = []
    if '(' not in s:
        return s
    else:
        i = find_first_index(s)
        j = find_pair_index(s, i)
        part = get_part(s, i, j)
        result.append(s[0:i])
        result.append(part)
        if len(s) != j+1:
            other_res = get_part_array(s[j+1:])
            if is_str(other_res):
                result += [other_res]
            else:
                result += other_res
    return result


def get_keyword_part_array(s):
    keyword = 'AND'
    clean_part_array = []
    part_array = get_part_array(s)

    if is_str(part_array):
        return split_and_or(part_array.strip())

    # trim all elements
    part_array = trim_array(part_array)

    # find keyword for part array. array contains "OR", "OR ...", "... OR"
    if 'OR' in part_array:
        keyword = 'OR'
    else:
        for p in part_array:
            if p[0:3] == 'OR ' or p[-3:] == ' OR':
                keyword = 'OR'

    # remove keywords
    for p in part_array:
        l = len(keyword)
        cp = p
        if cp[0:l+1] == keyword + ' ':
            cp = cp[l+1:]
        if cp[-l-1:] == ' ' + keyword:
            cp = cp[:-l-1]
        if cp == keyword:
            pass
        else:
            clean_part_array.append(cp)

    clean_part_array = trim_array(clean_part_array)
    clean_part_array = clean_array(clean_part_array)
    return {'keyword': keyword, 'array': clean_part_array}


def split_without(data, indexes):
    result = []
    first_part = data[:indexes[0]].strip()
    middle_part = data[indexes[0]:indexes[1]+1].strip()
    last_part = data[indexes[1]+1:].strip()

    first_part_split = split_and_or(first_part)
    last_part_split = split_and_or(last_part)
    if len(first_part_split) > 0 and first_part_split[0] != '':
        result += first_part_split
    if len(middle_part) > 0:
        result += [middle_part]
    if len(last_part_split) > 0 and last_part_split[0] != '':
        result += last_part_split
    return result


def recursive_for_str_1(s):
    res = split_and_or(s)
    if len(res['array']) == 1:
        return res['array'][0]
    else:
        return res


def recursive_for_str_2(s):
    return get_keyword_part_array(s)


def recursive_for_obj(o):
    new_o = {'keyword': o['keyword'], 'array': []}
    for i in o['array']:
        new_o['array'].append(recursive_for_item(i))
    return new_o


def recursive_for_item(i):
    new_i = ''
    if is_str(i):
        if '(' in i:
            new_i = recursive_for_str_2(i)
        else:
            new_i = recursive_for_str_1(i)
    else:
        new_i = recursive_for_obj(i)
    return new_i


def recursive_for_all(o):
    new_o = {'keyword': o['keyword'], 'array': []}
    for i in o['array']:
        new_o['array'].append(recursive_for_item(i))
    return new_o


def is_require_recursive_for_all(o):
    res_flag = False
    for i in o['array']:
        if is_str(i):
            if ' AND ' in i or ' OR ' in i:
                res_flag = True
                break
        else:
            res_flag = is_require_recursive_for_all(i)
    return res_flag


def sql_exp_object(expressions_fields):
    exp_object = get_keyword_part_array(expressions_fields)
    while is_require_recursive_for_all(exp_object):
        exp_object = recursive_for_all(exp_object)
    return exp_object
