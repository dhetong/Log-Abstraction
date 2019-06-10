

from flask import Flask

from flask import Blueprint
main = Flask(__name__)

from pyspark import SparkContext
from pyspark.streaming import StreamingContext

from demo.dictionary.ReadLogFile import dictionarySingleSetUp;
from demo.parsing.MatchLine import tokenMatchSingle;
from demo.dictionary.ReadLogFile import dictionaryDoubleSetUp;
from demo.parsing.MatchLine import tokenMatchDouble;
from demo.dictionary.ReadLogFile import dictionaryTripleSetUp;
from demo.parsing.MatchLine import tokenMatchTriple;


#@main.route("/Downloads", methods=["GET","POST"])
#def run_Singledictionary():
dictionarySingleSetUp('Zookeeper.log','SingleDictionaryzoo.txt');

#@main.route("/Downloads", methods=["GET","POST"])
#def run_doubledictionary():
dictionaryDoubleSetUp('Zookeeper.log','DoubleDictionaryzoo.txt');


#@main.route("/Downloads", methods=["GET","POST"])
#def run_tripledictionary():
dictionaryTripleSetUp('Zookeeper.log','TripleDictionaryzoo.txt');

#@main.route("/", methods = ["POST"])
#    def run_MatchSingle():
tokenMatchSingle('Zookeeper.log','LogEventSingle.txt','SingleDictionaryzoo.txt',3);

#@main.route("/", methods = ["POST"])
#    def run_MatchDouble():
tokenMatchDouble('Zookeeper.log','LogEventDouble.txt','DoubleDictionaryzoo.txt',2);

#@main.route("/", methods = ["POST"])
#    def run_MatchTriple():

sc = tokenMatchTriple('Zookeeper.log','logEventTriplezoo.txt','TripleDictionaryzoo.txt','DoubleDictionaryzoo.txt',2,3);
ssc = StreamingContext(sc, 2)
lines = ssc.socketTextStream("localhost", 9999)

if __name__ == "__main__":

    main.run(host='0.0.0.0',debug=True)
