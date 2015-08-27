import os
import sqlite3

import config as cfg


def _get_conn():
    global _conn
    if not _conn:
        var_dir = cfg.get('var_dir')
        cfg.make_dirs(var_dir)
        db_file = cfg.get('db_file')
        db_file_path = os.path.join(var_dir, db_file)
        _conn = sqlite3.connect(db_file_path)
    return _conn


_conn = _get_conn()


def get_cursor():
    return _conn.cursor()


def commit():
    """Commit changes"""
    _conn.commit()


def close():
    """Do not call this function"""
    _conn.close()
