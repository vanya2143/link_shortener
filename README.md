# link_shortener
Link shortener project written in Django Rest Framework

## Run
1. Clone project and create virtualenv
```shell
git clone https://github.com/vanya2143/link_shortener.git
cd link_shortener
pip3 install virtualenv
python3 -m venv .env
```

2. Activate virtualenv, install requirements and runserver

```shell
source .env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Usage
Use [curl](https://en.wikipedia.org/wiki/CURL) utility in code examples

### Create short link
```shell
curl --request POST \
  --header "Content-Type: application/json" \
  --data '{"url":"https://github.com/vanya2143"}' \
  http://localhost:8000/
```
Response
```json
{
  "short_url":"http://localhost:8000/links/ab2ae469/"
}
```

### Get all short links
```shell
curl --request GET http://127.0.0.1:8000
```
Response
```json
{
  "count":1,
  "next":null,
  "previous":null,
  "results":[
    {
      "id":1,
      "url":"https://github.com/vanya2143",
      "short_url":"http://127.0.0.1:8000/links/ab2ae469/"
    }
  ]
}
```

### Follow the link
```shell
curl --request GET -I \
     --url 'http://127.0.0.1:8000/links/ab2ae469/'
```
Response
```log
HTTP/1.1 302 Found
Date: Thu, 25 Mar 2021 13:04:48 GMT
Server: WSGIServer/0.2 CPython/3.8.3
Content-Type: text/html; charset=utf-8
Location: https://github.com/vanya2143
```

### Get all links in csv format
```shell
curl --request GET -sLv \
     --url 'http://127.0.0.1:8000/export'
```
Response
```csv
short_url,url
http://127.0.0.1:8000/links/ab2ae469/,https://github.com/vanya2143
```

### Delete short link
```shell
curl -v --request DELETE \
  --header "Content-Type: application/json" \
  http://localhost:8000/links/ab2ae469/
```
Response
```log
HTTP/1.1 204 No Content
```
