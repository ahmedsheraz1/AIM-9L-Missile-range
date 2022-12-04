Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
from statistics import median
from math import isnan
from itertools import filterfalse
data = [20.7, float('NaN'),19.2, 18.3, float('NaN'), 14.4]
sorted(data)  # This has surprising behavior
[20.7, nan, 14.4, 18.3, 19.2, nan]
median(data)  # This result is unexpected
16.35
sum(map(isnan, data))    # Number of missing value
2
clean = list(filterfalse(isnan, data))  # Strip NaN values
clean
[20.7, 19.2, 18.3, 14.4]
sorted(clean)  # Sorting now works as expected
[14.4, 18.3, 19.2, 20.7]
median(clean)
18.75
