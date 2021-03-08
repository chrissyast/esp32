import time

dot_length = 0.2

def dot(led):
    print("dot")
    led.value(1)  # Set led turn on
    time.sleep(dot_length)
    led.value(0)

def dash(led):
    print("dash")
    led.value(1)  # Set led turn on
    time.sleep(dot_length * 3)
    led.value(0)

def translate_to_morse_code(string, led):
    for character in string:
        print(character)
        morse_functions_for_letter = morse_code[character.lower()]
        for function in morse_functions_for_letter:
            if isinstance (function, list):
                print("space")
                function[0](function[1])
            else:
                function(led)
                time.sleep(dot_length)
        time.sleep(dot_length * 2)


morse_code = {
    "a": [dot, dash],
    "b": [dash, dot, dot, dot],
    "c": [dash, dot, dash, dot],
    "d": [dash, dot, dot],
    "e": [dot],
    "f": [dot, dot, dash, dot],
    "g": [dash, dash, dot],
    "h": [dot, dot, dot, dot],
    "i": [dot, dot],
    "j": [dot, dash, dash, dash],
    "k": [dash, dot, dash],
    "l": [dot, dash, dot, dot],
    "m": [dash, dash],
    "n": [dash, dot],
    "o": [dash, dash, dash],
    "p": [dot, dash, dash, dot],
    "q": [dash, dash, dot, dash],
    "r": [dot, dash, dot],
    "s": [dot, dot, dot],
    "t": [dash],
    "u": [dot, dot, dash],
    "v": [dot, dot, dot, dash],
    "w": [dot, dash, dash],
    "x": [dash, dot, dot, dash],
    "y": [dash, dot, dash, dash],
    "z": [dash, dash, dot, dot],
    " ": [[time.sleep, 1.2]]
}