# Hand gesture mouse controller
A Python-based system to control mouse movements and perform click actions using hand gestures, powered by MediaPipe, OpenCV, and PyAutoGUI.

# 🚀 Features

- Move the mouse cursor using index finger
- Left click, Right Click and Double Click using **custom gestures**
- Take screenshots using gestures
- Real-time feedback overlay by OpenCV

# 📦 Requirements

- Python 3.7+
- OpenCV
- MediaPipe
- PyAutoGUI
- NumPy
- pynput

  Install/Download Dependencies using command
  <code> pip install opencv-python mediapipe pyautogui numpy pynput </code>

# 🛠️ Usage
Run the application using <code> main.py </code>
Press <code> Q </code> from the keybaord to close the application

# ✋ Gesture Mapping

| Gesture                    | Action       |
| -------------------------- | ------------ |
| Index finger moves         | Move mouse   |
| Index bent, thumb apart    | Left click   |
| Middle bent, thumb apart   | Right click  |
| Both index and middle bent | Double click |
| Both bent, thumb close     | Screenshot   |

# 🧠 How It Works
- MediaPipe detects hand landmarks (21 keypoints).
- Gestures are recognized based on angles between fingers and distances.
- Actions like mouse clicks or screenshots are triggered using <code> pyautogui </code> and <code> pynput </code>

# 🧪 Future Improvements
- Add multi-hand support.
- Add gesture customization via GUI.
- Add sound or haptic feedback for events.
