

from flask import Flask

from flask import Blueprint
main = Flask(__name__)

import json
from demo.dictionary.ReadLogFile import dictionarySingleSetUp;
from demo.parsing.MatchLine import tokenMatchSingle;
from demo.dictionary.ReadLogFile import dictionaryDoubleSetUp;
from demo.parsing.MatchLine import tokenMatchDouble;
from demo.dictionary.ReadLogFile import dictionaryTripleSetUp;
from demo.parsing.MatchLine import tokenMatchTriple;


@main.route("/logs", methods=["GET"])
def run_Singledictionary():
    dictionarySingleSetUp('Zookeeper.log','SingleDictionaryzoo.txt');

@main.route("/logs", methods=["GET"])
def run_doubledictionary():
    dictionaryDoubleSetUp('Zookeeper.log','DoubleDictionaryzoo.txt');


@main.route("/logs", methods=["GET"])
def run_tripledictionary():
    dictionaryTripleSetUp('Zookeeper.log','TripleDictionaryzoo.txt');

#@main.route("/", methods = ["POST"])
#    def run_MatchSingle():
    tokenMatchSingle('Zookeeper.log','LogEventSingle.txt','SingleDictionaryzoo.txt',3);

#@main.route("/", methods = ["POST"])
#    def run_MatchDouble():
    tokenMatchDouble('Zookeeper.log','LogEventDouble.txt','DoubleDictionaryzoo.txt',2);

#@main.route("/", methods = ["POST"])
#    def run_MatchTriple():
    tokenMatchTriple('AZookeeper.log','logEventTriple.txt','TripleDictionaryzoo.txt','DoubleDictionaryzoo.txt',2,3);

if __name__ == '__main__':
    main.run(host= 'schen@192.168.165.202')