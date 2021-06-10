# AvroReadWrite.py
# Importing required packages For file Read & Write
import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter

# Schema parsing from a schema file
schema = avro.schema.parse(open("measure.avsc").read())

# Creation of DataFileWriter instance with above schema
writer = DataFileWriter(open("measure.avro", "wb"), DatumWriter(), schema)

# Write some pair records
writer.append({
    "MeasureId": "nifiHeartBeat",
    "Value": "1",
    "AuditDateTime": "Tue Jan 16 13:48:58 CET 2018",
    "DATA_SOURCE": "20083"
})

writer.append({
    "MeasureId": "nifiHeartBeat - 2",
    "Value": "2",
    "AuditDateTime": "Tue June 09 15:30:40 IST 2021",
    "DATA_SOURCE": "20084"
})
writer.append({
    "MeasureId": "nifiHeartBeat - 3",
    "Value": "3",
    "AuditDateTime": "Wed June 10 12:01:01 IST 2021",
    "DATA_SOURCE": "20085"
})


# Array:
# writer.append([{
#     "MeasureId": "nifiHeartBeat - 2",
#     "Value": "2",
#     "AuditDateTime": "Tue June 09 15:30:40 IST 2021",
#     "DATA_SOURCE": "20084"
# },
#     {
#     "MeasureId": "nifiHeartBeat - 3",
#     "Value": "3",
#     "AuditDateTime": "Wed June 10 12:01:01 IST 2021",
#     "DATA_SOURCE": "20085"
# }])

# Close the data file
writer.close()

# Read the above created avro data file. Opening file in read mode.
reader = DataFileReader(open("measure.avro", "rb"), DatumReader())
for pair in reader:
    print(pair)

# Close the avro data file after completion of reading it.
reader.close()
