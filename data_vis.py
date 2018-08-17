'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt

plt.hist(polarity, bins=[-3.5, -3, -2.5, -2, -1.5])
plt.xlabel('Values')
plt.ylabel('Number of Items')
plt.title('Histogram of Numbers')
plt.axis([-1, 2, 0, 40])
plt.grid(True)
plt.show()


#Get the JSON data
tweetFile = open("tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# Continue your program below!
polarity = []
subjectivity = []
for tweets in tweetData:
    value = TextBlob(tweets["text"])
    value = value.sentiment
    subjectivity.append(value)
    polarity.append(value)
print(subjectivity)
print(polarity)



# Textblob sample:
tb = TextBlob("You are a brilliant computer scientist.")
print(tb.polarity)




plt.hist(polarity, bins=[-3.5, -3, -2.5, -2, -1.5])
plt.xlabel('Values')
plt.ylabel('Number of Items')
plt.title('Histogram of Numbers')
plt.axis([-1, 2, 0, 40])
plt.grid(True)
plt.show()
