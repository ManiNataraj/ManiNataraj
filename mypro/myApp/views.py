# news/views.py
from django.shortcuts import render, get_object_or_404
from .models import Article, Advertisement
from .forms import ContactForm

# View for article detail
def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'article_detail.html', {'article': article})

# View for homepage listing all articles
def home(request):
    articles = Article.objects.all().order_by('-published_date')  # Fetch articles
    advertisements = Advertisement.objects.all()  # Fetch advertisements

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        # Render the partial template for AJAX requests
        return render(request, 'article_list.html', {'articles': articles})

    # Render the full page with both articles and advertisements
    return render(request, 'home.html', {'articles': articles, 'advertisements': advertisements})


def article_list(request):
    # Fetch all articles from the database, ordered by the latest published date
    articles = Article.objects.all().order_by('-published_date')
    return render(request, 'article_list.html', {'articles': articles})

def world(request):
    articles = Article.objects.filter(category='world').order_by('-published_date')
    return render(request, 'world.html', {'articles': articles})

def politics(request):
    articles = Article.objects.filter(category='politics').order_by('-published_date')
    return render(request, 'politics.html', {'articles': articles})

def sports(request):
    articles = Article.objects.filter(category='sports').order_by('-published_date')
    advertisements = Advertisement.objects.all()
    return render(request, 'sports.html', {'articles': articles,'advertisements': advertisements})

def entertainment(request):
    articles = Article.objects.filter(category='entertainment').order_by('-published_date')
    return render(request, 'entertainment.html', {'articles': articles})

def innovations(request):
    articles = Article.objects.filter(category='innovations').order_by('-published_date')
    return render(request, 'innovations.html', {'articles': articles})

def business(request):
    articles = Article.objects.filter(category='business').order_by('-published_date')
    return render(request, 'business.html', {'articles': articles})



def like_article(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
        article.like_count += 1
        article.save()
        return JsonResponse({'status': 'success', 'like_count': article.like_count})
    except Article.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Article not found'}, status=404)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact_success.html')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})