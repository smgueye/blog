""" User Model """

from masoniteorm.models import Model


class Tag(Model):
    """Tag Model"""

    __table__ = "posts"
    __fillable__ = ["name"]
    __timezone__ = "Africa/Dakar"
