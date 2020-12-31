@ECHO OFF
FOR /F "tokens=*" %%i in ('type .env') do SET %%i
docker run -it --env-file .env -v %~dp0/config:/workspace/config:ro -p 4711:4711 -p 8080:8080 -p 25566:25566 jkutner/pycraft