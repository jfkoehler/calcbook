#!/usr/bin/env python
# coding: utf-8

# # Problem Set I: Functions
# 
# **OBJECTIVES**
# 
# - Represent functions with symbols, graphs, tables, and words
# - Interpret key characteristics of *polynomial*, *logarithmic*, and *trigonometric* functions
# 

# ## Basic Definitions and Plotting

# ### Problem 1
# 
# - Define a function $f(x) = x^2$
# - Create a plot of this function on the domain $x \in [-3, 3]$.
# - Where does $f(x) = 0$?

# In[ ]:





# In[ ]:





# In[ ]:





# ### Problem 2
# 
# - Define a function $f(x) = x^2 + 2x - 3$
# - Plot this function on the domain $x \in [-2, 5]$
# - Where does $f(x) = 0$?  How can you be sure?

# In[ ]:





# In[ ]:





# In[ ]:





# ### Problem 3
# 
# - Define a function $h(x) = \frac{1}{x + 4}$
# - Plot this function on the domain $x \in [-5, -3]$.  Is the function defined everywhere?  Explain.

# In[ ]:





# In[ ]:





# In[ ]:





# ### Problem 4
# 
# A company is interested in predicting the amount of revenue it will receive depending on the price it charges for a particular item. Using the data from Table 1.6, the company arrives at the following quadratic function to model revenue $R$ (in thousands of dollars) as a function of price per item $p$:
# 
# $$R(p)=p·(−1.04p+26)=−1.04p^2+26p$$
# 
# for $0\leq x \leq 25$.
# 
# - Predict the revenue if the company sells the item at a price of $p = \$5$ and $p = \$17$.
# - Find the zeros of this function and interpret the meaning of the zeros.
# - Sketch a graph of $R$.
# - Use the graph to determine the value of $p$ that maximizes revenue. Find the maximum revenue.

# In[ ]:





# In[ ]:





# In[ ]:





# ### Problem 5
# 
# Starting with the function $f(x) = x^2$ on the domain $x \in [-5, 5]$, describe the effect of the following transformations:
# 
# - $f(x) = -x^2$
# - $f(x) = x^2 + 3$
# - $f(x) = (x - 1)^2$
# 
# Your answer should be a single plot with 4 appropriate labels.

# In[ ]:





# In[ ]:





# In[ ]:





# ### Problem 6
# 
# In the context of artificial neural networks, the rectifier is an activation function defined as the positive part of its argument:
# 
# $\displaystyle f(x)=x^{+}=\max(0,x)$
# 
# where x is the input to a neuron. This is also known as a ramp function and is analogous to half-wave rectification in electrical engineering.  We can rewrite this as a piecewise function:
# 
# $$\displaystyle f(x)={\begin{cases}x&{\text{if }}x>0,\\0&{\text{otherwise}}.\end{cases}}$$
# 
# Define and plot the function on the domain $x \in [-5, 5]$ below.

# In[ ]:





# In[ ]:





# In[ ]:





# ### Problem 7
# 
# The cost of mailing a letter is a function of the weight of the letter. Suppose the cost of mailing a letter is 49¢ for the first ounce and 21¢ for each additional ounce. Write a piecewise-defined function describing the cost $C$ as a function of the weight $x$ for $0 \leq x \leq 3$, where $C$ is measured in cents and $x$ is measured in ounces.

# In[ ]:





# In[ ]:





# In[ ]:





# ### Problem 8
# 
# Given the pair of points $A = (-3, 3)$ and $B = (2, 1)$, find:
# 
# - The slope of the line through the points
# - An equation of a line through the points
# - Plot the points and line on the same graph.

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ### Problem 9
# 
# Total online shopping during the Christmas holidays has increased dramatically during the past 5 years. In 2012 $(t = 0)$, total online holiday sales were $\$42.3$ billion, whereas in 2013 they were $\$48.1$ billion.
# - Find a linear function $S$ that estimates the total online holiday sales in the year t.
# - Interpret the slope of the graph of S.
# - Use your equation to predict the year when online shopping during Christmas will reach $\$60$ billion.
# - Plot your function and its prediction.

# In[ ]:





# In[ ]:





# In[ ]:





# ### Problem 10
# 
# A house purchased for $250,000 is expected to be worth twice its purchase price in 18 years.
# - Find a linear function that models the price P of the house versus the number of years t since the original purchase.
# - Interpret the slope of the graph of P.
# - Find the price of the house 15 years from when it was originally purchased.

# In[ ]:





# In[ ]:





# In[ ]:





# ### Problem 11
# 
# Define and plot the following functions on the domain $x \in [-6, 6]$:
# 
# - $f(x) = \sin{x}$
# - $g(x) = \ln(x)$
# - $h(x) = e ^x$
# - $j(x) = \sin(x^2)$

