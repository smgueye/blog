""" User Model """

from masoniteorm.models import Model
from masoniteorm.relationships import has_many


class Category(Model):
    """Category Model"""

    __fillable__ = ["name", "slug"]
    __guarded__ = ["slug"]
    __timezone__ = "Africa/Dakar"

    @has_many("id", "category_id")
    def posts(self):
        from app.models.Post import Post
        return Post
