import psycopg2

connect = psycopg2.connect(user="postgres", password="artd2006st", host="localhost", port=5432)


def create_reports_db():
    curs = connect.cursor()
    curs.execute('''CREATE TABLE reports (
                                    user_id BIGINT NOT NULL,
                                    headline TEXT NOT NULL,
                                    text TEXT NOT NULL
                                    );''')
    connect.commit()
    curs.close()


def add_report(report):
    curs = connect.cursor()
    curs.execute('''INSERT INTO reports (user_id, headline, text) VALUES (%s, %s, %s)''', report)
    connect.commit()
    curs.close()


def get_reports():
    curs = connect.cursor()
    curs.execute('''SELECT * from reports''')
    record = curs.fetchall()
    connect.commit()
    curs.close()
    return record


def delete_report(user_id):
    curs = connect.cursor()
    curs.execute('''DELETE from reports where user_id = %s''', (user_id,))
    connect.commit()
    curs.close()
