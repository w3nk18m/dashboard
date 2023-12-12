from pcweb.route import Route
# from .docs import doc_routes
# from .changelog import changelog_routes
# from .blog import blog_routes
# from .index import index
# from .faq import faq_routes
from .input import input_routes
from .output import output_routes

routes = [r for r in locals().values() if isinstance(r, Route)]
