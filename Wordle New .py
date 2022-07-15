#!/usr/bin/env python
# coding: utf-8

# ## Make words list

# In[10]:


from nltk.corpus import words
import random
import seaborn as sns
import matplotlib.pyplot as plt
import nltk


word_list = []
for i in words.words():
    if len(i)==5:
        word_list.append(i.lower()) 
print(len(word_list))


# ## Main function 
# this function takes a word as an input and asks user to further imput 2 things
# 1) green letters - Letters which are placed in correct order <br>
# 2) yellow letters- Letters which are placed in incorrect order but present in the final word
# and returns the progress in final word. <br>
# The function stores the progress and updates further values which are required for suggesting next word

# In[11]:


def main(word):
    mylist = list(word)
    x=input("Enter which of the 5 spaces are green seperated by comma")
    X=x.split(",")
    if X==['']:
        pass
    else:
        ## Convert to Integer
        for i in X:
               X[X.index(i)]=int(i)
    y=input("Enter which of the 5 spaces are yellow or green seperated by comma")
    Y = y.split(",")    
    if Y==['']:
        pass
    else:
        for j in Y:
            Y[Y.index(j)]=int(j)
    for i in range(1,6):
        if i in X:
            final_word[i-1]=mylist[i-1]
            green_list.append(mylist[i-1])
            colour[i-1]=2
        if i in Y:
            yellow_list.add(mylist[i-1])
            colour[i-1]=1
        else:
            grey_list.add(mylist[i-1])
    list_cleaner()
    return final_word


# ## List Cleaner functions
# The way green_list, grey_list and yellow list are created there is a chance of an element of green or yellow  list appearing in grey list which is not true. hence we clean the lists

# In[12]:


def list_cleaner():
    for i in green_list:
        if i in grey_list:
            grey_list.remove(i)
    for j in yellow_list:
        if j in grey_list:
            grey_list.remove(j)
    for k in green_list:
        if k in yellow_list:
            yellow_list.remove(k)


# ## Checker function
# This functions takes a word in input and checks if it meets all the condition required to suggest next word <br>
# these conditions are nothing but consideration of progress at each iteration.
# for example shuffling yellow letters and keeping green letter as it is as well as not using any letter which has been previously rejected

# In[13]:


def list_check(x):
    ## early tries and repeated letters in suggestions
    if tries<4 and len(list(set(x)))<5:
        return('repeated letters at early try')
    else:
        chck='GG'
    
    ## previous word suggested
    if x in prev_word_list:
        return('Word tried already')
    else:
        chck='GG'
    ## Green List check
    for i in range (len(final_word)):
        if final_word[i]==0 or final_word[i]==x[i]:
            chck='GG'
            continue
        else:
            chck='green_list_error'
            return(chck)
    ## Yellow List check
    for j in yellow_list:
        
        prev_word_with_j=[]
        for i in prev_word_list:
            if j in i:
                prev_word_with_j.append(i)
        if j in x and x.index(j) not in [words.index(j) for words in prev_word_with_j]:
            chck='GG'
        else:
            chck='Yellow_list_error'
            return(chck)
    ## Grey list check
    for k in grey_list:
        if k in x:
            chck='grey_list_error'
            return(chck)
        else:
            chck='GG'
            continue
    return(chck)


# ## Word Suggestor Function using list check
# For each word in word list it uses the checker function to check if the conditions are satisfied and returns a word suggestion <br>
# till 3 tries the function tries to suggest words where letters are not repeated

# In[14]:


def word_suggestor():
    for i in word_list:
            x=list_check(i)
            if x=='GG':
                break
            else:
                continue
    return(i)


# ## Final Code
# This code runs all the above function in required order as well as displays the result in a user freindly manner. <br>
# ## Trying the code to run and guess a word.
# ## let the word be STORY

# In[20]:


yellow_list=set()
green_list=[]
grey_list=set()
final_word=[0,0,0,0,0]
colour = [0,0,0,0,0]
tries=0
#word=word_suggestor()
#print('Try the word %s'%word)
#main(word)
prev_word_list=[]
random.shuffle(word_list)
while 0 in final_word:
    tries=tries+1
    word = word_suggestor()
    print("Try the word %s"%word)
    colour = [0,0,0,0,0]
    main(word)
    sns.heatmap([colour], annot_kws={"size":30}, cmap = ['grey', 'yellow', 'green'], annot = [list(word)], fmt = '', vmin = 0, vmax = 3, square = True,linecolor='black', linewidth = 2,cbar = False)
    plt.show()
    prev_word_list.append(word)
print('The final word is %s'%word)

