from datetime import datetime

from masonite.controllers import Controller
from masonite.request import Request
from masonite.views import View

from app.helpers import sluglify
from app.models.Category import Category
from app.models.Post import Post


class BlogController(Controller):
    def show(self, view: View):
        posts = Post.all()
        return view.render("posts/list", {
            "posts": posts
        })

    def new(self, view: View):
        return view.render("posts/new", {
            "categories": Category.get().all()
        })

    def create(self, request: Request):
        category_id = request.input('category_id')
        content = request.input('content')
        title = request.input('title')

        slug = sluglify(title)
        date = datetime.now()

        Post.create(content=content, title=title, slug=slug, date=date,
                    category_id=category_id,
                    author_id=request.user().id)

        return 'Post created !'

    def detail(self, view: View, request: Request):
        post = Post.where('slug', request.params.get('slug')).first()

        return view.render('posts/detail', {'post': post})

    def edit(self, view: View, request: Request):
        post = Post.find(request.params.get('id'))
        return view.render("posts/edit", {
            "categories": Category.get().all(),
            "post": post
        })

    def update(self, request: Request):
        post = Post.find(request.params.get('id'))

        post.category_id = request.input('category_id')
        post.content = request.input('content')
        post.title = request.input('title')
        post.slug = sluglify(request.input('title'))
        post.date = datetime.now()
        post.save()

        return 'Post updated !'

    def delete(self, request: Request):
        post = Post.find(request.param('id'))
        post.delete()
        return 'post deleted'
