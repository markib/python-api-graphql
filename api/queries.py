from .models import Post
from ariadne import convert_kwargs_to_snake_case


def listPosts_resolver(obj, info):
    try:
        posts = [post.to_dict() for post in Post.query.all()]
        # posts = [
        #     {
        #         "id": "1",
        #         "title": "Post 1",
        #         "description": "Content of Post 1",
        #         "created_at": "2024-06-25T12:00:00Z",
        #     },
        #     {
        #         "id": "2",
        #         "title": "Post 2",
        #         "description": "Content of Post 2",
        #         "created_at": "2024-06-26T12:00:00Z",
        #     },
        # ]
        # posts = Post.findAll()
        print(posts)
        payload = {"success": True, "posts": posts}
    except Exception as error:
        # Log the exception for debugging purposes
        print(f"Error fetching posts: {str(error)}")
        payload = {"success": False, "errors": [str(error)]}
    return payload


@convert_kwargs_to_snake_case
def getPost_resolver(obj, info, id):
    try:
        post = Post.query.get(id)
        payload = {"success": True, "post": post.to_dict()}
    except AttributeError:  # todo not found
        payload = {"success": False, "errors": ["Post item matching {id} not found"]}
    return payload
