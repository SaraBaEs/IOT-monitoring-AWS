# Arquitectura del Sistema

## Diagrama de Componentes

```
┌─────────────────────┐
│  Sensor Simulator   │
│    (Python)         │
└──────────┬──────────┘
           │ MQTT/TLS
           ▼
┌─────────────────────┐
│   AWS IoT Core      │
│  (Message Broker)   │
└──────────┬──────────┘
           │ IoT Rule
           ▼
┌─────────────────────┐
│   AWS Lambda        │
│ (Process Data)      │
└──────────┬──────────┘
           │
           ├──────────────┐
           ▼              ▼
┌──────────────┐  ┌──────────────┐
│  DynamoDB    │  │ CloudWatch   │
│  (Storage)   │  │   (Logs)     │
└──────────────┘  └──────────────┘
```

## Flujo de Datos

1. **Generación**: El simulador genera datos de sensores cada 60 segundos
2. **Transmisión**: Datos enviados a AWS IoT Core vía MQTT con TLS
3. **Enrutamiento**: IoT Rule detecta mensajes en topic `sensors/data`
4. **Procesamiento**: Lambda procesa y valida los datos
5. **Almacenamiento**: Datos guardados en DynamoDB
6. **Monitoreo**: Logs enviados a CloudWatch

## Componentes

### Sensor Simulator
- **Lenguaje**: Python 3.11
- **Función**: Simula 3 tipos de sensores industriales
- **Frecuencia**: 60 segundos
- **Protocolo**: MQTT sobre TLS 1.2

### AWS IoT Core
- **Función**: Message broker MQTT
- **Topic**: `sensors/data`
- **Seguridad**: Certificados X.509
- **Free Tier**: 500K mensajes/mes

### AWS Lambda
- **Runtime**: Python 3.11
- **Memoria**: 128 MB
- **Timeout**: 30 segundos
- **Función**: Validar y almacenar datos
- **Free Tier**: 1M invocaciones/mes

### Amazon DynamoDB
- **Tipo**: NoSQL
- **Modo**: On-Demand
- **Partition Key**: sensor_id
- **Sort Key**: timestamp
- **Free Tier**: 25 GB

### CloudWatch
- **Logs**: Registro de eventos
- **Métricas**: Monitoreo de Lambda
- **Free Tier**: 5 GB logs/mes

## Consideraciones de Seguridad

1. **Autenticación**: Certificados X.509 para IoT
2. **Autorización**: Políticas IAM restrictivas
3. **Encriptación**: TLS 1.2 en tránsito
4. **Almacenamiento**: Encriptación en reposo (DynamoDB)

## Escalabilidad

- **Actual**: 1 sensor, 1 mensaje/minuto = 43,200 mensajes/mes
- **Máximo Free Tier**: ~347 sensores a 1 msg/min
- **Optimización**: Batch de mensajes para mayor eficiencia

## Costos Estimados (Free Tier)

| Servicio | Uso Mensual | Costo |
|----------|-------------|-------|
| IoT Core | 43,200 msgs | $0.00 |
| Lambda | 43,200 invoc | $0.00 |
| DynamoDB | < 1 GB | $0.00 |
| CloudWatch | < 1 GB logs | $0.00 |
| **TOTAL** | | **$0.00** |
