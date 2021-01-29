from Etat import Etat
from ValueTree import ValueTree

global count
count = 0

def minimax(etat):
    global count

    tree = ValueTree(0)
    count = 0
    max_value(tree, etat)
    return tree

def max_value(tree, etat):
    global count

    tree.set_etat(etat)
    count = count + 1
    if etat.is_final():
        return 0

    u = float("-inf")
    i = 0

    actions = etat.get_next_actions()
    tree.allocate(len(actions))
    for action in actions:
        etat = Etat(action)
        val = min_value(tree.get_action(i),etat )
        tree.set_action(i, val)
        u = max(u, val)
        i = i + 1

    tree.value = u
    return u

def min_value(tree, etat):
    global count
    
    tree.set_etat(etat)
    count = count + 1
    if etat.is_final():
        return 1

    u = float("inf")
    i = 0

    actions = etat.get_next_actions()
    tree.allocate(len(actions))
    for action in actions:
        etat = Etat(action)
        val = max_value(tree.get_action(i), etat)
        tree.set_action(i, val)
        u = min(u, val)
        i = i + 1

    tree.value = u
    return u

def alphabeta(etat):
    global count
    
    tree = ValueTree(0)
    count = 0
    alpha_value(tree, etat, float("-inf"), float("inf"))
    return tree


def alpha_value(tree, etat, alpha, beta):
    global count

    tree.set_etat(etat)
    count = count + 1
    if etat.is_final():
        return 0

    u = float("-inf")
    i = 0

    actions = etat.get_next_actions()
    tree.allocate(len(actions))
    for action in actions:
        etat = Etat(action)
        val = min_value(tree.get_action(i), etat)
        tree.set_action(i, val)
        u = max(u, val)
        i = i + 1

        if u > beta: return u
        alpha = max(u, alpha)

    tree.value = u
    return u


def beta_value(tree, etat, alpha, beta):
    global count

    tree.set_etat(etat)
    count = count + 1
    if etat.is_final():
        return 1

    u = float("inf")
    i = 0

    actions = etat.get_next_actions()
    tree.allocate(len(actions))
    for action in actions:
        etat = Etat(action)
        val = alpha_value(tree.get_action(i), etat, alpha, beta)
        tree.set_action(i, val)
        u = min(u, val)
        i = i + 1

        if u < alpha: return u
        beta = min(u, beta)

    tree.value = u
    return u
