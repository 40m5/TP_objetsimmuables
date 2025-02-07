from dataclasses import dataclass

@dataclass(frozen=True)
class Article:
    nom: str
    prix: float
    stock: int
    
def ajouter_article(inventaire, article):
    return inventaire + [article]


inventaire = []
inventaire = ajouter_article(inventaire, Article("Ordinateur", 1200.0, 10))
print(inventaire)  


def mettre_a_jour_stock(inventaire, nom_article, nouvelle_quantite):
    return [
        Article(a.nom, a.prix, nouvelle_quantite) if a.nom == nom_article else a
        for a in inventaire
    ]


inventaire = mettre_a_jour_stock(inventaire, "Ordinateur", 5)
print(inventaire)  



def supprimer_article(inventaire, nom_article):
    return [a for a in inventaire if a.nom != nom_article]


inventaire = supprimer_article(inventaire, "Ordinateur")
print(inventaire)  



@dataclass(frozen=True)
class Commande:
    articles: list  


def calculer_montant_total(commande, inventaire):
    return sum(
        a.prix * q for nom, q in commande.articles for a in inventaire if a.nom == nom
    )


inventaire = [Article("Ordinateur", 1200.0, 5), Article("Souris", 25.0, 50)]
commande = Commande([("Ordinateur", 1), ("Souris", 2)])

print(calculer_montant_total(commande, inventaire))  



@dataclass(frozen=True)
class Promotion:
    nom: str
    condition: callable  
    reduction: float  

def appliquer_promotions(commande, inventaire, promotions):
    total = calculer_montant_total(commande, inventaire)
    for promo in promotions:
        if promo.condition(total):
            total *= (1 - promo.reduction / 100)
    return total


promos = [
    Promotion("Réduction 10% si plus de 1000€", lambda total: total > 1000, 10)
]

print(appliquer_promotions(commande, inventaire, promos))  



def mettre_a_jour_inventaire_apres_commande(inventaire, commande):
    return [
        Article(a.nom, a.prix, a.stock - dict(commande.articles).get(a.nom, 0))
        for a in inventaire
    ]
    



inventaire = [Article("Ordinateur", 1200.0, 5), Article("Souris", 25.0, 50)]
commande = Commande([("Ordinateur", 1), ("Souris", 2)])

nouvel_inventaire = mettre_a_jour_inventaire_apres_commande(inventaire, commande)
print(nouvel_inventaire)  



