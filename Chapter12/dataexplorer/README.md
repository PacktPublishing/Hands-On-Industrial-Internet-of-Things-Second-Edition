# Mapping for data explorer


 .create table data ingestion json mapping "JsonMapping"
'['
'{ "column" : "deviceid", "datatype" : "string", "Properties":{"Path":"$.deviceid"}},'
'{ "column" : "temperature", "datatype" : "float", "Properties":{"Path":"$.Body.temperature"}},'
'{ "column" : "cpu", "datatype" : "float", "Properties":{"Path":"$.Body.cpu"}},'
'{ "column" : "timestamp", "datatype" : "datetime", "Properties":{"Path":"$.timestamp"}},'
']'
