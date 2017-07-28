## Tabula

I decided to test Tabula just because it is a popular library. It works specifically for tabular data. 

**The good**
It has a user friendly user interface and is very human centered. This is great for many use cases. My goal was to incorporate pdf extraction into a data pipeline. 
I decided to label the data and store it as json, a dense representation of data. In json, each "row" includes its labels. In tabular data, this is inferred.

**Appropriate use**
In my test data, the column headings didn't align with the data they should label. It was a simple correction and one that an individual working with a single document may well overlook. Still it was a correction that needed additional thought. An explicit mapping would have corrected for this prior to extraction. The explicit mapping works better for a pipeline purpose.

It seems slow. I'd have to benchmark to tell appropriately.

The UI


Faults
