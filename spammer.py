from pynput.keyboard import Key, Controller
import time
time.sleep(5)
Keyboard = Controller()
while True:
      for letter in "take it ec uyir":
            Keyboard.press(letter)
            Keyboard.release(letter)
      Keyboard.press(Key.enter)
      Keyboard.release(Key.enter)