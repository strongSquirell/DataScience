### Regularization

underfit/high bias - if our algorithm works badly with points in our data set

overfit/high variance - a statistical model describes random error or noise instead of the underlying relationship (If our algorithm works well with points in our data set, but not on new points)

Addressing overfitting:
  * Reduce number of features
    * Manually select which features to keep
    * Model selection algorithm
  * Regularization
    * Keep all the features but reduce magnitude/values of parameters
    * Works well when we have a lot of features, each of which contributes a bit to predicting y  
 
J(B) = 1/m sum(h(xi)-yi) + lambda*sum(bj^2), lambda - regularization parameter

Machine learning diagnostic - a test that you can run to gain insight what is/isn`t working with a learning algorithm, and gain guidance as to how best to improve its performance.

Diagnostic bias vs variance:  
Plot Jtrain and Jcv y = error x = degree of polynomial(for example)

Fix:
  * high variance(Jcv>>Jtrain)
    * try geting more training examples
    * try smaller sets of feature
    * try increasing lambda
  * high bias(Jcv=Jtrain will be high)
    * try getting additional features
    * try adding polynominal features
    * try decreasing lambda

Evaluation the hypothesis:  
1. Split data into training/test sets(70/30) or training/ cross-validation/ test sets(60/20/20)  
2. Learn parameter from training set  
3. Choose model from cross-validation set  
4. Compute training, criss-validation, test errors  

Model selection:  
d - degree of polynomial  
d=1  h = b0+b1x  
d=2  h = b0+b1x+b2x^2  
...  
models -> min J(B) -> B -> Jcv(B) -> pick model -> estimate generalization error for test set

### Machine learning system design

Approach:  
1. Start with a simple algorithm that you can implement quickly, implement it and test it on your cv data  
2. Plot learning curves to deside if more data, ..., are likely to help  
3. Error analysis: manually examine the examples in cv set that your algorithm made error on. See if you spot any systemetic trend in what type of examples it is making error  

Skewed classed - a lot more of examples from one class than from the other class.  
Precision = TP/(TP+FP)  
Recall = TP/(TP+FN)  
h > treshold  
higher treshold -> higher precision and lower recall  
F = 2PR/(P+R) (bigger - better)  

Large data rationale - assume feature x has sufficient information to predict y accurately  
  * use a learning algorithm with many parameters
  * use a very large training set



