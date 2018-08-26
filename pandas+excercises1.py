
# coding: utf-8

# In[1]:

import numpy as np


# In[2]:

num=np.arange(1,101)


# In[3]:

num


# In[4]:

slides=num*1000


# In[6]:

slides


# In[7]:

np.random.shuffle(slides)


# In[8]:

slides


# In[10]:

department=slides.reshape(10,10)


# In[11]:

department


# In[17]:

counter=0
for dept in department:
     
        print("the {} of sum${}".format(counter,np.sum(dept)))
        counter+=1


# In[20]:

for index,dept in enumerate(department):
    print("the {} of ${}".format(index,np.sum(dept)))


# In[ ]:



