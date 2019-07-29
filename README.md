### Перед запуском

```bash
docker-compse build
```


### `CDN_HOST` 

Доступные способы задать `CDN_HOST`:

- `.env`
- `docker-compose.yml`, в секции `environment`

или

- Использовать для запуска `docker-composer run -e CDN_HOST=path -p 8000:8000 sanic python main.py`


### Запуск приложения

```bash
docker-compose up
```

Приложение запускается внутри контейнера на `8000` порту и также доступно на `8000` вне его(можно поменять в `docker-compose.yml`).


### Пример работы

```bash
curl -L "localhost:8000/?video=http://h8.origin-cluster/video/666/s47anl4n9m3ad0114r.m3u8" -i
```
 Приложение прокидывает запрос либо на `http://{CDN_HOST}/h8/video/666/s47anl4n9m3ad0114r.m3u8`, либо на указанный в параметре адрес `http://h8.origin-cluster/video/666/s47anl4n9m3ad0114r.m3u8`.
