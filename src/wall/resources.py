from src.wall.models import Post, Comment
from import_export import resources

class PostResource(resources.ModelResource):

    class Meta:
        model = Post
        fields = ('id', 'title', 'text', 'user', 'idtechnology',)



class CommentResource(resources.ModelResource):

    class Meta:
        model = Comment
        fields = ('id', 'text', 'post', 'user',)


