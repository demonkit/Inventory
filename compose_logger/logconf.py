#!/usr/bin/python
# -*- coding: utf-8 -*-


import os

LOG_FILE_DIR = "/var/log/your_project"

MAX_BYTES = 1024 * 1024 * 100
BACK_UP_COUNT = 50


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'formatter': 'verbose',
            'class': 'cloghandler.ConcurrentRotatingFileHandler',
            'maxBytes': MAX_BYTES,
            'backupCount': BACK_UP_COUNT,
            'filename': os.path.join(LOG_FILE_DIR, 'debug.log'),
        },
        'root': {
            'level': 'DEBUG',
            'formatter': 'verbose',
            'class': 'cloghandler.ConcurrentRotatingFileHandler',
            'maxBytes': MAX_BYTES,
            'backupCount': BACK_UP_COUNT,
            'filename': os.path.join(LOG_FILE_DIR, 'root.log'),
        }
    },
    'formatters': {
        'verbose': {
            'format': '%(asctime)s %(levelname)s [%(name)s: %(lineno)s]: %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        }
    }
}
