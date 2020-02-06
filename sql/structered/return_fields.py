def get_return_fields(sql_fields):
    if sql_fields.strip() == '*':
        return '_all_fields'
    else:
        return sql_fields
