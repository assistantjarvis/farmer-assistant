#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import random
import math 
import time

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.svm import SVR
#from sklearn.svm import LinearSVR 
from sklearn.metrics import mean_squared_error, mean_absolute_error

import datetime
import operator
plt.style.use('fivethirtyeight')
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


crop_df = pd.read_csv("crop_production.csv")
crop_df=crop_df.dropna().reset_index(drop=True)
crop_df


# In[3]:


cols = crop_df.keys()
cols


# In[4]:


def totalCropProductionByStateAndYear(state, year):
    states =  crop_df.loc[ crop_df["State_Name"] == state]
    years =  states.loc[ states["Crop_Year"] == year]
    total_production = years['Production'].sum()
    return total_production


# In[5]:


def plot_bar_graphs_all_state(title, states, total_state_productions):
    plt.figure(figsize=(8, 8))
    plt.barh(states, total_state_productions, color='blue')
    plt.title(title, size=10)
    plt.xticks(size=10)
    plt.yticks(size=10)
    plt.show()


# In[6]:


def plotAllStateTotalProduction(year):
    total_state_productions = []
    states = crop_df["State_Name"].unique()
    for state in states:
        total_production = totalCropProductionByStateAndYear(state, year)
        total_state_productions.append(total_production)

    plot_bar_graphs_all_state("Total crops productions of year("+str(year)+')', states, total_state_productions)


# In[7]:


def totalCropProductionByStateAndYearSeason(state, year, season):
    states =  crop_df.loc[ crop_df["State_Name"] == state]
    years =  states.loc[ states["Crop_Year"] == year]
    seasons =  years.loc[ years["Season"] == season]
    #return seasons
    total_production = seasons['Production'].sum()
    return total_production
    #return total_production


# In[8]:


def plot_bar_graphs_all_seasons(title, seasons, total_season_productions):
    plt.figure(figsize=(4, 4))
    plt.barh(seasons, total_state_productions, color='blue')
    plt.title(title, size=10)
    plt.xticks(size=10)
    plt.yticks(size=10)
    plt.show()


# In[9]:


def plot_pi_charts_all_seasons(title, seasons, total_season_productions):
    c = random.choices(list(mcolors.CSS4_COLORS.values()), k = len(seasons))
    plt.figure(figsize=(16,16))
    plt.title(title, size=20)
    plt.pie(total_season_productions,colors=c)
    plt.legend(seasons, loc='right', fontsize=10)
    plt.show()


# In[10]:


def plotStateWiseSeasonsChart(bar, state, year):
    total_season_productions = []
    seasons = crop_df["Season"].unique()
    for season in seasons:
        #print(season)
        if season == 'Whole Year ':
            #total_season_productions.append(0)
            continue
        total_production = totalCropProductionByStateAndYearSeason(state, year, season)
        total_season_productions.append(total_production)
        
    arr_new = np.delete(seasons, 1)
    
    if bar:
        plot_bar_graphs_all_seasons("Total season productions of year("+str(year)+')', arr_new, total_season_productions)
    else:
        plot_pi_charts_all_seasons("Total season productions of year("+str(year)+')', arr_new, total_season_productions)
    


# In[11]:


year = 2001
state = 'Uttar Pradesh'


# In[12]:


plotAllStateTotalProduction(year)


# In[13]:


plotStateWiseSeasonsChart(False, state, year)


# In[14]:


def totalCropProductionByStateAndYearCrop(state, year, crop):
    total_crops_productions = []
    states =  crop_df.loc[ crop_df["State_Name"] == state]
    dists =  states.loc[ states["Crop_Year"] == year]
    crops =  dists.loc[ dists["Crop"] == crop]
    total_production = crops['Production'].sum()
    
    return total_production


# In[15]:


totalCropProductionByStateAndYearCrop(state, year,'Sunflower')


# In[16]:


def plot_crop_wise_chart(bar, state, year):
    total_crop_productions = []
    crops = crop_df["Crop"].unique()
    #print(crops)
    for crop in crops:
        total = totalCropProductionByStateAndYearCrop(state,year, crop)
        total_crop_productions.append(total)
        
    plot_pi_charts_all_seasons("Total crop productions of year("+str(year)+')', crops, total_crop_productions)


# In[17]:


plot_crop_wise_chart(False, state,year)


# In[ ]:





# In[18]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import random
import math 
import time

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.svm import SVR
#from sklearn.svm import LinearSVR 
from sklearn.metrics import mean_squared_error, mean_absolute_error

import datetime
import operator
plt.style.use('fivethirtyeight')
get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:





# In[19]:


crop_df = pd.read_csv("crop_production.csv")
crop_df


# In[20]:


crop_df=crop_df.dropna().reset_index(drop=True)
crop_df


# In[21]:


cols = crop_df.keys()
cols


# In[22]:


states = crop_df["State_Name"].unique()
states


# In[23]:


districts = crop_df["District_Name"].unique()
districts


# In[24]:


len(districts)


# In[25]:


len(crop_df["District_Name"].unique())


# In[26]:


sessions = crop_df["Season"].unique()
sessions


# In[27]:


crops = crop_df["Crop"].unique()
crops


# In[28]:


pre_crop_df = crop_df.copy(deep=True)
pre_crop_df.head()


# In[29]:


index = 1
for crop in crops:
    pre_crop_df.loc[pre_crop_df["Crop"] == crop, "Crop"] = index
    index+=1
    


# In[30]:


index = 1
for session in sessions:
    pre_crop_df.loc[pre_crop_df["Season"] == session, "Season"] = index
    index+=1
    


# In[31]:


