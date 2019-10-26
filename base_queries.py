import psycopg2

def compose_query(query):
    conn = None
    response = None
    try:
        conn = psycopg2.connect("dbname='test' user='postgres' host='localhost' password='password'")
        cur = conn.cursor()
        cur.execute(query)
        response = cur.fetchall()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()
            conn = None
            print("Database Connection Closed.")

    return(response)

table = "jsontable4"
query = """SELECT * from {}""".format(table)
rows = compose_query(query)
for row in rows:
    print(row)

query = """

select *
  from jsontable4
      ,jsonb_each(data) with ordinality arr(item, value, index)
      where item->>'snacks' = 'cookies'
      and name = 'John'
;

with snack as ( select('{' || index - 1 || ',value}')::text[] as path
from jsontable4, jsonb_object_keys(data) with ordinality arr(item, index)
where item->> 'snacks' = 'cookies'
and name = 'John'
)
update jsontable4 set data = jsonb_set(data, snack.path, '"crazy"', false) from snack

where
name = 'John';

select *
from customers;
"""
rows = compose_query(query)
# for row in rows:
#     print(row)