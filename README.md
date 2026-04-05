Magic Square Game

Objective:
Develop a console-based 2-player game using a 3×3 grid and numbers from 1 to 9.

---

Game Description:

- The game is played on a 3×3 grid
- Two players will take turns
- Players will place numbers from 1 to 9 on the grid

---

Rules:

1. Each player must choose:
   - A position on the grid (1–9)
   - A number (1–9) to place in that position
2. Each number can be used only once throughout the game
3. Each position on the grid can be filled only once
4. Players must alternate turns

---

Winning Condition:

- A player wins if any row, column, or diagonal contains three numbers whose sum is exactly 15

---

Program Requirements:

- Display the board clearly after every move
- Accept user input for position and number
- Implement proper validation:
  - Prevent reuse of numbers
  - Prevent overwriting of filled positions
  - Handle invalid inputs
- After each move, the program must:
  - Check for a winning condition
  - Check for a draw condition

---

Implementation Guidelines:

- The code must be modular and use functions
- Do not write the entire program in a single block

---

Evaluation Criteria:

- Correct implementation of logic
- Input validation
- Code structure and modularity
- Readability