index = 1
for district in districts:
    pre_crop_df.loc[pre_crop_df["District_Name"] == district, "District_Name"] = index
    index+=1
    


# In[32]:


index = 1
for state in states:
    pre_crop_df.loc[pre_crop_df["State_Name"] == state, "State_Name"] = index
    index+=1
    


# In[33]:


pre_crop_df

pre_crop_df['Production']


# In[34]:


#pren_crop_df = pre_crop_df.apply(pd.to_numeric, errors='coerce')
# pren_crop_df = pren_crop_df.dropna()

# #pren_crop_df.save('')
pre_crop_df.to_csv (r'pren_crop_df.csv', index = False, header=True)


# In[35]:


pre_crop_df


# In[36]:


pre_crop_df


# In[37]:


cols


# In[38]:


X=pre_crop_df[ ['State_Name', 'District_Name', 'Crop_Year', 'Season', 'Crop', 'Area']]
# X=df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]


# In[39]:


y=pre_crop_df['Production']
print(y)


# In[40]:


from sklearn import preprocessing
from sklearn import utils

#convert y values to categorical values
lab = preprocessing.LabelEncoder()
y_transformed = lab.fit_transform(y)

#view transformed values
print(y_transformed)
y = y_transformed


# In[41]:


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=22)


# In[42]:


from sklearn.neighbors import KNeighborsClassifier
model=KNeighborsClassifier()


# In[43]:


model.fit(X_train,y_train)


# In[44]:


y_predict=model.predict(X_test)


# In[45]:


from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
print("Accuracy of the model by KNN is :-",accuracy_score(y_test,y_predict)*1000)
print(confusion_matrix(y_test,y_predict))
# print(classification_report(y_test,y_predict))


# In[46]:


def getStateCode(state_get):
    index = 1
    for state in states:
        if state.strip() == state_get.strip():
            return index
    return -1


# In[47]:


def getDistrictCode(district_get):
    index = 1
    for district in districts:
        if district.strip() == district_get.strip():
            return index
    return -1


# In[48]:


def getSessionCode(session_get):
    index = 1
    for session in sessions:
        if session.strip() == session_get.strip():
            return index
    return -1


# In[49]:


def getSessionCode(session_get):
    index = 1
    for session in sessions:
        if session.strip() == session_get.strip():
            return index
    return -1


# In[50]:


def getCropCode(crop_get):
    index = 1
    for crop in crops:
        if crop.strip() == crop_get.strip():
            return index
    return -1


# In[51]:


def cropFromCode(crop_code):
    index = 1
    for crop in crops:
        if crop_code == index:
            return crop
        
        index+=1
        
    return "error!"


# In[52]:


def validateCode(code):
    if code == -1:
        print("Error invalide entry does not exist")


# <h1>Production</h1>

# In[53]:


state_name=input("Enter State_Name: ")
state_code = getStateCode(state_name)
validateCode(state_code)

district_name=input("Enter District_Name: ")
district_code = getDistrictCode(district_name)
validateCode(district_code)

crop_year= 2022 #float(input("Enter Crop_Year: "))

season_name=input("Enter Season: ")
season_code = getSessionCode(season_name)
validateCode(season_code)

crop_name=input("Enter Crop: ")
crop_code = getCropCode(crop_name)
validateCode(crop_code)
crop_area=float(input("Enter Area: "))

result=model.predict([[state_code, district_code, crop_year,season_code, crop_code,crop_area]])
print('Production: ',result[0],'\n\n\n\n\n\n\n')


# In[54]:


# #Manual Program
# Andaman and Nicobar Islands	NICOBARS	2000	Kharif	Arecanut	1254.0	2000.0
# 'State_Name', 'District_Name', 'Crop_Year', 'Season', 'Crop', 'Area'
# Andaman and Nicobar Islands	NICOBARS	2000	Kharif	Other Kharif pulses	2.0	1.0


# In[55]:


X=pre_crop_df[ ['State_Name', 'District_Name', 'Crop_Year', 'Season', 'Area']]


# In[56]:


y=pre_crop_df['Crop']
print(y)


# In[57]:


from sklearn import preprocessing
from sklearn import utils

#convert y values to categorical values
lab = preprocessing.LabelEncoder()
y_transformed = lab.fit_transform(y)

#view transformed values
print(y_transformed)
y = y_transformed


# In[58]:


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=22)


# In[59]:


from sklearn.neighbors import KNeighborsClassifier
model=KNeighborsClassifier()


# In[60]:


model.fit(X_train,y_train)


# <h1>Crop</h1>

# In[61]:


state_name=input("Enter State_Name: ")
state_code = getStateCode(state_name)
validateCode(state_code)

district_name=input("Enter District_Name: ")
district_code = getDistrictCode(district_name)
validateCode(district_code)

crop_year= 2022 #float(input("Enter Crop_Year: "))

season_name=input("Enter Season: ")
season_code = getSessionCode(season_name)
validateCode(season_code)

#crop_name=input("Enter Crop: ")
##crop_code = getCropCode(crop_name)
#validateCode(crop_code)
crop_area=float(input("Enter Area: "))

result=model.predict([[state_code, district_code, crop_year,season_code,crop_area]])
print('crop_code: ',result[0])

#print(result[0])
crop_name = cropFromCode(result[0])
print(crop_name,'\n\n')


# In[ ]:





# In[62]:


# #Manual Program
# Andaman and Nicobar Islands	NICOBARS	2000	Kharif	Arecanut	1254.0	2000.0
# 'State_Name', 'District_Name', 'Crop_Year', 'Season', 'Crop', 'Area'
# Andaman and Nicobar Islands	NICOBARS	2000	Kharif	Other Kharif pulses	2.0	1.0


# In[ ]:




