def is_str(o):
    return isinstance(o, str)


def term_pref(key_val_pair):  # returns 'term' for =, returns 'prefix' for 'LIKE'
    srt2 = key_val_pair.split('=')
    if len(srt2) == 2:
        return 'term'
    return 'prefix'


def key_val(key_val_pair):
    equal = True
    key_val = key_val_pair.split('=')
    if len(key_val) != 2:
        key_val = key_val_pair.split('LIKE')
        if len(key_val) == 2:
            key_val[1] = key_val[1].replace('%', '')
            if key_val[0][-4:] == 'NOT ':
                key_val[0] = key_val[0][:-4]
                equal = False
        else:
            key_val = key_val_pair.split('<>')
            if len(key_val) == 2:
                equal = False
    return [key_val[0].strip(), key_val[1].strip(), equal]


def q_eq_exp(and_exp_pair):
    str2 = key_val(and_exp_pair)
    term_pref_key = term_pref(and_exp_pair)
    return [term_pref_key + " field='" + str2[0] + "' " + str2[1], str2[2]]


def get_exp(sql_exp):
    if len(sql_exp) == 0:
        return ''
    q_eq = q_eq_exp(sql_exp)
    q = q_eq[0]
    q_exp = '(' + q + ')'
    if not q_eq[1]:
        q_exp = '(not ' + q_exp + ')'
    return q_exp


def get_exp_from_object(o):
    new_q_str = '(' + o['keyword'].lower() + ' '
    for i in o['array']:
        if is_str(i):
            if '(' not in i:
                e = get_exp(i)
                new_q_str += e + ' '
            else:
                new_q_str += i + ' '
        else:
            nested_a = get_exp_from_object(i)
            new_q_str += nested_a + ' '
        # new_q_str = new_q_str.strip()

    new_q_str = new_q_str.strip() + ')'
    return new_q_str


def get_query(sql_query_properties):
    return get_exp_from_object(sql_query_properties)
