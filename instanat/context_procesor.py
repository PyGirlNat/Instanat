# from .models import Post
#
#
# def my_cp(request):
#     user = request.user
#     # images = Post.objects.filter(user=user).order_by('added_date')
#     posts = Post.objects.filter(user=user.id).order_by('added_date')
#     ctx = {
#         'posts': posts,
#     }
#     return ctx
