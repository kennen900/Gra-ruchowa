# Movement Game

Movement Game is an interactive motion-based game built with Python that uses real-time hand tracking through a webcam. The player controls the game using their index finger and earns points by touching a dolphin displayed on the screen.

The application uses computer vision and hand landmark detection to track the player's hand and detect collisions between the index finger and the target object.

---

## Features

- Real-time hand tracking using MediaPipe
- Index finger detection for interaction
- Motion-based gameplay controlled with a webcam
- Random target spawning (dolphin)
- Score tracking system
- Countdown game timer
- Visual feedback after successful hit
- Automatic camera detection
- Fullscreen game mode

---

## Technologies

This project was developed using:

- Python `3.11.9`
- MediaPipe `0.10.9`
- OpenCV

---

## Requirements

Before running the project, ensure you have:

- Python `3.11.9`
- A working webcam
- Installed dependencies

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/kennen900/movement-game.git
cd movement-game
```

### 2. (Optional) Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate virtual environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install mediapipe==0.10.9 opencv-python
```

---

## Project Structure

```text
movement-game/
│
├── test.py
├── Delfin.png
├── README.md
└── requirements.txt
```

---

## Running the Game

Run the following command:

```bash
python test.py
```

After launching:

1. The application detects available cameras.
2. Select the camera index from the terminal.
3. The game starts in fullscreen mode.
4. Move your hand in front of the camera.
5. Touch the dolphin using your index finger to gain points.

Press `ESC` to exit the game.

---

## How It Works

The game detects the player's hand using MediaPipe Hands and extracts landmarks from the hand model.

The index fingertip position is retrieved using landmark `8`:

```python
index_tip = hand_landmarks.landmark[8]
```

The program calculates the Euclidean distance between the fingertip and the dolphin position:

```python
distance = ((x - target_x)**2 + (y - target_y)**2)**0.5
```

If the distance falls below the collision threshold, a point is awarded and a new target position is generated.

---

## Gameplay Logic

- The dolphin target appears at a random position on the screen.
- The player has a limited amount of time to score points.
- Every successful hit:
  - increases the score,
  - moves the dolphin to a new location,
  - displays a colored screen border as feedback.

If the target is not hit within several seconds, it respawns automatically.

---

## Dependencies

You can install all dependencies manually:

```bash
pip install mediapipe==0.10.9 opencv-python
```

Or create a `requirements.txt` file:

```txt
mediapipe==0.10.9
opencv-python
```

Then install:

```bash
pip install -r requirements.txt
```

---

## Future Improvements

Potential project extensions:

- Sound effects
- Difficulty levels
- Score leaderboard
- Multiple target objects
- Multiplayer support
- Better UI/UX
- Pose tracking integration

---
