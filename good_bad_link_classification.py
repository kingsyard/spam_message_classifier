#!/usr/bin/env python
# coding: utf-8

# ##Reading Dataset

# In[1014]:


#import required libreries

# Importing libraries

from __future__ import print_function
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report
from sklearn import metrics
from sklearn import tree
import warnings
warnings.filterwarnings('ignore')

import xgboost as xgb
from url_features import *

import joblib
 
# Save the model as a pickle in a file
#joblib.dump(XB, 'xgboost_url_final.pkl')
 
# Load the model from the file
loaded_XB=joblib.load('xgboost_url_final.pkl')
 
# Use the loaded model to make predictions

from external_features import *




def spam_good_url(url):

							# In[1671]:


							url=url


							# In[1672]:


							length_url=len(url) 
							length_url


							# In[1673]:


							from urllib.parse import urlparse
							# from urlparse import urlparse  # Python 2
							parsed_uri = urlparse(url)
							result = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
							print(result)

							# gives
							#'http://stackoverflow.com/'


							# In[1674]:


							length_hostname=len(result)


							# In[1675]:


							length_hostname


							# In[1676]:


							import re


							# In[ ]:





							# In[1677]:


							ip=having_ip_address(url)


							# In[1678]:


							ip


							# In[ ]:





							# In[1679]:


							nb_dots=count_dots(result)


							# In[1680]:


							nb_dots


							# In[1681]:


							nb_at=count_at(url)
							nb_at


							# In[1682]:


							nb_hyphens=count_hyphens(url)
							nb_hyphens


							# In[1683]:


							nb_qm=count_qm(url)
							nb_qm


							# In[1684]:


							nb_and=count_and(url)
							nb_and


							# In[1685]:


							nb_or=count_or(url)
							nb_or


							# In[1686]:


							nb_eq=count_equal(url)
							nb_eq


							# In[1687]:


							['length_url', 'length_hostname', 'ip', 'nb_dots', 'nb_hyphens',
							       'nb_at', 'nb_qm', 'nb_and', 'nb_or', 'nb_eq', 'nb_underscore',
							       'nb_tilde', 'nb_percent', 'nb_slash', 'nb_star', 'nb_colon', 'nb_comma',
							       'nb_semicolumn', 'nb_dollar', 'nb_space', 'nb_www', 'nb_com',
							       'nb_dslash','domain_registration_length', 'domain_age',
							       'web_traffic', 'dns_record', 'google_index', 'page_rank']


							# In[1688]:


							nb_underscore=count_underscore(url)
							nb_underscore


							# In[1689]:


							nb_tilde=count_tilde(url)
							nb_tilde


							# In[1690]:


							nb_percent=count_percentage(url)
							nb_percent


							# In[1691]:


							nb_slash=count_slash(url)
							nb_slash


							# In[1692]:


							nb_star=count_star(url)
							nb_star


							# In[1693]:


							nb_colon=count_colon(url)
							nb_colon


							# In[1694]:


							nb_comma=count_comma(url)
							nb_comma


							# In[1695]:


							nb_semicolumn=count_semicolumn(url)
							nb_semicolumn


							# In[1696]:


							['length_url', 'length_hostname', 'ip', 'nb_dots', 'nb_hyphens',
							       'nb_at', 'nb_qm', 'nb_and', 'nb_or', 'nb_eq', 'nb_underscore',
							       'nb_tilde', 'nb_percent', 'nb_slash', 'nb_star', 'nb_colon', 'nb_comma',
							       'nb_semicolumn', 'nb_dollar', 'nb_space', 'nb_www', 'nb_com',
							       'nb_dslash','domain_registration_length', 'domain_age',
							       'web_traffic', 'dns_record', 'google_index', 'page_rank']


							# In[1697]:


							nb_dollar=count_dollar(url)
							nb_dollar


							# In[1698]:


							nb_space=count_space(url)
							nb_space


							# In[1699]:


							def count_com(url):
							    return url.count('.com')


							# In[1700]:


							def count_www(url):
							    return url.count('www')


							# In[1701]:


							nb_www=count_www(url)
							nb_www


							# In[1702]:


							nb_com=count_com(url)
							nb_com


							# In[1703]:


							['length_url', 'length_hostname', 'ip', 'nb_dots', 'nb_hyphens',
							       'nb_at', 'nb_qm', 'nb_and', 'nb_or', 'nb_eq', 'nb_underscore',
							       'nb_tilde', 'nb_percent', 'nb_slash', 'nb_star', 'nb_colon', 'nb_comma',
							       'nb_semicolumn', 'nb_dollar', 'nb_space', 'nb_www', 'nb_com',
							       'nb_dslash','domain_registration_length', 'domain_age',
							       'web_traffic', 'dns_record', 'google_index', 'page_rank']


							# In[1704]:


							nb_dslash=count_double_slash(url)
							nb_dslash


							# In[1705]:


							


							# In[1706]:

