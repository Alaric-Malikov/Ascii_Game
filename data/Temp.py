class worldTile:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.passable = False
    
class Floor(worldTile):
  def __init__(self, x, y):
    self.onGround = []
    self.char = "."
    self.passable = True

  def dropped(self, item):
    self.onGround.append(item)


class Wall(worldTile):
  def __init__(self, x, y):
    self.char = "#"


