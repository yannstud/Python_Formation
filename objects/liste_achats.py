class Achats:
    def __init__(self):
        self.produits = {}

    def ajouter(self, name, price):
        self.produits[name] = price

    def afficher(self):
        print('----------------------')
        for i, p in enumerate(self.produits):
            print(f'{i} : {p} - {self.produits[p]}')

    def supprimer(self, name):
        if name in self.produits:
            del self.produits[name]
        else:
            print("Erreur: produit invalide")

    def prix_total(self):
        ret = 0.0
        for product, value in self.produits.items():
            ret += value
        print(f"prix total: {ret}")

achats = Achats()

achats.ajouter("Bananne", 3.6)
achats.ajouter("Oeuf", 2.5)
achats.ajouter("Salade", 3)

while True:
    cmd = input("entrez une commande (+: Ajouter, s: Supprimer, t: Prix total, a: Afficher, q: Quitter): ")

    if cmd == '+':
        achat = input("Entrez le nom du produit: ")
        prix = float(input("Entrez le prix: "))
        achats.ajouter(achat, prix)
    elif cmd == "t":
        print(achats.prix_total())
    elif cmd == "s":
        name = input("Entrez le nom de l\'article a supprimer")
        achats.supprimer(name)
    elif cmd == "a":
        achats.afficher()
    elif cmd == "q":
        break
    else:
        print("Commande invalide")
