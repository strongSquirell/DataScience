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
_dplyr package_
  * select - return a subset of the columns of a data frame
  * filter - extract a subset of rows from a data frame based on logical conditions
  * arrange - reorder rows of a data frame 
  * rename- rename variables in a data frame
  * mutate - add new variables or transform existing variables
  * summarise - generate summary statistics of a different variables in the data frame

Properties
  * The first argument is a data frame
  * The subsequent arguments describe what to do with it, and you can refer to columns directly
  * The result is a new data frame
  * Data frames must be properly formatted and annotated for this to all be useful
  * %>% - chain different operations

## Merging data
  * merge() merges data frames
  * important parameters: x, y, by, by.x, by.y, all
```
mergedData <- merge(X, Y, by.x = "solution_id", 
                    by.y = "id", all = TRUE)
intersect(names(X), names(Y))

library(plyr)
join(df1, df2)                                         # faster, but less full featured
dfList = list(df1, df2, df3)
join_all(dfList)
```
## Editing text variables
Text in data sets
  * Names of variables should be
    * All lower case when possible
    * Descriptive
    * Not duplicated
    * Not have underscores or dots or white spaces
  * Variables with character values
    * Should usually be made into factor variables
    * Should be descriptive (Male/Female instead of 0/1)

Fixing character vectors  
```
tolower(names(cameraData))
toupper(names(cameraData))
strsplit(names(cameraData), "\\.")                    # important parameters: x, split
sub("_", "", names(reviews),)                         # important parameters: pattern, replacement, x
gsub("_", "", testName)                               # substitude all underscores
```

Finding values  
```
grep("Almeda", x)                                     # returns vector of position
grepl("Almeda", x)                                    # returns vector of T/F
grepl("Almeda", x, value = TRUE)                      # returns the values where "Almeda" appears
```

Useful string functions  
```
library(stringr)
nchar("Alina")
substr("Alina", 1, 3)
paste("Alina", "is smart")
paste0("Alina", "is smart")                           # without any space between
str_stim("Alina         ")                            # remove spaces at the beginning or the end
```

Take first world from expression  
```
splitNames <- strsplit(names(names), " ")
firstElement <- function(x) {x[1]}
sapply(splitNames, firstElement)
```

## Regular expressions
_Regular expressions_ can be thought of as a combination of literals and metacharacters
_Metacharacters
  * __^__ i think - the start of the line
  * morning __$__ - the end of a line
  * __[__ Bb __]__ [Uu][Ss][Hh] -a set of characters we will accept at a given point in the match
  * ^[0 __-__ 9][a-zA-z] - range of letters or digits
  * [^?.]$ - ^ indicates matching characters not in the indicated class
  * 9 __.__ 11 - is used to refer to any character
  * flood __|__ blood - or (alternatives)
  * ^ __(__ [Gg]ood|[Bb]ad __)__
  * [Gg]eorge ([Ww]\.) __?__ [Bb]ush - expression is optional
  * __*__ - any number, including none, of the item
  * __+__ - at least one of the item, [0-9]+ (.*) [0-9]+
  * __{}__ - interval quantifiles, min and max number of matches (...){1,5}, {m}, {m,}
  * ()__\__ n - n matches 

## Working with dates
Date functions  
```
d1 <- date()                                         # class - "character"
d2 <- Sys.Date()                                     # class - "Date"
```

Formating dates  
```
format(d2, "%a %b %d")
```
  * %d = days as number
  * %a = abbreviated weekday
  * %A = unabbreviated weekday
  * %m = month(00-12)
  * %b = abbreviated month
  * %B = unabbreviated month
  * %y = 2 digit year
  * %Y = 4 digit year

Creating dates  
```
z <- as.Date(x, "%d%b%Y")
z[1] - z[2]
```

Converting to Julian  
```
weekdays(d2)
month(d2)
julian(d2)                                 # number of days that have occured since the origin date
```

Lubridate package  
```
library(lubridate)
ymd("20140108")                            # convert a number to a date
mdy("08/04/2013")
dmy("03-04-2013")
ymd_hms("2011-08-03 10:15:03", tz = "Pacific/Auckland")
wday(d1, label = TRUE)
```

Classes in R for dates: "Date", "POSIXct", "POSIXlt"

Change language in R time

```
sessionInfo()
Sys.setlocale("LC_TIME", "C")
```