class ValueTree:
    def __init__(self, v):
        self.value = v
        self.actions = []
        self.etat = None

    def set_action(self, index, v):
        self.actions[index].value = v

    def set_etat(self, etat):
        self.etat = etat

    def get_action(self, index):
        return self.actions[index]

    def allocate(self, n):
        for _ in range(n):
            self.actions.append(ValueTree(0))

    def __repr__(self):
        return f"{self.etat} => {self.value}"