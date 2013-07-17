#!/bin/bash /Applications/Orange.app/Contents/MacOS/python

import orange, orngTest, orngStat

bayes = orange.BayesLearner(name='naive bayes')
knn = orange.kNNLearner(name='knn')

learners = [bayes, knn]



data = orange.ExampleTable("testdata")
results = orngTest.crossValidation(learners, data, folds=10)

cdt = orngStat.computeCDT(results)


print "Learner   CA   IS   BRIER  AUC"
for i in range(len(learners)):
    print "%-8s %5.3f  %5.3f  %5.3f  %5.3f" % (
         learners[i].name,     
         orngStat.CA(results)[i], 
         orngStat.IS(results)[i], 
         orngStat.BrierScore(results)[i], 
         orngStat.AROCFromCDT(cdt[i])[7]) 
         
