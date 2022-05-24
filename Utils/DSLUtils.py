# worldKeys = {
#   ".": floorTile,
#   "#": wallTile,
#   "$": floorWithGold,
# }


worldKeys = {
  ".": None,
  "#": None,
  "$": None,
  "?": None,
  "!": None,
}

def decodeWorld(DSL):
  worldList = []
  worldRows = [row for row in DSL.splitlines() if row]
  for i, row in enumerate(worldRows):
    for j, col in [char for char in row]:
      worldKeys[col]()