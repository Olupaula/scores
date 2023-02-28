import pandas as pd
import numpy as np
import sklearn as sk
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
#import matplotlib.pyplot as plt


class StudentPerformance:
    def __init__(self):
        # reading data
        data = pd.read_csv("ml_codes/student-mat.csv", sep=";")
        data = data[["G3", "G1", "G2", "Fedu", "Medu", "studytime", "sex"]]
        encoder = LabelEncoder()

        #temp = data['sex']
        data['sex'] = encoder.fit_transform(data['sex'])

        #df = pd.DataFrame([temp, data['sex']])
        #  Note 0 = Female, 1 = Male
        # print(df)

        self.x = np.array(data.drop(labels=["G3"], axis=1))
        self.y = np.array(data["G3"])
        #print(y)

        #print(data)
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(self.x, self.y, test_size=0.1)
        self.model = LinearRegression()
        self.model.fit(self.x_train, self.y_train)
        # pred = model.predict(self.x_test)
        # print(pd.DataFrame(np.round(pred, 2)))

        #joining two dataframes
        #test_x= pd.DataFrame(x_test)
        #test_y = pd.DataFrame(y_test)
        #test= pd.concat([test_x,test_y], axis=1)

        #joining two numpy arrays
        #d1 = pd.DataFrame(y_test)
        #test = np.column_stack((x_test, y_test))
        #print(test)

        #print(len(x_test), len(y_test))

    def predictPerformance(self, x):
        predicted_score = round(float(self.model.predict(x)),2)
        # print("score", pd.DataFrame(np.round(pred, 2)))


        #print('accuracy:\n', asc(x_test, y_test))

        #plt.scatter(data["studytime"], data["G3"])
        #plt.show()
        return {'score': predicted_score, 'accuracy': self.model.score(self.x, self.y)}


student_p1 = StudentPerformance()
given = [[20, 16, 4, 4, 7, 1]]
print(student_p1.predictPerformance(given)['score'])

