import json
import time
import random
from datetime import datetime
from awscrt import mqtt
from awsiot import mqtt_connection_builder
import sys

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
    print(f"Conexion interrumpida. Error: {error}")

def on_connection_resumed(connection, return_code, session_present, **kwargs):
    print(f"Conexion restablecida. Return code: {return_code}")

def main():
    """Función principal para simular envío de datos"""
    
    print("=== Simulador de Sensores IoT ===")
    print(f"Endpoint: {ENDPOINT}")
    print(f"Client ID: {CLIENT_ID}")
    print(f"Certificados:")
    print(f"  - Cert: {CERT_PATH}")
    print(f"  - Key: {KEY_PATH}")
    print(f"  - CA: {ROOT_CA_PATH}")
    print("\nConectando a AWS IoT Core...")
    
    try:
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
        
        print("Intentando conectar (timeout: 30 segundos)...")
        connect_future = mqtt_connection.connect()
        
        # Esperar conexión con timeout
        connect_future.result(timeout=30)
        print("[OK] Conectado exitosamente a AWS IoT Core\n")
        
    except Exception as e:
        print(f"\n[ERROR] No se pudo conectar a AWS IoT Core")
        print(f"Error: {str(e)}")
        print("\nVerifica:")
        print("  1. Los certificados estan en la carpeta correcta")
        print("  2. El certificado esta adjunto al Thing y a la Policy")
        print("  3. Tienes conexion a Internet")
        print("  4. El endpoint es correcto")
        sys.exit(1)
    
    # Configuración del sensor
    sensor = IndustrialSensor("SENSOR-001")
    
    print("Generando y enviando datos cada 60 segundos...")
    print("Presiona Ctrl+C para detener\n")
    
    try:
        message_count = 0
        while True:
            # Obtener datos del sensor
            data = sensor.get_sensor_data()
            message_count += 1
            
            # Mostrar datos en consola
            print(f"Mensaje #{message_count} [{data['timestamp']}]")
            print(f"  Temperatura: {data['temperature']} C")
            print(f"  Vibracion: {data['vibration']} mm/s")
            print(f"  Presion: {data['pressure']} bar")
            
            # Enviar a AWS IoT Core
            message_json = json.dumps(data)
            try:
                mqtt_connection.publish(
                    topic=TOPIC,
                    payload=message_json,
                    qos=mqtt.QoS.AT_LEAST_ONCE
                )
                print(f"  [OK] Mensaje enviado a topic: {TOPIC}\n")
            except Exception as e:
                print(f"  [ERROR] No se pudo enviar mensaje: {str(e)}\n")
            
            # Esperar 60 segundos
            time.sleep(60)
            
    except KeyboardInterrupt:
        print("\n\nDesconectando...")
        try:
            disconnect_future = mqtt_connection.disconnect()
            disconnect_future.result(timeout=10)
            print("Simulador detenido por el usuario.")
        except:
            print("Simulador detenido.")

if __name__ == "__main__":
    main()
