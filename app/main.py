from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.utilities.getUptime import getUptime
from fastapi.middleware.cors import CORSMiddleware
from app.routers.v1 import (
    user_router,
    time_table_router,
    announcement_router,
    misc_router,
    hostel_router,
    placement_portal_router,
)
import time
from app.Config import settings

startTime = time.time()

app = FastAPI(
    title=settings.APP_NAME or "UMS API",
    version=settings.APP_VERSION or "1.0.0",
    description=settings.APP_DESCRIPTION or "University Management System API",
    docs_url=None,
    contact={
        "name": "Krishna",
        "url": "https://github.com/Krixhnnna",
        "email": "krishna@example.com",
    },
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health_route(req: Request):
    """
    Health Route : Returns App details.

    """
    return JSONResponse(
        {
            "app": settings.APP_NAME or "UMS API",
            "version": "v" + (settings.APP_VERSION or "1.0.0"),
            "ip": req.client.host,
            "uptime": getUptime(startTime),
            "mode": settings.PYTHON_ENV or "production",
        }
    )


app.include_router(user_router.router)
app.include_router(time_table_router.router)
app.include_router(announcement_router.router)
app.include_router(misc_router.router)
app.include_router(hostel_router.router)
app.include_router(placement_portal_router.router)

# Custom docs endpoint for Vercel
@app.get("/api-docs")
async def get_api_docs():
    """
    Returns the OpenAPI schema as JSON for API documentation.
    """
    return app.openapi()


@app.get("/docs")
async def get_docs_html():
    """
    Returns an HTML page with interactive API documentation.
    """
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>UMS API Documentation</title>
        <link rel="stylesheet" type="text/css" href="https://unpkg.com/swagger-ui-dist@5.9.0/swagger-ui.css" />
        <style>
            html { box-sizing: border-box; overflow: -moz-scrollbars-vertical; overflow-y: scroll; }
            *, *:before, *:after { box-sizing: inherit; }
            body { margin:0; background: #fafafa; }
        </style>
    </head>
    <body>
        <div id="swagger-ui"></div>
        <script src="https://unpkg.com/swagger-ui-dist@5.9.0/swagger-ui-bundle.js"></script>
        <script src="https://unpkg.com/swagger-ui-dist@5.9.0/swagger-ui-standalone-preset.js"></script>
        <script>
            window.onload = function() {
                const ui = SwaggerUIBundle({
                    url: '/api-docs',
                    dom_id: '#swagger-ui',
                    deepLinking: true,
                    presets: [
                        SwaggerUIBundle.presets.apis,
                        SwaggerUIStandalonePreset
                    ],
                    plugins: [
                        SwaggerUIBundle.plugins.DownloadUrl
                    ],
                    layout: "StandaloneLayout"
                });
            };
        </script>
    </body>
    </html>
    """
    from fastapi.responses import HTMLResponse
    return HTMLResponse(content=html_content)