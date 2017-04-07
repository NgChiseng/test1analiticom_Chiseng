from django.shortcuts import render, get_object_or_404,redirect
# Usado para sacar datos de la base de datos y usarlo en la plantilla.
from django.utils import timezone
from .models import Post
# Usado para sacar la clase PostForm
from .forms import PostForm
# Create your views here.

# Function that receive a request and give the template post_list.html.
#
# @date [06/04/2017]
#
# @author [Chiseng Ng]
#
# @param [request] request Request of the page.
#
# @returns [NONE]
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts': posts})

# Function that receive a request and  a primary key, then give the template post_detail.html.
#
# @date [06/04/2017]
#
# @author [Chiseng Ng]
#
# @param [request] request Request of the page.
#
# @returns [NONE]
def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})

# Function that call a Postform and send to post_edit template.
#If receive a POST request for validate it, complete it, and save it.
#
# @date [06/04/2017]
#
# @author [Chiseng Ng]
#
# @param [request] request Request of the page.
#
# @returns [NONE]
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