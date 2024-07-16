#ver schema
from pyspark.sql.types import StructType
schema = df3.schema
print(schema)

from pyspark.sql.functions import sum
schema2 = "Produtos STRING, Vendas INT"
vendas = [["Caneta",10],["Lápis",20],["Caneta",40]]
df3 = spark.createDataFrame(vendas , schema2 )
agrupado = df3.groupBy("Produtos").agg(sum("Vendas"))
agrupado.show()
#podemos contatenar as operações, neste caso sem persitir
df3.groupBy("Produtos").agg(sum("Vendas")).show()