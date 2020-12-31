@ECHO OFF
FOR /F "tokens=*" %%i in ('type .env') do SET %%i
if not exist "%~dp0/world" mkdir %~dp0/world
docker run -it --env-file .env -v %~dp0/config:/workspace/config:ro -v %~dp0/world:/workspace/world -p 4711:4711 -p 8080:8080 -p 25566:25566 jkutner/pycraft