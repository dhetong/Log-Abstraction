import sys
from pyspark import SparkContext
from pyspark.streaming import StreamingContext

"""
This is use for create streaming of text from txt files that creating dynamically 
from files.py code. This spark streaming will execute in each 3 seconds and It'll
show number of words count from each files dynamically
"""


def main():
    sc = SparkContext(appName="PysparkStreaming")
    ssc = StreamingContext(sc, 1)   #Streaming will execute in each 3 seconds
    lines = ssc.textFileStream("C://Users//skyba//Documents//GitHub//Log")  #'log/ mean directory name
    #lines = ssc.socketTextStream(hostname='0.0.0.0',port='8000')

    counts = lines.map(lambda line: line)

    counts.pprint()
    ssc.start()
    ssc.awaitTermination()



if __name__ == "__main__":
    main()