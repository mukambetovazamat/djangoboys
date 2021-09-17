from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Comment
from .forms import PostForm, CommentForm



def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=post)

    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def comment(request, pk):
    get_404 = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post_id = Post.objects.get(id=pk)
            post.post = post_id
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/post_detail.html', {'form': form})

















# def comment(request):
#     post = get_object_or_404(Comment, pk=pk)
#     error = ''
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('post_detail', pk=post.pk)
#         else:
#             error = 'No valid'
#
#     form = CommentForm
#     context = {
#         'form': form
#     }
#
#     return render(request, 'blog.post_detail.html', context)






# def comment(request):
#     form = CommentForm()
#     context = {
#         'form': form
#     }
#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             new_comment = form.save(commit=False)
#             new_comment.author = request.user
#             new_comment.published_date = timezone.now()
#             new_comment.save()
#             return redirect('post_detail', pk=new_comment.pk)
#     else:
#         form = CommentForm()
#     return render(request, 'blog/post_detail.html', context)


# def comm_list(request):
#     posts = Comment.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#     return render(request, 'blog/post_detail.html', {'posts': posts})


