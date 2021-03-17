# Integration: Extra Examples

**OBJECTIVES**

- Use Riemann Sums to approximate Areas
- Develop and Implement Trapezoidal Rule for Area Approximation
- Introduce Monte Carlo methods for Area Approximation

## Riemann Sums

from IPython.display import IFrame
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
pd.options.display.float_format = '{:,.10f}'.format

drawing = IFrame(src = '', width = 400, height = 600)



$${\displaystyle S=\sum _{i=1}^{n}f(x_{i}^{*})\,\Delta x_{i}}$$

def f(x): return x**2
x = np.linspace(0, 1, 100)
plt.plot(x, f(x))
plt.axhline(color = 'black')
for xval in [0, 0.2, 0.4, 0.6, 0.8, 1.0]:
    plt.vlines(xval, 0, f(xval), color = 'black')
x2 = np.array([0, 0.2, 0.4, 0.6, 0.8, 1.0])
plt.step(x2, f(x2), where = 'post', color = 'black')
plt.grid()
plt.title('Left Handed Riemann Sum');

drawing

### Symbolic Solution

import sympy as sy

x, p = sy.symbols('x p')

sy.integrate(x**2, x)

sy.integrate(x**p, x)

sy.integrate(x**2, (x, 0, 1))

### Compare to our Approximation

def riemann(x, n):
    '''
    This function computes a left-handed
    riemann approximation for area under
    a function f over an interval x
    ======
    Arguments
    x = array; domain of interest
    n = integer; number of rectangles to use
    ======
    Returns
    area = float; area approximation
    '''
    #find the width
    width = (x[-1] - x[0])/n
    #where we find heights
    endpoints = [x[0] + width*i for i in range(n)]
    #find the heights
    heights = f(np.array(endpoints))
    #total area
    area = width*sum(heights)
    return area

x = np.linspace(0, 1, 100)

#approximation with 4 rectangles
riemann(x, 4)

#error with 4 rectangles
1/3 - riemann(x, 4)

#approximations for many n's
approxs = [riemann(x, i) for i in [4, 40, 400, 4000, 40_000, 400_000]]
#error in approximations
errors = [1/3 - approx for approx in approxs]

#dataframe of errors
error_df = pd.DataFrame({'subdivisions': [4, 40, 400, 4000, 40_000, 400_000], 
                         'riemann_area': approxs, 
                         'riemann_error': errors})

#examine the errors
error_df

### Trapezoid Rule

<center>
 <img src = https://upload.wikimedia.org/wikipedia/commons/thumb/1/11/Trapezoid.svg/440px-Trapezoid.svg.png />
</center>

$$\text{Area} = \frac{a + b}{2} \times h$$

def f(x): return x**2
x = np.linspace(0, 1, 100)
plt.plot(x, f(x))
# plt.ylim(-2, 2)
plt.axhline(color = 'black')
for xval in [0, 0.2, 0.4, 0.6, 0.8, 1.0]:
    plt.vlines(xval, 0, f(xval), color = 'black')
x2 = np.array([0, 0.2, 0.4, 0.6, 0.8, 1.0])
plt.plot(x2, f(x2), '-ro')
plt.grid();
plt.title('Trapezoidal Approximations of Area');

drawing

#domain
x = np.linspace(0, 1, 100)

#heights
heights = f(x)

np.array([2*f(i) for i in x2[1:-1]])

#areas
sum(f(x2[0]) + np.array([2*f(i) for i in x2[1:-1]]) + f(x2[-1]) )

.2*sum(f(x2[0]) + np.array([2*f(i) for i in x2[1:-1]]) + f(x2[-1]) )

.2/2*sum(f(x2[0]) + 2*f(x2[1:-1]) + f(x2[-1]))

1/3 - .2/2*sum(f(x2[0]) + 2*f(x2[1:-1]) + f(x2[-1]))

def trapezoid_approx(x, n):
    '''
    This function computes a 
    trapezoidal approximation for 
    the area under function f on x
    ======
    Arguments
    x = array; domain of interest
    n = integer; number of trapezoids to use
    ======
    Returns
    area = float; area approximation
    '''
    width = (x[-1] - x[0])/n
    bases = np.array([x[0] + i*width for i in range(n + 1)])
    heights = f(bases)
    areas = f(heights[0]) + sum(2*(heights[1:-1])) + f(heights[-1])
    return width/2*areas

trapezoid_approx(x, 4)

#approximations for many n's
approxs = [trapezoid_approx(x, i) for i in [4, 40, 400, 4000, 40_000, 400_000]]
#error in approximations
errors = [round(abs(1/3 - approx), 10) for approx in approxs]

error_df['triangular_approximation'] = approxs
error_df['triangular_errors'] = errors

error_df

### Alternative Approach: Monte Carlo Integration

<center>
 <img src = https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Le_casino_de_Monte-Carlo.JPG/440px-Le_casino_de_Monte-Carlo.JPG />
 </center>

x = np.linspace(0, 1, 1000)

random_x = np.random.choice(x)

plt.plot(x, f(x))
plt.plot(random_x, f(random_x), 'o')
plt.axhline(f(random_x))
plt.fill_between(x, f(random_x), color = 'gray', alpha = 0.2)

fig, ax = plt.subplots(1, 4, figsize = (15, 5))
for i in range(4):
    random_x = np.random.choice(x)
    ax[i].plot(x, f(x))
    ax[i].plot(random_x, f(random_x), 'o')
    ax[i].axhline(f(random_x))
    ax[i].fill_between(x, f(random_x), color = 'gray', alpha = 0.2)
    ax[i].set_title(f'Approximation {i}\nArea {f(random_x):.3f}')

$$\text{Area} = \frac{1}{n} \sum_{i = 1}^n \text{area}_i $$

fig, ax = plt.subplots(4, 4, figsize = (15, 10))
for i in range(4):
    for j in range(4):
        random_x = np.random.choice(x)
        ax[i,j].plot(x, f(x))
        ax[i,j].plot(random_x, f(random_x), 'o')
        ax[i,j].axhline(f(random_x))
        ax[i,j].fill_between(x, f(random_x), color = 'gray', alpha = 0.2)
        ax[i,j].set_title(f'Area {f(random_x):.3f}')
fig.suptitle('More Approximations with Monte Carlo');
plt.tight_layout();

np.random.choice(x, 100)

np.mean(f(np.random.choice(x, 4)))

approxs = [np.mean(f(np.random.choice(x, i))) for i in [4, 40, 400, 4000, 40_000, 400_000]]
errors = [abs(1/3 - approx) for approx in approxs]

error_df['monte_carlo_approx'] = approxs
error_df['monte_carlo_error'] = errors

error_df

### Problems

1. Compare the left-handed riemann approximation with $n = 100$, trapezoidal approximation with $n = 100$, and monte carlo approximation with $n = 100$ for the following functions on the given interval:

- $f(x) = \sin(\sin(x) - x)dx \quad [0, 2\pi]$
- $g(x) = \cos^{2020}(x) dx \quad [0, 2\pi]$

2. Approximating $\pi$.  The circular region in the first quadrant can be defined by $y = \sqrt{1 - x^2}$.  We can determine an approximation for $\pi$ by doing the following:

- Drop many random points on the square.
- If the points are less than $\sqrt{1 - x^2}$ we will count them, if they are outside the circle we will not
- Determine the ratio of points dropped to points counted, multiply by 4

Write a small python program to conduct this simulation and plot the results coloring the points accepted and rejected blue and red respectively.  How good was your approximation?











