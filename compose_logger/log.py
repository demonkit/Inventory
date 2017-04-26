#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
import os

from cloghandler import ConcurrentRotatingFileHandler

import logconf


def compose_logger(name, log_file):
    logger = logging.Logger(name)
    hdlr = ConcurrentRotatingFileHandler(
        filename=os.path.join(LOG_FILE_DIR, log_file),
        maxBytes=logconf.MAX_BYTES, backupCount=logconf.BACK_UP_COUNT)
    formatter = logging.Formatter(logconf.VERBOSE_FORMATTER)
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    logger.setLevel(logging.DEBUG)
    return logger
