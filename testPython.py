
x = 1.1;
y = 2;
print('Résultat = ', x+y,'\n');

#[] pour liste modifiable, () pour tuples/listes non modifiables
liste_de_noms = ["Kevin", "Jean", "Mark", "Paul", "Lucy"];
bonjour = "Hello There"

#affiche premier element de liste
print(liste_de_noms[0], '\n');

#affiche dernier element de liste
print(liste_de_noms[-1], '\n');

#affiche premier character de chaine de charactere
print(bonjour[0],'\n');

#ajout dans une liste
liste_de_noms.append("Claire");
liste_de_noms.append("Jean");
print(liste_de_noms);

#supprime un element de la liste 
# (ne retire que le premier element correspondant)
liste_de_noms.remove("Jean");
print(liste_de_noms);

#connaitre longueur de la liste
print(bonjour,' contient ', len(bonjour), ' de charactères\n');

#tri alphabétiquement ou numériquement
liste_de_noms.sort();
print('tri de la lise de noms : ', liste_de_noms, "\n");


#---------------------------------------------------------------------


#Dictionnaire de donnée -> exemple : Rouge = #FF0000
#Rouge est la clé, #FF0000 est la valeur
Couleurs = {"Rouge" : "#FF0000",
            "Vert" : "#00FF00",
            "Bleu" : "#0000FF",
            "Blanc" : "#FFFFFF",
            "Noir" : "#000000"};

CouleurPref = {"Kim-Brice" : ["Rouge", "Noir"],
               "Alex" : "Bleu"};

#possible de créer un dictionnaire vide avec {} ou dict()
#ajout de valeur dans un dico existant
dictio1 = {};
dictio1["valeur1"] = 69.69;
dictio1["valeur2"] = 42;
dictio2 = dict();
dictio2["valeur1"] = 69.69;
dictio2["valeur2"] = 42;

print(Couleurs["Rouge"], CouleurPref["Kim-Brice"], dictio1["valeur1"], '\n');

#supprimer une paire clé-valeur
print('dictio2 avant suppression : ', dictio2, '\n');
del dictio2["valeur1"];
print('dictio2 après suppression de valeur1 : ', dictio2, '\n');

#verifier l'existance d'une clé
print('Il existe valeur2 dans dictio2 : ',"valeur2" in dictio2);


#------------------------------------------------------------------------------

#if else if et else
ensoleille = False;
neige = True;

if ensoleille:
    print("il fait beau !");
elif neige:
    print("Il neige !");
else:
    print("rien de spécial");

Pile = True;
Face = False;

if Pile and not Face:
    print("C'est Pile !");
elif Pile and Face:
    print("...How ?");
else:
    print("C'est Face !");



#Boucle for
for nom in liste_de_noms:
    print("\n",nom);
#f au début de string si on utilise {}
i = 0;
for nom in liste_de_noms:
    i += 1;
    print(f"\nNom de la personne {i} : {nom}");

#Boucle while
sortie = False;
while sortie == False and 5 != 2:
    print("cette boucle est inutile");
    sortie = True;

#----------------------------------------------------------------
#fonction
def mult(a,b):
    return a*b;

print("résultat de la multiplication : ",mult(125,85));

#-------------------------------------------------------------------------

#ouverture de texte
#r lecture seule, w écriture seule (supprime et écrit !!!!)
#a continuer d'écrire (n'efface pas et écrit derrière ce qui existe déjà)
#r+ Lire et écrire (supprime et écrit !!!!)
fichier = open("textTest.txt","r+");
fichier.write("Hello There\n");
fichier.close;

#en block avec with en read jusqu'à ce que toutes les lignes soient lues
with open("textTest.txt") as fichier:
    for ligne in fichier:
        print(ligne);

