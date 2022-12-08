import psycopg2

class MyDatabase:
    def __init__(self):
        try:
            self.conn = psycopg2.connect("dbname=chore_list user=my_user password=my_password")
            self.cursor = self.conn.cursor()
        except psycopg2.OperationalError as e:
            print(f'Unable to connect!\n{e}')
            exit(1)

    # Execute commands
    # if commit != 0 we commit the command
    # if fetchone != 0 we fetch one lign
    # if fetchall != 0 we fetch all
    def execute(self, command, commit=0, fetchone=0, fetchall=0):
        self.cursor.execute(command)
        if fetchone != 0:
            return self.cursor.fetchone()
        if fetchall != 0:
            return self.cursor.fetchall()
        if commit != 0:
            self.conn.commit()



    # Check if table exist if not create
    def check_table(self, tablename):
        command_check = f"""SELECT EXISTS(SELECT FROM pg_tables WHERE schemaname = 'public' AND tablename = '{tablename}' );"""
        # If table dont exist create it
        if self.execute(command_check, fetchone=1)[0] != True:
            # It would have been better to use IF NOT EXISTS
            # command_create_table = f""" CREATE TABLE IF NOT EXISTS {tablename} (id SERIAL PRIMARY KEY, name VARCHAR(255) NOT NULL, is_done BOOL NOT NULL)"""
            command_create_table = f""" CREATE TABLE {tablename} (id SERIAL PRIMARY KEY, name VARCHAR(255) NOT NULL, is_done BOOL NOT NULL)"""
            self.execute(command_create_table, 1)

    # Close cursor
    def close(self):
        self.cursor.close()

    def add_chore(self, chore_name):
        self.execute(f""" INSERT INTO chores (name, is_done) VALUES ('{chore_name}', FALSE)""", commit=1)

    def get_all_chores(self):
        return self.execute("SELECT * FROM chores", fetchall=1)

    def end_chore(self, id_chore):
        if self.exist(id_chore) != None:
            return self.execute(f"""UPDATE chores
                                    SET is_done = TRUE
                                    WHERE id = {int(id_chore)}""", commit=1)
        else:
            return 0

    def delete_chore(self, id_chore):
        if self.exist(id_chore) != None:
            return self.execute(f"""DELETE FROM chores 
                                    WHERE id = {int(id_chore)}""", commit=1)
        else:
            return 0

    # Check in database if chore with id exist or not
    def exist(self, id_chore):
        return self.execute(f"SELECT * FROM chores WHERE id = {int(id_chore)}", fetchone=1)


try:
    db = MyDatabase()
    db.check_table('chores')

    while True:
        cmd = input("Enter a command (+: Add, -: End, s: Delete, a: Show, q: Quit): ")

        if cmd == '+':
            tache = input("Enter the name: ")
            db.add_chore(tache)
        elif cmd == "-":
            idx = int(input("Enter the id of the chore "))
            db.end_chore(idx)
        elif cmd == "s":
            idx = int(input("Enter the id of the chore "))
            db.delete_chore(idx)
        elif cmd == "a":
            ret = db.get_all_chores()
            for l in ret:
                print(f"{l[0]} - {l[1]}, {l[2]}")
        elif cmd == "q":
            break
except Exception as e:
        print(f'Error !\n {e}')
finally:
    db.close()
