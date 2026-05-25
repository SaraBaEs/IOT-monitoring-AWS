# Guía para Subir el Proyecto a GitHub

## 1. Instalar Git (si no lo tienes)

### Opción A - Usando winget:
```cmd
winget install Git.Git
```

### Opción B - Descarga manual:
1. Ve a: https://git-scm.com/download/win
2. Descarga e instala Git para Windows
3. Reinicia tu terminal/IDE

## 2. Configurar Git (primera vez)

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu-email@ejemplo.com"
```

## 3. Inicializar Repositorio Local

```bash
cd C:\Users\katy0\Documents\proyecto-portfolio
git init
git add .
git commit -m "Initial commit: IoT monitoring system with AWS Free Tier"
```

## 4. Crear Repositorio en GitHub

1. Ve a: https://github.com/new
2. Nombre del repositorio: `iot-monitoring-aws`
3. Descripción: `Sistema IoT de monitoreo industrial con AWS (DynamoDB, Lambda, IoT Core) - Free Tier`
4. Selecciona: **Public** (para que aparezca en tu portafolio)
5. NO inicialices con README (ya lo tenemos)
6. Click en **Create repository**

## 5. Conectar y Subir a GitHub

Después de crear el repo en GitHub, ejecuta:

```bash
git remote add origin https://github.com/TU-USUARIO/iot-monitoring-aws.git
git branch -M main
git push -u origin main
```

## 6. Agregar Topics en GitHub (para mejor visibilidad)

En tu repositorio de GitHub, agrega estos topics:
- `aws`
- `iot`
- `lambda`
- `dynamodb`
- `python`
- `cloudformation`
- `aws-iot-core`
- `mechatronics`
- `portfolio-project`
- `free-tier`

## 7. Actualizar README con tu información

Edita el README.md y actualiza:
- Tu nombre en la sección "Autor"
- Tu perfil de LinkedIn
- Link a tu certificación AWS

## 8. Agregar Badge de AWS Certified

Agrega al inicio del README.md:

```markdown
[![AWS Certified](https://img.shields.io/badge/AWS-Certified%20Cloud%20Practitioner-orange?style=flat&logo=amazon-aws)](https://aws.amazon.com/certification/)
[![Python](https://img.shields.io/badge/Python-3.11+-blue?style=flat&logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
```

## 9. Crear archivo LICENSE

```bash
echo MIT License > LICENSE
```

O copia una licencia MIT completa desde: https://opensource.org/licenses/MIT

## 10. Comandos Git Útiles

### Ver estado:
```bash
git status
```

### Agregar cambios:
```bash
git add .
git commit -m "Descripción del cambio"
git push
```

### Ver historial:
```bash
git log --oneline
```

## 11. Para tu CV/LinkedIn

**Descripción del proyecto:**

"Desarrollé un sistema IoT de monitoreo industrial utilizando AWS (IoT Core, Lambda, DynamoDB) con arquitectura serverless. El proyecto simula sensores industriales que envían datos en tiempo real para procesamiento y almacenamiento en la nube, implementando infraestructura como código con CloudFormation. Todo dentro de AWS Free Tier."

**Skills demostradas:**
- AWS IoT Core, Lambda, DynamoDB, CloudFormation
- Python
- Arquitectura Serverless
- Infrastructure as Code (IaC)
- MQTT Protocol
- IoT Security (X.509 certificates)
- Cloud Computing
- Real-time data processing

**Link del proyecto:**
https://github.com/TU-USUARIO/iot-monitoring-aws

## 12. Capturas de Pantalla Recomendadas

Para el README, agrega capturas de:
1. Arquitectura del sistema (diagrama)
2. Consola de DynamoDB con datos
3. Logs de Lambda
4. Dashboard de CloudWatch (si lo creas)
5. Simulador en ejecución

## 13. Próximas Mejoras (para el README)

Lista de features futuras:
- [ ] Dashboard web con React
- [ ] Alertas SNS para valores críticos
- [ ] Machine Learning para predicción de fallos
- [ ] API REST con API Gateway
- [ ] Autenticación con Cognito
- [ ] Visualización con QuickSight
