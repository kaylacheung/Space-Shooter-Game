**Space Shooter Game**  

**Description**  
A fast-paced **2D space shooter game** built with **Python** and **Pygame**, where the player controls a spaceship to battle waves of enemies, including aliens, asteroids, and powerful bosses. The game features:  
- **4 progressively difficult levels**  
- **Increasing enemy waves and boss fights**  
- **Smooth controls (arrow keys + spacebar shooting)**  
- **Dynamic scrolling background**  
- **Score tracking & lives system**  
- **Level transitions & a victory screen**  

**Game Features**  
✔ **Player Spaceship** – Move with arrow keys and shoot projectiles (spacebar/ up arrow key) 
✔ **Enemy Waves** – Fight aliens and asteroids that spawn in increasing numbers
✔ **Boss Battles** – Defeat powerful bosses at the end of each level
✔ **Health & Lives System** – Lose lives on enemy collisions; game over at 0 lives  
✔ **Scoring System** – Earn points by defeating enemies 
✔ **Level Progression** – Clear waves to advance through 4 challenging levels
✔ **Visual Effects** – Smooth animations, scrolling backgrounds, and UI elements

**How to Play**  
1. **Run `game.py`** to start the game
2. **Main Menu** – Click Enter key to begin
3. **Controls:**  
   - **← / →** – Move spaceship leftt right  
   - **Spacebar** – Shoot projectiles  
4. **Objective:**  
   - Survive enemy waves and defeat bosses
   - Progress through all 4 levels to win

**Game Structure**  
The project follows **OOP principles** with modular classes:  
- **`Spaceship`** – Player-controlled ships
- **`Alien` & `Asteroid`** – Basic enemies
- **`Boss`** – Stronger enemies with special attacks
- **`Projectile` & `Blood`** – Player bullets & boss attacks 
- **`GameScreen`, `GameOverScreen`, `LevelTransitionScreen`, `CongratulationsScreen`** – Handles UI
- **`ScrollingBackground`** – Dynamic parallax effect

**Installation & Requirements**  
 **Dependencies**  
- Python 3.x  
- Pygame (`pip install pygame`)  

 **Running the Game**  
```sh
python game.py
```

 **Development Notes**  
- Built with **Python** and **Pygame** for 2D rendering
- Follows **OOP principles** (inheritance, encapsulation, polymorphism)
- Designed for **educational purposes** (demonstrates game development & OOP)

**Potential Future Improvements**  
- **Power-ups** (e.g., health boosts, rapid fire) 
- **More enemy types & attack patterns**  
- **Sound effects & background music**
- **High score system**

