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


def search_old():
    db = DbHelper('192.168.165.87', 'root', 'Canw@y2019_', 'cw-public')
    versions = db.search_all('cw_admin_appversion')
    return versions


def search_app_list():
    db = DbHelper('192.168.165.87', 'root', 'Canw@y2019_', 'auto-pack')
    apps = db.search_all('home_application_applist')
    app_codes = [app['app_code'] for app in apps]
    return app_codes


def get_app_by_code(code):
    db = DbHelper('192.168.165.87', 'root', 'Canw@y2019_', 'auto-pack')
    apps = db.search_all('home_application_appversion')
    app_codes = [app['app_code'] for app in apps]
    if code in app_codes:
        return True
    return False


def create_app_version(old):
    db = DbHelper('192.168.165.87', 'root', 'Canw@y2019_', 'auto-pack')
    fields = '(`app_code`, `version`, `version_name`, `version_info`, `when_created`, `when_modified`, `commit_info`, `commit_id`, `is_delete`, `is_pack`, `status`)'
    values = "('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', {8}, {9}, {10})".format(
        old['app_code'],
        old['version'],
        old['version_name'],
        old['version_info'],
        old['when_created'],
        old['when_modified'],
        old['commit_info'],
        old['commit_id'],
        0,
        0,
        0
    )
    sql = "insert into `home_application_appversion` {0} values {1}".format(fields, values)
    db.execute(sql)
    db.commit()

def get_app_version_id(old):
    db = DbHelper('192.168.165.87', 'root', 'Canw@y2019_', 'auto-pack')
    versions = db.search_all('home_application_appversion')
    id = 0
    for v in versions:
        if v['app_code'] == old['app_code'] and v['version'] == old['version']:
            id = v['id']
    return id


def create_pack(old):
    db = DbHelper('192.168.165.87', 'root', 'Canw@y2019_', 'auto-pack')
    fields = '(`app_code`, `pkg_url`, `pkg_type`, `when_created`, `when_modified`, `app_version_id`)'
    values = "('{0}', '{1}', '{2}', '{3}', '{4}', {5})".format(
        old['app_code'],
        old['pkg_url'],
        'saas_en' if old['is_encry'] else 'saas',
        old['when_created'],
        old['when_modified'],
        get_app_version_id(old)
    )
    sql = "insert into `home_application_appversionpackage` {0} values {1}".format(fields, values)
    db.execute(sql)
    db.commit()


def create_ald():
    try:
        olds = search_old()
        apps = search_app_list()
        for old in olds:
            if old['app_code'] not in apps:
                continue
            create_app_version(old)
        for old in olds:
            if old['app_code'] not in apps:
                continue
            create_pack(old)
    except Exception as e:
        print e


create_ald()
