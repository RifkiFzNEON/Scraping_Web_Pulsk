from fastapi import FastAPI, Depends, HTTPException, Security, status
from fastapi.security.api_key import APIKeyHeader
from fastapi.middleware.cors import CORSMiddleware
from apps.helper import Config
from apps.helper import Log
from fastapi.openapi.docs import (
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html
)
PARAMS = Config.PARAMS
from apps.routers import RifkiRouter
from fastapi.staticfiles import StaticFiles


API_TOKEN_NAME = "X-Api-Token"
API_TOKEN_HEADER = APIKeyHeader(name=API_TOKEN_NAME, auto_error=False)

app = FastAPI(**PARAMS.APPS_INFORMATION, docs_url=None, redoc_url=None)
app.add_middleware(CORSMiddleware,
                   allow_origins=PARAMS.ALLOWED_HOSTS,
                   allow_credentials=True,
                   allow_methods=PARAMS.ALLOW_METHODS,
                   allow_headers=["*"])

async def verify_token(api_token_header: str = Security(API_TOKEN_HEADER)):
    if api_token_header not in PARAMS.API_TOKEN:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Could not validate credentials")

app.mount("/static", StaticFiles(directory="assets"), name="static")

@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    openapi_url = ""
    if PARAMS.ENVIRONMENT == 'development':
        openapi_url = app.openapi_url
    elif PARAMS.ENVIRONMENT in ['staging', 'production']:
        openapi_url = f"/neon{app.openapi_url}"

    Log.info(openapi_url)
    return get_swagger_ui_html(
        openapi_url=openapi_url,
        title=app.title,
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url=f"/static/swagger-ui-bundle.js",
        swagger_css_url=f"/static/swagger-ui.css",
    )

app.include_router(
    RifkiRouter.router,
    tags=["URL Article PULSK"],
    prefix='/article',
    dependencies=[Depends(verify_token)]
)
