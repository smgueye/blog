""" User Model """

from masoniteorm.models import Model
from masoniteorm.relationships import belongs_to, belongs_to_many

from app.models.observers.PostObserver import PostObserver


class Post(Model):
    """Post Model"""

    __table__ = "posts"
    __fillable__ = ["title", "content", "slug", "date", "category_id", "author_id"]
    # __guarded__ = ["author_id"]
    __timezone__ = "Africa/Dakar"

    @belongs_to("category_id", "id")
    def category(self):
        from app.models.Category import Category
        return Category

    @belongs_to("author_id", "id")
    def author(self):
        from app.models.User import User
        return User

    @belongs_to_many(with_timestamps=True)
    def tags(self):
        from app.models.Tag import Tag
        return Tag


Post.observe(PostObserver())
