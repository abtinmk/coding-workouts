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
#random forest
from sklearn.neural_network import MLPClassifier
#accuracy after training for diffrent activation func: logostic>tanh=relu=identity
model=MLPClassifier(hidden_layer_sizes=(256,128,64),activation='logistic',solver='adam',max_iter=500,random_state=21,verbose=True)
model.fit(x_train,y_train)
y_val_pred=model.predict(x_val)
print(f'accuracy mlp classifier:{accuracy_score(y_val,y_val_pred):.2f}')
print(f'confusion matrix mlp classifier:\n{confusion_matrix(y_val,y_val_pred)}')
print(f'classifiction report:\n',classification_report(y_val,y_val_pred,zero_division=0))
# MLP 
from sklearn.svm import SVC
model=SVC(kernel='rbf',C=1 , random_state=21)
model.fit(x_train,y_train)
y_val_pred=model.predict(x_val)
print(f'accuracy svm:{accuracy_score(y_val,y_val_pred):.2f}')
print(f'confusion matrix svm:\n{confusion_matrix(y_val,y_val_pred)}')
print(f'classifiction report:\n',classification_report(y_val,y_val_pred,zero_division=0))
#svm
from sklearn.neighbors import KNeighborsClassifier
model=KNeighborsClassifier(n_neighbors=10)#more than 10 is going to overfiting
model.fit(x_train,y_train)
y_val_pred=model.predict(x_val)
print(f'accuracy KNN:{accuracy_score(y_val,y_val_pred):.2f}')
print(f'confusion matrix KNN:\n{confusion_matrix(y_val,y_val_pred)}')
print(f'classifiction report:\n',classification_report(y_val,y_val_pred,zero_division=0))
#KNN:a little better than svm but not good
#it seems the classical models can not creating a good model for this task
#for this task it seems we need use a complicated model like CNN and from my searchs the code is
#going to be like this
import tensorflow as tf
import keras as ks
num_classes=5
x=x.reshape(x.shape[0],51,59,1)
x=x.astype('float32')/np.max(x)
x_train,x_temp,y_train,y_temp=train_test_split(x,y,test_size=0.3,stratify=y,random_state=21)
x_val,x_test,y_val,y_test=train_test_split(x_temp,y_temp,test_size=0.5,random_state=21)
y_train=ks.utils.to_categorical(y_train,num_classes)
y_test=ks.utils.to_categorical(y_test,num_classes)
y_val=ks.utils.to_categorical(y_val,num_classes)
model=ks.Sequential([
  ks.layers.Conv2D(32,(3,3),activation='relu',input_shape=(51,59,1)),
  ks.layers.MaxPooling2D((2,2)),
  ks.layers.Conv2D(64,(3,3),activation='relu'),
  ks.layers.MaxPooling2D((2,2)),
  ks.layers.Flatten(),
  ks.layers.Dense(128,activation='relu'),
  ks.layers.Dropout(0.5),
  ks.layers.Dense(num_classes,activation='softmax')
]) 
model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])
history=model.fit(x_train,y_train,epochs=20,batch_size=32,validation_data=(x_val,y_val),verbose=1)
val_loss , val_acc=model.evaluate(x_val,y_val,verbose=0)
print(f'val accuracy for CNN:{val_acc:.2f}')
y_pred=model.predict(x_val)
y_pred_classes=np.argmax(y_pred,axis=1)
y_val_classes=np.argmax(y_val,axis=1)
print(f'confusion matrix CNN:\n{confusion_matrix(y_val_classes,y_pred_classes)}')
print(f'classifiction report:\n',classification_report(y_val_classes,y_pred_classes,zero_division=0))
# دقت این مدل نیز چندان فرقی نکرد
#ارزیابی داده های تست
y_test_pred=model.predict(x_test)
y_predtest_classes=np.argmax(y_test_pred,axis=1)
y_test_classes=np.argmax(y_test,axis=1)
print(f'confusion matrix :\n{confusion_matrix(y_test_classes,y_predtest_classes)}')
print(f'classifiction report:\n',classification_report(y_test_classes,y_predtest_classes,zero_division=0))
#test Accuracy = 52%