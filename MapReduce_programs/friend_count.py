import MapReduce
import sys

mr=MapReduce.MapReduce()

def mapper(records):
    name=records[0]
    value=1
    mr.emit_intermediate(name,value)

def reducer(key,listOfValues):
    count=0
    for v in listOfValues:
       count+=v
    mr.emit((key,count))


#main function
if __name__=="__main__":
    inputData=open(sys.argv[1])

    mr.execute(inputData,mapper,reducer)