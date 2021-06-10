# map_sample.py
# Importing required packages For file Read & Write 
import avro.schema
from avro.datafile import DataFileReader, DataFileWriter  
from avro.io import DatumReader, DatumWriter

# Schema parsing from a schema file
schema = avro.schema.parse(open("map_sample.avsc").read())

# Creation of DataFileWriter instance with above schema
writer = DataFileWriter(open("map_sample.avro", "wb"), DatumWriter(), schema)

# Write some pair records
writer.append({"ip": "172.18.80.109", "timestamp": "2015-09-17T23:00:18.313Z", "message": "blah blash", "additional": {"microseconds": "123", "thread": "http-apr-8080-exec-1147"}})
writer.append({ "ip": "172.18.80.112", "timestamp": "2015-09-17T23:00:08.297Z", "message":"blahblahblah", "additional": {"microseconds": "1335",}})

# Close the data file
writer.close()

# Read the above created avro data file. Opening file in read mode. 
reader = DataFileReader(open("map_sample.avro", "rb"), DatumReader())
for pair in reader:
    print(pair)

# Close the avro data file after completion of reading it.
reader.close()
