import boto3

s3 = boto3.client('s3')

# 1.- Realizar la consulta mediante S3Select
resp = s3.select_object_content(
    Bucket='caso1python',
    Key='TMDb_updated.csv',
    ExpressionType='SQL',
    Expression="SELECT s.title, s.overview, s.vote_count, s.vote_average FROM s3object s WHERE cast(s.vote_count as int)> 10000",
    InputSerialization={'CSV': {"FileHeaderInfo": "USE",
                                'AllowQuotedRecordDelimiter': True},
                        'CompressionType': 'NONE'},
    OutputSerialization={'CSV': {}},
)

# 2.- Unir los datos que vamos recibiendo en streaming
registros = ["title,overview,vote_count,vote_average\n"]
for evento in resp['Payload']:
    if 'Records' in evento:
        registros.append(evento['Records']['Payload'].decode())

# 3.- Generar el contenido en un String
file_str = ''.join(registros)

# 4.- Crear un nuevo objeto en S3
s3.put_object(Body=file_str, Bucket='caso1python',
              Key="TMDb_filtered.csv")