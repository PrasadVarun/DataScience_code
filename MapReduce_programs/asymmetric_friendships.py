import MapReduce
import sys

mr=MapReduce.MapReduce()

def mapper(records):
    person=records[0]
    friend=records[1]
    mr.emit_intermediate((person,friend),1)
    mr.emit_intermediate((friend,person),1)

def reducer(key,listOfValues):
    if len(listOfValues)<2:
        mr.emit(key)

#main Method

if __name__=="__main__":
    inputData=open(sys.argv[1])

    mr.execute(inputData,mapper,reducer)
