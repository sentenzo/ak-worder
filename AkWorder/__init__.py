try:
    import dotenv

    dotenv.load_dotenv()
except ImportError:
    pass

from AkWorder.__main__ import make_app, app

__all__ = [make_app, app]
