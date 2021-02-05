
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy

from .models import Post
from django.http import HttpRequest, HttpResponse, Http404
from django.views.generic import ListView, DetailView, ArchiveIndexView, YearArchiveView, DayArchiveView, CreateView, \
    UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

# post_list = \
#     login_required(ListView.as_view(model=Post, paginate_by=10))
from .forms import PostForm



# @login_required
# def post_new(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.save()
#             messages.success(request, '포스팅을 저장했습니다.')
#             return redirect(post)
#     else:
#         form = PostForm()
#
#     return render(request, 'instagram/post_form.html', {
#         'form': form,
#     })

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.ip = self.request.META['REMOTE_ADDR']
        messages.success(self.request, '포스팅을 저장했습니다.')
        return super().form_valid(form)

post_new = PostCreateView.as_view()

# @login_required
# def post_edit(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     # 작성자 체크 팁
#     if post.author != request.user:
#         messages.error(request, '작성자만 수정할 수 있습니다.')
#         return redirect(post)
#
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES, instance=post)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.ip = request.META['REMOTE_ADDR']
#             post.author = request.user
#             post.save()
#             messages.success(request, '포스팅을 수정 했습니다.')
#             return redirect(post)
#     else:
#         form = PostForm(instance=post)
#
#     return render(request, 'instagram/post_form.html', {
#         'form': form,
#     })

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.ip = self.request.META['REMOTE_ADDR']
        messages.success(self.request, '포스팅을 수정했습니다.')
        return super().form_valid(form)


post_edit = PostUpdateView.as_view()


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('instagram:post_list')
    def get_success_url(self):
        return reverse('instagram:post_list')

post_delete = PostDeleteView.as_view()


# @login_required
# def post_delete(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#
#     if request.method == "POST":
#         post.delete()
#         messages.success(request, '게시글을 삭제하였습니다.')
#         return redirect('instagram:post_list')
#
#     return render(request, 'instagram/post_confirm_delete.html', {
#         'post': post,
#     })

class PostListView(LoginRequiredMixin, ListView):
    model = Post
    paginate_by = 100

post_list = PostListView.as_view()

# @login_required
# def post_list(request):
#     q = request.GET.get('q', '')
#
#     qs = Post.objects.all()
#     if q:
#         qs = qs.filter(message__icontains=q)
#
#     # messages.info(request, 'messages 테스트')
#     # instagram/templates/instagram/post_list.html
#     return render(request, 'instagram/post_list.html', {
#         'post_list': qs, 'q': q,
#     })


# def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
#     try:
#         post = Post.objects.get(pk=pk) # DoesNotExist
#     except Post.DoesNotExist:
#         raise Http404
#     return render(request, 'instagram/post_detail.html', {
#         'post': post,
#     })

# def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'instagram/post_detail.html', {
#         'post': post,
#     })
# post_detail = DetailView.as_view(model=Post, pk_url_kwarg='pk',
#                                  queryset=Post.objects.filter(is_public=True))
# 데코레이터 이해할것!


class PostDetailView(DetailView):
    model = Post
    pk_url_kwarg = 'pk'

# post_detail = PostDetailView.as_view()
# class PostDetailView(DetailView):
#     model = Post
#
#     def get_queryset(self):
#         qs = super().get_queryset()
#         if self.request.user.is_authenticated:
#           qs = qs.filter(is_public=True)
#         qs = qs.filter()
#         return qs

post_detail = PostDetailView.as_view()

post_archive = ArchiveIndexView.as_view(model=Post, date_field='created_at', paginate_by=10)
post_archive_year = YearArchiveView.as_view(model=Post, date_field='created_at', make_object_list=True)
post_archive_year_month_day = DayArchiveView.as_view(model=Post, date_field='created_at')

def archives_year(request: HttpRequest, year: int) -> HttpResponse:
    response = HttpResponse()
    response.write(year)
    return response


def test_detail(request):
    return render(request, 'instagram/test.html')
