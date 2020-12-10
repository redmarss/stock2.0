from globalConfig import SQL_CONFIG
import pymysql

class zwdSql(object):
    def __init__(self):
        try:
            self.conn = pymysql.connect(
                host = SQL_CONFIG['host'],
                port = SQL_CONFIG['port'],
                db = SQL_CONFIG['db'],
                user = SQL_CONFIG['user'],
                passwd = SQL_CONFIG['passwd'],
                charset = SQL_CONFIG['charset']

            )
        except:
            pass
        
if __name__ == "__main__":
    
    print(SQL_CONFIG)