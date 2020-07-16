import MapReduce
import sys

mr=MapReduce.MapReduce()

def mapper(record):
    mappingKey=record[1]
    mr.emit_intermediate(mappingKey, record)

def reducer(key,listOfValues):
    baseElement=listOfValues[0]
    for value in listOfValues:
        if(baseElement[0]!=value[0]):
            mr.emit((baseElement+value))

#main Program
if __name__=="__main__":
    inputData=open(sys.argv[1])

    mr.execute(inputData,mapper,reducer)