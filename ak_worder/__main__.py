import uvicorn
from fastapi import FastAPI

from ak_worder.endpoints import v1


def make_app() -> FastAPI:
    """
    Creates FastAPI app
    """
    app_ = FastAPI()

    for api_version in [v1]:
        for router in api_version:
            app_.include_router(router, prefix="")

    return app_


app = make_app()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
