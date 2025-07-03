import os
import time

_delay = 0.01  # Default delay for typewriter effect
class TOOLS: 
    @staticmethod
    def simulate_sleep(delay:int, message):
        print("simulating delay...")
        time.sleep(delay)
        print(message)
    def sleep(delay:int):
        time.sleep(delay)
    
    @staticmethod
    def clear_screen():
        os.system("clear")
    
    def set_delay(self, delay:float):
        if isinstance(delay, (int, float)):
            _delay = delay
            self._delay = _delay
        else:
            raise TypeError("Delay must be a number (int or float).")

    @staticmethod
    def print_type(text, color=None, delay = _delay):
        match color:
            case "red":
                text = f"\033[91m{text}\033[0m"
            case "green":
                text = f"\033[92m{text}\033[0m"
            case "yellow":
                text = f"\033[93m{text}\033[0m"
            case "blue":
                text = f"\033[94m{text}\033[0m"
            case "magenta":
                text = f"\033[95m{text}\033[0m"
            case "cyan":
                text = f"\033[96m{text}\033[0m"
            case _:
                pass
        for letter in text:
            print(letter, end='', flush=True)
            # print(delay)
            time.sleep(delay)
        print()  # for newline

    @staticmethod
    def input_type(prompt="", color=None):
        match color:
            case "red":
                prompt = f"\033[91m{prompt}\033[0m"
            case "green":
                prompt = f"\033[92m{prompt}\033[0m"
            case "yellow":
                prompt = f"\033[93m{prompt}\033[0m"
            case "blue":
                prompt = f"\033[94m{prompt}\033[0m"
            case "magenta":
                prompt = f"\033[95m{prompt}\033[0m"
            case "cyan":
                prompt = f"\033[96m{prompt}\033[0m"
            case _:
                pass
        delay = _delay
        for letter in prompt:
            print(letter, end='', flush=True)
            time.sleep(delay)
        return input()