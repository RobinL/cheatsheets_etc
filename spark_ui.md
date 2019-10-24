It's difficult to get the spark jupyter 'opinionated stack' running, and be able to see the spark UI.

The easiest way I've found to do it is in Jupyter installed locally, with a apache toree kernel

I installed Spark using Homebrew and then:
```
jupyter toree install --spark_home /usr/local/Cellar/apache-spark/2.4.4/libexec
/usr/local/Cellar/apache-spark/2.4.4/libexec/
```

Then once you run 
```
from pyspark.context import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql import Window

sc = SparkContext.getOrCreate()
spark = SparkSession(sc)
```
in a notebook
you can access the spark ui at `http://127.0.0.1:4040/`
