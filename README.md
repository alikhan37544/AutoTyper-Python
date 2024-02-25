# AutoTyper

AutoTyper is an innovative Python script that utilizes `pyautogui` to simulate keyboard typing automatically. It reads text from a specified file and types it out in real-time on any active text input field. This utility is especially useful for typing out lengthy text on websites or applications that restrict the paste functionality, ensuring data entry tasks are more efficient and less tedious.

## Key Features

- **Customizable Initial Delay**: Configurable delay to switch to the target text input field before typing begins.
- **Typing Speed Control**: Ability to adjust the typing speed by setting the interval between keystrokes.
- **Versatile Use Cases**: Ideal for demonstrations, automated testing, or data entry on restrictive platforms.

## Getting Started

### Prerequisites

- Python 3.x installed on your system.
- `pyautogui` library for simulating keyboard typing.
- `tqdm` library for optional progress bar visualization (not used in the basic script but can be enabled for extended functionality).

### Installation

1. Clone this repository to get started:

```bash
git clone https://github.com/alikhan37544/AutoTyper-Python.git
```

2. Install the required libraries:

```bash
pip install pyautogui tqdm
```

### Preparing Your Text File

1. Create a text file (`typedstuff.txt`) and fill it with the content you want to be typed out. This could range from a simple sentence to a comprehensive document.

2. Place `typedstuff.txt` in the same directory as the `autotyper.py` script, or provide the full path to the file within the script.

### Configuring the Script

Open `autotyper.py` in a text editor to adjust the settings:

- **`delay`**: Set how many seconds the script waits before it starts typing. This gives you time to focus the desired text input field.
- **`name`**: Path to your text file. Use `typedstuff.txt` for simplicity, or replace it with the path to your file.
- **`interval`**: Controls the delay between keystrokes, allowing you to speed up or slow down the typing.

### Running AutoTyper

Execute the script with Python:

```bash
python autotyper.py
```

After the specified `delay`, the script will start typing the content of `typedstuff.txt` into the currently active text field.

## Use Cases

- **Filling Out Online Forms**: Automatically type information into forms on websites that disable paste functionality.
- **Testing**: Simulate real user input for testing software or websites that require text input.
- **Presentations and Demonstrations**: Show how data entry works in real-time without manual typing.
- **Bypassing Restrictions**: Useful for entering information on platforms that restrict copy-pasting for security reasons.

## Customization and Tips

- Increase the `delay` if you need more time to navigate to the target text input area.
- Adjust the `interval` to find a balance between typing speed and application responsiveness. Some applications may not register very fast keystrokes correctly.
- Ensure the text file does not contain more characters than the target application's input field can handle.

## Contributing

We welcome contributions! If you have ideas for new features, improvements, or bug fixes, feel free to fork the repository, implement your changes, and submit a pull request.

## License

This project is licensed under the MIT License. For more information, see the `LICENSE` file.
