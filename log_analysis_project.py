#!/usr/bin/env python

import psycopg2
import datetime as machine_time


# Main fuction in which all the queries are performed.
def main():
    # query to fetch the popular articles
    que1 = """select title, data from
             articlespopular order by
             data desc limit 3"""

    # query to fetch the popular authors
    que2 = """select name,count from authpopular
              ,countall where authpopular.id =
              countall.author"""

    # query to fetch the days with error requests more than 1%
    que3 = """select td,100.0* abcd/al as fa
             from errno21 where 100.0* abcd/al > 1
             order by fa desc
             """

    # function call to execute_q() to execute query 1
    result1 = execute_q(que1)

    # function call to execute_q() to execute query 2
    result2 = execute_q(que2)

    # function call to execute_q() to execute query 3
    result3 = execute_q(que3)

    # printing output of query 1 at the terminal
    print("3 most popular articles of all time are:")
    for var in range(len(result1)):
        print("{} - {} views".format(result1[var][0], result1[var][1]))

    # printing output of query 2 at the terminal
    print("\nAuthors with highest popularity are:")
    for var in range(len(result2)):
        print("{} - {} views".format(result2[var][0], result2[var][1]))

    # printing output of query 3 at the terminal
    print("\nNo of days with more than 1% error requests:")
    t_d = machine_time.datetime.strptime(str(result3[0][0]),
                                         '%Y-%m-%d').strftime("%B %d, %Y")
    print("{} - {}% errors".format(t_d, round(result3[0][1], 2)))


# function to execute queries and return the output
def execute_q(query):
    db = psycopg2.connect("dbname = news")
    cursor = db.cursor()
    result = None
    cursor.execute(query)
    result = cursor.fetchall()
    db.commit()
    db.close()
    return result

# checking whether main function is called by main file
# itself or by some other py file
if __name__ == '__main__':
    main()
