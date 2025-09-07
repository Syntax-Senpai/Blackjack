# Blackjack Game (Python)

A simple command-line **Blackjack game** built in Python.

## Features
- Implements standard Blackjack rules (hit, stand, dealer must draw until 17).
- Card deck is generated and shuffled dynamically.
- Handles Ace values (1 or 11 depending on hand).
- Interactive gameplay with dealer personality ("Syntax Senpai").
- Option to view game rules before playing.

##  How to Play
1. Clone the repository:
   ```bash
   git clone https://github.com/Syntax-Senpai/Blackjack.git
   ```
2. Navigate into the project folder:
   ```bash
   cd blackjack-game
   ```
3. Run the game:
   ```bash
   python main.py
   ```
4. Choose:
   - **1** → Play the game  
   - **2** → View rules

## Game Rules
1. Goal: Get as close to 21 as possible without going over.
2. Card Values:
   - 2–10 = face value  
   - J, Q, K = 10  
   - Ace = 1 or 11 (whichever benefits the player)
3. Gameplay:
   - Both player and dealer start with 2 cards.
   - Player can choose to **Hit** (draw card) or **Stand** (end turn).
   - If total > 21 → Bust (lose).  
4. Dealer:
   - Dealer reveals hidden card after player finishes.
   - Dealer must hit until reaching at least 17.  
5. Winner:
   - Closest to 21 without busting wins.  
   - Equal scores = Tie.

##  Project Structure
```
.
├── main.py      # Game logic & user interaction
├── cards.py     # Card & Deck classes
└── README.md    # Project documentation
```

##  Future Improvements
- Add support for multiple players
- Betting system with chips
- GUI-based version for better user experience

## Developed by **Syntax Senpai**
