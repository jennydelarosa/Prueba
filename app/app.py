from flask import Flask, render_template, request, redirect, url_for
import boto3
import uuid

app = Flask(__name__)

# Configuración de DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')  # Cambiar la región si es necesario
tabla = dynamodb.Table('Nombres')  # Nombre de tu tabla en DynamoDB

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        if nombre:
            tabla.put_item(
                Item={
                    'id': str(uuid.uuid4()),
                    'nombre': nombre
                }
            )
        return redirect(url_for('index'))

    # Obtener nombres desde la tabla
    response = tabla.scan()
    nombres = [item['nombre'] for item in response.get('Items', [])]

    data = {
        'titulo': 'Lista de Nombres',
        'saludo': 'Saludos cordiales de Jenny!!!',
        'nombres': nombres
    }
    return render_template('index.html', data=data)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)