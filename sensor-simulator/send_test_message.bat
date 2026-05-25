@echo off
echo === Enviando mensaje de prueba a AWS IoT Core ===
echo.

set TIMESTAMP=%date:~-4%-%date:~3,2%-%date:~0,2%T%time:~0,2%:%time:~3,2%:%time:~6,2%Z
set TEMP=45.5
set VIB=3.2
set PRES=5.8

echo Datos del sensor:
echo   Temperatura: %TEMP% C
echo   Vibracion: %VIB% mm/s
echo   Presion: %PRES% bar
echo.

echo Enviando a AWS IoT Core...
echo {"sensor_id":"SENSOR-001","timestamp":"%TIMESTAMP%","temperature":%TEMP%,"vibration":%VIB%,"pressure":%PRES%} > temp_payload.json

aws iot-data publish --topic sensors/data --cli-binary-format raw-in-base64-out --payload file://temp_payload.json --qos 1

if %errorlevel% equ 0 (
    echo [OK] Mensaje enviado exitosamente
) else (
    echo [ERROR] No se pudo enviar el mensaje
)

del temp_payload.json
echo.
pause
