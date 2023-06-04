from ssas_api import SSAS
from pyspark.sql import SparkSession

ssas = SSAS(
    server='<YOUR_SERVER>',
    db_name='<YOUR_DATABASE>',
    username='<USERNAME>',
    password='<PASSWORD>'
)

dax_string = '''
//any valid DAX query
EVALUATE
CALCULATETABLE(MyTable)
'''

result = ssas.execute(dax_string)

spark = SparkSession.builder.appName("PythonSSAS").getOrCreate()

df = spark.createDataFrame(result)

df.show()