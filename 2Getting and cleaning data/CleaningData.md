# Cleaning data
This folder contains information how to clean data in R and Python(will be added later).  

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

## Creating new variables

## Reshaping

## Menaging Data Frames

## Merging data

## Editing text variables

## Regular expressions

## Working with dates

## Data resources