from info import sr
from .import home_blu


@home_blu.route('/')
def index():
    # sr.set("name", "zs")
    # session["name"] = "ls"
    sr.set("name","zs")
    return 'index11111'
