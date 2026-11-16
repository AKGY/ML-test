from sklearn import svm

#clf = svm.SVC()
#clf.fit(data, label)
#clf.predict

#clf.fit([],[])

#XOR
'''
P Q XOR
0 0 0
1 1 0

1 0 1
0 1 1

P,Q 데이터
XOR label
'''
clf = svm.SVC()
clf.fit(
    [
        [0,0],
        [1,1],
        [0,1],
        [1,0],
    ],
    #이 데이터(벡터)가 들어오면
    [0,0,1,1]
    #답은 이렇게 한다
)
#predict로 예측한것
results = clf.predict([
    [0,0], #0
    [1,0]  #1
])
#리스트값으로 [0 1]
print(results)

