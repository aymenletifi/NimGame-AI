from Etat import Etat
import Utils
from ValueTree import ValueTree

n = input("Donnez N: ")
v = None

while v == None:
    algo = input("Donnez l'algorithme à simuler ((m)inimax, (a)lphabeta): ")
    if algo == "alphabeta" or algo == "a":
        v = Utils.alphabeta(Etat([int(n)]))
    elif algo == "minimax" or algo == "m":
        v = Utils.minimax(Etat([int(n)]))

count = Utils.count

while True:
    if (v.etat.is_final()):
        print("Le joueur gagne.")
        break

    i = 1
    etats = v.etat.get_next_actions()
    for etat in etats:
        print(f"{i}. {etat}")
        i = i + 1

    choix = input("Choisissez une action: ")
    player_action = v.actions[int(choix) - 1]

    if ((algo == "alphabeta" or algo == "a") and player_action.etat == None):
        player_action = Utils.alphabeta(Etat(etats[int(choix) - 1]))
        count = count + Utils.count

    if (len(player_action.actions) == 0):
        print("Le joueur gagne.")
        break

    machine_action = player_action.actions[0]
    
    for action in player_action.actions:
        if action.value == 0:
            machine_action = action
            break

    print(f"La machine joue {machine_action.etat}")
    v = machine_action

    if (v.etat.is_final()):
        print("La machine gagne.")
        break

# count est le nombre des noeuds visités