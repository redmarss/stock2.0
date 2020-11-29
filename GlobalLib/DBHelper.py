from globalConfig import sql_config
import pymysql

class zwdSql(object):
    def __init__(self):
        try:
            self.conn = pymysql.connect(
                host = sql_config['host'],
                port = sql_config['port'],
                db = sql_config['db'],
                user = sql_config['user'],
                passwd = sql_config['passwd'],
                charset = sql_config['charset']

            )
        except:
            pass
        
if __name__ == "__main__":
    
    print(sql_config)