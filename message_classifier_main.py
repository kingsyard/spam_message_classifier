
import numpy as np#arrays and matrices
import pandas as pd
import nltk
import re

import matplotlib.pyplot as plt
import seaborn as sns



import joblib
 
# Save the model as a pickle in a file
#joblib.dump(dataset, 'dataset.pkl')
 
# Load the model from the file
dataset = joblib.load('dataset.pkl')
 
# Use the loaded model to make predictions


def text_preprocess(sen): 
   sen=str(sen)

   sen = re.sub('[^a-zA-Z]', ' ', sen)#removes everything which is not  an alpabet  replace with none 

   sen = re.sub(r"\s+[a-zA-Z]\s+", ' ', sen)

   sen = re.sub(r'\s+', ' ', sen) # eliminate duplicates

   return sen

X = dataset["Message"]  
 
y = dataset["Type"]



X_messages = [] 
messages = list(X) 

print(messages[0:5])
for mes in messages: 
     X_messages.append(text_preprocess(mes))
     print(text_preprocess(mes))


import nltk
#nltk.download('stopwords')
from nltk.corpus import stopwords 
from sklearn.feature_extraction.text import TfidfVectorizer 

#tfidf_vec = TfidfVectorizer (max_features=2500, min_df=7, max_df=0.8, stop_words=stopwords.words('english')) 
tfidf_vec = TfidfVectorizer (max_features=5000, min_df=20, max_df=0.4, stop_words=stopwords.words('english')) 
import joblib
 
# Save the model as a pickle in a file
#joblib.dump(tfidf_vec, 'tfidf_vec.pkl')
 
# Load the model from the file
#tfidf_vec_fn = joblib.load('tfidf_vec.pkl')


#print("Feature Names ",tfidf_vec.get_feature_names())


# In[231]:


# Tf-Idf Representation Of Document1
#X = Tfidf_vect.transform(X_messages)
#print("Representation Of Document1: ", Tfidf1.toarray())


# In[402]:


X= tfidf_vec.fit_transform(X_messages).toarray()




import joblib
 
# Save the model as a pickle in a file
#joblib.dump(rf_clf, 'best_random_forest_message_classification_model.pkl')
 
# Load the model from the file
rf_from_joblib = joblib.load('best_random_forest_message_classification_model.pkl')
 
# Use the loaded model to make predictions


def classify_text_msg(message_inpt):
							user_input=message_inpt

							# In[420]:


							dataset["Message"][0]=str(user_input)


							# In[421]:


							X1 = dataset["Message"]  
							 



							X_messages1 = [] 
							messages1 = list(X1) 



							#print(messages1[-4])
							for mes1 in messages1: 
							     X_messages1.append(text_preprocess(mes1))
							    # print(text_preprocess(mes1))


							# In[425]:


							X2= tfidf_vec.fit_transform(X_messages1).toarray()



							#len(list(X2[8]))

							len(list(X2[0]))




							# In[428]:


							#import joblib
							 
							# Save the model as a pickle in a file
							#joblib.dump(X2, 'vecter_array.pkl')
							 
							# Load the model from the file
							#vec_array = joblib.load('vecter_array.pkl')
							 
							# Use the loaded model to make predictions


							# In[ ]:

							X3=X2[0][0:605]




							y_pred = rf_from_joblib.predict([X3])


							# In[430]:


							print("the final prediction for the data",y_pred)



							return y_pred

#print(classify_text_msg("Now, Postaga has a spreadsheet-style view for you, helping you to more easily manage and edit your outreach contacts. It has all of your contacts' relevant values filled in automatically, letting you easily edit them before you send!"))