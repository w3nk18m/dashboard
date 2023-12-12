from pcweb.route import Route
from .output import *
from .subject_concept import *

output_routes = [r for r in locals().values() if isinstance(r, Route)]
