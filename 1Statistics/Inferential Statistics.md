Statistical inference methods:
  * estimation
  * test hypothesis   
_Estimation_  
  * Point-estimate - single number that is  best quess for the population parameter
  * Interval estimate - range of values within which we espect the parameter to fall

_Confidence level_ - probability that interval contains population parameter (most common 0.95)
_Confidence interval_  
  * with known population sd - x +- z_asigma_x
  * with unknown population sd - x +- t_aSE, SE- standart error = s/sqrt(n)

_T - distribution_ - bell-shaped, symmetric, mean of 0, takes into account extra error for small distribution  
df - degrees of freedom, df = n-1  
T-dist ~ N(0,1) df = infty

Assumptions:  
  * randomization 
  * population approximately normal
  * no extreme outliers

95% confidence interval - 95% confident that our point estimate falls within our confidence interval  
confidence vs precision

Constructinf a confidence interval:  
1. Which confidence level  
2. Proportion or mean  
3. Compute endpoints of interval  
4. Interpret results substantively  

Hypotheses - expextation about population  
Significance test - test hypotheses on sample data  
_Null hypothesis testing_  
H_0 - null hypothesis  
H_a - alternetive hypothesis  
H_0 and H_a - mutually exclusive  
H_0 - the parameter you are interested in takes a specific value, will be rejected if the data in your sample suggest it is highly unlikely expectation  
H_a - claims that the parameter you are interested in falls within an alternative range of values
H_0  - assumed to be true unless convincing evidence proofs otherwise

Failing to reject your null hypothesis doesn`t mean that the null hypothesis is true.

Proportions:    
_test statistic_ - number of standart errors sample value is removed from H_0 value, z = (p- pi_0)/se_0  
_p -value_ shows that finding a sample proportion of x if the population proportion y is p% probable 
_significance level_ - how small p-value needs to be to reject H_0

alpha = 0.05
  * one-tailed test(p>p_0 | p<p_0) - z_0 = -1.64, z < z_0 - rejection region
  * two tailed test(p!=p_0) - z_0 = 1.96,  z < - z_0, z > z_0 - rejection region

p < alpha - rejection region

Mean:  
t = (x - mu_0)/se, se = s/sqrt(n)

Plan:
  * Proportion or mean? 
  * Formulate hypotheses: Ho: p = p_0 H_a: p>p_o, p!=p_0
  * Check assumptions(randomization, sample size)
  * Determibe alpha
  * Compute test statistic
  * Draw sampling distribution
  * Find location of test statistic
  * Reject H_0?
  * Interpret finding

_Errors_:
  * Type I - hypothesis is true and you decide to reject it(alpha) FP
  * Type II - hypothesis is false and you not decide to reject it(beta) FN  
Decrease significant level - decrease the probability of making a type I error, but increase the probability of making a type II error  
_power_ - probability of rejecting H_0 giben it is false (1-beta) 
larger alpha/sample/sample - more power  
test type: one-side has more power than two-side, parametric vs non-parametric 

### Comparing two groups

__Independent__  
_Z -test for independent proportions_:
  * binary response variable
  * binary independent variable   
Assumptions:
  * independence(randon assignment and/or selection)
  * sufficient number of observation(violation - Fisher`s exact test)

Hypothesis:  
H_0: p1 = p2  
H_a: p1 != p2, >, <.  
z=(p1-p2)/sqrt(p(1-p)(1/n1+1/n2)), p = (n1p1+n2p2)/(n1+n2)
p <= alpha -> reject H_o

CI = p1-p2 +- z_(alpha/2)sqrt(p1(1-p1)/n1+p2(1-p2)/n2)

```
prop.test(x, n, p = NULL,
          alternative = c("two.sided", "less", "greater"),
          conf.level = 0.95, correct = TRUE)
```

_t-test for independent means_:
  * quantitative response variable
  * binary independent variable   
Assumptions:
  * independence(randon assignment and/or selection)
  * normally distributed(violation - no proplem if large sample or 2-sided test)  
Hypothesis:  
H_0: m1 = m2  
H_a: m1 != m2, >, <.  
t = (m1-m2)/sqrt(s1^2/n1+s2^2/n2), df = (s1^2/n1+s2^2/n2)^2/(1/(n1-1) (s1^2/n1)^2+1/(n2-1) (s2^2/n2)^2)

if equal variances - larger df, smaller se (assumption: larger sd/smaller sd < 2)

