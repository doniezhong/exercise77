# -*- coding: utf-8 -*-
"""
用于测试环境的全局配置
"""
import os

from settings import APP_ID, BASE_DIR

# ===============================================================================
# 数据库设置, 测试环境数据库设置
# ===============================================================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # 默认用mysql
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),                        # 数据库名 (默认与APP_ID相同)
        'USER': 'root',                            # 你的数据库user
        'PASSWORD': 'L*vIW=.lTr',                        # 你的数据库password
        'HOST': '192.168.163.212',                   		   # 数据库HOST
        'PORT': '3306',                        # 默认3306
    },
}