#
#							domain_registration_length=domain_registration_length(url)
#							domain_registration_length
#

							# In[1707]:


#							domain_age=domain_age(url)
#							domain_age


							# In[1708]:

#
#							web_traffic=web_traffic(url)
#							web_traffic


							# In[1709]:

#
#							dns_record=dns_record(url)
#							dns_record


							# In[1710]:

#
#							google_index=google_index(url)
#							google_index


							# In[1711]:


#							page_rank=page_rank('gkko8o84ocwgkc8ssco8kwg4gg0oocggskw8ggg8',url)
#							page_rank


							# In[1712]:


							inpt1=[length_url, length_hostname, ip, nb_dots, nb_hyphens,
							       nb_at, nb_qm, nb_and, nb_or, nb_eq, nb_underscore,
							       nb_tilde, nb_percent, nb_slash, nb_star, nb_colon, nb_comma,
							       nb_semicolumn, nb_dollar, nb_space, nb_www, nb_com,
							       nb_dslash]


							# In[ ]:





							# In[1713]:


							#predicted_values
							#[int_features2]


							# In[1714]:



							int_features2 = np.array([inpt1])

							#int_features3 = int_features2.reshape(1, -1)
							int_features2
							              

							predicted_values = loaded_XB.predict(int_features2)
							return predicted_values


#print(spam_good_url("https://documentos.sfo2.digitaloceanspaces.com/ordem.html"))



# Python code to find the URL from an input string
# Using the regular expression
import re
  
def Find(string):
  
    # findall() has been used 
    # with valid conditions for urls in string
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex,string)      
    return [x[0] for x in url]
def all_links_message(string1):      
# Driver Code
#string = 'My Website is : https://smartaitechnologies.com and you can visit this for further information also visit our linkedin profile https://www.linkedin.com/in/%E0%B2%B0%E0%B2%BE%E0%B2%9C%E0%B3%81-%E0%B2%AE%E0%B2%B9%E0%B2%A6%E0%B3%87%E0%B2%B5%E0%B2%AA%E0%B3%8D%E0%B2%AA-%E0%B2%AE%E0%B2%BE%E0%B2%B5%E0%B2%BF%E0%B2%A8%E0%B2%AE%E0%B2%B0-59b133168/'
          print("Urls: ", Find(string1))


          return  Find(string1)

link_tag=[]
#link_list=[]
#link_list=all_links_message("hi i m using https://www.missfiga.com/  to know how to use data science and also please visit  http://swallowthisbitchpics.com/jpg/www.global.visa.com/myca/oce/emea/action/request_type=un_Activation/visa.html")

def list_link_tag(string):

	#link_list.clear()


	link_tag.clear()



	link_list=all_links_message(string)

	print("total links availlable for detection ",link_list)





	for tt in link_list:


		print(spam_good_url(tt)[0])


		if spam_good_url(tt)[0]==0:


			tag="good"

		else:

			tag="bad"

		link_tag.append(tag)
		
	print("both link list and the spam or ham tags",link_list,link_tag)
	

	w=link_tag




	return   link_list,w


