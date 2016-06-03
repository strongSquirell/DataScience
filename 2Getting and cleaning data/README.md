# Getting and cleaning data
This folder contains information how to get and clean data in R and Python(will add later).

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

## XML, JSON files

## From SQL

## HDF5 files

## Download from web, ftp

getwd()
setwd("C:\Users\Downloads")

Path:
  * Relative - ".\data"
  * Absolute - "C:\Users\data"

Checking for and creating directories
  * file.exists("directoryName")
  * dir.create("directoryName")

##### Download File from the Internet
  download.file(url, destfile, method, quiet = FALSE, mode = "w", cacheOK = TRUE,
                extra = getOption("download.file.extra"))

  * _url_ A character string naming the URL of a resource to be downloaded.
  * _destfile_ A character string with the name where the downloaded file is saved. Tilde-expansion is performed.
  * _method_ Method to be used for downloading files. Current download methods are "internal", "wininet" (Windows only) "libcurl", "wget" and "curl", and there is a value "auto": see ‘Details’ and ‘Note’.
  * _quiet_ If TRUE, suppress status messages (if any), and the progress bar.
  * _mode_ character. The mode with which to write the file. Useful values are "w", "wb" (binary), "a" (append) and "ab". Only used for the "internal" method.
  * _cacheOK_ logical. Is a server-side cached value acceptable?
  * _extra_ character vector of additional command-line arguments for the "wget" and "curl" methods.

##### Download File from the ftp server
The File Transfer Protocol (FTP) is a standard network protocol used to transfer computer files between a client and server on a computer network.

```{r, eval = F} # downloading complete folders via ftp with R
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

## Multiple files, zip
