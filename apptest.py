import os
import findspark
findspark.init('/spark/spark-2.4.2-bin-hadoop2.7')
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import json
os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-streaming-kafka_2.10:1.6.0 pyspark-shell'
sc = SparkContext(appName="PythonSparkStreamingKafka")
sc.setLogLevel("WARN")
ssc = StreamingContext(sc,5)
print('ssc =================== {} {}');
kafkaStream = KafkaUtils.createStream(ssc, 'victoria.com:2181', 'spark-streaming', {'imagetext':1})
print('contexts =================== {} {}');
lines = kafkaStream.map(lambda x: x[1])
lines.pprint()

ssc.start()
ssc.awaitTermination()



def decoder(msg):
    baseMessage = json.loads(zlib.decompress(msg[4:]))
    message = {"headers": baseMessage["headers"],
               "data": b64decode(baseMessage["data"])}
    return message