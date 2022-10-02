import sqlite3 as sl


class Database:
    """A class storing user information in a sqlite3 database"""

    def __init__(self, dbname: str):
        if not dbname.endswith('.db'):
            self.con = sl.connect(dbname + '.db')
        else:
            self.con = sl.connect(dbname)
        self.cursor = self.con.cursor()
        with self.con:
            self.con.execute(
                """CREATE TABLE IF NOT EXISTS
                  users(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        slackID TEXT
                        );
                """)
        with self.con:
            self.con.execute(
                """CREATE TABLE IF NOT EXISTS rooms(
                  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                  name TEXT,
                  description TEXT,
                  img TEXT
                  );
                """)
        with self.con:
            self.con.execute(
                """CREATE TABLE IF NOT EXISTS events(
                  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                  name TEXT,
                  description TEXT,
                  roomid INTEGER,
                  organizer INTEGER,
                  );
                """)
        with self.con:
            self.con.execute(
                """CREATE TABLE IF NOT EXISTS events_users(
                 eventID INTEGER,
                 userID INTEGER
                 );
                """)
        with self.con:
            self.con.execute(
                """CREATE TABLE IF NOT EXISTS events_rooms(
                  eventID INTEGER,
                  roomID INTEGER
                  );
                """)