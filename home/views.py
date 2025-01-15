
from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from .models import Article , Category
from django.core.paginator import Paginator

# Create your views here.
def home(request , page=1):
    Article_list = Article.objects.Published()
    paginator = Paginator(Article_list, 4)
    articles = paginator.get_page(page)
    context = {
        "Articles" : articles,
        }
    return render(request , 'home.html',context)
def detail(request , slug):
    context = {
      "Article" : get_object_or_404(Article.objects.Published() , sluge = slug),
    }
    return render(request , 'detail.html',context)

def category(request , slug , page = 1):
    category = get_object_or_404(Category , sluge = slug , status = True)
    Articles_List = category.Articles.Published()
    paginator = Paginator(Articles_List, 4)
    articles = paginator.get_page(page)

    context = {
      "Category" : category,
      "articles" : articles
    }
    return render(request , 'Category.html',context)

    

    
    