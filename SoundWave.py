"""
Author: Navjot Saroa
The purpose of this file is to help me create a database, in a quick manner.
The program will wait for a user input of sound. Carry out FFT, return frequencies and their amplitudes.
After that the user will be asked what note was just played, and that data will be stored.

The dataset will also be included in the repo, it is a collection of notes either sung or played on some sort of instrument.
I have mostly kept the sounds to the 3rd octave and the notes are represented by their ASCII values.

Do note that the code is recording frequencies between 0Hz and 600Hz but I have narrowed the dataset down to between 100Hz and 400Hz.
This is to make the dataset a bit smaller and easier to work with, and the 3rd octave only ranges between 130Hz and 260Hz so realistically 
I could make that range narrower but I wanted to make the life of the program a little harder for fun, also because my excel was being weird 
and stored data for frequencies out of that range weirdly...
"""


import pyaudio
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import os


def collectaudio():
    # Parameters for audio stream
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 4096
    CHUNK = 2048
    RECORD_SECONDS = 1

    # Initialize PyAudio
    audio = pyaudio.PyAudio()

    # Open audio stream
    stream = audio.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

    print("Recording...")

    frames = []

    for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Finished recording.")

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Convert recorded data to numpy array
    audio_data = np.frombuffer(b''.join(frames), dtype=np.int16)

    # Perform FFT on the audio data
    fft_data = np.fft.fft(audio_data)
    freq = np.fft.fftfreq(len(fft_data), 1.0 / RATE)

    # Ensure the freq array is a numpy array of floats
    freq = np.array(freq, dtype=np.float64)

    # Only keep the positive frequencies within 50 to 600 Hz
    pos_freq_indices = np.where((freq >= 50) & (freq <= 600))
    pos_fft_data = np.abs(fft_data[pos_freq_indices])
    pos_freq = freq[pos_freq_indices]

    return(pos_freq[::5], pos_fft_data[::5])


def write_to_excel(df, filename):
    if os.path.exists(filename):
        # If file exists, load existing data and append the new data
        existing_df = pd.read_excel(filename, index_col=0)
        df = pd.concat([existing_df, df], ignore_index=True)
    
    # Write the DataFrame to the Excel file
    with pd.ExcelWriter(filename, engine='openpyxl') as writer:
        df.to_excel(writer, index=False)

# Initialise dataframe

if __name__ == "__main__":
    df = pd.DataFrame(columns = list(range(50,605,5)))
    df["note"] = []


    # Start data collection process
    inp = (input("Press enter to start: "))

    while inp == "":
        m = collectaudio()

        note = input("What note was that?: ").lower()
        if len(note) == 1 and ord(note) >= 97 and ord(note) <= 103:
            df.loc[len(df)] = np.append(m[1], np.array([int(ord(note))]))

        else:
            print("Invalid Entry.")

        inp = (input("Press enter to continue, type -1 to exit: "))



    filename = "notes.xlsx"

    write_to_excel(df, filename)

