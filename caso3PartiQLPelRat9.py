import boto3

rating = 9

# Recuperar las películas rating >= 9 con PartiQL con parámetros indicados mediante ?
print("-----Películas rating >= 9 con PartiQL")
clientDDB = boto3.client('dynamodb', region_name='us-east-1')
resp = clientDDB.execute_statement(
    Statement="SELECT title, year, info.rating FROM SeveroPeliculas WHERE info.rating >= ?",
    Parameters=[{'N': str(rating)}])
for i in resp['Items']:
    print(i['year']['N'], ":", i['title']['S'])