@echo off
echo ========================================
echo   Simulador de Sensores IoT - AWS
echo ========================================
echo.
echo Enviando datos cada 60 segundos...
echo Presiona Ctrl+C para detener
echo.

set COUNT=0

:loop
set /a COUNT+=1

REM Generar valores aleatorios simulados
set /a TEMP=%RANDOM% %% 60 + 20
set /a VIB=%RANDOM% %% 10
set /a PRES=%RANDOM% %% 9 + 1

echo [Mensaje #%COUNT%] %date% %time%
echo   Temperatura: %TEMP% C
echo   Vibracion: %VIB% mm/s
echo   Presion: %PRES% bar

REM Crear payload JSON
echo {"sensor_id":"SENSOR-001","timestamp":"%date:~-4%-%date:~3,2%-%date:~0,2%T%time:~0,8%Z","temperature":%TEMP%,"vibration":%VIB%,"pressure":%PRES%} > temp_payload.json

REM Enviar a AWS IoT
aws iot-data publish --topic sensors/data --cli-binary-format raw-in-base64-out --payload file://temp_payload.json --qos 1 >nul 2>&1

if %errorlevel% equ 0 (
    echo   [OK] Mensaje enviado
) else (
    echo   [ERROR] Fallo al enviar
)

del temp_payload.json >nul 2>&1
echo.

REM Esperar 60 segundos
timeout /t 60 /nobreak >nul

goto loop
