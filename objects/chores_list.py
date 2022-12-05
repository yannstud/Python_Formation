import itertools

class Chore:
    id_obj = itertools.count ()
    def __init__(self, chore):
        self.id = next(Chore.id_obj)
        self.chore = chore
        self.done = False

    def do_chore(self):
        self.done = True

    def show(self):
        print(f"{t.id} : {t.chore} - {t.done}")

if __name__ == '__main__':
    chores = []
    chores.append(Chore("Take out the trash"))
    chores.append(Chore("Make some food"))
    chores.append(Chore("Take a shower"))

    cmd = input("Add + \nEnd -\nDelete s\nShow a\nQuit q\nHelp h\nSelect a command: ")
    while cmd != "q":
        if cmd == "s" or cmd == "-":
            id_chore = int(input("Enter the Id of the chore: "))
            for tache in chores:
                if tache.id == id_chore and cmd == "-":
                    tache.do_chore()
                elif tache.id == id_chore and cmd == "s":
                    chores.remove(tache)
        elif cmd == "+":
            new_chore_name = input("Enter the name of the chore you want to add: ")
            chores.append(Chore(new_chore_name))
        elif cmd == "a":
            print ("id:       Chore      - Is done")
            for t in chores:
                t.show()
        elif cmd == "h":
            print("Add: + \nEnd: -\nDelete: s\nShow: a\nQuit: q\nHelp: h\nSelect a command: ")
        else:
            print ("Unknown command")
        cmd = input(">>> ")
