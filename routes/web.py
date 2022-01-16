from masonite.authentication import Auth
from masonite.routes import Route

ROUTES = [
    Route.get("/", "HomeController@show"),

    # Blog Routes
    Route.get("/blog", "BlogController@show"),
    Route.get("/blog/new", "BlogController@new"),
    Route.post("/blog/create", "BlogController@create"),
    Route.get("/blog/@slug", "BlogController@detail"),
    Route.get("/blog/edit/@id", "BlogController@edit"),
    Route.post("/blog/update/@id", "BlogController@update"),
    Route.get("/blog/@id/delete", "BlogController@delete"),
]

ROUTES += Auth.routes()
