import threading
import pyautogui
from datetime import datetime
from time import sleep
from random import randint

# Global flag to indicate if the stop event is triggered
stop_event = threading.Event()


def listen_for_stop_event():
    """Function to continuously monitor mouse position."""
    while not stop_event.is_set():
        width, height = pyautogui.size()
        x, y = pyautogui.position()

        # Check if the mouse is at any of the corners
        if x <= 0 or x >= width - 1 or y <= 0 or y >= height - 1:
            print(f"Stop event detected at {datetime.now()}. Exiting...")
            stop_event.set()  # Signal the main thread to stop

        # Sleep for a short period to avoid excessive CPU usage
        sleep(0.1)


def move_mouse_randomly():
    """Function to randomly move the mouse around the screen."""
    while not stop_event.is_set():
        width, height = pyautogui.size()

        # Avoid corners
        threshold = 100

        x = randint(threshold, width - threshold)
        y = randint(threshold, height - threshold)

        pyautogui.moveTo(x, y, duration=0.5)

        # Print the mouse position for debugging purposes
        print(f"Moved to ({x}, {y}) at {datetime.now()}")

        # Wait before moving again (in seconds)
        time_to_wait = randint(4, 10)
        sleep(time_to_wait)


def main():
    # Create and start the thread for the stop event listener
    stop_thread = threading.Thread(target=listen_for_stop_event, daemon=True)
    stop_thread.start()

    move_mouse_randomly()

    stop_thread.join()


if __name__ == '__main__':
    main()
