from pcweb.route import Route
from .input import *
from .subject_concept import *
from .subject_grading_criteria import *
from .ability_grading_criteria import *

input_routes = [r for r in locals().values() if isinstance(r, Route)]
