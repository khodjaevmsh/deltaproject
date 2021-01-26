from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post, Comment
from django.db.models import Q
from .forms import RegisterForm
# Create your views here.


def index(request):
    # posts = Post.objects.all()[:3]
    posts = Post.objects.all().order_by('-date')[:3]
    popular = Post.objects.filter(popular__gte=10)
    return render(request, 'blog/index.html', {'posts': posts, 'popular': popular})


def search_result(request):
    query = request.GET.get('search')
    search_obj = Post.objects.filter(
        Q(title__icontains=query) | Q(description__icontains=query)
    )
    return render(request, 'blog/search.html', {'search_obj': search_obj, 'query': query})


def post_detail(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    post.popular += 1
    post.save()
    return render(request, 'blog/post_detail.html', {'post': post})


def register(surov):
    if surov.method == 'POST':
        form = RegisterForm(surov.POST)
        if form.is_valid():
            form.save()
            # log the user in
            return redirect('home')
    else:
        form = RegisterForm()
    return render(surov, 'blog/register.html', {'form': form})


def leave_comment(request, slug):
    try:
        post = Post.objects.get(slug__iexact=slug)
    except:
        raise Http404("Статья не найдена")
    if request.user.is_authenticated:
        user = request.user.first_name
        post.comments.create(author_name=user,
                             comment_text=request.POST.get('comment_text'))
    else:
        post.comments.create(
            author_name=request.POST.get('name'), comment_text=request.POST.get('comment_text'))
        comment = Comment.objects.order_by('-date')[:12]
    return HttpResponseRedirect(reverse('post_detail_url', args=(post.slug,)))
