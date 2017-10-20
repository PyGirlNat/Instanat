from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.views import View
from django.views.generic import CreateView
from .forms import LoginForm, RegisterForm
from .models import Post, Comment


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('instanat:user', args=[request.user.username]))

        form = LoginForm()
        return render(request, 'instanat/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(username, password)
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('instanat:user', args=[username]))
            else:
                return render(request, 'instanat/login.html', {'form': form})
        else:
            return render(request, 'instanat/login.html', {'form': form})


class UserView(View):
    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        posts = Post.objects.filter(user=user.id)
        return render(request, 'instanat/user.html', {'posts': posts})


class UploadView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['image']
    template_name = 'instanat/upload.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(UploadView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('instanat:user', kwargs={'username': self.request.user.username})

class AddCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['text']
    template_name = 'instanat/add_comment.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = Post.objects.get(pk=self.kwargs['post_id'])
        return super(AddCommentView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('instanat:show_post', kwargs={'post_id': self.kwargs['post_id']})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('instanat:login'))


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'instanat/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=username, password=password)
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect(reverse('instanat:main', kwargs={'username': username}))
        else:
             return HttpResponse('Incorrect username or password')


class DeleteImageView(LoginRequiredMixin, View):
    def get(self, request, id):
        if request.user.is_authenticated:
            post = Post.objects.get(pk=id)
            if post.user == request.user:
                post.delete()

        return HttpResponseRedirect(reverse('instanat:user', kwargs={'username': request.user}))

class SubscribeView(LoginRequiredMixin, View):
    def get(self, request, username):
        user = get_object_or_404(User, username=username)


class ShowPostView(View):
    def get(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        user = get_object_or_404(User, pk=post.user.id)
        comments = Comment.objects.filter(post=post.id)
        context = {
            'post': post,
            'user': user,
            'comments': comments
        }
        return render(request, 'instanat/show_post.html', context)
