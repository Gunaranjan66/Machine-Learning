import random
import math
from sklearn import datasets
from sklearn.model_selection import train_test_split
class KnnClassifier():
    def fit(self,x_train,y_train):
        self.x_train=x_train
        self.y_train=y_train
    def predict(self,x_test):
        predict=[]
        for row in x_test:
            label=self.closest(row)
            predict.append(label)
        return predict
    def euc(self,a,b):
        su=0
        for i,j in zip(a,b):
            su+=(i-j)*(i-j)
        return math.sqrt(su)
    def closest(self,row):
        dist_cost=self.euc(row,self.x_train[0])
        dist_index=0 
        for i in range(1,len(self.x_train)):
            dist=self.euc(row,self.x_train[i])
            if dist<dist_cost:
                dist_cost=dist
                dist_index=i
        return self.y_train[dist_index]
    def accuracy_score(self,y,ydef):
        equal=y==ydef
        return sum(equal)/len(equal)
def main():
    iris=datasets.load_iris()
    x=iris.data
    y=iris.target
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.3)
    classifier=KnnClassifier()
    classifier.fit(x_train,y_train)
    label=classifier.predict(x_test)
    print(classifier.accuracy_score(y_test,label))
main()
    
    
            
            
        
