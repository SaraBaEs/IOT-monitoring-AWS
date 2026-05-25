import json
import time
import random
from datetime import datetime
import boto3

# Cliente AWS IoT Data
iot_client = boto3.client('iot-data', region_name='us-east-1')

TOPIC = "sensors/data"

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

def main():
    """Función principal para simular envío de datos"""
    
    print("=== Simulador de Sensores IoT (Boto3) ===")
    print(f"Topic: {TOPIC}")
    print(f"Region: us-east-1\n")
    
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
            
            # Enviar a AWS IoT Core usando boto3
            try:
                response = iot_client.publish(
                    topic=TOPIC,
                    qos=1,
                    payload=json.dumps(data)
                )
                print(f"  [OK] Mensaje enviado exitosamente\n")
            except Exception as e:
                print(f"  [ERROR] No se pudo enviar: {str(e)}\n")
            
            # Esperar 60 segundos
            time.sleep(60)
            
    except KeyboardInterrupt:
        print("\n\nSimulador detenido por el usuario.")

if __name__ == "__main__":
    main()
