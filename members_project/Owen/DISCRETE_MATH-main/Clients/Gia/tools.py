import os  # Import the os module for interacting with the operating system
import time  # Import the time module for delays

# This variable sets the default delay for the typewriter effect
_delay = 0.01

# Define a class called TOOLS to group related functions together
class TOOLS:
    @staticmethod
    def simulate_sleep(delay: int, message):
        # This function waits for 'delay' seconds, then prints a message
        print("simulating delay...")
        time.sleep(delay)  # Pause the program for 'delay' seconds
        print(message)

    @staticmethod
    def sleep(delay: int):
        # This function just pauses the program for 'delay' seconds
        time.sleep(delay)

    @staticmethod
    def clear_screen():
        # This function clears the terminal screen
        os.system("clear")

    def set_delay(self, delay: float):
        # This function sets a new delay value for the typewriter effect
        if isinstance(delay, (int, float)):
            global _delay  # Use the global _delay variable
            _delay = delay
            self._delay = _delay  # Also set it as an attribute of the object
        else:
            raise TypeError("Delay must be a number (int or float).")

    @staticmethod
    def print_type(text, color=None, delay=_delay):
        # This function prints text one letter at a time, like a typewriter
        # It can also color the text if a color is given
        if color == "red":
            text = f"\033[91m{text}\033[0m"
        elif color == "green":
            text = f"\033[92m{text}\033[0m"
        elif color == "yellow":
            text = f"\033[93m{text}\033[0m"
        elif color == "blue":
            text = f"\033[94m{text}\033[0m"
        elif color == "magenta":
            text = f"\033[95m{text}\033[0m"
        elif color == "cyan":
            text = f"\033[96m{text}\033[0m"
        # Print each letter with a delay
        for letter in text:
            print(letter, end='', flush=True)
            time.sleep(delay)
        print()  # Print a newline at the end

    @staticmethod
    def input_type(prompt="", color=None):
        # This function prints a prompt like a typewriter and gets user input
        if color == "red":
            prompt = f"\033[91m{prompt}\033[0m"
        elif color == "green":
            prompt = f"\033[92m{prompt}\033[0m"
        elif color == "yellow":
            prompt = f"\033[93m{prompt}\033[0m"
        elif color == "blue":
            prompt = f"\033[94m{prompt}\033[0m"
        elif color == "magenta":
            prompt = f"\033[95m{prompt}\033[0m"
        elif color == "cyan":
            prompt = f"\033[96m{prompt}\033[0m"
        # Print each letter of the prompt with a delay
        delay = _delay
        for letter in prompt:
            print(letter, end='', flush=True)
            time.sleep(delay)
        # Get input from the user
        return input()