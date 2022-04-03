import boto3

clientDDB = boto3.client('dynamodb', region_name='us-east-1')

title = "Interstellar"
year = 2014

# Recuperar una película con PartiQL con parámetros indicados mediante ?
print("------ Datos de Interstellar mediante PartiQL con parámetros")
resp = clientDDB.execute_statement(
    Statement='SELECT * FROM SeveroPeliculas WHERE year = ? AND title = ?',
    Parameters=[{'N': str(year)}, {'S': title}])
item = resp['Items'][0]
print(item)