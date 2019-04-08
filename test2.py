# -*- coding: utf-8 -*-
import pymysql


class DbHelper(object):
    def __init__(self, host, user, pwd, db):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db
        self.cursor = self._connect()

    def execute(self, sql):
        self.cursor.execute(sql)

    def search_all(self, table_name):
        self.execute('desc `{}`'.format(table_name))
        fields = self.cursor.fetchall()
        self.execute('select * from `{}`'.format(table_name))
        data = self.cursor.fetchall()
        search_data = []
        for d in data:
            one = {}
            index = 0
            for f in fields:
                one[f[0]] = d[index]
                index += 1
            search_data.append(one)
        return search_data

    def commit(self):
        self.con.commit()

    def _connect(self):
        self.con = pymysql.connect(self.host, self.user, self.pwd, self.db)
        return self.con.cursor()

    def __del__(self):
        self.cursor.close()


def search_all_app():
    db = DbHelper('192.168.169.12', 'root', '1qaz@WSX3edc', 'open_paas')
    apps = db.search_all('paas_app')
    return [app['code'] for app in apps]


def create_auth(code, username):
    db = DbHelper('192.168.169.12', 'root', '1qaz@WSX3edc', 'uam')
    fields = '(`app_id`, `user_id`, `expiration_time`)'
    values = "('{0}', '{1}', '9999-09-09 00:00:00')".format(code, username)
    sql = "insert into home_application_appuser {0} values {1}".format(fields, values)
    db.execute(sql)
    db.commit()

def get_auth(code, username):
    db = DbHelper('192.168.169.12', 'root', '1qaz@WSX3edc', 'uam')
    apps = db.search_all('home_application_appuser')
    for app in apps:
        if app['app_id'] == code and username == app['user_id']:
            return True
    return False

def add_auth(username):
    apps = search_all_app()
    for app in apps:
        if get_auth(app, username):
            continue
        create_auth(app, username)


if __name__ == '__main__':
    username = 'test'
    add_auth(username)
