import boto3

year = 2016

# Recuperar todas las películas de 2016 con PartiQL con parámetros indicados mediante ?
print("-----Películas de 2016 con PartiQL")
clientDDB = boto3.client('dynamodb', region_name='us-east-1')
resp = clientDDB.execute_statement(
    Statement="SELECT title, year FROM SeveroPeliculas WHERE year = ?",
    Parameters=[{'N': str(year)}])
for i in resp['Items']:
    print(i['year']['N'], ":", i['title']['S'])