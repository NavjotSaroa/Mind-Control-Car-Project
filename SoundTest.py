"""
Author: Navjot Saroa

I did not HAVE to create a new file for this but thought it would be nice to keep it separate in case anyone ever 
wanted to make their own dataset. As the name suggests, this one will just test if the KNN model works the way I think it does 
because that means I can decompose waves into their individual frequencies and use that to my advantage in the mind control car project.

Basically just want to see if the way I am going about it is going to give any respectable results. It should but still worth trying.
"""


from SoundWave import collectaudio
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd

df = pd.read_excel("notes.xlsx")

notes = df["note"]

df = df.drop(columns = ["note"])


trainingDict = {}
testingDict = {}

n = int(0.7 * len(df.columns)) # 70% of dataset will be used for training

for i in df.columns:
    trainingDict[i] = df[i][:n]
    testingDict[i] = df[i][n:]

trainingData = list(zip(*trainingDict.values()))
testingData = list(zip(*testingDict.values())) # I still kept this around so that you can test with a pre made data set if you want

trainNote = notes[:n]
testNote = notes[n:]

knn = KNeighborsClassifier(n_neighbors = 10)
knn.fit(trainingData, trainNote)


# Here is the model in action with a whopping 50% accuracy.

input("Press enter to record audio")

newPoint = collectaudio()[1][10:71] # I couldn't be bothered to tinker with SoundWave.py so this is a quicker workaround

predictions = knn.predict([newPoint])

print(chr(predictions[0]))