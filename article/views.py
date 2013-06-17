# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.template import Context
from django.views.generic.base import TemplateView
from article.models import Article, Comment
from forms import ArticleForm, CommentForms
from django.core.context_processors import csrf
from django.utils import timezone


def articles(request):
    language = 'en-gb'
    session_language = 'en-gb'

    if 'lang' in request.COOKIES:
        language = request.COOKIES['lang']

    if 'lang' in request.session:
        session_language = request.session['lang']

    args = {}
    args.update(csrf(request))

    args['articles'] = Article.objects.all()
    args['language'] = language
    args['session_language'] = session_language

    return render_to_response('articles.html', args)


def article(request, article_id=1):
    return render_to_response('article.html',
                              {'article':Article.objects.get(id=article_id)})


def language(request, language='en-gb'):

    response = HttpResponse("settings language %s" % language)

    response.set_cookie('lang', language)

    request.session['lang'] = language

    return response


def create(request):
    if request.POST:
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/articles/all/')
    else:
        form = ArticleForm()

    args = {}
    args.update(csrf(request))
    args['form'] = form

    return render_to_response("create.html", args)


def like_article(request, article_id):
    a = Article.objects.get(id = article_id)
    count = a.likes
    count+= 1
    a.likes = count
    a.save()
    return HttpResponseRedirect('/articles/get/%s/'% article_id)


def add_comment(request, article_id):
    a = Article.objects.get(id = article_id)

    if request.method == "POST":
        f = CommentForms(request.POST)
        if f.is_valid():
            c = f.save(commit=False)
            c.pub_date = timezone.now()
            c.article = a
            c.save()
            return HttpResponseRedirect('/articles/get/%s/' % article_id)
    else:
        f = CommentForms()

    args ={}
    args.update(csrf(request))
    args['article'] = a
    args['form'] = f
    return render_to_response('add_comment.html', args)


def search_title(request):
    if request.method == "POST":
        search_text = request.POST['search_text']
    else:
        search_text = ''

    articles = Article.objects.filter(title__contains = search_text)

    return render_to_response('ajax_search.html', {'articles': articles})


def hello(request):
    name = "Step"
    html = "<html><body>Hi %s. It's work</body></html>" % name
    return HttpResponse(html)


def hello_template(request):
    name = "Step"
    t = get_template("hello.html")
    html = t.render(Context({'name':name}))
    return HttpResponse(html)

def hello_template_simple(request):
    name = "Step"
    return render_to_response("hello.html",{'name':name})


class HelloTemplate(TemplateView):
    template_name = "hello_class.html"

    def get_context_data(self, **kwargs):
        context = super(HelloTemplate, self).get_context_data(**kwargs)
        context['name'] = 'Step'
        return context

