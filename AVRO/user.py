# user.py
import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter
 
schema = avro.schema.parse(open("user.avsc").read())
 
writer = DataFileWriter(open("users.avro", "wb"), DatumWriter(), schema)
writer.append({"name": "Sharon", "age": 25,"gender":"female"})
writer.append({"name": "Bucky", "age": 35,"gender":"male"})
writer.close()
 
reader = DataFileReader(open("users.avro", "rb"), DatumReader())
for user in reader:
    print(user)
    print('===================')
reader.close()
