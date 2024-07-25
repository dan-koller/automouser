# AutoMouser

AutoMouser is a small programm that randomly moves the mouse cursor on the screen. It is intended to prevent the computer from going to sleep, locking the screen, or simulating user activity for other reasons.

## Requirements

-   Python 3.10 or higher
-   Requirements from `requirements.txt`

## Get started

1. Clone the repository

    ```bash
    git clone https://github.com/dan-koller/automouser
    ```

2. Create a virtual environment

    ```bash
    python3 -m venv .venv && source .venv/bin/activate
    ```

    > On Windows, open a command prompt and run .venv\Scripts\activate.bat

3. Install the requirements

    ```bash
    pip3 install -r requirements.txt
    ```

4. Run the script

    ```bash
    python3 automouser.py
    ```

## Usage

The script will start moving the mouse cursor randomly on the screen. To stop the script, move the mouse to the top left corner of the screen or press `Ctrl + C`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
