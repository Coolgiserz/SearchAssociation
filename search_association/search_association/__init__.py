import pymysql

# 针对Python3.x，避免该异常：django.core.exceptions.ImproperlyConfigured: Error loading MySQLdb module.
pymysql.install_as_MySQLdb()