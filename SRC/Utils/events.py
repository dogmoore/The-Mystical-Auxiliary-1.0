from Utils.debug import Debug
from nicegui import background_tasks, ui, app, Client
from nicegui.events import KeyEventArguments
from nicegui.page import page
from fastapi import Request, Response

class Events:
    @app.exception_handler(404)
    async def exception_handler_404(request: Request, exception: Exception) -> Response:
        with Client(page(''), request=request) as client:
            ui.navigate.to('/login')
            ui.notify('Sorry the page you requested wasn\'t found', color='negative')
        return client.build_response(request, 404)
