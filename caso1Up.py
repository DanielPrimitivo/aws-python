# Caso de uso 1: Comunicación son S3

import boto3

ficheroUpload = 'datosPeliculas.json'
nombreBucket = 'caso1python'

s3r = boto3.resource('s3', region_name='us-east-1')
object = s3r.Object(nombreBucket, 'datosPeliculasUp.json').upload_file(ficheroUpload)