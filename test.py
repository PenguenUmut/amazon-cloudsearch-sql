import threading
from sql.main import get_sql_properties
from sql.main import get_query
from sql.main import query

# http://XYZ.cloudsearch.amazonaws.com
endpoint_url = 'YOUR_CLOUDSEARCH_ENDPOINT_URL'

sqls = [
    "select * from poi WHERE name = 'Hanashi' and (city_id=41 or (name='casa' and city_id=42))",
    "select * FROM poi where name LIKE 'Casa'",
    "select * From poi where city_id = 41",
    "SELECT id from poi WHERE tags = 'cocktail' And city_id = 41",
    "Select id,name,tags from poi where tags like 'beer' order by id",
    "SELECT id, name,city_id FROM poi Where placetype_id = 3 AND tags Like 'res'",
    "select id from poi where tag_ids = 46",
    "select id from poi where name like 'Casa'",
    "SELECT id,city_id FROM poi WHERE id = 44822",
    "SELECT name,tags FROM poi WHERE name LIKE 'Ca' order by name desc",
    "SELECT id FROM poi WHERE name LIKE 'Cas' order by id",
    "SELECT * FROM poi WHERE tags = 'wifi' order by name,id",
    "SELECT TOP 10 * FROM table WHERE name='asd' or id = 123 OR tags LIKE 'qwe'",
    "SELECT * FROM table WHERE (name='asd' AND id = 123) OR tags NOT LIKE 'qwe' Order By name desc",
    "SELECT * FROM table WHERE name='asd' AND (id = 123 OR tags NOT LIKE 'qwe')",
    "SELECT id, name, duration FROM poi WHERE name LIKE 'Casa' order by name,id",
]

for sql in sqls:
    print('')
    print('*** MAIN TEST ***')

    print(sql)
    # sql_properties = get_sql_properties(sql)
    # q_object = sql_properties[3]
    # query_text = get_query(q_object)
    # print(query_text)

    result = query(sql, endpoint_url)
    print(result)