# In[ ]:





# In[ ]:





# In[ ]:





# ### Problem 12
# 
# The number of hours of daylight in a northeast city is modeled by the function
# 
# $$N(t) = 12 + 3\sin[\frac{2\pi}{365}(t-79)]$$,
# 
# where t is the number of days after January 1.
# 
# - Find the amplitude and period.
# - Determine the number of hours of daylight on the longest day of the year.
# - Determine the number of hours of daylight on the shortest day of the year.
# - Determine the number of hours of daylight 90 days after January 1.
# - Sketch the graph of the function for one period starting on January 1.

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ## Functions and Data

# ### Problem 13
# 
# For each of the problems below, you are given a table and graph of a real world dataset.  You are asked to choose what kind of function you believe would be a good model of the data; *linear, quadratic, exponential*, or *trigonometric*.
# 
# The dataset below is on measurements of three different species of *iris* flowers. We have plotted the petal length on the horizontal axis and petal width on the vertical axis.  What kind of function would be a more appropriate model for this data where we input a measure of a petal length, and output a width? 

# In[1]:


from sklearn.datasets import load_boston, load_diabetes, load_iris
iris = load_iris()
iris = pd.DataFrame(iris.data, columns = iris.feature_names)
iris.head()


# In[ ]:


iris.plot('petal length (cm)','petal width (cm)', kind = 'scatter', title = 'Petal Length vs. Petal Width')


# ### Problem 14
# 
# The data below is from Motor Trend magazine and contains data on different models of cars from multiple manufacturers.  We have plotted the measurements for horsepower on the horizontal axis and miles per gallon on the vertical axis.  What kind of function do you think would be an appropriate model for this?

# In[ ]:


import pandas as pd
cars = pd.read_csv('https://raw.githubusercontent.com/jfkoehler/calcbook/master/intro/data/mtcars.csv')


# In[ ]:


cars.head()


# In[ ]:


cars.plot('hp', 'mpg', kind = 'scatter', title = 'Horsepower vs. Miles Per Gallon')


# ### Problem 15
# 
# The data below comes from the gapminder organization and contains data on countries GDP, Life Expectancy, and Population.  We have plotted the data from life expectancy in 2007 on the horizontal axis and GDP on the vertical axis.  What kind of relationship would be an appropriate model for this relationship?

# In[ ]:


gapminder = pd.read_csv('https://raw.githubusercontent.com/jfkoehler/calcbook/master/intro/data/gapminder_all.csv')


# In[ ]:


gapminder.head()


# In[ ]:


import matplotlib.pyplot as plt
gapminder.plot('gdpPercap_2007', 'lifeExp_2007', kind = 'scatter', title = 'Life Expectancy vs. GDP')
plt.ylabel('Life Expectancy')
plt.xlabel('GDP Per Capita');


# ### Problem 16
# 
# The data below comes from the Central Park weather station for the maximum temperature on each day since 1870.  We have plotted the most recent five years of the data where the date is on the horizontal axis and temperature on vertical.  What kind of a function would be the right model for this data?

# In[ ]:


temps = pd.read_csv('https://raw.githubusercontent.com/jfkoehler/calculus/master/data/2017018.csv', usecols=['DATE', 'TMAX'], 
                    parse_dates = ['DATE'], index_col='DATE')


# In[ ]:


temps.head()


# In[ ]:


temps['2015':].plot()
plt.title('Temperatures in Central Park')


# In[ ]:





# ## Using Models
# 
# For each of the questions below, you are given a model that your team of data scientists have developed based on a given dataset.  You are asked three main questions:
# 
# 1. Evaluate model at given value.
# 2. Compare model prediction to actual value.
# 3. Discuss whether the model is a good model for the data and why or why not.

# ### Problem 17: Iris Data
# 
# - **Model**: petal length = petal width $\times$ .7 or $f(x) = .7x$.

# Use the example observation below to compare the offered model to the real data.  How close was your prediction?  Was this good or bad?  Would you recommend this model for other data?  Explain.

# In[ ]:


iris.iloc[3]


# ### Problem 18: Cars
# 
# - **Model**: mpg = hp/10 or $f(x) = \frac{1}{10} x$ . 
# 
# Same questions above using the test point below.

# In[ ]:


cars.iloc[21]


# In[ ]:





# ### Problem 19
# 
# - Plot the function $f(x) = 3^x$ on $x \in [-5, 5]$.
# - Plot the function $g(x) = \ln(f(x))$ on $x \in [-5, 5]$.
# - Describe the transformation you observe.

# In[ ]:





# In[ ]:




