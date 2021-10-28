"""This file is used call HTTP methods"""
from aiohttp import web
from controllers import user_operations
URL = '/users'
URL_WITH_ID = '/users/{id}'


def get_app():
    """
    @description - Used to create database session and calls HTTP methods
    @returns - returns web app
    """
    app = web.Application()
    app.session = user_operations.user.get_db_seesion()
    app.router.add_get('/', user_operations.UserCrud.handle)
    app.router.add_get(URL, user_operations.UserCrud.get)
    app.router.add_get(URL_WITH_ID, user_operations.UserCrud.get)
    app.router.add_post(URL, user_operations.UserCrud.post)
    app.router.add_put(URL_WITH_ID, user_operations.UserCrud.put)
    app.router.add_delete(URL_WITH_ID, user_operations.UserCrud.delete)
    return app


if __name__ == '__main__':
    web.run_app(get_app())
