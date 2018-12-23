# -*- coding:utf-8 -*-
__author__ = 'snake'

import os, sys


DevelopConfig = {
    "DEBUG": True,
    "HOST": "0.0.0.0",
    "JSON_AS_ASCII": False,  # json 中文支持
    "BABEL_DEFAULT_LOCALE": "zh",
    "SECRET_KEY": os.urandom(24)  # SESSION配置
}

ProductionConfig = {
    "DEBUG": False,
    "HOST": "0.0.0.0",
    "JSON_AS_ASCII": False,  # json 中文支持
    "BABEL_DEFAULT_LOCALE": "zh",
    "SECRET_KEY": os.urandom(24)  # SESSION配置
}

FlaskConfig = {
    "DevelopConfig": DevelopConfig,
    "ProductionConfig": ProductionConfig
}

DBConfig = {
    'host': '118.24.29.59',
    'port': 3306,
    'user': 'root',
    'password': '123456',
    'db': 'jinks',
    'charset': 'utf8mb4'
}

UploadConfig = {
    "UPLOAD_FOLDER": sys.path[1] + "\\app\\static\\uploads"
}


if __name__ == "__main__":
    print(UploadConfig["UPLOAD_FOLDER"])
