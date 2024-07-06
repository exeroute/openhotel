import sqlite3

class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def get_free_rooms(self):
        with self.connection:
            return self.cursor.execute('SELECT * FROM rooms WHERE isfree = "Свободно"').fetchall()

    def get_busy_rooms(self):
        with self.connection:
            return self.cursor.execute('SELECT * FROM rooms WHERE isfree = "Занято"').fetchall()

    def get_all_rooms(self):
        with self.connection:
            return self.cursor.execute('SELECT * FROM rooms').fetchall()

    def add_cliet(self, surname, name, lastname, phone, room):
        with self.connection:
            self.cursor.execute('UPDATE rooms SET isfree = "Занято" WHERE number = ?', (room))
            return self.cursor.execute('INSERT OR IGNORE INTO clients (surname, name, lastname, phone, room) VALUES (?, ?, ?, ?, ?)',
                                       (surname, name, lastname, phone, room))

    def del_cliet(self, room):
        with self.connection:
            self.cursor.execute('UPDATE rooms SET isfree = "Свободно" WHERE number = ?', (room))
            return self.cursor.execute('DELETE FROM clients WHERE room = ?', (room))

    def get_all_clients(self):
        with self.connection:
            return self.cursor.execute('SELECT * FROM clients').fetchall()

    def get_room(self, room):
        with self.connection:
            return self.cursor.execute('SELECT * FROM clients WHERE room = ?', (room)).fetchone()

