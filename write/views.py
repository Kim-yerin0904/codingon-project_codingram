from django.shortcuts import render,redirect
from .models import Post

# Create your views here.
def index(request):
    return render(request,"index.html")

def blog(request):
    postlist = Post.objects.all()
    if request.method == 'POST':
            new_article=Post.objects.create(
                postname=request.POST.get('postname'),
                contents=request.POST.get('contents')
            )
            return redirect('../blog/')

    return render(request,'blog.html',{'postlist':postlist})

def posting(request, pk):
    #게시글(Post)중 pk를 이용해 하나의 게시글을 검색
    post = Post.objects.get(pk=pk)
    #posting.html 열때 찾아낸 게시글을 post란 이름으로 가져옴
    return render(request,'posting.html',{'post':post})


def portfolio(request):
    return render(request,"portfolio.html")
