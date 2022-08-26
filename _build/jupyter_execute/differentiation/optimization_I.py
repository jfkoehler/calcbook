#!/usr/bin/env python
# coding: utf-8

# # Using Derivatives to Find Maximum and Minimum Values
# 
# **OBJECTIVES**
# - Use Derivatives to find maximum and minimum values
# - Understand what a *critical point* is and how to find them.
# - Use first derivatives to explore behavior near critical points
# - Use second derivatives to determine nature of critical point

# ## Review: Finding and Interpreting Derivatives
# 
# The problems below are meant to review our work finding derivatives of functions using rules and symbolic computer systems. In the questions below, your small group can use a table like that from [OpenStax](https://openstax.org/books/calculus-volume-1/pages/b-table-of-derivatives), use [Wolfram Alpha](https://www.wolframalpha.com/), or the `sympy` library in Python to determine your derivatives as necessary.    

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sympy as sy
from scipy.integrate import quad


# -----
# 
# **PROBLEMS**
# 
# 1. Find an equation of the line tangent to the graph of $f(x) = x(1 - 2x)^3$ at the point $(1, -1)$. 
# 2. If $f(x) = \sin(x)$ then $f'(\frac{\pi}{3}) = $?
# 3. If $f(x) = \sqrt{2x}$ then $f'(2)=$?
# 4. A particle moves along the $x$-axis so that at any time $t \geq 0$ its position is given by $x(t) = t^3 - 3t^2 - 9t + 1$.  For what values of $t$ is the particle at rest?
# 5. The area of the region enclosed by the graphs of $y = x$ and $y = x^2 - 3x + 3$ is?
# ------

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ## Review: Shapes of Graphs and Derivatives
# 
# ![Source: https://opentextbc.ca/calculusv1openstax/chapter/derivatives-and-the-shape-of-a-graph/](https://s3-us-west-2.amazonaws.com/courses-images/wp-content/uploads/sites/2332/2018/01/11210914/CNX_Calc_Figure_04_05_002.jpg)

# Use what you know about finding derivatives to complete the following sentences:
# 
# 1. If the function $f$ is increasing its derivative $f'$ is ______ ?
# 2. If the function $f$ is decreasing its derivative $f'$ is ______ ?
# 3. If a function $f$ is concave up on some interval, it's derivative $f'$ is _________ ?
# 4. If a function $f$ is concave down on some interval, it's derivative $f'$ is _________ ?

# **EXAMPLES**
# 
# 1. Use the function $f'(x) = 3x^2 - 6x - 9$ to determine where the function $f$ is increasing, decreasing, concave up, and concave down on the interval $[-4, 7]$. 
# 2. For $f(x) = x^3 + \frac{3}{2}x^2 + 18x$, find all intervals where $f$ is concave up and all intervals where $f$ is concave down. 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ## Optimization and Extremum: Fermat's Theorem
# 
# ![](https://upload.wikimedia.org/wikipedia/commons/f/f3/Pierre_de_Fermat.jpg)
# 
# One way to state Fermat's theorem is that, if a function has a local extremum at some point and is differentiable there, then the function's derivative at that point must be zero. In precise mathematical language:
# 
# Let ${\displaystyle f\colon (a,b)\rightarrow \mathbb {R} }f\colon (a,b) \rightarrow \mathbb{R}$ be a function and suppose that ${\displaystyle x_{0}\in (a,b)}{\displaystyle x_{0}\in (a,b)}$ is a point where ${\displaystyle f}$ has a local extremum. If $f$ is differentiable at $\displaystyle x_{0}$, then $f'(x_{0})=0$.

# ### Critical Points
# 
# <div class = "alert-info">
#     <p style="color:white"><strong>DEFINITION</strong></p>
#     <p>When dealing with functions of a real variable, a <strong style="color:white">critical point</strong> is a point in the domain of the function where the function is either not differentiable or the derivative is equal to zero.</p>
# </div>

# 1. Use the function $f'(x) = 3x^2 - 6x - 9$ to determine critical points of $f$. 
# 2. For $f(x) = x^3 + \frac{3}{2}x^2 + 18x$, find all critical points.

# In[ ]:





# In[ ]:





# ### First Derivative to determine Maximum or Minimum
# 
# 
# 1. Find all critical points of $f$.
# 2. Analyze the sign of $f'$ on intervals determined by the critical points.
# 3. If $f'$ goes from + to -, we have a maximum, from - to + we have a minimum, if the sign does not change we have neither.
# 

# Use our critical points from above to analyze the nature of the critical points.

# In[2]:


from IPython.display import IFrame


# In[3]:


IFrame(src = '', width = 300, height = 400)


# **PROBLEM**
# 
# Use the first derivative test to find the location of all local extrema for:
# 
# - $f(x) = 5x^{1/3} - x^{5/3}$. 
# - $g(x) = \sqrt[3]{x-1}$

# In[4]:


from sympy.functions.elementary.miscellaneous import cbrt


# In[5]:


def f(x): return 5*cbrt(x) - cbrt(x**5)


# In[6]:


x = sy.Symbol('x')


# In[7]:


sy.diff(f(x), x)


# In[8]:


equation = sy.Eq(sy.diff(f(x), x), 0)


# In[9]:


sy.solve(equation, x)


# In[10]:


def g(x): return cbrt(x-1)


# In[11]:


sy.diff(g(x), x)


# In[12]:


equation = sy.diff(g(x), x)


# In[13]:


sy.solve(equation, x)


# ### Second Derivative Test
# 
# Suppose that we have a critical point $x = c$. If:
# 
# - $f''(c) > 0$, then $f$ has a local minimum at $c$.
# - $f''(c) < 0$, then $f$ has a local maximum at $c$.
# - $f''(c) = 0$, then the test is inconclusive.

# **EXAMPLE**
# 
# Use the second derivative to find the location of all local extrema for $f(x) = x^5 - 5x^3$.

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# **PROBLEM**
# 
# AP Calculus Free-Response Question 2017 Problem 5.

# ![](images/ap_frq_2017_5.png)

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




