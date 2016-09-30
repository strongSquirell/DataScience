# Decision Trees 
Method of organizing decisions over time in the face of uncertainties  
Decision nodes:  
• Represented as boxes  
• Lines coming from the nodes represent different choices  

Event nodes:  
• Represented as circles  
• Lines coming from the nodes represent different outcomes    

_Building a decision tree_:  
Step 1. Map out Decision Problem  
Step 2. Assign Probabilities to Events  
Step 3. Evaluate the end nodes  
Step 4. Work Backwards and Evaluate  
evaluate event node: sum(expected value*probabilities)  
evaluate decision node: max(expected values)  

_Implementation_:  
• choose rule to split on  
• divide data using splitting rule into disjoint subsets  
• repeat recursively for each subset  
• stop when leaves are (almost) “pure”  
• key problem: choosing best rule to split on - idea: choose rule that leads to greatest increase in “purity”

Algorithms:  
• ID3 (Iterative Dichotomiser 3)  
• C4.5  
• CART (Classification and Regression Trees)  
• Random Forest (many decision trees)  

__ID3__  
• Core in other decision tree algorithms  
• Constructs the tree top down  
• Greedy search algorithm  (Finds local minimum at each iteration)
• Calculates information gain  

Entropy(S) = sum(-pi log_2 pi), pi - proportion of S belonging to class i  
Gain(S,A) = Entropy(S) - sum(Sv/S *Entropy(Sv)), Sv - examples belonging to class S, entropy after partition with attribute A  
• Information gain indicates reduction of entropy due to attribute partitioning  
• ID3 calculates information gain at each step  

Advantages:  
• Can be visualized  
• Computation complexity is small  
• Robust to noise  
• Can take wide range of data  
Disadvantages:  
• Tend to overfit  

To avoid overfitting  
• Use separate training and evaluation
datasets.  
• Consider using only the key features.  
• Limit number of branches

__Random Forest__  
Algorithm  
• Ensemble: use multiple models for prediction  
• Constructs a number of trees with random variations  
• Incorporates bagging  
• All trees predict by voting  

• Good for predicting complex datasets  
• Usually doesn’t overfit  
• Computationally slow.   