from fastapi import FastAPI
from src.core.configs import settings
from src.api.api import api_router


app = FastAPI(title='API de Orçamentos')
app.include_router(api_router, prefix=settings.API_STR)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run('src.main:app', host='0.0.0.0', port=8000,
                log_level='info', reload=True)