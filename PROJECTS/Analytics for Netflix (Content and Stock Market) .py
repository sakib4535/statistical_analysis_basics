#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


game = pd.read_csv("video_game_film.csv")
game
game.head(11)


# In[3]:


game.iloc[0:3]


# In[4]:


game.index[5:20]


# In[5]:


print(game.describe())
game_sort = sorted(game['Worldwide_box_office'])

for i in enumerate(game_sort):
    print(i)


# In[6]:


display(game)


# In[7]:


game1 = game[game.Title == "Street Fighter"]
game1


# In[8]:


import matplotlib.pyplot as plt

plt.plot(game.Metacritic, c="r", alpha=1)
plt.title("Metacritics Rates")


# In[9]:


import matplotlib.pyplot as plt

plt.plot(game.Metacritic, c="r", alpha=1)
plt.plot(game.Rotten_tomatoes, alpha=1)
plt.xlabel("Meta")
plt.ylabel("Rotten")
plt.legend(["Metacritic", "Rotten Tomatoes"])


# In[10]:


game["Worldwide_box_office"].rolling(30).mean().plot()
plt.show()
game.sort_index(inplace=True)
game


# In[11]:


plt.hist(game["Worldwide_box_office"], bins=8, density=True, ec="black", label="Data Histogram")
plt.xlabel("Numbers")
plt.ylabel("Box Office Return")
plt.legend();


# In[12]:


import numpy as np

plt.hist(game["Worldwide_box_office"], ec="red", label="Data")
plt.axvline(np.mean(game["Worldwide_box_office"]), ls="--", c="r", label="Mean Data")
plt.axvline(np.median(game["Worldwide_box_office"]), ls=":", label="Median Data")
plt.legend()


# In[13]:


import scipy.stats as st

mean = np.mean(game["Worldwide_box_office"])
std = np.std(game["Worldwide_box_office"])
xs = np.linspace(game["Worldwide_box_office"].max(), game["Worldwide_box_office"].min(), 100)
ys = st.norm.pdf(xs, loc=mean, scale=std)

plt.hist(game["Worldwide_box_office"], bins=9, density=True, histtype="step", label="Data")
plt.plot(xs, ys, label="Normal approximation")
plt.legend();
plt.xlabel("Interval")
plt.ylabel("Probability");


# In[14]:


ser = game.groupby(["Distributor"])
ser
ser1 = game.groupby(["Distributor", "Title"]).count()
ser1


# In[15]:


game.Distributor.value_counts()


# In[16]:


dist = list(enumerate(game.Distributor))
title = list(enumerate(game.Title))
print(dist, title)
print("---------------------------------------")

for index, house in enumerate(game.Distributor):
    print(index, house)


# In[17]:


import seaborn as sns
sns.set(color_codes=True)


# In[18]:


sns.jointplot(game["Rotten_tomatoes"], game["Worldwide_box_office"])
sns.jointplot(game["Metacritic"], game["Worldwide_box_office"])


# In[19]:


sns.jointplot(game["Rotten_tomatoes"], game["Metacritic"], kind="hex")


# In[20]:


sns.jointplot(game["Rotten_tomatoes"], game["Metacritic"], game["Worldwide_box_office"], kind="hex")


# In[21]:


sns.pairplot(game[["Rotten_tomatoes", "Metacritic", "Worldwide_box_office"]])


# In[22]:


print(game.count())
type(game)


# In[23]:


sns.countplot(game.groupby(game["Distributor"])["Title"].count())


# In[24]:


#Map the Game


# In[25]:


game_map = game.copy()


# In[26]:


game_3 = game.sort_values(by=["Distributor"])
print(game_3.reset_index(drop=True))


# In[57]:


dist_1 = game[["Distributor", "Title"]].value_counts()
print(dist_1.sort_index())


# In[61]:


dist_1.sum()


# In[98]:


def main():
    
    stock = pd.read_csv("NFLX.csv")
    fig = plt.figure(figsize=(13,8))
    
    ax = fig.add_subplot(1, 1, 1)
    stock["Date"] = pd.to_datetime(stock["Date"])
    ax.plot(stock["Date"], stock["Open"], linestyle="solid")
    return

main()


# In[116]:


def main():
    
    stock_1 = pd.read_csv("NFLX.csv")
    fig_1 = plt.figure(figsize=(13,8))
    
    ax_1 = fig_1.add_subplot(1, 1, 1)
    stock_1["Date"] = pd.to_datetime(stock_1["Date"])
    ax_1.plot(stock_1["Date"], stock_1["Close"], color="red", linestyle="solid")
    ax_1.xlabel("Timeline")
    ax_1.ylabel("Price(in Dollar)")    
    ax_1.grid(True)
    plt.title("Closing Price Data (In Five Years of Timeline)")
    return

main()


# In[117]:


stock = pd.read_csv("NFLX.csv")

x = plt.figure(figsize=(15,8))
plt.plot(stock["Volume"], color="green")
plt.xlabel("Timeline")
plt.ylabel("Volume Size")
plt.title("Volumn Size of the Netflix Market (In total Five Years of Timeline)")


# In[ ]:




