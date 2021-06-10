# pair.py
# Importing required packages For file Read & Write 
import avro.schema
from avro.datafile import DataFileReader, DataFileWriter  
from avro.io import DatumReader, DatumWriter

# Schema parsing from a schema file
schema = avro.schema.parse(open("pair.avsc").read())

# Creation of DataFileWriter instance with above schema
writer = DataFileWriter(open("pairs.avro", "wb"), DatumWriter(), schema)

# Write some pair records
writer.append({"first": "left", "second": "right"})
writer.append({"first": "correct", "second": "wrong"})
writer.append({"first": "good", "second": "bad"})
# Close the data file
writer.close()

# Read the above created avro data file. Opening file in read mode. 
reader = DataFileReader(open("pairs.avro", "rb"), DatumReader())
for pair in reader:
    print(pair)

# Close the avro data file after completion of reading it.
reader.close()
