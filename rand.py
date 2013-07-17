import math
import random
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
    polarity = random.choice([0,1]) 
    
    if polarity == 1: # 1 = pos
        pos_as_pos += 1
    else:
        pos_as_neg += 1

print "Threshold: %s" % threshold
print "%s pos correct. %s incorrect as neg. %s unknown" % (pos_as_pos, pos_as_neg, below_thrs)
        
neg = open('rt-polaritydata/rt-polarity.500.neg')

for sent in neg:
    total_neg += 1
    polarity = random.choice([0,1]) 
    
    if polarity == 1: # 1 = pos
        neg_as_pos += 1
    else:
        neg_as_neg += 1
    
print "%s neg correct. %s incorrect as pos. %s unknown" % (neg_as_neg, neg_as_pos, below_thrs)

precision = float(pos_as_pos) / float(pos_as_pos+neg_as_pos)
recall = float(pos_as_pos) / float(total_pos)
f1 = precision * recall * 2.0 / (precision + recall)
accuracy = float(pos_as_pos + neg_as_neg) / float(total_pos + total_neg)

print "Precision (pos): %s" % precision
print "Recall (pos): %s" % recall
print "F1 (pos): %s" % f1
print "Accuracy (total): %s" % accuracy

