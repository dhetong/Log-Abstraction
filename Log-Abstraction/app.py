

from flask import Flask

from flask import Blueprint


import sys
from pyspark import SparkContext, SparkConf
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from pyspark.streaming.kafka import KafkaUtils

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

@main.route("/", methods=["GET","POST"])
def updating():

    sc = SparkContext(appName="PysparkStreaming")
    ssc = StreamingContext(sc, 1)  # Streaming will execute in each 3 seconds
    lines = ssc.textFileStream("C://Users//skyba//Documents//GitHub//Log")  # 'log/ mean directory name
    # lines = ssc.socketTextStream(hostname='0.0.0.0',port='8000')

    counts = lines.map(lambda line: line)

    p = counts.pprint()
    counts.saveAsTextFiles("C://Users//skyba//Documents//GitHub//Log//logs//file2.txt")
    ssc.start()
    ssc.awaitTermination()


if __name__ == "__main__":
    main.run()
