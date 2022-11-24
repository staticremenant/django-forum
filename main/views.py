from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm, PostForm, CommentForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User, Group
from .models import Post, Comment
import os

# Create your views here.
def home(request):
    posts = Post.objects.all()
    comments = Comment.objects.all()
    form = CommentForm()

    if request.method == 'POST':
        post_id = request.POST.get('post-id')
        user_id = request.POST.get('user-id')
        leave_a_comment = request.POST.get('leave_a_comment')
        delete_comment = request.POST.get('delete_comment')
        ban_user_by_comment = request.POST.get('ban_user_by_comment')

        if post_id:
            post = Post.objects.filter(id=post_id).first()
            if post and (post.author == request.user or request.user.has_perm('main.delete_post')):
                if post.image:
                    try:
                        os.remove(post.image.path)
                    except:
                        pass
                post.delete()
            messages.success(request, f'Post have been deleted')

        elif user_id:
            user = User.objects.filter(id=user_id).first()
            if user and request.user.is_staff and (request.user != user):
                try:
                    group = Group.objects.get(name='default')
                    group.user_set.remove(user)
                except:
                    pass

                try:
                    group = Group.objects.get(name='mod')
                    group.user_set.remove(user)
                except:
                    pass
            messages.success(request, f'{user} have been banned')

        elif leave_a_comment:
            form = CommentForm(data=request.POST, files=request.FILES)
            if form.is_valid():
                post_id = leave_a_comment
                comment = form.save(commit=False)
                comment.author = request.user
                comment.post = Post.objects.filter(id=post_id).first()
                if comment.content or comment.image:
                    if not comment.content:
                        comment.content = "image"
                    comment.save()
            form = CommentForm()

        elif delete_comment:
            comment = Comment.objects.filter(id=delete_comment).first()
            if comment and (comment.author == request.user or request.user.has_perm('main.delete_post')):
                if comment.image:
                    try:
                        os.remove(comment.image.path)
                    except:
                        pass
                comment.delete()
            messages.success(request, f'Comment have been deleted')

        elif ban_user_by_comment:
            user = User.objects.filter(id=ban_user_by_comment).first()
            if user and request.user.is_staff and (request.user != user):
                try:
                    group = Group.objects.get(name='default')
                    group.user_set.remove(user)
                except:
                    pass

                try:
                    group = Group.objects.get(name='mod')
                    group.user_set.remove(user)
                except:
                    pass
            messages.success(request, f'{user} have been banned')

    return render(request, 'main/home.html', {'posts': posts[::-1], 'comment': form, 'comments': comments})

@login_required(login_url='/login')
@permission_required('main.add_post', login_url='/ban_warning')
def create_post(request):
    if request.method == 'POST':
        form = PostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            if post.description or post.title or post.image:
                if not post.title and not post.description:
                    post.title = "image"
                post.save()
                return redirect('/home')
    else:
        form = PostForm()

    return render(request, 'main/create_post.html', {'form': form})


def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {'form': form})

@login_required(login_url='/login')
def account(request):
    if request.method == 'POST':
        user_id = request.POST.get('user-id')
        user = User.objects.filter(id=user_id).first()
        user.delete()
        return redirect('/home')

    return render(request, 'main/account.html', {})

def ban_warning(request):
    return render(request, 'main/ban_warning.html')