CI = x1-x2 +- t_(alpha/2)SE

```
t.test(x, y = NULL,
       alternative = c("two.sided", "less", "greater"),
       mu = 0, paired = FALSE, var.equal = FALSE,
       conf.level = 0.95, ...)
```

__Dependent__

_McNewar`a test for dependent proportions_
  * binary response variable
  * binary independent variable
  * related/paired samples(same cases - different time, matched pairs)   
Assumptions:
  * sufficient observation
  * 1-sided: n01+n10 >= 30  
Hypothesis:  
H_0: p1 = p2  
H_a: m1 != m2, >, <.  
z = (n01-n10)/sqrt(n01+n10)

```
mcnewar.test(matrix)
```

_t-test for dependent means_:
  * quantitative response variable
  * binary independent variable   
  * related/paired samples
Assumptions:
  * normally distributed(violation - no proplem if large sample or 2-sided test)  
Hypothesis:  
H_0: md=0  
H_a: md != 0, >, <.  
t = md/sd/sqrt(n), df = n-1

```
t.test(x,y,data,paired=T)
```
__Controling variables__

How to control variable(if related to both independent and dependent variable):
  * experimental
  * statistical

Spurious relation can be explain by common cause  
Experimental control:
  * randomization
  * keeping constant  
Statistical control 
  * measure and check at every level of control variable(if it behaves the same at all levels - var does not provide alternative explanation)

Control variables:
  * confounder - common cause in both dependent and independent var 
  * moderator - relation becomess weaker or stronger dependent on moderator
  * mediator - indep var influence dep var through this mediator

Simpson`s paradox - direction indep var ~ dep var changes due to control var
  
### Cathegorical association
Relation between cathegorical variables:
  * contingency table
  * joint/marginal/conditional probabilities

Correlation coefficient - quantify relation between 2 vars. 
 
Marginal probability: the probability of an event occurring (p(A)), it may be thought of as an unconditional probability.  It is not conditioned on another event.  Example:  the probability that a card drawn is red (p(red) = 0.5).  Another example:  the probability that a card drawn is a 4  (p(four)=1/13).
 
Joint probability:  p(A and B).  The probability of event A and event B occurring.  It is the probability of the intersection of two or more events.  The probability of the intersection of A and B may be written p(A ? B). Example:  the probability that a card is a four and red =p(four and red) = 2/52=1/26.  (There are two red fours in a deck of 52, the 4 of hearts and the 4 of diamonds).
 
Conditional probability:  p(A|B) is the probability of event A occurring, given that event B occurs. Example:  given that you drew a red card, what’s the probability that it’s a four (p(four|red))=2/26=1/13.  So out of the 26 red cards (given a red card), there are two fours so 2/26=1/13.

_Chi-squared for cathegorical var independence(association)_:  
Assumptions:
  * random sample or randomized experiment
  * cathegories are exclusive
  * cathegories are exhaustive
  * sample large  
Requirement: each cathegory has frequency equals at least 5  
H_0: variables X and Y are independent  
H_a: variables X and Y are dependent

expected joint frequencies = (nrX + nrY)/total nr  
Chi-squared = sum((observed-expected)^2/expected)  
df = (r-1)(c-1), r-row, c-column  - mean  
more degreed of freedom - less skewed, wider, higher values for chi-squared  
p-value is small -> reject H_0

Strength of association between 2 nominal vars - Cramer`s V = sqrt( chi-squared/(nm)), n - total number of counts, m = min(r,c)-1  
table less square -> V higher without evidence of association

Pattern of association: residual/se, se = sqrt(res(1-prob_c)(1-prob_r))  
Two observed distribution can be compared

_Chi-squared test for goodness of fit_:  
compare an observed frequency distribution with a frequency distribution you expect on a basis of a theory  
H_0: observed = expected  
H_a: observed != expected

Chi-squared = sum((observed-expected)^2/expected), df = N-1  
large Chi-squared, small p-value, reject H_0

_Fishers`s exact test_(if sample is small):  
|   |  A  |  B  |
|---|:---:|----:|
| 1 |  a  |  b  |
| 2 |  c  |  d  |

H_0: Observed count = expected count  
H_a: Observed count != expected count  
k possible configurations (+-1)
probability of specific configuration = (a+b)!(c+d)!(a+c)!(b+d)!/(n!a!b!c!d!)


### Non-parametric tests