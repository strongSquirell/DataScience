# Python Core

##### Built-in Types

  * Boolean: True, False
  * Numeric types: int, float, long, complex
  * Iterator type: container.__iter__(), iterator.__iter__(), iterator.next()
  * Sequence types: str, unicode, list, tuple, bytearray, buffer, xrange
  * Set types: set, frozeset
  * Mapping types: dict

__Lists__
```
l = list()
l = []
l[0:]
l.append(1)
l.extend([2,3])
l.insert(4,3)
l.remove(4,3)
l.pop()
l.index(1)
l.count(1)
l.sort()
l.reverse()
```
List comprehention
```
[ expression-involving-loop-variables for outer-loop-variable in outer-sequence for inner-loop-variable in inner-sequence ] 

This is equivalent to writing: 

results = []
for outer_loop_variable in outer_sequence:
    for inner_loop_variable in inner_sequence:
        results.append( expression_involving_loop_variables )
```

Example:
result = [ [x1, y1, z1] for x1 in range(X+1) for y1 in range(Y+1) for z1 in range(Z+1)  if (x1 + y1 + z1) != N ]

Nested Lists
```
students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
```

__Sets__
```
s = set()
s.add(1)
s.update([1,2])
s.remove(1)             # If that value is not present, it will raise a KeyError exception
s.discard(1)
a.union(b)
a.intersection(b)
a.difference(b) 
```

__Strings__
```
s[:5]
s.swapcase()
s.split()
"-".join(s)
s.find(s1, k)
s.isalnum() 
s.isalpha()
s.isdigit()
s.islower()
s.isupper()
s.ljust(width, '-')
s.rjust(width, '-')
s.center(width, '-')
textwrap.wrap(s, n)
textwrap.fill(s, n)  
```

##### Operations

  * Comparison operations: <; <=; >; >=; ==; !=; is; is not; and; or
  * +, -, *, /, //, %, (divmod(x,y)), -x, +x, x**y (pow(x,y))
  * Built-in operations: https://docs.python.org/2/library/functions.html#built-in-funcs 
  * Bitwise operations: |, ^, &, <<, >>, ~

// from __future__ import division

##### Reading and writing data
Console
```
N = list(map(int, raw_input().split))
print N
print "Hello %s %s! You just delved into python." % (firstName, lastName)
```

```
from __future__ import print_function
print(i, sep='', end='')
```

CSV
```
import csv
with open('D:/DataScience0/GrupoBimboKaggle/rawData/town_state.csv', 'rb') as csvfile1:
    with open('D:/DataScience0/GrupoBimboKaggle/tidyData/locations.csv', 'wb') as csvfile2:
        duplicatesReader = csv.reader(csvfile1)
        duplicatesWriter = csv.writer(csvfile2)
```
##### IF ELIF ELSE
```
if i == 0:
    print 0
elif i <= 0:
    print 'negative'
else:
    print 'positive'
```

##### Loops

```
for i in range(0, 5):
    print i
```

```
i = 0
while i < 5:
    print i
    i += 1
```

##### Functions
```
def functionname(parameters):
   function body
   return [expression]
```

##### Intertools
```
from itertools import product
from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement()

list(product([1, 2, 3], [4, 5]))     # cartesian product
list(permutations(l, n))
list(combinations(l, n))
l = [(len(list(cgen)), c) for c,cgen in groupby(s)]

```

##### Collections

collections.Counter() A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.

```
from collections import Counter
myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
print Counter(myList).items()
print Counter(myList).keys()
print Counter(myList).values()
Counter(myList)[1]
```

collections.defaultdict() The defaultdict tool is a container in the collections class of Python. It's similar to the usual dictionary (dict) container, but it has one difference: The value fields' data type is specified upon initialization.

```
from collections import defaultdict
d = defaultdict(list)
d['python'].append("awesome")
d['something-else'].append("not relevant")
d['python'].append("language")
for i in d.items():
    print i
```

collections.namedtuple(). They turn tuples into convenient containers for simple tasks

```
from collections import namedtuple
Point = namedtuple('Point','x,y')
pt1 = Point(1,2)
pt2 = Point(*[3,4])
dot_product = ( pt1.x * pt2.x ) +( pt1.y * pt2.y )
print dot_product
```

collections.OrderedDict() An OrderedDict is a dictionary that remembers the order of the keys that were inserted first. If a new entry overwrites an existing entry, the original insertion position is left unchanged.

```
ordDict = OrderedDict()
for i in xrange(int(raw_input())):
    line = raw_input().split()
    key = ' '.join(line[:-1])
    if key not in ordDict: 
        ordDict[key] = int(line[-1])
    else:
        ordDict[key] += int(line[-1])
```

collections.deque() A deque is a double-ended queue. It can be used to add or remove elements from both ends.

```
d = deque()
d.append(1)       #appendleft()
d.clear()
d.extend('1')     #extendleft()
d.count('1')
d.pop()           #popleft()
d.remove('1')
d.reverse()
d.rotate('3')
```

##### Date and time

_Calendar Module_

The calendar module allows you to output calendars and provides additional useful functions for them.
class calendar.TextCalendar([firstweekday])
This class can be used to generate plain text calendars.

```
import calendar
print calendar.TextCalendar(firstweekday=6).formatyear(2015)
```

##### Exeptions

_ZeroDivisionError_ 
This error is raised when the second argument of a division or modulo operation is zero.

_ValueError_ 
This error is raised when a built-in operation or function receives an argument that has the right type but an inappropriate value.

other: https://docs.python.org/2/library/exceptions.html#module-exceptions

_Handling exeptions_

```
#Code
try:
    print 1/0
except ZeroDivisionError as e:
print "Error Code:",e

#Output
Error Code: integer division or modulo by zero
```