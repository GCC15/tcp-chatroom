import os
import threading

import env

_var_dir = env.get_var_dir()
env.make_dirs(_var_dir)
_log_file = env.get_log_file()
_log_file_path = os.path.join(_var_dir, _log_file)

_f = open(_log_file_path, 'a')
_write_lock = threading.Lock()


def log(message: str):
    with _write_lock:
        _f.write('{}: {}\n'.format(threading.current_thread().name, message))


def main():
    log('test')


if __name__ == '__main__':
    main()
