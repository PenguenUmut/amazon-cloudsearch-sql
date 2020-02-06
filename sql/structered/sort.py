def get_sort(order_by):
    order_by = order_by.strip()
    if order_by == '':
        return 'id asc'
    else:
        order_by = order_by.strip().replace(' ASC', ' asc').replace(' DESC', ' desc')
        if ',' in order_by:
            print(order_by[-3:])
            if order_by[-3:] == 'asc':
                order_by = order_by.replace(',', ' asc,')
            else:
                order_by = order_by.replace(',', ' desc,')
    return order_by
