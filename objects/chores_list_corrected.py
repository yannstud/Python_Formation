class Taches:
    def __init__(self):
            self.taches = []
            self.termine = []

    def ajouter(self, tache):
        self.taches.append(tache)
        self.termine.append(False)

    def idx_valid(self, idx):
        if idx >= 0 and idx < len(self.taches):
            return True
        else:
           print("Erreur: indice hors limites")
           return False

    def terminer(self, idx):
        if self.idx_valid(idx):
            self.termine[idx] = True

    def supprimer(self, idx):
        if self.idx_valid(idx):
            del self.taches[idx]
            del self.termine[idx]

    def afficher(self):
        print('----------------------')
        for i, t in enumerate(self.taches):
            print(f'{i} : {t} - {self.termine[i]}')

taches = Taches()

while True:
    cmd = input("entrez une commande (+: Ajouter, -: Terminer, s: Supprimer, a: Afficher, q: Quitter): ")

    if cmd == '+':
        tache = input("Entrez le nom: ")
        taches.ajouter(tache)
    elif cmd == "-":
        idx = int(input("Entrez l'id de la tache "))
        taches.terminer(idx)
    elif cmd == "s":
        idx = int(input("Entrez l'id de la tache "))
        taches.supprimer()
    elif cmd == "a":
        taches.afficher()
    elif cmd == "q":
        break
    else:
        print("Commande invalide")