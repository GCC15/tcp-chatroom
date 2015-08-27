"""
Data access object
High-level abstraction of the database
"""

from . import db_adapter
from . import names


def main():
    """For testing"""
    c = db_adapter.get_cursor()

    # Create table
    c.execute('''CREATE TABLE stocks
                 (date text, trans text, symbol text, qty real, price real)''')

    # Insert a row of data
    c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

    # Save (commit) the changes
    db_adapter.commit()


if __name__ == '__main__':
    main()
