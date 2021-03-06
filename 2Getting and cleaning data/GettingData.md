# Getting data
This file contains information how to get data in R and Python(will be added later).

__Data__ are values of qualitative or quantitative variables, belonging to a set of items.

The 4 things you should have:
  * The raw data
  * A tidy data set
  * A code book describing each variable and its values in the tidy data set
  * An explicit an exact recipe you used to go from the raw data to the tidy data set

The tidy data:
  1. Each variable you measure should be in one column
  2. Each different observation of that variable should be in a different row
  3. There should be one table for each kind of variable
  4. If you have multiple tables, they should include a column in the table that allows them to be linked

## Local files

``` 
read.table(file, header = FALSE, sep = "", quote = "\"'", dec = ".", numerals = c("allow.loss", "warn.loss", "no.loss"),
             row.names, col.names, as.is = !stringsAsFactors, na.strings = "NA", colClasses = NA, nrows = -1,
             skip = 0, check.names = TRUE, fill = !blank.lines.skip, strip.white = FALSE, blank.lines.skip = TRUE,
             comment.char = "#", allowEscapes = FALSE, flush = FALSE, stringsAsFactors = default.stringsAsFactors(),
             fileEncoding = "", encoding = "unknown", text, skipNul = FALSE)
``` 
__CSV__
``` 
read.csv(file, header = TRUE, sep = ",", quote = "\"",
           dec = ".", fill = TRUE, comment.char = "", ...)
``` 
__Delim__ (for reading delimited files, defaulting to the TAB character for the delimiter)
``` 
read.delim(file, header = TRUE, sep = "\t", quote = "\"",
             dec = ".", fill = TRUE, comment.char = "", ...)
``` 
 
  * _file_ the name of the file which the data are to be read from. 
  * _header_ a logical value indicating whether the file contains the names of the variables as its first line. 
  * _sep_ the field separator character. 
  * _quote_ the set of quoting characters. 
  * _dec_ the character used in the file for decimal points.
  * _numerals_ string indicating how to convert numbers whose conversion to double precision would lose accuracy.
  * _row.names_	a vector of row names. 
  * _col.names_	a vector of optional names for the variables. 
  * _as.is_ the default behavior of read.table is to convert character variables (which are not converted to logical, numeric or complex) to factors. The variable as.is controls the conversion of columns not otherwise specified by colClasses. 
  * _na.strings_ a character vector of strings which are to be interpreted as NA values. Blank fields are also considered to be missing values in logical, integer, numeric and complex fields. 
  * _colClasses_ character. A vector of classes to be assumed for the columns.
  * _nrows_ integer: the maximum number of rows to read in. Negative and other invalid values are ignored.
  * _skip_ integer: the number of lines of the data file to skip before beginning to read data.
  * _check.names_ logical. If TRUE then the names of the variables in the data frame are checked to ensure that they are syntactically valid variable names. If necessary they are adjusted (by make.names) so that they are, and also to ensure that there are no duplicates.
  * _fill_ logical. If TRUE then in case the rows have unequal length, blank fields are implicitly added.
  * _strip.white_ logical. Used only when sep has been specified, and allows the stripping of leading and trailing white space from unquoted character fields (numeric fields are always stripped). 
  * _blank.lines.skip_ logical: if TRUE blank lines in the input are ignored.
  * _comment.char_ character: a character vector of length one containing a single character or an empty string. Use "" to turn off the interpretation of comments altogether.
  *_allowEscapes_ logical. Should C-style escapes such as \n be processed or read verbatim (the default)? Note that if not within quotes these could be interpreted as a delimiter (but not as a comment character). For more details see scan.
  * _flush_ logical: if TRUE, scan will flush to the end of the line after reading the last of the fields requested. This allows putting comments after the last field.
  * _stringsAsFactors_ logical: should character vectors be converted to factors? Note that this is overridden by as.is and colClasses, both of which allow finer control.
  * _fileEncoding_ character string: if non-empty declares the encoding used on a file (not a connection) so the character data can be re-encoded. See the �Encoding� section of the help for file, the �R Data Import/Export Manual� and �Note�.
  * _encoding_	encoding to be assumed for input strings. 
  * _text_ character string: if file is not supplied and this is, then data are read from the value of text via a text connection. Notice that a literal string can be used to include (small) data sets within R code.
  * _skipNul_ logical: should nuls be skipped?
  * _..._ Further arguments to be passed to read.table.

