# Statistics

__Descriptive Statistics__ - method of summarizing the information we have collected for an analysis.   
__Inferential Statistics__ - drawing conclusion about a population on the basis of only limited number of cases.   
_Variables_ - characteristics of something or someone.  
_Cases_ - something or someone.  

__Level of measurement__

|              |          | Difference | Order | Similar intervals | Meaningful zero point | Example |
|--------------|----------|------------|-------|-------------------|-----------------------|---------|
| Cathegorical | nominal  | +          | -     | -                 | -                     | gender  |
|              | ordinal  | +          | +     | -                 | -                     | win     |
| Quantitative | interval | +          | +     | +                 | -                     | age     |
|              | ratio    | +          | +     | +                 | +                     | height  |

_Data Matrix_ - overview of all cases and variables. The values in the cells of this table are called _observations_.  
_Frequency Table_ shows how the values are distributed over the cases (frequency, percentage, cumulative percentage).

__The distribution of a variable__ is a description of the relative numbers of times each possible outcome will occur in a number of trials.  
Summarizing a distribution:
  * graph (histogram, pie chart, dot plot, bar graph, ...)
  * center tendency (mode, median, mean) + variability

_Mode_ - value that occurs most frequently (nominal, ordinal level).  
_Median_ - the middle value of your observation when arranged from the smallest to the largest.  
_Mean_ -  a weighted average of the possible values, reflecting the fact that all outcomes might not be equally likely.   

__Variability__
  * _range_ - highest value - lowest value
  * _interquantile range_ divides values in 4 quantiles, Q1, Q2, Q3. IQR = Q3-Q1.  
An _outlier_ is an observation that lies an abnormal distance from other values in a random sample from a population(=value lower than Q1 - 1.5*IQR or higher Q3 + 1.5*IQR).
  * _box plot_ - graph to describe center, variability and outliers.  
  * _variance_ and _standart deviation_ - measure of dispersion (the average distance of an observation from the mean).
_z-score_ - number of standart deviations removed from the mean.  

```
x<-rnorm(10)
names(sort(-table(x)))[1]    # Mode
median(x)                    # Median
mean(x)                      # Mean
var(x)                       # Variation
sd(x)                        # Standard deviation
fivenum(x)                   # Tukey's five number summary, usefull for boxplots
IQR(x)                       # Interquartile range
quantile(x)                  # Compute sample quantiles
range(x)                     # Get minimum and maximum
(x[i]-mean(x))/sd(x)         # z-score
```

_Contingency table_ enabled you to display the relationship between two ordinal or nominal variables. Can be expressed with conditional and marginal proportions. For quantitative variables - scatterplot.

_Pearson`s R_
  * direction and strength of linear correlation
(strong/week, positive/negative, linear/curvilinear)

_Regression line_ line with the smallest sum of squared residuals

__Law of Large Numbers__ - as the number of randomly drawn observations (n) in a sample increases, the mean of the sample (x bar) gets closer and closer to the population mean µ. 

### Randomness and Probability

A _random variable_ is a variable whose value is a numerical outcome of a random phenomenon.  
A discrete random variable X has a finite number of possible values.  
A continuous random variable X takes all values in an interval. 

Gambler`s fallacy - fals idea that a random phenomenon can be predicted from a series of preceding random phenomena.

The _probability_ of any outcome of a random phenomenon can be defined as the proportion of times the outcome would occur in a very long series of repetitions.
  
Two events are _independent_ if the probability that one event occurs on any given trial of an experiment is not affected or changed by the occurrence of the other event.
Probability models describe, mathematically, the outcome of random processes. They consist of two parts:
  * S = Sample Space: This is a set, or list, of all possible outcomes
of a random process. An event is a subset of the sample space.
  * A probability for each possible event in the sample space S.

Probabilities range from 0 (no chance of the event) to 1 (the event has to happen).  
Because some outcome must occur on every trial, the sum of the probabilities for all possible outcomes (the sample space) must be exactly 1.  
Two events A and B are disjoint if they have no outcomes in common and can never happen together. The probability that A or B occurs is then the sum of their individual probabilities.  
The complement of any event A is the event that A does not occur, written as Ac. 
Two events A and B are independent if knowing that one occurs does not change the probability that the other occurs.   

Probability tree diagram - list of the possibilities.

We can assign probabilities either:  
  * empirically - from our knowledge of numerous similar past events
  * or theoretically - from our understanding of the phenomenon and symmetries in the problem

_Marginal probability_: the probability of an event occurring (p(A)), it may be thought of as an unconditional probability.  It is not conditioned on another event.  Example:  the probability that a card drawn is red (p(red) = 0.5).  Another example:  the probability that a card drawn is a 4  (p(four)=1/13).
 

_Joint probability_:  p(A and B).  The probability of event A and event B occurring.  It is the probability of the intersection of two or more events.  The probability of the intersection of A and B may be written p(A ? B). Example:  the probability that a card is a four and red =p(four and red) = 2/52=1/26.  (There are two red fours in a deck of 52, the 4 of hearts and the 4 of diamonds).
 

_Conditional probability_:  p(A|B) is the probability of event A occurring, given that event B occurs. Example:  given that you drew a red card, what’s the probability that it’s a four (p(four|red))=2/26=1/13.  So out of the 26 red cards (given a red card), there are two fours so 2/26=1/13.
Conditional probabilities reflect how the probability of an event can change if we know that some other event has occurred/is occurring.  
Bayes' theorem is stated mathematically as the following equation:  
P(A|B)=frac {P(B|A)P(A)/P(B)
where A and B are events and P(B) not equals 0.

P(A) and P(B) are the probabilities of observing A and B without regard to each other.
P(A | B), a conditional probability, is the probability of observing event A given that B is true.
P(B | A) is the probability of observing event B given that A is true.

Permutation
  * repetition allowed - n^r
  * repetition not allowed - n!/(n-r)! 
Combination
  * repetition allowed - n!/(r!(n-r)!)
  * repetition not allowed - (n+r-1)!/(r!(n-1)!) 

### Distributions

_Random variable_ variables whose possible values are numerical outcomes of a random phenomemom: discrete(countable number of distinct values) and continuous(infinite number of possible values)  
Large sample -> relative frequencies = probabilities  
_Probability distribution_ a list of probabilities associated with each of the values: discrete(probability mass function) and continuous(probability density function)  
_Probability density function_ - probability per unit of the random variable  

_Continuous uniform_ - outcome with equal density  
_Exponential_ - time between events; time until an event  
_Normal_ - values with a bell-shaped distribution (continuous), symmetric, characterized by their mean and standart deviation 
_Standart normal(Z)_ -standart scores  
_Binomial approximation_ - number of successes in large number of trials  
_Poison approximation_ - number of occurrences in a fixed time period  

__Central limit theorem__ states that, given certain conditions, the arithmetic mean of a sufficiently large number of iterates of independent random variables, each with a well-defined (finite) expected value and finite variance, will be approximately normally distributed, regardless of the underlying distribution  

