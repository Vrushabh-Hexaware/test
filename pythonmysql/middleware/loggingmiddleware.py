from starlette.middleware.base import BaseHTTPMiddleware
from starlette.concurrency import iterate_in_threadpool
from core.logger import logger
import uuid


class LoggingMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request, call_next):
        req_uuid = uuid.uuid4()

        logger.info(f'{req_uuid} - {request.method} - {request.url}')
        response = await call_next(request)
        response_body = [section async for section in response.body_iterator]
        response.body_iterator = iterate_in_threadpool(iter(response_body))
        logger.info(f'{req_uuid} - {response_body}')

        return response
