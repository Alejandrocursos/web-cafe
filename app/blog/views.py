from django.shortcuts import render, get_object_or_404
from .models import Post, Category
# Create your views here.

def blog(request):
    model = Post
    posts = Post.objects.all()
    args= {'posts':posts}
    return render(request,"blog/blog.html",args)


#Vieja forma
'''
def category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.filter(categories=category)
    return render(request, 'blog/category.html', {'category':category,
                                                    'posts':posts})
'''

#Nueva forma
def category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    return render(request, 'blog/category.html', {'category':category})
                                                