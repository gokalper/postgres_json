import psycopg2

table_name = "json_table7"


def compose_query(query):
    conn = None
    response = None
    try:
        conn = psycopg2.connect("dbname='test' user='postgres' host='localhost' password='daycare'")
        cur = conn.cursor()
        cur.execute(query)
        try:
            response = cur.fetchall()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        cur.close()
        print("SUCCESS")

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()
            conn = None
            print("Database Connection Closed.")

    return response


def get_all_rows(table_name):
    some_query = """SELECT * from {}""".format(table_name)
    rows = compose_query(some_query)
    for row in rows:
        print(row)


get_all_rows(table_name)

query = """update json_table7 set data = jsonb_set(data, '{snacks}', '"what"'::jsonb) where name = 'John';"""
compose_query(query)

get_all_rows(table_name)

