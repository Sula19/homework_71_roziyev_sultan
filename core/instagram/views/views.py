from django.shortcuts import redirect, get_object_or_404, reverse
from django.views.generic import CreateView, ListView, View, UpdateView, DeleteView, DetailView
from instagram.models import Comment
from instagram.models.post import Post
from django.db.models import Q
from instagram.forms import PostForm, CommentForm
from accounts.models import Account
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin


class IndexView(ListView):
    template_name = 'home.html'
    model = Post
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['posts'] = Post.objects.all()
        search = self.request.GET.get('search')
        if search:
            query = get_user_model().objects.filter(
                Q(email__icontains=search) | Q(first_name__icontains=search) | Q(username__icontains=search)
            )
            context['query'] = query
        context['form'] = CommentForm
        return context


class CreatePost(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'posts/create_post.html'
    form_class = PostForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = self.request.user
            form.save()
            return redirect('/')
        context = {'form': form}
        return self.render_to_response(context)


class DetailPost(DetailView):
    template_name = 'posts/detail_post.html'
    model = Post
    context_object_name = 'post'


class UpdatePost(UserPassesTestMixin, UpdateView):
    template_name = 'posts/update_post.html'
    model = Post
    form_class = PostForm

    def test_func(self):
        return self.get_object().author == self.request.user

    def get_success_url(self):
        return redirect('/')


class DeletePost(UserPassesTestMixin, DeleteView):
    template_name = 'posts/delete_post.html'
    model = Post
    success_url = '/'

    def test_func(self):
        return self.get_object().author == self.request.user


class Subscribes(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = get_object_or_404(Account, pk=kwargs.get('pk'))
        current_user = request.user
        if current_user in user.subscriptions_acc.all():
            user.subscriptions_acc.remove(current_user)
        else:
            user.subscriptions_acc.add(current_user)
        return redirect('/')


class AddLike(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs.get('pk'))
        user = request.user
        if post not in user.laked_post.all():
            messages.success(request, f'Пользователь {request.user} поставил лайк')
            user.laked_post.add(post)
        else:
            messages.warning(request, 'Вы не можете лакайтаь пост больше одного раза')
            pass
        return redirect('/')


class CommentList(ListView):
    template_name = 'comments/comments.html'
    model = get_user_model()
    context_object_name = 'comments'


class AddComment(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        post = get_object_or_404(Post, pk=self.kwargs.get('pk'))
        comment = form.save(commit=False)
        comment.post = post
        comment.author = self.request.user
        form.save()
        messages.success(self.request, f'Пользователь {self.request.user} прокомментировал пост автора {post.author}')
        comment.author.commented_post.add(post)
        return redirect('/')


class UpdateComment(UserPassesTestMixin, UpdateView):
    template_name = 'comments/update_comment.html'
    model = Comment
    form_class = CommentForm
    success_url = '/'

    def test_func(self):
        return self.get_object().author == self.request.user


class DeleteComment(UserPassesTestMixin, DeleteView):
    model = Comment

    def post(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, pk=kwargs.get('pk'))
        comment.author.commented_post.remove(comment.post)
        comment.delete()
        return redirect('/')

    def test_func(self):
        return self.get_object().author == self.request.user
