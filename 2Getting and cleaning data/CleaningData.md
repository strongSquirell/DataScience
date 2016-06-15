# Cleaning data
This file contains information how to clean data in R and Python(will be added later).  

## Subseting and sorting
_Subseting_  
```
X[, 1]                                   # first column
X[1:2, "var1"]
X[X$var1 <= 3 & X$var3 > 11,]            # logical subseting
X[X$var1 <= 3 | X$var3 > 11,]
X[which(X$var2 > 8),]                    # return indeces
```  

_Sorting_  
```
sort(X$var1)
sort(X$var1, decreasing = TRUE)
sort(X$var1, na.last = TRUE)
X[order(X$var1),]                        # ordering data frame X by var1

library(plyr)
arrange(X, desc(var1))
```

_Adding rows and columns_  
```
X$var4 <- y                              # add column
Y <- cbind(X, y)
```

## Summarizing
Looking at a bit of the data  
```
head(X, n = 3)
tail(X, n = 3)
```
Make summary  
```
summary(X)                                # show min, max, quartiles, mean
str(X)                                    # info about data frame 
quantile(X$var1, na.rm = TRUE, 
         probs = c(0.5, 0.75, 0.9))
```
Make table  
```
table(X$var1, useNA = "ifany")
table(X$var1, X$var2)
```
Check for missing values  
```
sum(is.na(X$var1))
any(is.na(X$var1))                        # returns T/F           
all(is.na(X$var1))
colSums(is.na(restData))
``` 
Values with specific characteristics  
```
table(X$var1 %in% c("a","c"))
```
Cross tabs  
```
DF = as.data.frame(data)
xt <- xtabs(Freq ~ Gender + Admit, data = DF)
```
Size of data set  
```
object.size(DF)
print(object.size(DF), units = "Mb")
``` 

## Creating new variables
  * Often the raw data won`t have a value you are looking for
  * You will need to transform the data to get the values you would like
  * Usually you will add those values to the data framed you are working with
  * Common variables to create
    * Missingness indicators
    * Cutting up quantitative variables
    * Applying transform  

_Creating sequences_  
```
seq <- seq(1, 10, by = 2)
seq <- seq(1, 10, length = 3)
seq <- seq(along = x)                   # indices for x                               
```  

_Creating binary variables_  
```
X$var5 <- ifelse(X$var1 < 0, TRUE, FALSE)
```

_Creating cathegorical variables_  
```
X$Groups <- cut(X$var1, breaks = quantile(X$var1))

library(Hmisc)
X$Groups <- cut2(X$var1, q = 4)
```

_Creating factor variables_  
```
X$varf <- factor(X$var1)
yesnofac <- factor(x, levels = c("yes", "no"))
relevel(yesnofac, ref = "yes")
as.numeric(yesnofac)
```

_Using the mutate function_
```
library(Hmisc)
library(plyr)
X2 <- mutate(X, Groups = cut2(X, g = 4))
```

_Common transforms_
  * abs(x)
  * sqrt(x)
  * ceiling(x)
  * floor(x)
  * round(x, digits = n)
  * signif(x, digits = n)
  * cos(x), sin(x)
  * log(x), log2(x), log10(x)
  * exp(x)

## Reshaping
The goal is tidy data
  * each variable forms a column
  * each observation forms a row
  * each table/file stores data about one kind of observation
_Reshaping_  
```
library(reshape2)
carMelt <- melt(mtcars, id = c("carname", "gear", "cyl"),      # melting data frame (cut)
                measure.vars = c("mpg", "hp"))
cylData <- dcast(carMelt, cyl ~ variable, mean)                # casting data frame
tapply(InsectSprays$count, InsectSprays$count, sum)            # summing values
spIns = split(InsectSprays$count, InsectSprays$count)
sprCount = lapply(spIns, sum)
unlist(sprCount)
sapply(spIns, sum)
library(plyr)
spraySum <- ddply(InsectSprays, .(spray), summarize,           # creating a new variable
                  sum = ave(count, FUN = sum))
```
Also useful functions
  * acast() - for casting as multi-dimensional arrays
  * arrange() - for faster reordering without using order() commands
  * mutate() - adding new variables


## Menaging Data Frames

## Merging data

## Editing text variables

## Regular expressions

## Working with dates

## Data resources