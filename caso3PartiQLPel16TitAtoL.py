import boto3

year = 2016
letraInicial = "A"
letraFinal = "F"

# Recuperar las películas de 2016 cuyo título está entre la A y la L con PartiQL con parámetros indicados mediante ?
print("-----Películas de 2016 cuyo título empieza desde A hasta L con PartiQL")
clientDDB = boto3.client('dynamodb', region_name='us-east-1')
consulta = 'SELECT year, title, info.genres, info.actors[0] FROM SeveroPeliculas WHERE year = ? AND title between ? and ?'
resp = clientDDB.execute_statement(
    Statement=consulta,
    Parameters=[{'N': str(year)}, {'S': letraInicial}, {'S': letraFinal}])
for i in resp['Items']:
    print(i)
    for genero in i['genres']['L']:
        print(genero['S'])