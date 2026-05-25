# Guía de Inicio Rápido

## ✅ Infraestructura Desplegada

La infraestructura AWS ya está completamente desplegada:

- ✅ **DynamoDB Table**: SensorData
- ✅ **Lambda Function**: ProcessSensorData
- ✅ **IoT Thing**: IndustrialSensor001
- ✅ **IoT Policy**: SensorPolicy
- ✅ **IoT Topic Rule**: ProcessSensorDataRule
- ✅ **Certificados IoT**: Creados y configurados

### Endpoint IoT
```
a994pioqbl03-ats.iot.us-east-1.amazonaws.com
```

## 🚀 Cómo Ejecutar el Simulador

### 1. Instalar Dependencias

```bash
cd C:\Users\katy0\Documents\proyecto-portfolio
pip install -r requirements.txt
```

### 2. Ejecutar el Simulador

```bash
cd sensor-simulator
python sensor_simulator.py
```

El simulador:
- Se conectará a AWS IoT Core
- Generará datos de sensores cada 60 segundos
- Enviará los datos automáticamente
- Lambda procesará y guardará en DynamoDB

### 3. Verificar Datos en DynamoDB

```bash
aws dynamodb scan --table-name SensorData --limit 5
```

O desde la consola AWS:
1. Ve a DynamoDB
2. Selecciona la tabla "SensorData"
3. Click en "Explore table items"

## 📊 Monitoreo

### Ver logs de Lambda
```bash
aws logs tail /aws/lambda/ProcessSensorData --follow
```

### Ver métricas de IoT
```bash
aws iot get-statistics --query-string "*"
```

## 🛑 Detener el Simulador

Presiona `Ctrl+C` en la terminal donde está corriendo el simulador.

## 🧹 Limpiar Recursos (cuando termines)

```bash
# Eliminar el stack de CloudFormation
aws cloudformation delete-stack --stack-name iot-monitoring-stack

# Eliminar certificados
aws iot delete-certificate --certificate-id 0dd5934b0671cbef48412e78b44c7ad63ae4fdf6275ce52faa9ec075e1c4fe40 --force-delete
```

## 📝 Próximos Pasos

1. ✅ Ejecutar el simulador y verificar que los datos lleguen a DynamoDB
2. 🔄 Crear dashboard web para visualizar datos en tiempo real
3. 🔔 Configurar alertas SNS para valores críticos
4. 📈 Agregar gráficos con CloudWatch Dashboard
5. 🤖 Implementar ML para predicción de fallos

## 🐛 Troubleshooting

**Error de conexión MQTT:**
- Verifica que los certificados estén en la carpeta `certificates/`
- Verifica que el endpoint sea correcto

**Error de permisos Lambda:**
- Verifica que el rol IAM tenga permisos para DynamoDB

**No llegan datos a DynamoDB:**
- Verifica los logs de Lambda
- Verifica que la IoT Rule esté activa
