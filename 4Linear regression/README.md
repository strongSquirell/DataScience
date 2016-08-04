# Linear regression
Learning algorithm:
  * supervised learning - labeled output (regression, classification)
  * unsupervised learning - unlabeled output (clustering(organize computing clusters, social network analysis, market segmentation, astronomical data analysis))

   training set  
        |  
learning algorithm   
        |    
input -> h -> output  

Assumption:  
  * linearity: for each predictor xj, xj and y linearly related for any combination of other x
  * homoscedasticity: variability of residuals for each predictor is the same over the entire range of values
  * independence of errors: residuals unrelated
  * normality of residuals
  * absence of regression outliers

Plan: 
  * expectations and analysis plan
  * data preparation
  * inspect data, check assumptions
  * perform analysis, interpret F-test
  * F significant? interpret individual t-test(summary(lm())
  * nested models? compare


Regression coefficient gives the change in the response variable per unit increase of that predictor given the values of the other predictors  
Pegression problem - predict real-valued problem

### Linear regression with one variable
n - number of training examples
x - input variable, features
y - output variable, target variable

h = b0+b1x  
Cost function:  
J(b0,b1) = 1/2n sum(h(xi)-yi)^2,  
J - convex -> local extremum -> global extremum  
_Gradient descent_:  
  * start with some b0, b1
  * keep changing b0, b1 to reduce J(b0, b1), bi=bi-a d/dbi J(b0, b1), a - learning rate 
  * end up at minimum  
if learning rate is too small, gradient descent can be slow  
if learning rate is too large, gradient descent can overshoot the minimum

### Multivariate linear regression  
m - number of features  
h = b0 + sum(bi*xi) = B`x, m features  
H_0: bi = 0, i > 0   
Multiple correlation R-squares(explained variation) = sum(yi-y`)(yi(hat)-y(hat)`)/SySy(hat),  
(total sum of squars - residuals sum of squares)/ total sum of squares, sum(yi(hat)-y`)^2/sum(yi-y`)^2  
Tests: 
  * Overall test: F = explained variance/(k-1)/error variance/(n-k), df1 = k-1, df2 = n-k (k=m+1)
  * Individual t-test: H_0: bi=0, controlling for other preditors, t = bi/SE, df = n-k 

Cathegorical predictors(indicators, dummy variables) = number of categories - 1 

Gradient descent:  
bj = bj - a d/dbj J(b0, ... , bm)  
- features scaling - make sure features are on a similar scale
  * mean normalization
  * z-score  
- debugging - nake sure gradient descent working correctly
  * plot cost function(number of iterations) as gradient descent runs, cost function should decrease  
if it increase -> try smaller a, =0.001, 0.01, 0.1

_Normal equation_:  
d/dbj J= 0, for all j  
b = (X`X)^{-1}X`y

| GD                   | NE                      |
|----------------------|-------------------------|
| need to choose a     | slow if m is very large |
| need many iterations |                         |

### Polynominal regression
h = b0+b1x+b2x^2 ... + bk xixj