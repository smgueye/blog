"""Post Observer"""

from masoniteorm.models import Model


class PostObserver:
    def created(self, post):
        """Handle the Post "created" event.

        Args:
            post (masoniteorm.models.Model): Post model.
        """
        pass

    def creating(self, post):
        """Handle the Post "creating" event.

        Args:
            post (masoniteorm.models.Model): Post model.
        """
        print(1, post)
        pass

    def saving(self, post):
        """Handle the Post "saving" event.

        Args:
            post (masoniteorm.models.Model): Post model.
        """
        print(2, post)
        pass

    def saved(self, post):
        """Handle the Post "creating" event.

        Args:
            post (masoniteorm.models.Model): Post model.
        """
        pass

    def updating(self, post):
        """Handle the Post "creating" event.

        Args:
            post (masoniteorm.models.Model): Post model.
        """
        pass

    def updated(self, post):
        """Handle the Post "creating" event.

        Args:
            post (masoniteorm.models.Model): Post model.
        """
        pass

    def booted(self, post):
        """Handle the Post "creating" event.

        Args:
            post (masoniteorm.models.Model): Post model.
        """
        pass

    def booting(self, post):
        """Handle the Post "creating" event.

        Args:
            post (masoniteorm.models.Model): Post model.
        """
        pass

    def hydrating(self, post):
        """Handle the Post "creating" event.

        Args:
            post (masoniteorm.models.Model): Post model.
        """
        pass

    def hydrated(self, post):
        """Handle the Post "creating" event.

        Args:
            post (masoniteorm.models.Model): Post model.
        """
        pass

    def deleting(self, post):
        """Handle the Post "creating" event.

        Args:
            post (masoniteorm.models.Model): Post model.
        """
        pass

    def deleted(self, post):
        """Handle the Post "creating" event.

        Args:
            post (masoniteorm.models.Model): Post model.
        """
        pass
