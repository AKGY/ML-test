import pandas as pd
from sklearn import svm, metrics
import glob, os.path, re, json

#출현 빈도 벡터
#alpha = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

train_files = glob.glob("./lang/18b-lang/train/*")
test_files = glob.glob("./lang/18b-lang/test/*")


for file_name in train_files:
    basename = os.path.basename(file_name)
    print(file_name)
    print("train_file : ",basename)
    print("--------")
for file_name in test_files:
    basename = os.path.basename(file_name)
    print("test_file : ",basename)
    print("--------")


'''
clf = svm.SVC()
clf.fit([alpha],['en'])

results = clf.predict()

score = metrics.accuracy_score(result, )
'''