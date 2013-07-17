from reverend.thomas import Bayes

guesser = Bayes()

# train on the full set minus 500 reviews of each type

pos = open('rt-polaritydata/rt-polarity.pos')
for sent in pos:
    guesser.train('pos', sent.rstrip())

neg = open('rt-polaritydata/rt-polarity.neg')
    
for sent in neg:
    guesser.train('neg', sent.rstrip())    

# now we evaluate the 1000 reserved reviews


neg_as_neg = 0
neg_as_pos = 0
pos_as_pos = 0
pos_as_neg = 0
below_thrs = 0
total_pos = 0
total_neg = 0

threshold = 0.0 #

pos = open('rt-polaritydata/rt-polarity.500.pos')

for sent in pos:
    total_pos += 1
    polarity = guesser.guess(sent.rstrip())
    for possible in polarity:
        if possible[0]=='pos':
            cur_pos = possible[1]
        elif possible[0] =='neg':
            cur_neg = possible[1]
    
    if cur_pos - cur_neg > threshold:
        pos_as_pos += 1
    elif cur_neg - cur_pos > threshold:
        pos_as_neg += 1
    else:
        below_thrs += 1

print "Threshold: %s" % threshold
print "%s pos correct. %s incorrect as neg. %s unknown" % (pos_as_pos, pos_as_neg, below_thrs)
        
neg = open('rt-polaritydata/rt-polarity.500.neg')

for sent in neg:
    total_neg += 1
    polarity = guesser.guess(sent.rstrip())
    for possible in polarity:
        if possible[0]=='pos':
            cur_pos = possible[1]
        elif possible[0] =='neg':
            cur_neg = possible[1]
    
    if cur_pos - cur_neg > threshold:
        neg_as_pos += 1
    elif cur_neg - cur_pos > threshold:
        neg_as_neg += 1
    else:
        below_thrs += 1

print "%s neg correct. %s incorrect as pos. %s unknown" % (neg_as_neg, neg_as_pos, below_thrs)

precision = float(pos_as_pos) / float(pos_as_pos+neg_as_pos)
recall = float(pos_as_pos) / float(total_pos)
f1 = precision * recall * 2.0 / (precision + recall)
accuracy = float(pos_as_pos + neg_as_neg) / float(total_pos + total_neg)

print "Precision (pos): %s" % precision
print "Recall (pos): %s" % recall
print "F1 (pos): %s" % f1
print "Accuracy (total): %s" % accuracy

