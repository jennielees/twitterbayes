from reverend.thomas import Bayes
import twitter

guesser = Bayes()

# train on the full set minus 500 reviews of each type

pos = open('pos_smiles_5k')
for sent in pos:
    guesser.train('pos', sent.rstrip())

neg = open('neg_smiles_5k')
    
for sent in neg:
    guesser.train('neg', sent.rstrip())    

guesser.save('twitter_guesser.bay')

api = twitter.Api()
latest = api.GetPublicTimeline()

threshold = 0.1

for tweet in latest:
    classif = guesser.guess(tweet.text)
    if len(classif) == 2:
        if classif[0][1] - classif[1][1] > threshold:
            print "%s : %s!" % (tweet.text, classif[0][0])
        else:
           print "%s : NOISE" % tweet.text
    else:
        if len(classif) == 1:
            print "%s : %s!" % (tweet.text, classif[0][0])
        else:
           print "%s : NOISE" % tweet.text
