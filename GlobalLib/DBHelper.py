from GlobalLib.globalConfig import SQL_CONFIG
import GlobalLib.mylogger as mylogger
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
            mylogger.mylogger().error("连接数据库失败")

        self.cur = self.conn.cursor()
        
if __name__ == "__main__":
    
    zwdSql()