__Excel__
``` 
  library(xlsx)
  read.xlsx(file, sheetIndex, sheetName=NULL, rowIndex=NULL, startRow=NULL, endRow=NULL, colIndex=NULL,
            as.data.frame=TRUE, header=TRUE, colClasses=NA, keepFormulas=FALSE, encoding="unknown", ...)
``` 
## XML, JSON files

__XML__
__Extensible Markup Language (XML)__ is a markup language that defines a set of rules for encoding documents in a format that is both human-readable and machine-readable.
Components:
  * Markup - labels that gives the text structure
  * Content - the actual text of the document

  * Tags corresponds to general labels:
    * Start tags <section>
    * End tags </section>
    * Empty tags <line-break />
  * Elements are specific examples of tags
  * Attributes are components of the label
```
library(XML)
fileUrl <- "http://www. ..."
doc <- xmlTreeParse(fileUrl, useInternal = T) # htmlTreeParse(fileUrl, useInternal = T)
rootNode <- xmlRoot(doc)
xmlName(rootNode)
rootNode[[1]]
rootNode[[1]][[1]]
xmlSApply(rootNode, xmlValue)
xpathSApply(rootNode, "//price", xmlValue)
```

__JSON__
  * Javascript Object Notation
  * Lightweight data storage
  * Common format for data from application programming interfaces (APIs)
  * Similar structure to XML but different syntax/format
  * Data stored as
    - Numbers (double)
    - Strings (double quoted)
    - Boolean (true or false)
    - Array (ordered, comma separated enclosed in square brackets)
    - Object (unordered, comma separated collection of key:value pairs in square brackets))

```
library(jsonlite)
jsonData <- fromJSON("https://api...")
names(jsonData)
jsonData$owner$login
myJson <- toJson(iris, pretty = T) # writing data frames to JSON
cat(myJson)
iris2 <- fromJSON(myJson)          # convert back to JSON 
```
## From SQL
__mySQL__ is an object-relational database management system (ORDBMS) with an emphasis on extensibility and standards-compliance. As a database server, its primary function is to store data securely, supporting best practices, and to allow for retrieval at the request of other software applications.

Data are structured in
  * Databases
  * Tables within databases
  * Fields within tables

```
install.packages("RMySQL")
DB <- dbConnect(MySQL(), user = "genome",
                hist = "genome-mysql.cse.uscs.edu")
result <- dbGetQuery(DB, "show databases;")
allTables <- dbListTables(DB)
dbListFields(DB, "TableName")
dbGetQuery(DB, "select count(*) from Table1")
query <- dbSentQuery(DB, "select * from ... where")
res <- fetch(query)
dbClearResult(query)
dbDisconnect(ucscDb)
```
Do not acces that server to delete, add or join things. 

## HDF5 files
__Hierarchical Data Format (HDF)__ is a set of file formats (HDF4, HDF5) designed to store and organize large amounts of data.
  * Supports storing a range of data types

HDF5 simplifies the file structure to include only two major types of object:
  * _Datasets_ multidimensional arrays of data elemens with metadata
    * Have a _header_ with name, datatype, dataspace, and storage layout
    * Have a _data array_ with the data
  * _Groups_ which are container structures which can hold datasets and other groups
    * Have a _group header_ with group name and list of attributes
    * Have a _group symbol table_ with a list of objects in group

```
source("http://bioconductor.org/bioLite.R")
biolite("rhdf5")
library(rhdf5)
created = h5createFile("example.h5")
created = h5createGroup("example.h5", "foo")
created = h5createGroup("example.h5", "foo/baa")
h5ls("example.h5")
h5write(A, "example.h5", "foo/A")                 # write to group matrix A
h5write(B, "example.h5", "foo/baa/B")             # write to group array B (attr(B, "scale") <- "liter")
h5write(df, "example.h5", "df")                   # write a data set df
readA= h5read("example.h5", "foo/A")              # read matrix A
h5write(c(12,13,14), "example.h5",                # write and read chunks
        "foo/A", index = list(1:3,1))
h5read("example.h5", "foo/A")
```
hdf5 can be used to optimize reading/writing from disc in R

