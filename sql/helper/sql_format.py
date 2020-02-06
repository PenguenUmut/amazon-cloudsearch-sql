# import sys


def replace_for_select(sql_query):  # uppercase select, Select to SELECT
    return sql_query.replace('select ', 'SELECT ').replace('Select ', 'SELECT ')


def replace_for_top(sql_query):  # uppercase top, Top to TOP
    return sql_query.replace('SELECT top ', 'SELECT TOP ').replace('SELECT Top ', 'SELECT TOP ')


def replace_for_from(sql_query):  # uppercase from, From to FROM
    return sql_query.replace(' from ', ' FROM ').replace(' From ', ' FROM ')


def replace_for_where(sql_query):  # uppercase where, Where to WHERE
    return sql_query.replace(' where ', ' WHERE ').replace(' Where ', ' WHERE ')


def replace_for_and(sql_query):  # uppercase and, And to AND
    return sql_query.replace(' and ', ' AND ').replace(' And ', ' AND ')


def replace_for_or(sql_query):  # uppercase or, Or to OR
    return sql_query.replace(' or ', ' OR ').replace(' Or ', ' OR ')


def replace_for_like(sql_query):  # uppercase like to LIKE
    return sql_query.replace(' like', ' LIKE').replace(' Like', ' LIKE')


def replace_for_not(sql_query):  # uppercase not, Not to NOT
    return sql_query.replace(' not ', ' NOT ').replace(' Not ', ' NOT ')


def replace_for_not_equal(sql_query):  # replace != to <>
    return sql_query.replace('!=', '<>')


def replace_for_percent(sql_query):  # remove %
    return sql_query.replace('%', '')


def replace_for_order(sql_query):  # uppercase order, Order to ORDER
    return sql_query.replace(' order ', ' ORDER ').replace(' Order ', ' ORDER ')


def replace_for_by(sql_query):  # uppercase by, By to BY
    return sql_query.replace(' by ', ' BY ').replace(' By ', ' BY ')


def replace_for_asc(sql_query):  # uppercase asc, Asc to ASC
    last_4 = sql_query[-4:].upper()
    if last_4 == ' ASC':
        return sql_query[:-4] + ' ASC'
    return sql_query


def replace_for_desc(sql_query):  # uppercase desc, Desc to DESC
    last_5 = sql_query[-5:].upper()
    if last_5 == ' DESC':
        return sql_query[:-5] + ' DESC'
    return sql_query


def replace_for_order_by(sql_query):  # join and uppercase ORDER BY to ORDER_BY
    asc_desc_order_by = replace_for_asc(replace_for_desc(
        replace_for_by(replace_for_order(sql_query))))
    return asc_desc_order_by.replace('ORDER BY', 'ORDER_BY')


def sql_format(sql_query):
    return replace_for_order_by(replace_for_percent(replace_for_not_equal(replace_for_not(replace_for_like(replace_for_or(replace_for_and(replace_for_where(replace_for_from(replace_for_top(replace_for_select(sql_query)))))))))))

# sys.modules[__name__] = sql_format
