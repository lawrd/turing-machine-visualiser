
# Cellular Automata Visualizers

This repository contains visualizers for two cellular automata: Langton's Ant and Paterson's Worms. Both are implemented using the `pygame` library.

## Dependencies

Both scripts require the `pygame` library. You can install it using:
```
pip install pygame
```


## langtons_ant.py

This script visualizes the behavior of Langton's Ant, a two-dimensional Turing machine with simple rules but complex emergent behavior. The ant moves based on the color of the cell it is currently on.

### How to Run
```
python langtons_ant.py
```

### Controls
- Press `RETURN` (or `ENTER`) to start the movement of the ant.

## patersons_worm.py

This script visualizes the behavior of Paterson's Worms. It's a simple cellular automaton where the worm moves in a random direction unless it encounters a previously visited cell.

### How to Run
```
python patersons_worm.py
```

### Controls
- Press `RETURN` (or `ENTER`) to start the movement of the worm.



