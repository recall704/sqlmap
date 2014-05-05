#!/usr/bin/env python

"""
Copyright (c) 2006-2014 sqlmap developers (http://sqlmap.org/)
See the file 'doc/COPYING' for copying permission
"""

import sys

# sys.version => '2.7.3 (default, Jan  2 2013, 13:56:14) \n[GCC 4.7.2]'
PYVERSION = sys.version.split()[0]

# 判断python 执行版本
if PYVERSION >= "3" or PYVERSION < "2.6":
    exit("[CRITICAL] incompatible Python version detected ('%s'). For successfully running sqlmap you'll have to use version 2.6 or 2.7 (visit 'http://www.python.org/download/')" % PYVERSION)


# 导入 gzip ssl sqlite3 zlib 模块
extensions = ("gzip", "ssl", "sqlite3", "zlib")
try:
    for _ in extensions:
        __import__(_)
except ImportError:
    errMsg = "missing one or more core extensions (%s) " % (", ".join("'%s'" % _ for _ in extensions))
    errMsg += "most probably because current version of Python has been "
    errMsg += "built without appropriate dev packages (e.g. 'libsqlite3-dev')"
    exit(errMsg)
