docker-compose build 
docker-compose up -d
ab -c 5 -n 1000 http://127.0.0.1:80/round-robin

Viewing results:
127.0.0.1:8081/round-robin/stat
127.0.0.1:8082/round-robin/stat
