from django.shortcuts import render
from .forms import UserForm, CommentForm, BlogForm
from .models import User, Blog, Comment, Category

from django.shortcuts import redirect
from django.urls import reverse

from .modules.weatherparser import parse_url
from .modules.hashutils import check_pw_hash, make_pw_hash

from .modules.Weather import Weather
from .modules.ImagesParser import ImagesParser

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.utils import timezone

COUNT_BLOG_ON_PAGE=10


def get_paginated_blogs(request, paginator):
    page = request.GET.get('page')
    try:
        page = int(page)
    except:
        page = 1
    a = ""
    blog = ""
    pages=[]
    if page:
        try:
            blog = paginator.page(page)
        except EmptyPage:
            blog = paginator.page(paginator.num_pages)
            page = paginator.num_pages

        for i in range(page-2, page+3):
            try:
                a = paginator.page(i)
                pages.append(i)
            except:
                continue
        print(pages)
        if pages[-1] != paginator.num_pages:
            pages.append(paginator.num_pages)

        if pages[0] != 1:
            pages.insert(0, 1)
    else:
        pages = [1,2,3,4,5,paginator.num_pages]
        blog = paginator.page(1)
    return blog, pages


def get_current_user(request):
    try:
        user_id = request.session["user_id"]
        user = User.objects.get(id=user_id)
        return user 
    except:
        return None  

def get_parameter(request, name):
    try:
        return request.GET[name]
    except:
        return None 


def logout(request):
    user = None
    if request.method == "POST":
        try:
            del request.session["user_id"]
        except:
            print("error")
    return redirect(reverse('main:index'))

def login(request):
    user1 = None
    user2 = None
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            try:
                user1 = User.objects.get(email=request.POST['email'])
            except:
                print("not logged")
            try:
                user2 = User.objects.get(username=request.POST['email'])
            except:
                print("not logged")
            if user1:
                if check_pw_hash(request.POST['password'], user1.password):
                    request.session["user_id"] = user1.id
                    return redirect(reverse('main:index'))
                else:
                    return redirect(reverse('main:index') + "?login_error=true")
            elif user2:
                if check_pw_hash(request.POST['password'], user2.password):
                    request.session["user_id"] = user2.id
                    return redirect(reverse('main:index'))
                else:
                    return redirect(reverse('main:index') + "?login_error=true")
            else:
                return redirect(reverse('main:index') + "?login_error=true")
    return redirect(reverse('main:index'))

def register(request):
    user1 = None
    user2 = None
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            password_confirm = request.POST['password_confirm']
            username = request.POST['username']
            
            if password != password_confirm:
                return redirect(reverse('main:registration') + "?register_error=2")

            if len(password) < 8:
                return redirect(reverse('main:registration') + "?register_error=3")


            try:
                user1 = User.objects.get(email=email)
            except:
                print("not logged")
            
            try:
                user2 = User.objects.get(username=username)
            except:
                print("not logged")
            
            if user1 or user2:
                 return redirect(reverse('main:registration') + "?register_error=1")

            hash_password = make_pw_hash(password)
            
            user = User.objects.create(email=email, password=hash_password, username=username)
            user.save()
            return redirect(reverse('main:index'))
            
               
    return redirect(reverse('main:registration'))
                

def index(request):
    user = get_current_user(request)
    login_error = get_parameter(request, "login_error")
    register_error = get_parameter(request, "register_error")

    return render(request, 'index.html', {
        "login_error" : login_error,
        "user": user,
        "register_error" : register_error,
    })

def not_found(request):
    user = get_current_user(request)
    return render(request, '404.html', {
        "user": user
    })

def about(request):
    user = get_current_user(request)
    return render(request, 'about-us.html', {
        "user": user
    })

def base(request):
    user = get_current_user(request)
    return render(request, 'base.html', {
        "user": user
    })

def blog(request, id):
    current_blog = None
    try:
        current_blog = Blog.objects.filter(id=id).first()
    except:
        print("blog not found!")
    if not current_blog:
        return redirect(reverse('main:index'))

    popular_blogs = Blog.objects.order_by("-views")[:3]
    user = get_current_user(request)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.owner = user
            comment.save()

            current_blog.comments.add(comment)
            current_blog.save()
            return redirect(reverse('main:blog', args=[id]) + "#comments")

    current_blog.views += 1
    current_blog.save()
    
    return render(request, 'blog-item.html', {
        "user": user,
        "blog": current_blog,
        "popular_blogs": popular_blogs
    })

