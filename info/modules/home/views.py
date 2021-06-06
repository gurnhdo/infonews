from .import home_blu


@home_blu.route('/')
def index():
    # sr.set("name", "zs")
    # session["name"] = "ls"
    return 'index11111'
