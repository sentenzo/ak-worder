"""
Parsing / scraping / caching the information about English words (from various online dictionaries) under a unified API
"""
try:
    import dotenv

    dotenv.load_dotenv()
except ImportError:
    pass

from ak_worder.__main__ import app, make_app


__all__ = ["make_app", "app"]