## Download from web, ftp
```
getwd()
setwd("C:\Users\Downloads")
```

Path:
  * Relative - ".\data"
  * Absolute - "C:\Users\data"

Checking for and creating directories
  * file.exists("directoryName")
  * dir.create("directoryName")

dateDownloaded <- Date()

##### Download File from the Internet
```
  download.file(url, destfile, method, quiet = FALSE, mode = "w", cacheOK = TRUE,
                extra = getOption("download.file.extra"))
```

  * _url_ A character string naming the URL of a resource to be downloaded.
  * _destfile_ A character string with the name where the downloaded file is saved. Tilde-expansion is performed.
  * _method_ Method to be used for downloading files. Current download methods are "internal", "wininet" (Windows only) "libcurl", "wget" and "curl", and there is a value "auto": see ‘Details’ and ‘Note’.
  * _quiet_ If TRUE, suppress status messages (if any), and the progress bar.
  * _mode_ character. The mode with which to write the file. Useful values are "w", "wb" (binary), "a" (append) and "ab". Only used for the "internal" method.
  * _cacheOK_ logical. Is a server-side cached value acceptable?
  * _extra_ character vector of additional command-line arguments for the "wget" and "curl" methods.

##### Download File from the ftp server
The File Transfer Protocol (FTP) is a standard network protocol used to transfer computer files between a client and server on a computer network.


``` 
  library(RCurl)
  url <- "ftp://yourServer"
  userpwd <- "yourUser:yourPass"
  filenames <- getURL(url, userpwd = userpwd,
                      ftp.use.epsv = FALSE, dirlistonly = TRUE)
  filenames <- paste(url, strsplit(filenames, "\r*\n")[[1]], sep = "") 
  con <- getCurlHandle( ftp.use.epsv = FALSE) 
  contents <- mapply(download.file, filenames, basename(filenames)) 
  names(contents) <- filenames[1:length(contents)] 
```

## Webscraping
__Webscraping__ - programatically extracting data from the HTML code of websites.

```
url <- "http://"
con = url(url)                                         # 1st method
htmlCode = readLines(con)
close(con)

library(XML)                                           # parsing with XML
html <- htmlTreeParse(url, useInternalNodes = T)
xpathSApply(html, "//title", xmlValue)

library(httr)                                          # GET from the httr package
html2 = GET(url)
content2 = content(html2, as = "text")
parsedHtml - htmlParse(content2, asText = TRUE)
xpathSApply(html, "//title", xmlValue)

pg2 = GET(url, authenticate("user", "passwd"))         # accessing websites with passwords

google = handle("http://google.com")                   # using handles
pg1 = GET(handle = google, path = "/")
pg2 = GET(handle = google, path = "search") 
```

## Application Programming Interfaces(Twitter)

  * Creating an application (https://dev.twitter.com/apps)
  * Accesing Twitter from R

```
myapp = oauth_app("twitter", key = "yourConsumerKeyHere",
                   secret = "yourConsumerSecretHere")
sig = sign_oauth1.0(myapp, token = "yourTokenHere",
                    token_secret = "yourTokenSecretHere")
homeTL = GET("https://api.twitter.com/1.1/statuses/home_timeline.json", sig)
```
  * Converting the json object
```
json1 = content(homeTL)
json2 = jsonlite::fromJSON(toJSON(json1))
json2[1, 1:4]
```
httr allows GET, POST, PUT, DELETE request if you are authotized

## Multiple files, zip
__ZIP__

```
data <- read.table(unz("Sales.zip", "Sales.dat"), nrows=10, header=T, quote="\"", sep=",")
```

__Multiple files__

```
temp = list.files(pattern="*.csv")
for (i in 1:length(temp)) assign(temp[i], read.csv(temp[i]))
```
or
```
emp = list.files(pattern="*.csv")
list2env(
  lapply(setNames(temp, make.names(gsub("*.csv$", "", temp))), 
         read.csv), envir = .GlobalEnv)
```