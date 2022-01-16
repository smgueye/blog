"""User Model."""
from masonite.authentication import Authenticates
from masoniteorm.models import Model
from masoniteorm.relationships import has_many
from masoniteorm.scopes import SoftDeletesMixin


class User(Model, SoftDeletesMixin, Authenticates):
    """User Model."""

    __fillable__ = ["name", "email", "password"]
    __hidden__ = ["password"]
    __auth__ = "email"
    __timezone__ = "Africa/Dakar"

    @has_many("id", "author_id")
    def posts(self):
        from app.models.Post import Post
        return Post
