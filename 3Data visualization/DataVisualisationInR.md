# Exloratory data analysis in R

_Principles of Analytic Graphics_
  * Show comparison
  * Show causality, mechanism, explanation, systematic structure
  * Show multivariate data
  * Integration of evidence
  * Describe and document the evidence with appropriate labels, scales, sources, etc.
  * Content is king

_Why do we use graphs in data analysis?_
  * to understand data properties
  * to find patterns in data
  * to suggest modeling strategies
  * to "debug" analysis
  * to communicate results

__Simple summaries of data__  
_One dimension_
  * Five-number summary (summary())
  * Boxplot             (boxplot(x, col = ""))
  * Histograms          (hist(x, col = "", breaks = ); rug(x); abline(median(x)))
  * Density plot        (plot(density(x)))
  * Barplot             (barplot(y))

_Two dimensions_
  * Multiple/overlayed 1-D plots
  * Scatterplots
  * Smooth scatterplots

_> 2 dimensions_
  * Overlayed/multiple 2-D plots; coplots
  * Use color, size, shap to add dimensions
  * Spinning plots
  * Actual 3-D plots

## Base plotting system
  * "Artist`s palette" model 
  * Start with blank canvas and build up from there
  * Start with plot function (or similar)
  * Use annotation functions to add/modify

  * Convenient, mirrors how we think of building plots and analyzing data
  * Can't go back once plot has started
  * Difficult to translate to others once a new plot has been created
  * Plot is just a series of R commands

The core plotting and graphics engine in R is encapsulated in the following packages:
  * _graphics:_ contains plotting functions for the "base" graphing systems, including __plot, hist, boxplot,__ ...
  * _grDevices:_ contains all the code implementing the various graphics devices, including X11, PDF, PostScript, PNG,...

There are 2 phrases to creating a base plot
  * initializing a new plot
  * annotating an existing plot
Calling plot(x, y) will launch a graphics device (if one is not already open) and draw a new plot on the device

```
library(datasets)
hist(airquality$Ozone)
with(airquality, plot(Wind, Ozone))
boxplot(Ozone ~ factor(Month), airquality, xlab = "Month", ylab = "Ozone")
```

Common paremeters
  * __pch__ the plotting symbol
  * __lty__ the line type(can be dashed, dotted, ...)
  * __lwd__ the line width
  * __col__ a colour to be used to fill the bars. The default of NULL yields unfilled bars
  * __main, xlab, ylab__ these arguments to title have useful defaults here
  * __type__ what type of plot should be drawn. Possible types are
    * "p" for points,
    * "l" for lines,
    * "b" for both,
    * "c" for the lines part alone of "b",
    * "o" for both ‘overplotted’,
    * "h" for ‘histogram’ like (or ‘high-density’) vertical lines,
    * "s" for stair steps,
    * "S" for other steps, 
    * "n" for no plotting.

The __par()__ function is used to specify global graphic parameters that affect all plots in an R session. These parameters can be overridden when specified as arguments to specific plotting functions.
  * __las__ the orientation of the axis labels on the plot
  * __bg__ the background color
  * __mar__ the margin size
  * __oma__ the outer margin size
  * __mfrow, mfcol__ number of plots per row, column (row-wise, column-wise)

_Base plotting functions_
  * __plot__ make a scatterplot, or other type of plot depending on the class of the object neing plotted
  * __lines__ add lines to a plot, given a vector x values and a corresponding vector of y values
  * __points__ add points to a plot
  * __text__ add text labels to a plot using specified x, y coordinates
  * __title__ add annotation to x, y axis labels, title, subtitle, outer margin
  * __mtext__ add arbitrary text to the margin ( inner or outer) of the plot
  * __axis__ adding axis ticks/labels

```
with(X, plot(x,y))
title(main = "Title")
with(X, plot(x, y, main = "Title", type = "n"))
with(subset(X, z >= 0), points(x, y, col = "blue"))
with(subset(X, z < 0), points(x, y, col = "red"))
legend("topright", pch = 1, col = c("blue", "red"), 
       legend = c("Above 0", "Under 0"))
abline(lm(x ~ y, X), lwd = 2)

par(mfrow = c(1, 2), mar = c(4, 4, 2, 1), oma = c(0, 0, 2, 0))       # multiple base plot
with(X, {
     plot(x, y)
     plot(x, y)
     mtext("General title")
})
```

