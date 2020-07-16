import MapReduce
import sys

mr=MapReduce.MapReduce()

def mapper(records):
    nucleotide=records[1]
    length = len(nucleotide)
    if length!=0:
        mr.emit_intermediate(nucleotide[0:length-10],1)

def reducer(key, listOfValues):
    mr.emit(key)


if __name__=="__main__":
    inputData=open(sys.argv[1])

    mr.execute(inputData,mapper,reducer)
