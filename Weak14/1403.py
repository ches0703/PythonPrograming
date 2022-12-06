import pyaudio
import numpy as np
from tkinter import *
lower_cases = \
    [262, 196, 165, 330, 659, 349, 392, 440, 1046, 494,
     # a(C4), b, c, d, e, f, g, h, i, j,
     523, -1, 247, 220, -1, -1, 523, 698, 294, 784,
     # k, l, m, n, o, p, q(C5), r, s, t,
     988, 175, 587, 147, 880, 131]
# u, v, w, x, y, z (C3)
upper_cases = \
    [2093, 1568, 1318, 2637, 5274, 2794, 3136, 3520, -1, 3951,
     # A(C7), B, C, D, E, F, G, H, I, J,
     4186, -1, 1975, 1760, -1, -1, 4186, 5587, 2349, 6272,
     # K, L, M, N, O, P, Q(C8), R, S, T,
     7902, 1397, 4969, 1175, 7040, 1046]
# U, V, W, X, Y, Z(C6)


def pyaudio_init():
    global pa, stream
    pa = pyaudio.PyAudio()
    stream = pa.open(format=pyaudio.paFloat32,
                     channels=1, rate=48000, output=True)


def pyaudio_play(freq, duration, volume):
    global pa, stream
    rate = 48000
    sample = (np.sin(2 * np.pi *
                     np.arange(rate * duration) * freq / rate)).astype(np.float32)
    stream.write(volume * sample)


def pyaudio_close():
    global pa, stream
    stream.stop_stream()
    stream.close()
    pa.terminate()


def keyEvent(event):
    # key = event.keycode
    if len(event.char) == 0:
        return
    key = ord(event.char)
    if (ord('a') <= key <= ord('z')):
        freq = lower_cases[key - ord('a')]
    elif (ord('A') <= key <= ord('Z')):
        freq = upper_cases[key - ord('A')]
    else:  # undefined key
        return
    # print("Keyboard_Event, Pressed Key : {0}, freq {1}".format(chr(key), freq))
    if freq > 40:
        print("keyChar({}), freq({})".format(chr(key), freq), end=" ")
        pyaudio_play(freq, 1, 0.5)
# main loop


def main():
    pyaudio_init()
    window = Tk()
    window.bind("<Key>", keyEvent)
    window.mainloop()
    pyaudio_close()


if __name__ == "__main__":
    main()
