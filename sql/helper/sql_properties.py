# import sys
from .sql_exp_object import sql_exp_object


def get_top(splits):
    if splits[1] == 'TOP':
        return splits[2]
    return 0


def get_return_fields(splits):
    start_index = 1
    FROM_index = splits.index('FROM')
    if splits[1] == 'TOP':
        start_index = 3
    fields = ''
    fields = fields.join(splits[start_index:FROM_index])
    # print(fields)
    return fields


def get_table_name(splits):
    FROM_index = splits.index('FROM')
    return splits[FROM_index + 1]


def get_expressions_fields(splits):
    result = ' '
    if 'WHERE' in splits:
        FROM_index = splits.index('WHERE')
        if 'ORDER_BY' in splits:
            ORDER_BY_index = splits.index('ORDER_BY')
            # print(ORDER_BY_index)
            return result.join(splits[FROM_index+1:ORDER_BY_index])
        return result.join(splits[FROM_index+1:])
    return ''


def get_order_fields(splits):
    if 'ORDER_BY' in splits:
        ORDER_BY_index = splits.index('ORDER_BY')
        # print(ORDER_BY_index)
        result = ' '
        if splits[len(splits)-1] != 'ASC' and splits[len(splits)-1] != 'DESC':
            splits.append('ASC')
        return result.join(splits[ORDER_BY_index+1:])
    return ''


# array [size, return fileds, table_name, expressions, sort]
def sql_properties(sql_query):
    sql_query = sql_query.replace('  ', ' ').replace('  ', ' ')
    result = [0, '*', 'TABLE_NAME', '', '']
    sql_query = sql_query.replace(' ORDER BY ', ' ORDER_BY ')
    splits = sql_query.split(' ')
    for i in splits:
        i = i.strip()

    # print('')
    # print(splits)
    expressions_fields = get_expressions_fields(splits)

    result[0] = get_top(splits)
    result[1] = get_return_fields(splits)
    result[2] = get_table_name(splits)
    result[3] = sql_exp_object(expressions_fields)
    result[4] = get_order_fields(splits)
    # print(result)
    return result

# sys.modules[__name__] = sql_properties
