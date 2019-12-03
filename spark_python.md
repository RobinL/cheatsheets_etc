```
from pyspark.context import SparkContext, SparkConf
from pyspark.sql import SparkSession
import pyspark.sql.functions as f

conf=SparkConf()
conf.set('spark.driver.memory', '8g')
conf.set("spark.sql.shuffle.partitions", "8") 
conf.set("spark.jars.ivy", "/home/jovyan/.ivy2/")
 
sc = SparkContext.getOrCreate(conf=conf)

spark = SparkSession(sc)
```
