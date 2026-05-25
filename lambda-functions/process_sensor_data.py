import json
import boto3
from datetime import datetime
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('SensorData')

def lambda_handler(event, context):
    """
    Procesa datos de sensores IoT y los almacena en DynamoDB
    """
    
    try:
        # Parsear datos del sensor
        sensor_data = json.loads(event['body']) if 'body' in event else event
        
        # Convertir floats a Decimal para DynamoDB
        item = {
            'sensor_id': sensor_data['sensor_id'],
            'timestamp': sensor_data['timestamp'],
            'temperature': Decimal(str(sensor_data['temperature'])),
            'vibration': Decimal(str(sensor_data['vibration'])),
            'pressure': Decimal(str(sensor_data['pressure']))
        }
        
        # Guardar en DynamoDB
        table.put_item(Item=item)
        
        # Verificar umbrales críticos
        alerts = []
        if float(sensor_data['temperature']) > 75:
            alerts.append("Temperatura crítica")
        if float(sensor_data['vibration']) > 8:
            alerts.append("Vibración excesiva")
        if float(sensor_data['pressure']) > 9:
            alerts.append("Presión alta")
        
        response = {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Datos procesados correctamente',
                'sensor_id': sensor_data['sensor_id'],
                'alerts': alerts
            })
        }
        
        print(f"Datos guardados: {sensor_data['sensor_id']} - {sensor_data['timestamp']}")
        if alerts:
            print(f"ALERTAS: {', '.join(alerts)}")
        
        return response
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
