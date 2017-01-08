from distributed import local_client
import os
import time
import glob


def fib(n):
    if n < 2:
        return n
    else:
        with local_client() as c:
           a = c.submit(fib, n - 1)
           b = c.submit(fib, n - 2)
           a, b = c.gather([a, b])
           return a + b

def create_dirs(dir_name, root_dir=r'Sandbox/dask/working'):
    time.sleep(2)
    home_dir = os.environ.get('HOME')
    root_dir = os.path.join(home_dir, root_dir)
    os.mkdir(os.path.join(root_dir, str(dir_name)))
    print('creating %s' %str(dir_name))
    return None

def get_dirs(depend_on, root_dir=r'Sandbox/dask/working'):
    time.sleep(2)
    print('Get dirs success')
    home_dir = os.environ.get('HOME')
    root_dir = os.path.join(home_dir, root_dir)
    dirs = glob.glob(os.path.join(root_dir, '*'))
    flags = []
    with local_client() as lc:
        for i_dir in dirs:
            flags.append(lc.submit(print_flag, i_dir))
        return flags


def print_flag(which_dir):
    print(which_dir)

def add_flag(future_dir):
    time.sleep(2)
    print('create flag to %s' %future_dir)
    if not os.path.isdir(future_dir):
        os.makedirs(future_dir)
    f = open(os.path.join(future_dir, 'success.txt'), 'a')
    f.close()
    return None


def double(x):
    return 2*x
