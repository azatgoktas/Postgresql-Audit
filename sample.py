import psycopg2
from connect import cur


def get_database_functions():
    cur.execute("""SELECT  p.proname
                    FROM    pg_catalog.pg_namespace n
                    JOIN    pg_catalog.pg_proc p
                    ON      p.pronamespace = n.oid
                    WHERE   n.nspname = 'public'""")

def get_function_content(func_name):
    cur.execute("""SELECT routine_definition
                    FROM
                    information_schema.routines
                    WHERE specific_schema
                    LIKE 'public'
                    AND routine_name
                    LIKE """ + "'" + str(func_name) + "'")

def check_function(function_declaration):
    if "security definer" in function_declaration.lower():
        return True
    return False


try:
    get_database_functions() #return declared functions in db
    rows = cur.fetchall() # get all functions into list
except psycopg2.Error as err:
    print("there is an error",err)


#After getting functions from database
#We need to look at function defenitons one by one
#Rows returns 2 dimensions array
#With for loops we get the function name
#And getting function definition by get_function_content function

for row in rows: #rows return 2 dimension array
    for ro in row:
        if ro:
            try:
                get_function_content(ro)
                func_content = cur.fetchall()
            except psycopg2.Error as err:
                print("func content error",err)


for func in func_content:
    for single_func in func:
        try:
            print(check_function(single_func))
        except psycopg2.Error as err:
            print("function checking error")
