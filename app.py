

from flask import Flask

from flask import Blueprint


import sys
from pyspark import SparkContext, SparkConf
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from pyspark.streaming.kafka import KafkaUtils
from uuid import uuid1
import json
import time, sys, cherrypy, os

from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType

from demo.dictionary.ReadLogFile import dictionarySingleSetUp;
from demo.parsing.MatchLine import tokenMatchSingle;
from demo.dictionary.ReadLogFile import dictionaryDoubleSetUp;
from demo.parsing.MatchLine import tokenMatchDouble;
from demo.dictionary.ReadLogFile import dictionaryTripleSetUp;
from demo.parsing.MatchLine import tokenMatchTriple;

main = Flask(__name__)


#@main.route("/Downloads", methods=["GET","POST"])
#def run_Singledictionary():
#dictionarySingleSetUp('Zookeeper.log','SingleDictionaryzoo.txt');

#@main.route("/Downloads", methods=["GET","POST"])
#def run_doubledictionary():
#dictionaryDoubleSetUp('Zookeeper.log','DoubleDictionaryzoo.txt');


#@main.route("/Downloads", methods=["GET","POST"])
#def run_tripledictionary():
#dictionaryTripleSetUp('Zookeeper.log','TripleDictionaryzoo.txt');

#@main.route("/", methods = ["POST"])
#def run_MatchSingle():
#tokenMatchSingle('Zookeeper.log','LogEventSingle.txt','SingleDictionaryzoo.txt',3);

#@main.route("/", methods = ["POST"])
#def run_MatchDouble():
#tokenMatchDouble('Zookeeper.log','LogEventDouble.txt','DoubleDictionaryzoo.txt',2);

@main.route("/", methods=["GET"])
def updating():

    # Set up The Spark App
    conf = SparkConf().setAppName("Log_Analyzer").setMaster("local[2]").setSparkHome("C://spark//spark-2.4.2-bin-hadoop2.7").set("spark.executor.memory", "2g")
    # Create Spark Context
    sc = SparkContext(conf=conf)
    sss = sc.textFile("C://Users//skyba//Documents//GitHub//Log//logs//Zookeeper.txt")
    ssc = StreamingContext(sc, 3)

    # Input File Path
    lines = ssc.textFileStream("file:///Users/skyba/Documents/GitHub/Log/logs")
    dataStream = ssc.textFileStream("C://Zookeeper");
# sourceFile = os.path.join("C:/Users/skyba/Documents/GitHub/Log/logs", lines);
#inFile = open(sourceFile, 'r');
#logLines = inFile.readlines(100000);
    test = lines.flatMap(lambda line: line.split(","))
    test.pprint()
    #read_lines = lines.flatMap(lambda line: line.split(" ")) \
     #   .map(lambda x: (x, 1)) \
     #   .reduceByKey(lambda a, b: a + b)

    #tokenMatchTriple('Zookeeper.log', 'logEventTriplezoo.txt', 'TripleDictionaryzoo.txt', 'DoubleDictionaryzoo.txt', 2,3)
    #count = lines.map(tokenMatchTriple('Zookeeper.log', 'logEventTriplezoo.txt', 'TripleDictionaryzoo.txt', 'DoubleDictionaryzoo.txt', 2,3))
    ssc.start()
    ssc.awaitTermination()


        #print('rdd partitions: {}'.format(rdd.getNumPartitions()))
        #lines.map(lambda line: read_lines() ).count()


if __name__ == "__main__":
    main.run()
