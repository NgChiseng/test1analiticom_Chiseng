from django.shortcuts import render, get_object_or_404,redirect
# Used for import database information and timezone information.
from django.utils import timezone
from .models import Post
# Used for import the PostForm class and UserProfileForm class.
from .forms import PostForm,UserForm,UserProfileForm, UserLogin

from django.contrib.auth.hashers import make_password

from django.contrib.auth import authenticate, login, logout
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
	user = request.user
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts': posts}, {'user':user})

# Function that receive a request and  a primary key, then give the template post_detail.html.
#
# @date [06/04/2017]
#
# @author [Chiseng Ng]
#
# @param [request] request Request of the page.
# @param [post.pk] pk primary key of a post object.
#
# @returns [NONE]
def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})

# Function that call a Postform and send to post_edit template.
#If receive a POST request then validate it, complete it, and save it.
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

# Function that manage the register of the users.
#If receive a POST request then validate it, complete it, and save it.
#
# @date [07/04/2017]
#
# @author [Chiseng Ng]
#
# @param [request] request Request of the page.
#
# @returns [NONE]
def post_register(request):
    if request.method == 'POST':
        uf = UserForm(request.POST, prefix='user')
        #upf = UserProfileForm(request.POST, prefix='userprofile')
        if uf.is_valid(): #* upf.is_valid():
            user = uf.save(commit=False)
            user.password = make_password(user.password)
            user.save()
            #userprofile = upf.save(commit=False)
            #userprofile.user = user
            #userprofile.save()
            return redirect('post_list')
    else:
        uf = UserForm(prefix='user')
        upf = UserProfileForm(prefix='userprofile')
    return render(request, 'blog/post_register.html', {'form':uf})

# Function that manage the log in of the users.
#
# @date [10/04/2017]
#
# @author [Chiseng Ng]
#
# @param [request] request Request of the page.
#
# @returns [NONE]
def log_in(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('post_list')
		else:
			return redirect('log_in')
	else:
		pass
	return render(request,'blog/log_in.html')

# Function that manage the log out of the users.
#
# @date [10/04/2017]
#
# @author [Chiseng Ng]
#
# @param [request] request Request of the page.
#
# @returns [NONE]
def log_out(request):
	logout(request)
	return redirect('post_list')