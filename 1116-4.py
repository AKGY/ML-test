from sklearn import svm, metrics

clf = svm.SVC()

datas = [[0, 0], [1, 0], [0, 1], [1, 1]]
labels = [0, 1, 1, 0]

clf.fit(datas, labels)

examples = [[0, 1], [1, 1]]
examples_label = [1 , 0]

results = clf.predict(examples)

print(results)

score = metrics.accuracy_score(examples_label, results)

print("정답률은 : ", score)