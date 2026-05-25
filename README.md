# Sistema IoT de Monitoreo Industrial con AWS

[![AWS Certified](https://img.shields.io/badge/AWS-Certified%20Cloud%20Practitioner-FF9900?style=flat&logo=amazon-aws&logoColor=white)](https://aws.amazon.com/certification/)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![AWS IoT](https://img.shields.io/badge/AWS-IoT%20Core-FF9900?style=flat&logo=amazon-aws)](https://aws.amazon.com/iot-core/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Proyecto personal que demuestra la integración de sensores IoT con servicios cloud de AWS, utilizando únicamente la capa gratuita (Free Tier).

## 🎯 Objetivo

Crear un sistema de monitoreo en tiempo real que simula sensores industriales (temperatura, vibración, presión) y envía datos a AWS para su procesamiento, almacenamiento y visualización.

## 🏗️ Arquitectura

```
Sensor Simulator (Python) → AWS IoT Core → Lambda → DynamoDB
                                              ↓
                                        CloudWatch Logs
                                              ↓
                                        S3 (históricos)
```

## 🛠️ Tecnologías Utilizadas

- **Python 3.x**: Simulador de sensores
- **AWS IoT Core**: Ingesta de datos IoT
- **AWS Lambda**: Procesamiento serverless
- **Amazon DynamoDB**: Base de datos NoSQL
- **Amazon S3**: Almacenamiento de datos históricos
- **AWS CloudWatch**: Monitoreo y logs
- **CloudFormation**: Infraestructura como código

## 📋 Servicios AWS (Free Tier)

- AWS IoT Core: 500,000 mensajes/mes
- Lambda: 1M solicitudes/mes
- DynamoDB: 25 GB almacenamiento
- S3: 5 GB (primeros 12 meses)
- CloudWatch: 10 métricas personalizadas

## 🚀 Instalación

### Prerrequisitos

- Python 3.8+
- AWS CLI configurado
- Cuenta AWS (Free Tier)

### Configuración

1. Clonar el repositorio:
```bash
git clone https://github.com/tu-usuario/proyecto-portfolio.git
cd proyecto-portfolio
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

3. Desplegar infraestructura:
```bash
cd infrastructure
aws cloudformation create-stack --stack-name iot-monitoring --template-body file://iot-stack.yaml --capabilities CAPABILITY_IAM
```

4. Ejecutar simulador de sensores:
```bash
cd sensor-simulator
python sensor_simulator.py
```

## 📁 Estructura del Proyecto

```
proyecto-portfolio/
├── README.md
├── requirements.txt
├── .gitignore
├── infrastructure/          # Plantillas CloudFormation
├── sensor-simulator/        # Simulador de sensores IoT
├── lambda-functions/        # Funciones Lambda
├── docs/                    # Documentación técnica
└── dashboard/              # Frontend (futuro)
```

## 📊 Características

- ✅ Simulación de 3 tipos de sensores (temperatura, vibración, presión)
- ✅ Envío de datos cada 60 segundos
- ✅ Procesamiento serverless con Lambda
- ✅ Almacenamiento en DynamoDB
- ✅ Logs y monitoreo con CloudWatch
- 🔄 Dashboard en tiempo real (en desarrollo)

## 🔐 Seguridad

- Certificados X.509 para autenticación IoT
- Políticas IAM con mínimos privilegios
- Datos encriptados en tránsito y reposo

## 📈 Roadmap

- [x] Configuración inicial de AWS
- [x] Simulador de sensores
- [x] Despliegue de infraestructura con CloudFormation
- [x] Funciones Lambda para procesamiento
- [x] Almacenamiento en DynamoDB
- [x] Certificados IoT y seguridad
- [ ] Dashboard web con visualización en tiempo real
- [ ] Alertas SNS para valores críticos
- [ ] Machine Learning predictivo con SageMaker

## 👨‍💻 Autor

**Sara** - Ingeniera Mecatrónica | AWS Certified Cloud Practitioner

## 📄 Licencia

MIT License
