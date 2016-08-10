# Classification
This folder will contain information about supervised learning - classification.

_Multiclass classification_  
  * one-vs-all - strategy involves training a single classifier per class, with the samples of that class as positive samples and all other samples as negatives. This strategy requires the base classifiers to produce a real-valued confidence score for its decision, rather than just a class label; discrete class labels alone can lead to ambiguities, where multiple classes are predicted for a single sample.
  * one-vs-one - eduction, one trains K (K ? 1) / 2 binary classifiers for a K-way multiclass problem; each receives the samples of a pair of classes from the original training set, and must learn to distinguish these two classes. At prediction time, a voting scheme is applied: all K (K ? 1) / 2 classifiers are applied to an unseen sample and the class that got the highest number of "+1" predictions gets predicted by the combined classifier.

### Logistic regression
y º {0,1} - binary classification problem  
0: 'Negative Class'  
0: 'Positive Class'  
Threshold classifier output h at 0.5:
  * if h > 0.5 predict y = 1
  * if h < 0.5 predict y = 0

Sigmoid/logistic function: h=g(Bx), g(t) = 1/(1+e^{-z})  
h = estimated probability that y = 1 on input x , P(y=1|x,B) 

Decision boundary:  
- 0 for linear, y = 1 if Bx >= 0, y = 0 if Bx < 0  
- 0 non-linear, y = 1 if f(Bx) >= 0, y = 0 if f(Bx) < 0  

Cost function:  
J(B) = 1/m sum(cost(h,y)) - convex function  
cost(h,y)= -ylog(h(x)) - (1-y)log(1-h(x)), y º {0,1}

Optimization algorithms:  
  * Gradient descent
  * Conjugate gradient
  * BFGS
  * L-BFGS  
Advantages:  
- no need to manually pick a  
- often faster than gradient descent  
Disadvantages:  
- more complex

_Multiclass classification(one-vs-all)_  
k - classes  
divide into k-1 binary problem  
hi(x) = P(y=i|x,B)  
train a logistic regression classifier hi for each class i to predict the probability that y=i
max hi(x)

_Multiclass classification(all-vs-all)_  
Build N(N?1) classifiers, one classifier to distinguish each pair of classes i and j. Let fij be the classifier where class i were positive examples and class j were negative. Note fji = ?fij. Classify using  
f(x) = arg max sum(fij(x))

### Naive Bayes

The Naive Bayes Classifier technique is based on so-called Bayesian theorem and is partikularly suited when the dimensionality of the inputs is high.

Input:  
a test set  
a fixed set of classes C  
Output:  
a predicted class c in C  

  * Simple (“naive”) classification  method based on Bayes rule	
  * Relies on very simple representation of document  
P(c|d) = P(d|c)P(c)/P(d) 

c_map = argmax P(d|c)P(c) = argmax(P(x1,...,xn|c)P(c))   
MAP is “maximum a posteriori” = most likely class  
Document d represented as features x1..xn  
Assumption:  
  * Assume position doesn`t mater
  * Assume the feature probabilities P(xi|cj) are independenr given the class c.  
P(x1,...,xn|c)= P(x1|c)P(x2|c)...P(xn|c)  

Learning:  
1. Maximum likelihood estimates
  * simply use the frequencies in the data
  * create a mega-document for topic j by concatenating all docs in this topic
  * problem: zero probabilities cannot be conditioned away  
P(xi|c) = (count(xi,c)+1)/sum(count(x,c)+1)  

• Very Fast, low storage requirements  	
• Robust to Irrelevant Features Irrelevant Features   
• Very good in domains with many equally important features  		
• Opimal if the	independence assumpions	hold  