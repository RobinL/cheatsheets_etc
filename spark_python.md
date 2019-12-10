```
from pyspark.context import SparkContext, SparkConf
from pyspark.sql import SparkSession, Row
import pyspark.sql.functions as f

conf=SparkConf()
conf.set('spark.driver.memory', '8g')
conf.set("spark.sql.shuffle.partitions", "8") 
conf.set("spark.jars.ivy", "/home/jovyan/.ivy2/")
 
sc = SparkContext.getOrCreate(conf=conf)

spark = SparkSession(sc)
```

data = [
            {"unique_id": 1, "name": "Robin"},
            {"unique_id": 2, "name": "John"},
            {"unique_id": 3, "name": "James"}
        ]
        
df = spark.createDataFrame(Row(**x) for x in data)
