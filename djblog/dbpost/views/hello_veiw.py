from django.http import HttpResponse
from dbpost.models.models import Post
from dbauth.models.models import User
from django.utils import timezone


def home_page_veiw(request):
    post_queryset = Post.objects.all()
    response = []

    for post in post_queryset:
        data = {
            "id": post.id,
            "title": post.title,
        }

        response.append(data)
    return HttpResponse(response)


def create_post(request, *args, **kwargs):
    response = []
    admin_user = User.objects.get(username="admin")
    post = Post(title="Test post", user=admin_user, description="This is the description of test post.",
                published=timezone.now())
    post.save()

    post_queryset = Post.objects.all()
    data = {
        "id": post_queryset[len(post_queryset) - 1].id,
        "title": post_queryset[len(post_queryset) - 1].title,
    }
    response.append(data)

    return HttpResponse(response)
