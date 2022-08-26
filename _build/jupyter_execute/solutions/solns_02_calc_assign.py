#!/usr/bin/env python
# coding: utf-8

# In[1]:


for i in range(10):
  print([comb(i, j) for j in range(i + 1)])


# ### Assignment 2
# 
# **OBJECTIVES**
# 
# - Solve discrete probability problems with binomial distributions
# - Solve continuous probability problems with normal distributions
# - Use summation notation and evaluate summation expressions

# In[ ]:


import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import pandas as pd


# ### Problem I
# 
# In a candy factory, chocolate bars can be either acceptable or defective. The probability of a given bar being defective is 0.5.   
# 
# - Suppose we select 8 candy bars.  
#   - How many ways different ways can we select 3 candy bars that are defective?
#   - How many ways could we select 5 defective candy bars?
#   - Make a plot of all possible outcomes.
#   - Make a table of all possible outcomes.
#   - If we select 8 bars, what is the probability that 2 will be defective? 
#   - If we select 8 bars, what is the probability that at no more than 2 will be defective?

# In[ ]:


from scipy.special import comb


# In[ ]:


comb(8, 3) #There are 56 ways to choose 3 from 56.


# In[ ]:


comb(8, 5) #There are 56 ways to choose 5 from 8


# In[ ]:


#plot
x = np.arange(9)
candy = stats.binom(8, 0.5)
plt.bar(x, candy.pmf(x))


# In[ ]:


#p(2 defective)
candy.pmf(2)


# In[ ]:


candy.pmf(0) + candy.pmf(1) + candy.pmf(2)


# In[ ]:


#p(no more than 2)
candy.cdf(2)


# ### Problem II
# 
# The probability of recovering from a certain disease is 90%.  Suppose that we select at random, 20 individuals currently suffering from the disease.  
# - What is the probability that all 20 survive?
# - What is the probability that at least 17 survive?
# - Draw a graph of all possible outcomes and their probabilities.
# - Construct a table of all possible outcomes and their probabilities.
# - Suppose a drug manufacturer conducted a clinical trial for a new treatment of the disease.  The manufacturer found that in a sample of 50 individuals treated, that 49 survived.  How likely was this and do you think the new drug had an effect?

# In[ ]:


#distribution
population = stats.binom(20, .9)


# In[ ]:


#p(all 20)
population.pmf(20)


# In[ ]:


#p(17)

population.pmf(17)


# In[ ]:


x = np.arange(21)
plt.bar(x, population.pmf(x))


# In[ ]:


table = pd.DataFrame({'survivors': x, 'probability': population.pmf(x)})
table.head()


# In[ ]:


stats.binom(50, 0.9).cdf(48) #we expect 2.86% survive so probably not


# In[ ]:


x = np.arange(51)
plt.bar(x, stats.binom(50, .9).pmf(x))


# In[ ]:


stats.binom(50, 0.9).cdf(48)


# ### Problem 3
# 
# For each example below, we are given a description for a binomial distribution where:
# 
# ```
# n = # of trials
# p = probability of success
# ```
# 
# You are to build a table and graph for each, and answer the subsequent questions on the probability distribution.
# 
# - $n = 10, p = .2$, draw a bar plot of all possible outcomes and their probabilities
# - With $n = 20, p = .2$, what is the probability of 12 successes?
# - With $n = 30, p = 0.13$, what is the average aka expected value of the probability distribution?  Its variance?  Draw a plot of the distribution.
# - With $n = 300, p = 0.13$, what is the average aka expected value of the probability distribution?  Its variance?  Draw a plot of the distribution.
# - With $n = 3000, p = 0.13$, what is the average aka expected value of the probability distribution?  Its variance?  Draw a plot of the distribution.
# - Using the three distributions above with $n = 30, 300, 3000$ and $p = 0.13$, explain what happens to the mean, variance, and graphs as you increase $n$.  
#  

# In[ ]:


x = np.arange(11)
y = stats.binom(10, 0.2).pmf(x)
plt.bar(x, y)


# In[ ]:


x = np.arange(21)
dist = stats.binom(20, 0.2)
y = dist.pmf(x) #all possible outcomes
plt.bar(x, y)


# In[ ]:


dist.pmf(12) #probability of 12 successes


# In[ ]:


x = np.arange(31)
dist = stats.binom(30, 0.13)
y = dist.pmf(x) #all possible outcomes
plt.bar(x, y)


# In[ ]:


dist.mean() #expected value is 3.9 -- should look like where high point in plot is


# In[ ]:


dist.var() #variance


# In[ ]:


x = np.arange(301)
dist = stats.binom(300, 0.13)
y = dist.pmf(x) #all possible outcomes
plt.bar(x, y)


# In[ ]:


dist.mean()


# In[ ]:


dist.var()


# In[ ]:


x = np.arange(3001)
dist = stats.binom(3000, 0.13)
y = dist.pmf(x) #all possible outcomes
plt.bar(x, y)


# In[ ]:


dist.mean()


# In[ ]:


dist.var()


# In[ ]:


pd.DataFrame({'n': [30, 300, 3000], 'mean': [3.9, 39, 390],
              'variance': [3.39, 33.9, 339]})


# ### Summations
# 
# Evaluate the following sums:
#  
# - $\sum_{i = 1}^5 2*i - 3$
# - $\sum_{i = 1}^{10} \frac{1}{i}$
# - $\sum_{i = 4}^9 3i^2 - 2i$

# In[ ]:


2*1 - 3 + 2*2 - 3 + 2*3 - 3 + 2*4 - 3 + 2*5 - 3


# In[ ]:


def s(x): return 1/x


# In[ ]:


np.arange(1, 11)


# In[ ]:


import numpy as np


# In[ ]:


sum(s(np.arange(1, 11)))


# In[ ]:


sum([1/1, 1/2, 1/3, 1/4, 1/5, 1/6, 1/7, 1/8, 1/9, 1/10])


# In[ ]:


def g(i): return 3*i**2 - 2*i #expression to sum


# In[ ]:


x = np.arange(4, 10) #values to sum


# In[ ]:


sum(g(x)) #sum


# ### Problem 4: Normal Distribution
# 
# Use the information given about the mean and standard deviation of a normal distribution to answer the questions.
# 
# - Suppose $\mu = 10, \sigma = 3$.  Draw a plot of this distribution on $x = [0, 20]$.  What is the probability $x > 15$?
# - Suppose $\mu = 0, \sigma = 3$.  Draw a plot of this distribution on $x = [-10, 10]$.  What is the probability $x < 0$?
# - Suppose $\mu = 0, \sigma = 1$.  Draw a plot of this distribution on $x = [-3, 3]$.  What is the probability $-1 < x < 1$?
# 
# 

# In[ ]:


ex1 = stats.norm(10, 3)
x = np.linspace(0, 20, 1000)
plt.plot(x, ex1.pdf(x))


# In[ ]:


1 - ex1.cdf(15)


# In[ ]:


ex1 = stats.norm(0, 3)
x = np.linspace(-10, 10, 1000)
plt.plot(x, ex1.pdf(x))


# In[ ]:


ex1.cdf(0)


# In[ ]:


ex1 = stats.norm(0, 1)
x = np.linspace(-3, 3, 1000)
plt.plot(x, ex1.pdf(x))


# In[ ]:


ex1.cdf(1) - ex1.cdf(-1)


# ### Problem 5
# 
# - Suppose we have two dogs; one weighs 40 lbs and the other 60 lbs.  Your goal is to design a see saw that will balance the two dogs, one on each end.  Where should its center be?  Draw a picture with appropriate labels for distances and dog weights.
# 
# 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




