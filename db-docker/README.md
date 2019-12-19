## to build the docker image

```bash
docker build -t dj-mysql .
```

## run the image

```bash
docker run -d -p 3306:3306 --name dj-mysql \
-e MYSQL_ROOT_PASSWORD=supersecret dj-mysql
```

## verify

```bash
$ docker exec -it dj-mysql bash
root@c86ff80d7524:/# mysql -uroot -p
Enter password: (supersecret)
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| djplay             |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.00 sec)
```

## create superuser for mysql

```
create user "master_user"@"%" identified by "password";
GRANT ALL PRIVILEGES ON *.* TO "master_user"@"%" WITH GRANT OPTION;
```

## transfer data from sqlite3 to mysql

```
python manage.py dumpdata > datadump.json
python manage.py loaddata datadump.json
```