## Graphics devices
A graphics device is something where you can make a plot appear
  * a window on your computer (screen device)
    * on a Mac it is launched with the quarts()
    * on Windows it is launched with windows()
    * on Unix/Linux it is launched with x11()
  * A PDF, PNG, JPEG, SVG (a dcalable vector graphics) file (file device)

The list of devices is found in __?Devices__.  
There are two basic approaches to plotting.  
First
  * call a plotting function
  * the plot appears on the screen device 
  * annotate plot if necessary
```
with(X, plot(x, y))
abline(lm(x ~ y, X))
```
Second
  * explicitly launch a graphics device
  * call a plotting function to make a plot
  * annotate plot if necessary
  * explicitly closr graphics device with __dev.off()__
```
pdf(file = "myplot.pdf")
with(X, plot(x, y))
abline(lm(x ~ y, X))
dev.off()
```

There are two basic types of file devices: _vector_ (pdf, svg, win.metafile, postscript) and _bitmap_ (png, jpeg, tiff, bmp) devices.  
  * vector formats are good for line drawing and plots with solid color using a modest number of point
  * bitmap formats are good for plots with a large number of points, natural scenes or web-based plots  

Multiple open graphics devices
  * It is possible to open multiple graphics devices 
  * Plotting can only occur on one graphics device at a time
  * The currently active graphics device can be found by calling __dev.cur()__
  * Every open graphics device is assigned an integer >=2
  * You can change the active graphics device with __dev.set(<integer>)__

Copying plots
  * __dev.copy()__ copy a plot from one device to another
  * __dev.copy2pdf()__  sprcifically copy a plot to a PDF file
```
with(X, plot(x, y))
dev.copy(png, file = "plot.png")
dev.off()
```

## Lattice plotting system
  * Plots are created with a single function call
  * Most useful for conditioning types of plots
  * Things like margins/spacing set automatically because entire plot is specified at once
  * Good for putting many plots on a screen

  * Sometimes awkward to specify an entire plot in a single function call 
  * Annotation in plot is not especially intuitive
  * Use of panel function and subscripting difficult to wield and requires intense preparation
  * Cannot "add" to the plot once it is created

The lattice plotting system is implemented using the following packages:
  * _lattice:_ contains code for producing Trellis graphics, which are independent of the "base" graphics system; includes functions like __xyplot, bwplot, levelplot__
  * _grid:_ implements a different graphing system independent of the "base" system; the lattice package builds on top of grid; we seldom call functions from the grid package directly

_Lattice plotting functions_
  * __xyplot__ this is the main function for creating scatterplots 
  * __bwplot__ box-and- whiskers plots 
  * __histogram__ histograms
  * __stripplot__ like a boxplot but with actual points
  * __dotplot__ plot dots on "violin strings"
  * __splom__ scatterplot matrix; like pairs in base plotting system
  * __levelplot, contourplot__ for plotting image data

Luttice functions generally take a formula for their first argument(y ~ x)  
```
library(lattice)
data <- transform(data, z = factor(z))
xyplot(y ~ x | z, data, layout = c(3,1))                             # splited by z
```

Lattice behavior
  * lattice graphics function return an object of class trellis
  * the print methods for lattice functions actually do not work of plotting the data on the graphics device
  * on the command line, trellis objects are auto-printed so that it appears the function is plotting the data

Lattice panel functions
  * lattice functions have a panel function which controls what happens inside each panel of the plot
  * the _lattice_ package comes with default panel functions, but you can supply your own if you want to customize what happens in each panel
  * panel functions receive the x/y coordinates of the data points in their panel
```
xyplot(y ~ x | f, panel = function(x, y, ...){
       panel.xyplot(x, y, ...)
       panel.abline( h = median(y), lty = 2)
})
```

## ggplot2
  * Splits the difference between base and lattice in a number of ways
  * Automatically deals with spacings, text, titles but also allows you to annotate by "adding" to a plot
  * Superficial similarity to lattice but generally easier/more intuitive to use
  * Default mode makes many choises for you

## Working with color