

from flask import Flask

import sys
from pyspark import SparkContext, SparkConf
from pyspark.streaming import StreamingContext



from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType

from demo.dictionary.ReadLogFile import dictionarySingleSetUp;
from demo.parsing.MatchLine import tokenMatchSingle;
from demo.dictionary.ReadLogFile import dictionaryDoubleSetUp;
from demo.parsing.MatchLine import tokenMatchDouble;
from demo.dictionary.ReadLogFile import dictionaryTripleSetUp;
from demo.dictionary.ReadLogFile import DictionaryUpload
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


import threading
from threading import Thread

@main.route("/", methods=["GET","POST"])
def updatingDictionary():
    dictionaryTripleSetUp('Zookeeper.log', 'TripleDictionaryZoo1.txt');
    tokenMatchTriple('Zookeeper.log', 'logEventTripleZoo5.txt', 'TripleDictionaryZoo1.txt', 'DoubleDictionaryZoo1.txt',2, 3);

    DictionaryUpload
    threading.Timer(3.0, updatingDictionary).start()

@main.route("/", methods=["GET","POST"])
def updating():

    sc = SparkContext(appName="PysparkStreaming")
    ssc = StreamingContext(sc, 1)  # Streaming will execute in each 1 seconds
    lines = ssc.textFileStream("/home/users/cchen/web")  # stream the change of new files in this folder
    # lines = ssc.socketTextStream(hostname='0.0.0.0',port='8000')

    counts = lines.map(lambda line: line)

    counts.pprint()
    counts.saveAsTextFiles("/home/users/cchen/web/results/result5_1sec") # save the result to the selected folder
    ssc.start()
    ssc.awaitTermination()



#@main.route("/", methods=["GET","POST"])
#def TripleLogs():
#tokenMatchTriple('Zookeeper.log', 'logEventTripleZoo5.txt', 'TripleDictionaryZoo1.txt', 'DoubleDictionaryZoo1.txt',2, 3);


if __name__ == "__main__":
    main.run(host="0.0.0.0",port=8899)
    Thread(target=updatingDictionary).start()
    Thread(target=updating).start()