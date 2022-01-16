"""CreatePostsTable Migration."""

from masoniteorm.migrations import Migration


class CreatePostsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("posts") as table:
            table.increments("id")
            table.string("title")
            table.string("slug")
            table.long_text("content")
            table.date("date")
            table.integer("category_id")
            table.integer("author_id")

            table.foreign("category_id") \
                .references("id") \
                .on("categories") \
                .on_delete('cascade')
            table.foreign("author_id") \
                .references("id") \
                .on("users") \
                .on_delete('cascade')

            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("posts")
