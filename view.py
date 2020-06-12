from aiohttp import web

import db


async def index(request):
    async with request.app['db'].acquire() as conn:
        email_ = await request.post()
        exist_emails = await conn.execute(db.email.select().where(db.email.c.email == email_["email"]))
        exist_rows = await exist_emails.fetchall()
        if len(exist_rows) == 0:
            await conn.execute(db.email.insert(values=email_))
            return web.Response(status=200)
        else:
            return web.Response(status=400)
