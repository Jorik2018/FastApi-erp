import time
from fastapi_erp.database import DBMiddleware
from fastapi import FastAPI, Request
from fastapi_erp.expose.item_controller import router as item_router
from fastapi_erp.expose.book_controller import router as book_router
import logging
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

app = FastAPI(
    title="ERP Details",
    description="You can perform CRUD operation by using this API",
    version="1.0.0"
)

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    response.headers["X-Process-Time"] = str(time.time() - start_time)
    return response

app.add_middleware(DBMiddleware, some_attribute="some_attribute_here_if_needed")

app.include_router(item_router)
app.include_router(book_router, tags= ["Book","Libro"])