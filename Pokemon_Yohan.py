import time
import random
import secrets

pokemonsJoueur = ["Pikachu", "Bulbizar", "Salamèche"]
pokemonsAdversaire = ["Araqua", "Triopikeur", "Electrode"]
votre_pokemon = {"Nom" : "", "PV" : 1, "Attaques" : []}
pokemon_adversaire = {"Nom" : "", "PV" : 1, "Attaques" : []}


print("Bonjour ! \nBienvenue dans l'arène Pokemon de Sunbeach City !")
time.sleep(2)
print("Hmm...")
time.sleep(2)
votre_nom = input("Vous ne m'avez pas l'air d'un dresseur ordinaire, je perçois en vous l'âme d'un grand dresseur dont la détermination intimidera sans aucun doute vos adversaires...! \nQuel est votre nom ? (Entrez votre nom de dresseur) : ")
time.sleep(1)
print("Ce nom inspire la victoire... Cependant " + votre_nom +", vous devrez faire vos preuves en affrontant les candidats de cette grande arène, \net croyez-moi, il vous faudra plus qu'un simple regard intimidant pour les vaincre haha !")
time.sleep(4)

choix = input("Alors dites-moi, êtes-vous prêt pour votre combat ? (oui / non) : ")
choix.lower()
if choix == "non":
    print("Haha ! Je le savais, votre regard n'était que du bluff !! Vous n'avez pas la trempe d'un vrai dresseur ! Allez, rentrez chez vous !")
    time.sleep(2)
    print("Fin du jeu")
    breakpoint

if choix == "oui":
    print("Haha ! J'apprécie cette détermination, je n'en attandais pas moins de vous.")
    time.sleep(2)
    print("Comme vous le savez, vous ne devez choisir qu'un seul pokémon pour ce combat.")
    time.sleep(3)



#DICTIONNAIRES DES POKEMONS

pikachu = {"Nom" : "Pikachu", "PV" : 86, "Attaque" : ["Attaque Eclaire",  "Morsure Electrique", "Bouclier de Foudre"]}
bulbizar = {"Nom" : "Bulbizar", "PV" : 67, "Attaque" : ["Fouet Lianes", "Canon Graines", "Synthese"]}
salameche = {"Nom" : "Salamèche", "PV" : 60, "Attaque" : ["Griffe", "Flammeche", "Crocs Feu"]}
araqua = {"Nom" : "Araqua", "PV" : 60, "Attaque" : ["Pistolet à Eau", "Coup de Boule", "Détrempage"]}
triopikeur = {"Nom" : "Triopikeur", "PV" : 73, "Attaque" : ["Jet de Sable", "Tranche Nuit", "Rugissement"]}
electrode = {"Nom" : "Electrode", "PV" : 80, "Attaque" : ["Charge", "Eclair", "Roulade"]}

#CARACTERISTIQUES DE PIKACHU

def attaque_eclair():
    attack = 14 + random.randint(0, 7)
    return attack
def morsure_electrique():
    attack = 5 + random.randint(0,2)
    return attack
def queue_de_foudre():
    attack = 3 + random.randint(0,2)
    return attack

#CARACTERISTIQUES DE BULBIZAR

def fouet_lianes():
    attack = 10 + random.randint(0, 8)
    return attack

def canon_graines():
    attack = 14 + random.randint( 0, 3)
    return attack

def synthese():
    attack = bulbizar["PV"]/3
    return attack
#CARACTERISTIQUES SALAMECHE
def griffe():
    attack = 17 + random.randint( 0, 1)
    return attack
def flammeche():
    attack = 16 + random.randint( 0, 2)
    return attack
def crocs_feu():
    chance = random.randint(1, 7)
    attack = 5
    if chance == 1:
        attack = 45
    return attack
#CARACTERISTIQUES D'ARAQUA
def pistolet_a_eau():
    attack = votre_pokemon["PV"]/8
    return attack
def coup_de_boule():
    attack = 20 + random.randint(0,2)
    return attack
