from sql.helper.sql_format import sql_format
from sql.helper.sql_properties import sql_properties

from sql.structered.query import get_query
from sql.structered.size import get_size
from sql.structered.return_fields import get_return_fields
from sql.structered.sort import get_sort

import boto3


def boto3_query(query, returnFields='_all_fields', size=20, sort='id asc', cursor='initial', queryParser='structured', partial=False, endpoint_url_=''):
    client = boto3.client('cloudsearchdomain', endpoint_url=endpoint_url_)
    resultResponse = client.search(
        query=query,
        returnFields=returnFields,
        size=size,
        sort=sort,

        cursor=cursor,
        queryParser=queryParser,
        partial=partial,
    )
    return resultResponse['hits']
    # arg = dict(x for x in enumerate(arg) if x)


def get_sql_properties(sql_query):
    sql_query_format = sql_format(sql_query)
    sql_query_properties = sql_properties(sql_query_format)
    # print(sql_query_properties)
    return sql_query_properties


def query(sql_query, endpoint_url=''):
    sql_query_format = sql_format(sql_query)
    # print(sql_query_format)

    sql_query_properties = sql_properties(sql_query_format)
    # print(sql_query_properties)

    # size
    structured_size = get_size(int(sql_query_properties[0]))
    # print(size)

    # query
    structured_query = get_query(sql_query_properties[3])
    # print(structured_query)

    # returnFields
    structured_return_fields = get_return_fields(sql_query_properties[1])
    # print(structured_return_fields)

    # sort
    structured_sort = get_sort(sql_query_properties[4])
    # print(structured_sort)

    return boto3_query(query=structured_query, returnFields=structured_return_fields, size=structured_size, sort=structured_sort, endpoint_url_=endpoint_url)
