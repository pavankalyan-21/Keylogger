
# Keylogger Program

## Overview

This Python-based keylogger is a tool designed for logging keyboard inputs. It features a graphical user interface (GUI) built with Tkinter, providing an easy way to start and stop the keylogging process. The program saves the captured keystrokes in both text and JSON formats for further analysis.

**Note**: This tool is intended for ethical and educational purposes. Ensure you have explicit permission to use it in any environment.

---

## Features

1. **Keyboard Input Logging**:
   - Captures keypress, hold, and release events.
   - Stores logs in a human-readable text file (`key_log.txt`).
   - Generates a structured log in JSON format (`key_log.json`).

2. **Graphical User Interface (GUI)**:
   - Start and stop the keylogger with ease.
   - Displays status updates in real-time.

3. **File Output**:
   - Keystrokes are stored in:
     - `key_log.txt`: Plain text log.
     - `key_log.json`: JSON-formatted log.

---

## Requirements

### Dependencies:
- Python 3.x
- [Pynput](https://pypi.org/project/pynput/) library (`pip install pynput`)

---

## Installation

1. Clone or download the repository.
2. Install the required library:
   ```bash
   pip install pynput
   ```

---

## Usage

1. Run the script:
   ```bash
   python keylogger.py
   ```

2. Use the GUI:
   - Click **Start** to begin logging keys.
   - Click **Stop** to stop logging.

3. Logs will be saved automatically in the program's directory as:
   - `key_log.txt`
   - `key_log.json`

---

## Code Highlights

- **Real-time Key Logging**:
  - The program captures and logs key events (pressed, held, released) using the Pynput library.

- **GUI for Accessibility**:
  - Built with Tkinter, the GUI enables easy operation with status messages.

- **Output Files**:
  - Textual representation in `key_log.txt`.
  - JSON-formatted log for structured data in `key_log.json`.

---

## Ethical Use

This program is a demonstration tool meant for:
- Educational purposes.
- Ethical hacking under legal compliance.

**Misuse of this tool for malicious activities is strictly prohibited. Always obtain consent before using it.**

---

## Disclaimer

The author is not responsible for any misuse or illegal activity arising from this program. Use it responsibly and ethically.

---
