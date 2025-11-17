from django.shortcuts import render,redirect
from . models import Post, Comment
from django.shortcuts import get_object_or_404
from .forms import CommentForm

def home(request):
    blogs = Post.objects.all()
    carowsel = Post.objects.all().order_by('-id')[:5]
    context= {
        'blogs':blogs,
        'carowsel':carowsel
    }
    return render(request, 'index.html', context)

def singlepage(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # post = Post.objects.get(slug=slug)
    comment = post.comment.all()
    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog_post = post
            comment.save()
            return redirect('singlepage', pk=pk)
    else:
        form = CommentForm()
    return render(request, 'singlepage.html', {'post':post,'form':form,'comment':comment} )

def post_like(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.likes +=1
    post.save()
    return redirect('singlepage', pk=pk)

def search(request):
    query = request.GET.get('q', '')
    results = Post.objects.filter(title__icontains=query)
    
    return render(request, 'search.html',{'query':query, 'results': results})
    