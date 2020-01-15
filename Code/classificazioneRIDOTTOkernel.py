import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pandas as pd
import numpy as np
import sys as s
import matplotlib.pyplot as plt
from matplotlib import colors as colo
import pylab as pl
import seaborn as sn
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.pipeline import  Pipeline
from sklearn.metrics import r2_score
from sklearn.svm import SVC

dfn = pd.read_excel(r'C:\Users\annit\Desktop\18luglio\ridottoCLASSfinoaventi.xlsx')

dfn.set_axis(['cum2gg', 'max2gg', 'etichetta'], axis='columns', inplace=True)
#plot cumulate con correlazione più alta
X = dfn[['cum2gg', 'max2gg']]
y = dfn['etichetta']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)

# Fitting Classifier to the Training set

classifie = SVC(kernel='rbf', gamma=0.010, C=100)
#svclassifier = SVC(gamma='auto')
classifie.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifie.predict(X_test)
#print(y_pred)
print("confusion matrix e performance del test")
print(confusion_matrix(y_test, y_pred))
target_names = ['non frane', 'frane']
print(classification_report(y_test, y_pred, target_names=target_names))

#confusion of training
print("confusion matrix e performance del training")
predtrain = classifie.predict(X_train)
conftrain = confusion_matrix(y_train, predtrain)
print(conftrain)
print(classification_report(y_train, predtrain, target_names=target_names))



#plot del grafico kernel
from mlxtend.plotting import plot_decision_regions
plot_decision_regions(np.array((X)), np.array(y), classifie)
plt.title("kernel gaussiano Abruzzo")

plt.show()


