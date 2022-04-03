import boto3
import pandas as pd
from decimal import Decimal

# 1.- Leemos el fichero desde S3 y lo metemos en un DataFrame
s3c = boto3.client('s3')
bucketNombre = "caso1python"
ficheroNombre = "TMDb_filtered.csv"
response = s3c.get_object(Bucket=bucketNombre, Key=ficheroNombre)
movies_df = pd.read_csv(response['Body'], delimiter = ',')

# 2.- Nos conectamos a DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
tabla = dynamodb.Table('SeveroPeliculas')

# 3.- Lo metemos en DynamoDB mediante un batch
with tabla.batch_writer() as batch:
    for index, fila in movies_df.iterrows():
        Item = {
            'year': 2022,
            'title': str(fila['title']),
            'info': {
                'plot' : fila['overview'],
                'rating' : Decimal(fila['vote_average']).quantize(Decimal('1.00'))
            }
        }
        batch.put_item(Item=Item)