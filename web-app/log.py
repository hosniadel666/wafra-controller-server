import os
import sqlite3
import db


class log():
    def __init__(self):
        self.database = db.db()
        self.cursor = self.database.get_cursor()
        self.response = {}

    def get_all(self):
        self.cursor.execute("select * from system_log")
        rows = self.cursor.fetchall()

        if len(rows) >= 1:
            cnt = 0
            for row in rows:
                self.response[cnt] = {}
                self.response[cnt]['id'] = row[0]
                self.response[cnt]['log_message'] = row[1]
                self.response[cnt]['time'] = row[2]
                self.response[cnt]['type'] = row[3]
                cnt = cnt + 1
            self.response['status_code'] = 201
        else:
            self.response['status_code'] = 401
        self.conn.commit()
        return self.response

    def add(self, msg, type):
        self.cursor = self.conn.cursor()
        sql_statement = "INSERT INTO system_log(log_message, type) VALUES (?,?)"
        self.cursor.execute(sql_statement, (msg, type))
        self.conn.commit()

