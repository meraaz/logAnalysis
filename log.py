#!/usr/bin/env python3
import psycopg2
from datetime import datetime

# Database Name to use
DB_NAME = "news"


# Function Connect
def connect(database_name=DB_NAME):
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except RuntimeError:
        print("Error Happened while connecting the DB")


# Question 1 Query
# What are the most popular three articles of all time ?
def popular_posts():
    # connect to the database
    db, cursor = connect()
    # The query to answer question 1
    cursor.execute("""\
        select title , max(count) as maxValue
        from  (
            select articles.title , count(log.path)
            from articles
            join log on log.path like concat('/article/',articles.slug)
            group by log.path , articles.title
            ) as articlesCount
            group by title
            order by maxValue desc
            limit 3
        """)
    # fetch the result of question 1 query
    posts = cursor.fetchall()
    # close the DB connection
    db.close()
    print("What are the most popular three articles of all time ?")
    # Fetch the question one query result
    for title, maxValue in posts:
        # Format question three answer
        print("\"", title, "\"", " - ", maxValue, " views")


# Question 2 Query
# Who are the most popular article author of all time ?
def popular_authors():
    # connect to the database
    db, cursor = connect()
    # The query to answer question 2
    cursor.execute("""\
        select author, max(counter) as views
        from (
                select authors.name as author, count(log.path) as counter
                from log
                join articles on
                    log.path like concat('/article/',articles.slug)
                join authors on authors.id = articles.author
                group by authors.name , articles.author
            ) as articlesCount
            group by author
            order by views desc
        """)
    # fetch the result of question 2 query
    posts = cursor.fetchall()
    # close the DB connection
    db.close()
    print("Who are the most popular article author of all time ?")
    # Fetch the question two query result
    for author, views in posts:
        # Format question three answer
        print(author, " - ", views, " views")


# Question 3 Query
# On Which days did more than 1% of requests lead to errors ?
def requests_errors():
    # connect to the database
    db, cursor = connect()
    # The query to answer question 3
    cursor.execute("""\
        with total as (
                select count(id) as total , time::timestamp::date as time
                from log
                group by time::timestamp::date
            ),
            errors as (
                select count(id) as errors , time::timestamp::date as time
                from log
                where status <> '200 OK'
                group by time::timestamp::date
                )
            select day , max(percentage) as percentage
            from (
                    select t.time as day ,
                    round((e.errors * 100.0) / t.total , 2) as percentage
                    from total as t
                    join errors as e on t.time = e.time
                ) as dayPercentage
                group by day
                order by percentage desc
                limit 1
            """)
    # fetch the result of question 3 query
    posts = cursor.fetchall()
    # close the DB connection
    db.close()
    print("On Which days did more than 1% of requests lead to errors ?")
    # Fetch the question three query result
    for day, percentage in posts:
        # Format question three answer
        print(datetime.strftime(day, '%b %d, %Y'), "-", percentage, "% errors")


# Question one Answer
popular_posts()
print("\n")

# Question two Answer
popular_authors()
print("\n")

# Question three Answer
requests_errors()