def detrempage():
    attack = araqua["PV"]/5
    return attack
#CARACTERISTIQUES TRIOPIKEUR
def jet_de_sable():
    attack = 12 + random.randint( 0, 2)
    return attack
def tranche_nuit():
    chance = random.randint( 1, 4)
    attack = 10
    if chance==4:
        attack = 28
    return attack
def rugissement():
    attack = 10
    return attack
#CARACTERISTIQUES ELECTRODE
def charge():
    attack = 15 + random.randint(0, 4)
    return attack
def eclair():
    attack = 14 + random.randint(0, 5)
    return attack
def roulade():
    attack = 3 + random.randint(0, 2)
    return attack
#COMBAT

choix = input("Alors, quel pokémon choisissez-vous pour ce combat ? (Entrez le numéro) : 1 : Pikachu ; 2 : Bulbizar ; 3 : Salamèche \n")
while choix != "1" and choix != "2" and choix != "3":
    choix = input("Veuillez entrer le NUMERO du pokémon correspondant : \n1 : Pikachu ; 2 : Bulbizar ; 3 : Salamèche : ")
time.sleep(2)

if choix == "1" :
    print("Très bon choix ! Les éclairs de Pikachu sont redoutables dans l'arène...")
    votre_pokemon = pikachu
    attaque_1 = attaque_eclair()
    attaque_2 = morsure_electrique()
    attaque_3 = queue_de_foudre()
if choix == "2" :
    print("Intéressant... Les racines de Bulbizar auront très certainement raison de son adversaire !")
    votre_pokemon = bulbizar
    attaque_1 = fouet_lianes()
    attaque_2 = canon_graines()
    attaque_3 = synthese()
if choix == "3":
    print("Le feu, quelle belle manière d'envoyer son adversaire en enfer !")
    votre_pokemon = salameche
    attaque_1 = griffe()
    attaque_2 = flammeche()
    attaque_3 = crocs_feu()


vos_attaques_liste = votre_pokemon["Attaque"]
pv_max = votre_pokemon["PV"]
time.sleep(2)
choix_ad = random.randint(1, 3)

if choix_ad == 1:
    pokemon_adversaire = araqua
    attaque_ad_1 = pistolet_a_eau()
    attaque_ad_2 = coup_de_boule()
    attaque_ad_3 = detrempage()
    print("En parlant de votre adversaire, il a choisi Araqua.")
if choix_ad == 2:
    pokemon_adversaire = triopikeur
    attaque_ad_1 = jet_de_sable()
    attaque_ad_2 = tranche_nuit()
    attaque_ad_3 = rugissement()
    print("En parlant de votre adversaire, il a choisi Triopikeur.")
if choix_ad == 3:
    pokemon_adversaire = electrode
    attaque_ad_1 = charge()
    attaque_ad_2 = eclair()
    attaque_ad_3 = roulade()
    print("En parlant de votre adversaire, il a choisi Electrode.")

time.sleep(2)
pv_max_ad = pokemon_adversaire["PV"]
liste_attaques_ad = [attaque_ad_1, attaque_ad_2, attaque_ad_3]
print("Tiens ! Le voilà déjà dans l'arène ! Que le combat... COMMENCE !!!")
time.sleep(2)

print("DEBUT DU COMBAT")

