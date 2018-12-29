# -*- coding:utf-8 -*-

import os
import ConfigParser
import cx_Oracle

#proDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#conf_path = proDir + r"\config\config.ini"

conf = ConfigParser.ConfigParser()
conf.read(conf_path)
# section = conf.sections()
# options = conf.options("DB")
# kvs = conf.items("DB")

# ------------DB-------------#
host = conf.get("DB", "host")
username = conf.get("DB", "username")
password = conf.get("DB", "password")
email = conf.get("Email", "email")


def selectsql(sql, param):  # 查询sql语句的函数

    conn = cx_Oracle.connect(username, password, host)
    # conn = cx_Oracle.connect(username,password,host)
    cursor = conn.cursor()
    cursor.execute(sql, param)
    data = cursor.fetchall()
    cursor.close()
    conn.commit()
    conn.close()
    return data

    # # 不要使用这种获取项目根目录的方式，如果在其它类中引用，是相对其它类的目录进行。
    # # proDir1 = os.path.abspath(os.path.join(os.getcwd(), ".."))
    #
    # proDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # conf_path = proDir + r"\config.ini"
    #
    #
    # class ReadConfig:
    #     """
    #     创建ConfigParser对象，读取指定目录conf_path配置文件config_name
    #     """
    #     def __init__(self, config_name):
    #         self.conf = configparser.ConfigParser()
    #         # 中文乱码问题需要添加encoding="utf-8-sig"
    #         self.conf.read(conf_path + config_name, encoding="utf-8-sig")
    #
    #     def get_bs(self, name):
    #         value = self.conf.get("BS", name)
    #         return value
    #