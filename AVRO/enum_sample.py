# enum_sample.py
# Importing required packages For file Read & Write 
import avro.schema
from avro.datafile import DataFileReader, DataFileWriter  
from avro.io import DatumReader, DatumWriter

# Schema parsing from a schema file
schema = avro.schema.parse(open("enum_sample.avsc").read())

# Creation of DataFileWriter instance with above schema
writer = DataFileWriter(open("enum_sample.avro", "wb"), DatumWriter(), schema)

# Write some pair records
writer.append({"name": "Ajay Singala", "kind": "ONE"})
writer.append({"name": "Ajay Singala", "kind": "TWO"})
writer.append({"name": "Ajay Singala", "kind": "THREE"})
# The following will not work.
#writer.append({"name": "Ajay Singala", "kind": "one"})
#writer.append({"name": "Ajay Singala", "kind": "FOUR"})

# Close the data file
writer.close()

# Read the above created avro data file. Opening file in read mode. 
reader = DataFileReader(open("enum_sample.avro", "rb"), DatumReader())
for pair in reader:
    print(pair)

# Close the avro data file after completion of reading it.
reader.close()
