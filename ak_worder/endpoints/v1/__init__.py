from .ping import api_router as ping_router


v1_routers = [ping_router]

__all__ = ["v1_routers"]
