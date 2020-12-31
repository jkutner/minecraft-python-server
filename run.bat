@ECHO OFF
if not exist "world" mkdir world
if not exist ".env" echo. 2>.env
docker run -it^
    --env-file .env^
    -v %~dp0/config:/workspace/config:ro^
    -v %~dp0/world:/workspace/world^
    -p 4711:4711 -p 8080:8080 -p 25566:25566^
    jkutner/pycraft