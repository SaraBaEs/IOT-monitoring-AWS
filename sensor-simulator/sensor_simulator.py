import json
import time
import random
from datetime import datetime
from awscrt import mqtt
from awsiot import mqtt_connection_builder
import os

# Configuración AWS IoT
ENDPOINT = "a994pioqbl03-ats.iot.us-east-1.amazonaws.com"
CLIENT_ID = "IndustrialSensor001"
TOPIC = "sensors/data"
CERT_PATH = "../certificates/certificate.pem.crt"
KEY_PATH = "../certificates/private.pem.key"
ROOT_CA_PATH = "../certificates/AmazonRootCA1.pem"

class IndustrialSensor:
    """Simula sensores industriales: temperatura, vibración y presión"""
    
    def __init__(self, sensor_id):
        self.sensor_id = sensor_id
    
    def get_temperature(self):
        """Simula sensor de temperatura (20-80°C)"""
        return round(random.uniform(20.0, 80.0), 2)
    
    def get_vibration(self):
        """Simula sensor de vibración (0-10 mm/s)"""
        return round(random.uniform(0.0, 10.0), 2)
    
    def get_pressure(self):
        """Simula sensor de presión (1-10 bar)"""
        return round(random.uniform(1.0, 10.0), 2)
    
    def get_sensor_data(self):
        """Retorna todos los datos del sensor"""
        return {
            "sensor_id": self.sensor_id,
            "timestamp": datetime.utcnow().isoformat(),
            "temperature": self.get_temperature(),
            "vibration": self.get_vibration(),
            "pressure": self.get_pressure()
        }

def on_connection_interrupted(connection, error, **kwargs):
    print(f"Conexión interrumpida. Error: {error}")

def on_connection_resumed(connection, return_code, session_present, **kwargs):
    print(f"Conexión restablecida. Return code: {return_code}")

def main():
    """Función principal para simular envío de datos"""
    
    print("=== Simulador de Sensores IoT ===")
    print(f"Conectando a AWS IoT Core: {ENDPOINT}")
    
    # Crear conexión MQTT
    mqtt_connection = mqtt_connection_builder.mtls_from_path(
        endpoint=ENDPOINT,
        cert_filepath=CERT_PATH,
        pri_key_filepath=KEY_PATH,
        ca_filepath=ROOT_CA_PATH,
        client_id=CLIENT_ID,
        clean_session=False,
        keep_alive_secs=30,
        on_connection_interrupted=on_connection_interrupted,
        on_connection_resumed=on_connection_resumed
    )
    
    print("Conectando...")
    connect_future = mqtt_connection.connect()
    connect_future.result()
    print("[OK] Conectado exitosamente a AWS IoT Core\n")
    
    # Configuración del sensor
    sensor = IndustrialSensor("SENSOR-001")
    
    print("Generando y enviando datos cada 60 segundos...")
    print("Presiona Ctrl+C para detener\n")
    
    try:
        while True:
            # Obtener datos del sensor
            data = sensor.get_sensor_data()
            
            # Mostrar datos en consola
            print(f"[{data['timestamp']}]")
            print(f"  Temperatura: {data['temperature']}°C")
            print(f"  Vibración: {data['vibration']} mm/s")
            print(f"  Presión: {data['pressure']} bar")
            
            # Enviar a AWS IoT Core
            message_json = json.dumps(data)
            mqtt_connection.publish(
                topic=TOPIC,
                payload=message_json,
                qos=mqtt.QoS.AT_LEAST_ONCE
            )
            print(f"  [OK] Mensaje enviado a AWS IoT Core\n")
            
            # Esperar 60 segundos
            time.sleep(60)
            
    except KeyboardInterrupt:
        print("\n\nDesconectando...")
        disconnect_future = mqtt_connection.disconnect()
        disconnect_future.result()
        print("Simulador detenido por el usuario.")

if __name__ == "__main__":
    main()
