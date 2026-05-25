# Sistema IoT de Monitoreo Industrial con AWS

[![AWS Certified](https://img.shields.io/badge/AWS-Certified%20Cloud%20Practitioner-FF9900?style=flat&logo=amazon-aws&logoColor=white)](https://aws.amazon.com/certification/)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![AWS IoT](https://img.shields.io/badge/AWS-IoT%20Core-FF9900?style=flat&logo=amazon-aws)](https://aws.amazon.com/iot-core/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Proyecto académico-profesional que integra sistemas de control industrial con tecnologías cloud, demostrando la convergencia entre automatización con PLC Siemens S7-1500 y servicios IoT de AWS.

## 🎯 Contexto del Proyecto

Este proyecto representa la evolución natural de los sistemas de automatización industrial desarrollados en entornos académicos. Partiendo de la experiencia con controladores lógicos programables (PLC Siemens S7-1500) para control y automatización de procesos, se extiende la funcionalidad hacia la nube mediante AWS IoT Core, permitiendo monitoreo remoto, análisis de datos históricos y escalabilidad.

**Caso de uso:** Sistema de monitoreo industrial que captura datos de sensores (temperatura, vibración, presión) desde un proceso automatizado con PLC, transmite la información a la nube para su procesamiento y almacenamiento, facilitando la toma de decisiones basada en datos y el mantenimiento predictivo.

## 🏭 Arquitectura del Sistema

### Capa Física (Simulada)
```
Sensores Industriales → PLC Siemens S7-1500 → Gateway IoT → AWS IoT Core
```

### Capa Cloud (Implementada)
```
AWS IoT Core → Lambda → DynamoDB
       ↓
  CloudWatch Logs
       ↓
  S3 (históricos)
```

**Nota:** En esta implementación se simula la capa física mediante scripts Python que emulan el comportamiento de sensores industriales conectados a un PLC. En un entorno de producción, el PLC Siemens S7-1500 se conectaría directamente a AWS IoT Core mediante protocolos industriales (OPC UA, MQTT).

## 🛠️ Tecnologías y Herramientas

### Automatización Industrial
- **PLC Siemens S7-1500**: Controlador lógico programable
- **Protocolos Industriales**: MQTT, OPC UA (preparado para integración)
- **Sensores**: Temperatura, vibración, presión

### Cloud Computing (AWS)
- **AWS IoT Core**: Ingesta y gestión de dispositivos IoT
- **AWS Lambda**: Procesamiento serverless de datos
- **Amazon DynamoDB**: Base de datos NoSQL para almacenamiento
- **Amazon S3**: Almacenamiento de datos históricos
- **AWS CloudWatch**: Monitoreo, logs y métricas
- **CloudFormation**: Infraestructura como código (IaC)

### Desarrollo
- **Python 3.11+**: Métodos de obtención de datos físicos y lógica de negocio
- **Git**: Control de versiones

## 📋 Servicios AWS Utilizados

- **AWS IoT Core**: Gestión de dispositivos y mensajería MQTT
- **AWS Lambda**: Procesamiento de eventos
- **Amazon DynamoDB**: Almacenamiento de datos de sensores
- **Amazon S3**: Repositorio de datos históricos
- **AWS CloudWatch**: Monitoreo y logs del sistema
- **AWS CloudFormation**: Despliegue de infraestructura

## 🚀 Instalación

### Configuración

1. Clonar el repositorio:
```bash
git clone https://github.com/SaraBaEs/IOT-monitoring-AWS.git
cd IOT-monitoring-AWS
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

3. Desplegar infraestructura:
```bash
cd infrastructure
aws cloudformation create-stack --stack-name iot-monitoring-stack --template-body file://iot-stack.yaml --capabilities CAPABILITY_NAMED_IAM
```

4. Ejecutar simulador de sensores:
```bash
cd sensor-simulator
run_simulator.bat
```

## 📁 Estructura del Proyecto

```
IOT-monitoring-AWS/
├── README.md
├── requirements.txt
├── .gitignore
├── LICENSE
├── QUICKSTART.md
├── GITHUB_SETUP.md
├── infrastructure/          # Plantillas CloudFormation
├── data-acquisition/        # Scripts de adquisición de datos de sensores
├── lambda-functions/        # Funciones Lambda para procesamiento
├── docs/                    # Documentación técnica
├── certificates/            # Certificados IoT (no versionados)
└── dashboard/              # Frontend (futuro)
```

## 📊 Funcionalidades Implementadas

- ✅ Simulación de sensores industriales (temperatura, vibración, presión)
- ✅ Transmisión de datos cada 60 segundos vía MQTT
- ✅ Procesamiento serverless con AWS Lambda
- ✅ Almacenamiento persistente en DynamoDB
- ✅ Monitoreo y logs con CloudWatch
- ✅ Infraestructura desplegada con CloudFormation
- ✅ Seguridad mediante certificados X.509 y políticas IAM
- 🔄 Dashboard web para visualización en tiempo real (en desarrollo)
- 🔄 Integración física con PLC Siemens S7-1500 (próxima fase)

## 🔐 Seguridad

- Certificados X.509 para autenticación IoT
- Políticas IAM con mínimos privilegios
- Datos encriptados en tránsito y reposo
- Gestión segura de credenciales

## 📈 Roadmap y Evolución del Proyecto

### Fase 1: Infraestructura Cloud (Completada)
- [x] Configuración de cuenta AWS y servicios
- [x] Despliegue de infraestructura con CloudFormation
- [x] Configuración de AWS IoT Core, Lambda y DynamoDB
- [x] Implementación de seguridad (certificados X.509, IAM)
- [x] Simulador de sensores en Python

### Fase 2: Integración Industrial (En planificación)
- [ ] Conexión con PLC Siemens S7-1500 real
- [ ] Implementación de protocolo OPC UA
- [ ] Gateway IoT para comunicación PLC-Cloud
- [ ] Sincronización de datos en tiempo real

### Fase 3: Análisis y Visualización (Próxima)
- [ ] Dashboard web con React para visualización
- [ ] Alertas automáticas vía SNS para valores críticos
- [ ] Análisis predictivo con AWS SageMaker
- [ ] API REST con API Gateway para integración externa

## 👨💻 Autor

**Sara Barbosa Escobar** - Ingeniera Mecatrónica | AWS Certified Cloud Practitioner

Especializada en la integración de sistemas de automatización industrial con tecnologías cloud, combinando experiencia en control con PLC y desarrollo de soluciones IoT escalables.

- 📧 Email: sarakatherinebarbosa3@gmail.com
- 💼 LinkedIn: [Sara Barbosa Escobar](https://www.linkedin.com/in/sara-barbosa-b562aa3b1)
- 🌐 GitHub: [SaraBaEs](https://github.com/SaraBaEs)

## 🎓 Competencias Demostradas

- ☁️ AWS Cloud Services (IoT Core, Lambda, DynamoDB, CloudFormation)
- 🐍 Python Programming & Scripting
- 🏭 Sistemas de Automatización Industrial (PLC Siemens S7-1500)
- 🏗️ Arquitectura Serverless
- 📡 Protocolos IoT (MQTT, OPC UA)
- 🔐 Seguridad en Cloud (IAM, X.509 Certificates)
- 📊 Infrastructure as Code (IaC)
- 🔄 Procesamiento de Datos en Tiempo Real

## 📄 Licencia

MIT License
