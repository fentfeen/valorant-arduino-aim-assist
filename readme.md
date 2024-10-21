# How the Aimbot Works

The aimbot is designed to improve targeting precision in gameplay. When a player is within the designated Field of View (FOV) and clicks the left mouse button, the aimbot quickly adjusts the mouse cursor to align with the target's location.
This swift flicking action helps to focus the player's aim directly on the enemy, enabling accurate targeting before shooting. The aimbot calculates the optimal angle and distance to the target, ensuring a seamless aiming experience. By significantly increasing the likelihood of hitting targets, the aimbot provides players with a substantial advantage in fast-paced gaming scenarios, where split-second decisions can determine the outcome of a match.


## Required Libraries

Before running the script, ensure you have the following Python libraries installed:

- `opencv-python`
- `mss`
- `numpy`
- `pyserial`
- `pywin32`

You can install these libraries by running the following command:

```bash
pip install opencv-python mss numpy pyserial pywin32
```

# How to Use the Aimbot

1. **Setup:**
   - Ensure you have the following hardware:
     - [Arduino Leonardo R3 Main Board](https://www.jaycar.com.au/duinotech-leonardo-r3-main-board/p/XC4430)
     - [USB Host Shield for Arduino](https://www.amazon.com.au/ARCELI-Shield-Arduino-Support-Android/dp/B07J2KKGZ4)

2. **Run the Script:**
   - Save the provided Python script as `KM.py`.
   - Connect your Arduino board and upload the provided Arduino sketch (`snappy.ino`) to your board.
   - Open a terminal or command prompt and run the Python script using:
     ```bash
     python KM.py
     ```

3. **Input FOV and Speed:**
   - When prompted, enter the desired Field of View (FOV) value (in pixels).
   - Enter the speed factor that will determine how fast the mouse cursor adjusts to the target.

4. **Gameplay:**
   - Start the game and position yourself where you can see the enemy.
   - When an enemy enters the specified FOV, click the left mouse button. The aimbot will automatically flick the mouse cursor to the target's location, allowing for precise aim and shooting.
  


# Caution:
   - While this aimbot may go undetected, it is important to play responsibly. Avoid being too blatant in your gameplay style, as manual bans are still a possibility.