def category_blogs(request, category):
    blogs = []
    c = Category.objects.filter(name=category).first()
    blogs = Blog.objects.filter(category__id=c.id)

    categories = Category.objects.all()
    popular_blogs = Blog.objects.order_by("-views")[:3]
    
    paginator = Paginator(blogs, COUNT_BLOG_ON_PAGE)

    paginated_blogs, pages = get_paginated_blogs(request, paginator)
    
    user = get_current_user(request)
    return render(request, 'blog.html', {
        "user": user,
        "blogs": paginated_blogs,
        "pages": pages,
        "categories": categories,
        "current_category": c,
        "popular_blogs": popular_blogs,
    })

def blogs(request):
    blogs = Blog.objects.all()

    popular_blogs = Blog.objects.order_by("-views")[:3]

    categories = Category.objects.all()

    paginator = Paginator(blogs, COUNT_BLOG_ON_PAGE)

    paginated_blogs, pages = get_paginated_blogs(request, paginator)

    user = get_current_user(request)
    return render(request, 'blog.html', {
        "user": user,
        "blogs": paginated_blogs,
        "pages": pages,
        "categories": categories,
        "popular_blogs": popular_blogs,
    })

def career(request):
    user = get_current_user(request)
    return render(request, 'career.html', {
        "user": user
    })    

def contact(request):
    user = get_current_user(request)
    return render(request, 'contact-us.html', {
        "user": user
    })

def faq(request):
    user = get_current_user(request)
    return render(request, 'faq.html', {
        "user": user
    })

def pricing(request):
    user = get_current_user(request)
    return render(request, 'pricing.html', {
        "user": user
    })

def privacy(request):
    user = get_current_user(request)
    return render(request, 'privacy.html', {
        "user": user
    })

def raw_images(request):
    rover = get_parameter(request, "rover")
    sol = get_parameter(request, "sol")
    camera = get_parameter(request, "camera")
    links = []

    if rover and sol and camera:
        imagesParser = ImagesParser(rover, camera, sol)
        data = imagesParser.get_images_links()
        print(data)
        links = []
        for i in range(0, len(data["photos"])):
            links.append(data["photos"][i]["img_src"])

    print(links)

    user = get_current_user(request)
    return render(request, 'rawImages.html', {
        "user": user,
        "links": links,
    })

def registration(request):
    user = get_current_user(request)
    login_error = get_parameter(request, "login_error")
    register_error = get_parameter(request, "register_error")

    return render(request, 'registration.html', {
        "user": user,
        "register_error": register_error,
    })

def services(request):
    user = get_current_user(request)
    return render(request, 'services.html', {
        "user": user
    })

def terms(request):
    user = get_current_user(request)
    return render(request, 'terms.html', {
        "user": user
    })

def typography(request):
    user = get_current_user(request)
    return render(request, 'typography.html', {
        "user": user
    })

def admin_panel(request):
    user = get_current_user(request)
    categories = Category.objects.all()
    

    if request.method == "POST":
        image = request.FILES['preview']
        title = request.POST["title"]
        description = request.POST["description"]
        post_category = request.POST["category"]
        
        if not image.name.endswith(".png") and not image.name.endswith(".jpg"):
            upload_error = "Выберите .jpg или .png формат для картинки!" 
            return render(request, 'admin.html', {
                "user": user,
                "upload_error": upload_error,
                "error_code": "1",
                "categories": categories
            })
        
        c = Category.objects.filter(name=post_category).first()
        
        blog = Blog.objects.create(title=title, description=description, owner=user)
        
        new_img_url = '/home/AKNYR/nova/static/images/blogs/blog'+str(blog.id)+'.jpg'
        with open(new_img_url, 'wb') as handler:
            for chunk in image.chunks():
                handler.write(chunk)
        
        new_img_url = "/static/images/blogs/blog" + str(blog.id) + ".jpg"
        blog.img_url = new_img_url
        
        blog.category.add(c)
        
        blog.save()
        return render(request, 'admin.html', {
            "user": user,
            "success": True,
            "categories": categories,
        })
        

    return render(request, 'admin.html', {
        "user": user,
        "categories": categories,
    })

def weather(request):
    data = parse_url()
    keys = data['sol_keys']

    weathers = []

    for key in keys:
        weathers.append(Weather(data[key], key))

    user = get_current_user(request)
    return render(request, 'weather.html', {
        "user": user,
        "weathers": reversed(weathers)
    })