time.sleep(2)
tour = 1
while votre_pokemon["PV"] >=0 and araqua["PV"] >=0:
    print(tour, "e tour :")

     #VOTRE TOUR

    attaque = input("Quelle attaque souhaitez-vous lancer ? (Entrez le numéro) : 1 : " + vos_attaques_liste[0] + ", 2 :" + vos_attaques_liste[1] + ", 3 : " +
                    vos_attaques_liste[2] + "\n")
    while attaque != "1" and attaque != "2" and attaque != "3":
        attaque = input("Veuillez entrer le NUMERO de l'attaque correspondante : \n1 : " + vos_attaques_liste[0] + " ; 2 : " + vos_attaques_liste[1] + " ; 3 : " + vos_attaques_liste[2])

    if attaque == "1" :
        degats_infliges = attaque_1
        pokemon_adversaire["PV"] = pokemon_adversaire["PV"] - degats_infliges
        if pokemon_adversaire["PV"]<0:
            pokemon_adversaire["PV"]=0
        print("Vous avez infligé", degats_infliges, "points de dégâts à", pokemon_adversaire["Nom"], ". Il lui reste", pokemon_adversaire["PV"],
              "pv.")
    elif attaque == "2":
        degats_infliges = attaque_2
        pokemon_adversaire["PV"] = pokemon_adversaire["PV"] - degats_infliges
        if pokemon_adversaire["PV"] < 0:
            pokemon_adversaire["PV"] = 0
        print("Vous avez infligé", degats_infliges, "points de dégâts à", pokemon_adversaire["Nom"], ". Il lui reste", pokemon_adversaire["PV"],
              "pv.")
    elif attaque == "3":
        heal = attaque_3
        healed = pv_max - votre_pokemon["PV"]
        votre_pokemon["PV"]= votre_pokemon["PV"] + heal
        if votre_pokemon["PV"]>pv_max:
            votre_pokemon["PV"] = pv_max
            print("Vous vous êtes soignés de ", healed ," pv. Il vous reste " , votre_pokemon["PV"] , " pv.")
        else :
            print("Vous vous êtes soignés de " , heal , " pv. Il vous reste " , votre_pokemon["PV"] ," pv.")
    if pokemon_adversaire["PV"]<=0 :
        print("FIN DU COMBAT")
        break
    time.sleep(1)

    #TOUR DE L'ADVERSAIRE

    attaque_ad = secrets.choice(liste_attaques_ad)

    if attaque_ad == attaque_ad_1:
        degats_infliges = attaque_ad_1
        votre_pokemon["PV"] = votre_pokemon["PV"] - degats_infliges
        if votre_pokemon["PV"]<0:
            votre_pokemon["PV"]=0
        print(pokemon_adversaire["Nom"], "vous a infligé", degats_infliges, "points de dégâts. Il vous reste", votre_pokemon["PV"], "pv.")
    if attaque_ad == attaque_ad_2:
        degats_infliges = attaque_ad_2
        votre_pokemon["PV"] = votre_pokemon["PV"] - degats_infliges
        if votre_pokemon["PV"]<0:
            votre_pokemon["PV"]=0
        print(pokemon_adversaire["Nom"], "vous a infligé", degats_infliges, "points de dégâts. Il vous reste", votre_pokemon["PV"], "pv.")
    if attaque_ad == attaque_ad_3:
        heal = attaque_ad_2
        healed = pv_max_ad - pokemon_adversaire["PV"]
        pokemon_adversaire["PV"] = pokemon_adversaire["PV"] + heal
        if pokemon_adversaire["PV"]> pv_max_ad:
            pokemon_adversaire["PV"]=pv_max_ad
            print(pokemon_adversaire["Nom"]+" s'est soigné de " , healed  , " pv. Il lui reste " , pokemon_adversaire["PV"] , " pv.")
        else :
            print(pokemon_adversaire["Nom"] +" s'est soigné de " , heal , " pv. Il lui reste " , pokemon_adversaire["PV"] , " pv.")


    if votre_pokemon["PV"] <= 0:
        print("FIN DU COMBAT")
        break
    time.sleep(1)

    tour += 1.
    print("fin du tour")
    time.sleep(1)
if votre_pokemon["PV"]<=0:
    print("Vous avez été vaincu.")
    time.sleep(2)
    print("Argh...!! Votre pokémon a été battu, vous êtes vaincu " + votre_nom +"... Retournez vous entraîner et revenez l'année prochaine ! Rien n'est perdu encore.")
else :
    print("Vous avez vaincu !")
    time.sleep(2)
    print("Bien joué " + votre_nom + " !! Vous avez remporté votre premier combat dans l'arène !! Et quel combat ce fut !")
    time.sleep(1)