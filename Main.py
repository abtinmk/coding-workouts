import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,confusion_matrix,recall_score,accuracy_score
import os
from sklearn.ensemble import RandomForestClassifier 
data_path='C:/Users/ASUS/Desktop/EEG_Data'
def data_load(data_path):
  classes=["0","1","2","3",'4']
  x,y=[],[]
  for cls in classes:
    folder_path=os.path.join(data_path,cls)
    for file in os.listdir(folder_path):
      file_path=os.path.join(folder_path,file)
      if os.path.isfile(file_path) and file.endswith('.npy'):
       data=np.load(file_path)
       x.append(data)
       y.append(cls)
  return np.array(x),np.array(y)
x,y=data_load(data_path)
x=x.reshape(x.shape[0],-1)
print(x.shape)
x/=np.max(x)
x_train,x_temp,y_train,y_temp=train_test_split(x,y,test_size=0.3,stratify=y,random_state=21)
x_val,x_test,y_val,y_test=train_test_split(x_temp,y_temp,test_size=0.5,random_state=21)
model=RandomForestClassifier(n_estimators=100,random_state=21)
model.fit(x_train,y_train)
y_val_pred=model.predict(x_val)
print(f'accuracy random forest:{accuracy_score(y_val,y_val_pred):.2f}')
print(f'confusion matrix random forest:\n{confusion_matrix(y_val,y_val_pred)}')
print(f'classifiction report:\n',classification_report(y_val,y_val_pred,zero_division=0))
#random forest is not a good model
from sklearn.neural_network import MLPClassifier
#accuracy after training for diffrent activation func: logostic>tanh=relu=identity
model=MLPClassifier(hidden_layer_sizes=(256,128,64),activation='logistic',solver='adam',max_iter=500,random_state=21,verbose=True)
model.fit(x_train,y_train)
y_val_pred=model.predict(x_val)
print(f'accuracy mlp classifier:{accuracy_score(y_val,y_val_pred):.2f}')
print(f'confusion matrix mlp classifier:\n{confusion_matrix(y_val,y_val_pred)}')
print(f'classifiction report:\n',classification_report(y_val,y_val_pred,zero_division=0))
# MLP not good
from sklearn.svm import SVC
model=SVC(kernel='rbf',C=1 , random_state=21)
model.fit(x_train,y_train)
y_val_pred=model.predict(x_val)
print(f'accuracy svm:{accuracy_score(y_val,y_val_pred):.2f}')
print(f'confusion matrix svm:\n{confusion_matrix(y_val,y_val_pred)}')
print(f'classifiction report:\n',classification_report(y_val,y_val_pred,zero_division=0))
#svm very bad
import xgboost as xgb
model=xgb.XGBClassifier(n_estimators=100,learning_rate=0.1,max_depth=6,random_state=42)
model.fit(x_train,y_train)
y_val_pred=model.predict(x_val)
print(f'accuracy xgboost:{accuracy_score(y_val,y_val_pred):.2f}')
print(f'confusion matrix xgboost:\n{confusion_matrix(y_val,y_val_pred)}')
print(f'classifiction report:\n',classification_report(y_val,y_val_pred,zero_division=0))
from sklearn.neighbors import KNeighborsClassifier
model=KNeighborsClassifier(n_neighbors=10)
model.fit(x_train,y_train)
y_val_pred=model.predict(x_val)
print(f'accuracy KNN:{accuracy_score(y_val,y_val_pred):.2f}')
print(f'confusion matrix KNN:\n{confusion_matrix(y_val,y_val_pred)}')
print(f'classifiction report:\n',classification_report(y_val,y_val_pred,zero_division=0))
#KNN:a little better than mlp and svm but not good
#it seems the classical models can not creating a good model for this task
#for this task it seems we need use a complicated model
import tensorflow as tf
import keras as ks
num_classes=5

model=tf.keras.Sequential([
  tf.keras.layers.Conv2D(32,(3,3),activation='relu',input_shape=(51,59,1)),
  tf.keras.layers.MaxPooling2D((2,2)),
  tf.keras.layers.Conv2D(64,(3,3),activation='relu'),
  tf.keras.layers.MaxPooling2D((2,2)),
  tf.keras.layers.Flatten(),
  tf.keras.layers.Dense(128,activation='relu'),
  tf.keras.layers.Dropout(0.5),
  tf.keras.layers.Dense(num_classes,activation='softmax')
]) 