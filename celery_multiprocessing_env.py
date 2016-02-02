#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
This is the billiard assertion error, use EVN to avoid it,
In shell:    export PYTHONOPTIMIZE=1
Or in python: os.environ["PYTHONOPTIMIZE"] = "1" # the value is of type string

See: https://github.com/celery/celery/issues/1709 for more infomation.
"""

from __future__ import absolute_import

import os
import multiprocessing

from celery import Celery


app = Celery("multi-process")


def m(arg):
    print arg


@app.task
def multi(arg):
    os.environ["PYTHONOPTIMIZE"] = "1"
    th = multiprocessing.Process(target=m, args=(arg,))
    th.start()
    th.join()
    return None
