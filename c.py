import ctypes
from invoke import task
import subprocess

shared_lib_path = './clib/build/libcalc.so'
cfile = 'test.c'
cfile_path = './clib/{cfile}'


@task(name='build-clib')
def build_clib(c):
    c.run(f'gcc -fPIC -shared -o {shared_lib_path} {cfile_path}')


task_name = 'build-clib'
subprocess.run(['invoke', task_name], check=True)


a, b = 5.5, 6.5


c_lib = ctypes.CDLL(shared_lib_path)

c_lib.add.restype = ctypes.c_float

res = c_lib.add(ctypes.c_float(a), ctypes.c_float(b))

print(res)
