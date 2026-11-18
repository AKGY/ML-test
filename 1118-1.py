#붓꽃 데이터

import pandas as pd
from sklearn import svm, metrics

csv = pd.read_csv("16c-iris.csv")



data = csv[["SepalLength","SepalWidth","PetalLength","PetalWidth"]]
label = csv["Name"]

clf = svm.SVC()
clf.fit(data, label)

result = clf.predict([
    [5.1, 3.0, 1.3, 0.2]
])

print(result)


