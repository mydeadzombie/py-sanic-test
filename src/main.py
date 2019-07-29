import os
from collections import Counter

from sanic import Sanic
from sanic.response import json, redirect, text

app = Sanic()
c = Counter(n=0)
CDN_HOST = '127.0.0.1'
cdn_string = 'http://{CDN_HOST}/{server}/{path}'


async def inc():
    c['n'] += 1


@app.listener('before_server_start')
async def get_env(app, loop):
    global CDN_HOST
    if os.environ.get('CDN_HOST'):
        CDN_HOST = os.environ['CDN_HOST']


@app.middleware("request")
async def track_requests(request):
    await inc()


@app.route('/')
async def main(request):
    if not 'video' in request.args:
        return json({'CDN_HOST': CDN_HOST})

    if not c['n'] % 10:
        return redirect(request.args['video'][0])

    url_parts = request.args['video'][0].split('/')
    subdomain = url_parts[2].split(".")[0]
    path = "/".join(url_parts[3:])

    return redirect(cdn_string.format(CDN_HOST=CDN_HOST, server=subdomain, path=path))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
