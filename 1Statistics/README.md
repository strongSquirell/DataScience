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
_Mean_ - the sum of all the values divided by the number of observations.  

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

##### Distributions

_Random variable_ variables whose possible values are numerical outcomes of a random phenomemom: discrete(countable number of distinct values) and continuous(infinite number of possible values)  
Large sample -> relative frequencies = probabilities  
_Probability distribution_ a list of probabilities associated with each of the values: discrete(probability mass function) and continuous(probability density function)  

_Continuous uniform_ - outcome with equal density  
_Exponential_ - time between events; time until an event  
_Normal_ - values with a bell-shaped distribution (continuous)  
_Standart normal(Z)_ -standart scores  
_Binomial approximation_ - number of successes in large number of trials  
_Poison approximation_ - number of occurrences in a fixed time period   