# Platformer

## Overview
Platformer is a 2D platformer game built using Python and Pygame. The game features a player character that navigates through a randomly generated terrain, avoiding obstacles and interacting with various game elements. The objective is to find and reach a special target block while enjoying a visually appealing background and smooth gameplay mechanics.

## Features
- **Dynamic Terrain Generation**: The game creates a unique terrain layout each time you play, ensuring a fresh experience.
- **Player Movement**: The player can move left, right, and jump, with gravity applied for realistic movement.
- **Fire Hazards**: Players must avoid fire traps that can damage them.
- **Target Block**: A special block that the player must reach to win the game.
- **Congratulations Screen**: Upon reaching the target block, players are greeted with a congratulatory message.
- **Camera Scrolling**: The camera follows the player, providing a smooth gameplay experience.

## Installation

### Prerequisites
- Python 3.x
- Pygame (version 2.6.1)

### Steps
1. Clone the repository:
   ```bash
   git clone github.com/LancemDev/platformer-game.git
   cd platformer-game
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Ensure you have the necessary assets in the `assets` directory, including images for the background, player, terrain, and fire traps.

## Usage
To start the game, run the following command:
```bash
python main.py
```

Use the following controls:
- **Left Arrow**: Move left
- **Right Arrow**: Move right
- **Spacebar**: Jump

## Contributing
Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments
- Thanks to the Pygame community for their support and resources.
- Special thanks to the contributors who have helped improve this project.

## Contact
For any inquiries, please reach out to [your-email@example.com].