class Cell:
    def __init__(self, x, y, size, playerid):
        self.x = x
        self.y = y
        self.size = size
        self.playerid = playerid

    def IsTaken(self):
        if self.playerid is not None:
            return True
        else:
            return False

