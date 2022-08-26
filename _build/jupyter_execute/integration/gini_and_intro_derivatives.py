#!/usr/bin/env python
# coding: utf-8

# ### Reviewing Gini and Introduction to Derivatives
# 
# **OBJECTIVES**
# 
# 
# - Review slope and linear equations
# - Introduce derivatives
# - Explore relationships between graph of function and its derivative

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.integrate import quad


# ### Slope of a Line: Reminders
# 
# $$\text{slope} = \frac{y_1 - y_0}{x_1 - x_0}$$
# 
# - Find the slope of the line through $(8, 3)$ and $(4, 7)$.
# - Write an equation for the line above. 
# - Plot the line through the points.

# In[2]:


def f(x): return 3 - (x - 8)


# In[3]:


x = np.linspace(4, 8, 100)
plt.plot(x, f(x), '--')
plt.plot(8, 3, 'ro')
plt.plot(4, 7, 'ro')
plt.title('Line between (8, 3) and (4, 7)');


# In[ ]:





# In[ ]:





# **Problems**
# 
# - Plot the line $y = x^2$ on $[-2, 2]$, and on $[0.99, 1.01]$.  
# - What would the slope of the line in the second plot be? 
# - Write the equation of the line and plot it alongside the curve using the first domain.
# - Repeat the process above to approximate the equation for the line tangent to the function at $x = -1$.

# In[4]:


def f(x): return x**2
def l(x): return 1 + 2*(x - 1)
x = np.linspace(-2,2)
plt.plot(x, f(x))
plt.plot(x, l(x))
plt.plot(1, 1, 'o')


# In[5]:


slope = (f(1.01) - f(0.99))/(1.01 - .99)


# In[6]:


slope


# ### Finding the Derivative at Some Point
# 
# $$f'(x) = \frac{f(x + h) - f(x)}{h}$$

# In[7]:


#define the derivative
(f(-1 + 0.001) - f(-1))/(0.001)


# Use the equation above to determine the value of $f'(a)$.  Use that information to write the equation of the line tangent to $f$ at $x = a$. 
# 
# 1. $f(x) = x^2 + x, a = 1$
# 2. $f(x) = \frac{-3}{x - 1}, a = -2$
# 3. $f(x) = \frac{3}{x^2}, a = 3$

# In[8]:


def df(x): return (f(x + 0.001) - f(x))/0.001


# In[9]:


def f(x): return x**2 + x


# In[10]:


(f(1 + 0.001) - f(1))/0.001


# In[11]:


df(1)


# In[12]:


def f(x): return -3/(x - 1)


# In[13]:


df(-2)


# In[14]:


def f(x): return 3/x**2


# In[15]:


df(3)


# ### Rules for Derivatives
# 
# - Polynomials
# - Trigonometric
# - Exponential
# - Logarithmic
# 

# In[16]:


import sympy as sy


# In[17]:


x, y, p = sy.symbols('x y p')


# In[18]:


sy.diff(x**2, x)


# In[19]:


sy.diff(x**3, x)


# In[20]:


sy.diff(x**4, x)


# In[21]:


sy.diff(sy.sin(x), x)


# In[22]:


sy.diff(sy.cos(x), x)


# In[23]:


sy.diff(sy.exp(x), x)


# In[24]:


sy.diff(sy.log(x), x)


# ### A Function and its Derivative
# 
# Let $f(x) = x^5 + 2x^4 - x^3 - 2x^2$.  
# 
# a. Find $f'(x)$ and plot on [-2.5, 1.5].
# 
# b. Over what intervals does the graph of $f$ appear to be rising as you move left to right?
# 
# c. Over what intervals does the graph of $f'$ appear to be able the $x$-axis?
# 
# d. Over what intervals does the graph of $f$ appear to be falling as you move from left to right?
# 
# e. Over what intervals does the graph of $f'$ appear to be below the x-axis?
# 
# f. What are the $x$-coordinates of all the high points and low points of the graph of $f$?
# 
# g. For what value of $x$ does the graph of $f'$ appear to meet the $x$-axis?
# 
# Repeat for $y = \frac{x}{1 + x^2}$.  
# 
# On the basis of these examples, write a statement that relates where a function is rising, is falling, and has a high point or low point to properties you observed about the graph of its derivative.
# 
# 

# In[ ]:




