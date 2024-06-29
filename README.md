# Mind-Control-Car-Project

## Introduction

This is a personal project that I am taking on and this file will evolve as it progresses. I am looking to make a car that is controlled by using nothing but brain waves of the user. This will of course require the use of EEG technology.
I intend on it having only 4 functions for starters, turn left, turn right, accelerate, brake/reverse.
The user will achieve these functions by thinking of the movement of a limb. Right leg = accelerate, left foot = brake/reverse, right arm = turn right, left arm = turn left.


## Start of project
Since I am extremely new to machine learning, I am taking baby steps to get to my final goal. For starters, I have recognised the fact that I will be dealing with waves from the eeg machine, and that these waves will be rather noise.
That is because I would prefer not to use an invasive procedure to get these signals on account of the fact that I neither have a medical license, nor am I a crazy scientist in a mansion trying to recreate Frankenstein's monster.
However, the equipment that I might need for this project is immensely expensive, meaning that I need to be REALLY sure it works. For that I am starting off by just working with sound waves. I will create a database that will take single note sounds as input and return a note.
The catch is that I will not directly be relying on the frequency of the note being played because my EEG signals wont have specified frequencies like that, or so I presume.

## SoundWave and SoundTest
These files are the preliminary tests I did to see if my idea holds any water at all. SoundWave.py collects audio from the user's mic and asks the user for the note that was played. This was to make a dataset that the ML model could be trained on.
SoundTest.py takes this database and tests is out. In its current version, the program does not actually use the testing data and directly asks user for an audio input and determines the note played, so it is less of a test and more of an actual implementaiton in a way?

Anyway the idea worked, I can fFt sound waves and use their data to make a ML model that can predict what the audio is doing. I can now move on to the pricier part of the project.
