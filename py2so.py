#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
Compile python file to linux so file.
"""


import copy
import multiprocessing
import os
import shutil
import subprocess
import sys


RAW_SETUP = """#!/usr/bin/python
# -*- coding: utf-8 -*-


from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("%s")
)
"""


def write_setup(setup_string):
    with open("setup_o.py", "w") as fout:
        fout.write(setup_string)


def real_cmd():
    args = ["python", "setup_o.py", "build_ext", "--inplace"]
    process = subprocess.Popen(args)
    process.wait()


def run_cmd(file_path):
    process = multiprocessing.Process(name='real_cmd', target=real_cmd)
    process.start()
    process.join()

    while 1:
        if not process.is_alive():
            break


def copy_so(file_path):

    filename = os.path.basename(file_path)
    dirpath = os.path.dirname(file_path)
    so = os.path.splitext(filename)[0] + ".so"
    so_path = os.path.join(dirpath, so)
    shutil.move(so, so_path)


def rm_c(file_path):
    filename = os.path.basename(file_path)
    dirpath = os.path.dirname(file_path)
    c = os.path.splitext(filename)[0] + ".c"
    c_path = os.path.join(dirpath, c)

    os.unlink(c_path)



def compile_file(file_path):
    """
    The steps of compile a py file to a .so file:
    1. Write a setup.py file. In this case, we use `setup_o.py` instead
    2. Compile the python file.
    3. Copy .so file to the folder where the original py file holds.
    4. Remove c file & setup_o.py, remove build folder.
    """
    if not file_path.endswith(".py"):
        return
    setup_string = copy.deepcopy(RAW_SETUP)
    setup_string = setup_string % file_path
    write_setup(setup_string)
    run_cmd(file_path)
    copy_so(file_path)
    rm_c(file_path)


def walk(base_dir):
    for root, dirs, files in os.walk(base_dir):
        for _file in files:
            compile_file(os.path.join(root, _file))
        for _dir in dirs:
            walk(os.path.join(root, _dir))
    base_dir = os.path.dirname(os.path.abspath(__file__))
    shutil.rmtree(os.path.join(base_dir, "build"))
    os.unlink("setup_o.py")


if __name__ == '__main__':
    walk(sys.argv[1])
