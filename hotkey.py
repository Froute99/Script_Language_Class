import keyboard
import winsound

def play_start_sound():
    winsound.Beep(440, 200)
    winsound.Beep(440, 200)

def play_end_sound():
    winsound.Beep(440, 200)
    winsound.Beep(440, 200)
    winsound.Beep(440, 200)

def report():
    winsound.Beep(400, 500)
    keyboard.write('shift+window+w is pressed')

keyboard.add_hotkey('shift+windows+w', report)
play_start_sound()
keyboard.wait('esc')
play_end_sound()
keyboard.remove_all_hotkeys()