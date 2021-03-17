# Assignment 2

**OBJECTIVES**

- Solve discrete probability problems with binomial distributions
- Solve continuous probability problems with normal distributions
- Use summation notation and evaluate summation expressions

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import pandas as pd
from scipy.special import comb

for i in range(10):
    print([comb(i, j) for j in range(i + 1)])

## Problem I

In a candy factory, chocolate bars can be either acceptable or defective. The probability of a given bar being defective is 0.5.   

- Suppose we select 8 candy bars.  
  - How many ways different ways can we select 3 candy bars that are defective?
  - How many ways could we select 5 defective candy bars?
  - Make a plot of all possible outcomes.
  - Make a table of all possible outcomes.
  - If we select 8 bars, what is the probability that 2 will be defective? 
  - If we select 8 bars, what is the probability that at no more than 2 will be defective?













## Problem II

The probability of recovering from a certain disease is 90%.  Suppose that we select at random, 20 individuals currently suffering from the disease.  
- What is the probability that all 20 survive?
- What is the probability that at least 17 survive?
- Draw a graph of all possible outcomes and their probabilities.
- Construct a table of all possible outcomes and their probabilities.
- Suppose a drug manufacturer conducted a clinical trial for a new treatment of the disease.  The manufacturer found that in a sample of 50 individuals treated, that 49 survived.  How likely was this and do you think the new drug had an effect?















## Problem 3

For each example below, we are given a description for a binomial distribution where:

```
n = # of trials
p = probability of success
```

You are to build a table and graph for each, and answer the subsequent questions on the probability distribution.

- $n = 10, p = .2$, draw a bar plot of all possible outcomes and their probabilities
- With $n = 20, p = .2$, what is the probability of 12 successes?
- With $n = 30, p = 0.13$, what is the average aka expected value of the probability distribution?  Its variance?  Draw a plot of the distribution.
- With $n = 300, p = 0.13$, what is the average aka expected value of the probability distribution?  Its variance?  Draw a plot of the distribution.
- With $n = 3000, p = 0.13$, what is the average aka expected value of the probability distribution?  Its variance?  Draw a plot of the distribution.
- Using the three distributions above with $n = 30, 300, 3000$ and $p = 0.13$, explain what happens to the mean, variance, and graphs as you increase $n$.  
 













## Summations

Evaluate the following sums:
 
- $\sum_{i = 1}^5 2*i - 3$
- $\sum_{i = 1}^{10} \frac{1}{i}$
- $\sum_{i = 4}^9 3i^2 - 2i$

2*1 - 3 + 2*2 - 3 + 2*3 - 3 + 2*4 - 3 + 2*5 - 3

def s(x): return 1/x

np.arange(1, 11)

import numpy as np

sum(s(np.arange(1, 11)))

sum([1/1, 1/2, 1/3, 1/4, 1/5, 1/6, 1/7, 1/8, 1/9, 1/10])



## Problem 4: Normal Distribution

Use the information given about the mean and standard deviation of a normal distribution to answer the questions.

- Suppose $\mu = 10, \sigma = 3$.  Draw a plot of this distribution on $x = [0, 20]$.  What is the probability $x > 15$?
- Suppose $\mu = 0, \sigma = 3$.  Draw a plot of this distribution on $x = [-10, 10]$.  What is the probability $x < 0$?
- Suppose $\mu = 0, \sigma = 1$.  Draw a plot of this distribution on $x = [-3, 3]$.  What is the probability $-1 < x < 1$?













## Problem 5

- Suppose we have two dogs; one weighs 40 lbs and the other 60 lbs.  Your goal is to design a see saw that will balance the two dogs, one on each end.  Where should its center be?  Draw a picture with appropriate labels for distances and dog weights.













