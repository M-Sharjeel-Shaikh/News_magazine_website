from django.shortcuts import render, redirect
from django.conf import settings
from post.models import Post
from django.core.paginator import Paginator
from subscriber.models import Subscriber
from django.shortcuts import HttpResponse
from django.http import HttpResponseNotFound
from django.contrib import messages
from contact.models import Contact



# Create your views here.
def home(request):
    # Getting all required Data for rnder
    title = Post.objects.all().order_by('title')[:7]
    category = Post.objects.filter(category = "10")[:10]
    business = Post.objects.filter(category = "7")[:6]
    technology = Post.objects.filter(category = "1")[:6]
    entertainment = Post.objects.filter(category = "3")[:6]
    sport = Post.objects.filter(category = "6")[:6]
    education = Post.objects.filter(category = "9")[:5]

    data = {
        'title' : title,
        'category' : category,
        'business' : business,
        'technology' : technology,
        'entertainment' : entertainment,
        'sport' : sport,
        'education' : education,
    }

    if request.method == "POST":
        email = request.POST['email']
        try:
            if Subscriber.objects.filter( Email = email ).first():
                messages.success(request, "'You have alreday our subscriber' ")
                return redirect('/')

            subcriber = Subscriber.objects.create( Email = email )        
            subcriber.save()
            messages.success(request, "'Thanks For Subcriber Us \n'  'You will be updated with our new sevices and offers' ")
            return redirect('/')
            
        except Exception as e:
            return HttpResponseNotFound(404)

    return render(request, "index.html", data)


# ====== Search Query ===
def search(request):
    if request.method=='GET':
        st = request.GET.get('search')
        if st!=None:
            result = Post.objects.filter(title__icontains=st)

            if not result:
                messages.info(request, "No Data Found")
                data = {
                    'empty' : 'empty'
                }
                return render(request, "detail.html", data)

            data = {
                'result' : result,
            }          
            return render(request, "detail.html", data)
        else:
            return render(request, "index.html")
    

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        msg = request.POST['message']

        try:
            contact = Contact.objects.create(
            name = name, 
            email = email,
            subject = subject,
            message = msg,
            )        
            contact.save()
            messages.success(request, 'Your message is received to our team and we will contact back you soon')
            return redirect('/contact')
        except Exception as e:
             
            return HttpResponse(404)

    return render(request, "contact.html")


def detail(request, slug):
    title = Post.objects.all().order_by('title')[:7]
    if slug or slug is not None:
        item = Post.objects.get(slug = slug )
        data ={
            'title' : title,
            'item' : item,
        }
        return render(request, "detail.html", data)
    else:
        data ={
            'title' : title,
            'item' : item,
        }
        return render(request, "detail.html", data)


def business(request):
    category = Post.objects.filter(category = "7")
    cat = Post.objects.filter(category = "7")[:6]

    paginator=Paginator(category,6)
    page_number=request.GET.get('page')
    final=paginator.get_page(page_number)
    total=final.paginator.num_pages

    data = {
        'category' : category,
        'cat' : cat,
        'url' : "Business",
        'label' : 'Business',
        'servciesdata':final,
        'newsdata':category,
        'totalpage':[n+1 for n in range(total)]
    }
    if request.method == "POST":
        email = request.POST['email']
        try:
            if Subscriber.objects.filter( Email = email ).first():
                messages.success(request, "'You have alreday our subscriber' ")
                return redirect('/Business')

            subcriber = Subscriber.objects.create( Email = email )        
            subcriber.save()
            messages.success(request, "'Thanks For Subcriber Us \n'  'You will be updated with our new sevices and offers' ")
            return redirect('/Business')
            
        except Exception as e:
            
            return HttpResponseNotFound(404)

    return render(request, "sub_category.html", data)


def technology(request):
    category = Post.objects.filter(category = "1")
    cat = Post.objects.filter(category = "1")[:6]

    paginator=Paginator(category,6)
    page_number=request.GET.get('page')
    final=paginator.get_page(page_number)
    total=final.paginator.num_pages

    data = {
        'category' : category,
        'cat' : cat,
        'url' : "Technology",
        'label' : 'Technology',
        'servciesdata':final,
        'newsdata':category,
        'totalpage':[n+1 for n in range(total)]
    }
    if request.method == "POST":
        email = request.POST['email']
        try:
            if Subscriber.objects.filter( Email = email ).first():
                messages.success(request, "'You have alreday our subscriber' ")
                return redirect('/Technology')

            subcriber = Subscriber.objects.create( Email = email )        
            subcriber.save()
            messages.success(request, "'Thanks For Subcriber Us \n'  'You will be updated with our new sevices and offers' ")
            return redirect('/Technology')
            
        except Exception as e:
            
            return HttpResponseNotFound(404)
    return render(request, "sub_category.html", data)


def entertainment(request):
    category = Post.objects.filter(category = "3")
    cat = Post.objects.filter(category = "3")[:6]

    paginator=Paginator(category,6)
    page_number=request.GET.get('page')
    final=paginator.get_page(page_number)
    total=final.paginator.num_pages

    data = {
        'category' : category,
        'cat' : cat,
        'url' : "Entertainment",
        'label' : 'Entertainment',
        'servciesdata':final,
        'newsdata':category,
        'totalpage':[n+1 for n in range(total)]
    }
    return render(request, "sub_category.html", data)


def sport(request):
    category = Post.objects.filter(category = "6")
    cat = Post.objects.filter(category = "6")[:6]

    paginator=Paginator(category,6)
    page_number=request.GET.get('page')
    final=paginator.get_page(page_number)
    total=final.paginator.num_pages

    data = {
        'category' : category,
        'cat' : cat,
        'url' : "Sport",
        'label' : 'Sport',
        'servciesdata':final,
        'newsdata':category,
        'totalpage':[n+1 for n in range(total)]
    }
    if request.method == "POST":
        email = request.POST['email']
        try:
            if Subscriber.objects.filter( Email = email ).first():
                messages.success(request, "'You have alreday our subscriber' ")
                return redirect('/Sport')

            subcriber = Subscriber.objects.create( Email = email )        
            subcriber.save()
            messages.success(request, "'Thanks For Subcriber Us \n'  'You will be updated with our new sevices and offers' ")
            return redirect('/Sport')
            
        except Exception as e:
            
            return HttpResponseNotFound(404)
    return render(request, "sub_category.html", data)


def health(request):
    category = Post.objects.filter(category = "8")
    cat = Post.objects.filter(category = "8")[:6]

    paginator=Paginator(category,6)
    page_number=request.GET.get('page')
    final=paginator.get_page(page_number)
    total=final.paginator.num_pages

    data = {
        'category' : category,
        'cat' : cat,
        'url' : "Health",
        'label' : 'Health',
        'servciesdata':final,
        'newsdata':category,
        'totalpage':[n+1 for n in range(total)]
    }
    if request.method == "POST":
        email = request.POST['email']
        try:
            if Subscriber.objects.filter( Email = email ).first():
                messages.success(request, "'You have alreday our subscriber' ")
                return redirect('/Health')

            subcriber = Subscriber.objects.create( Email = email )        
            subcriber.save()
            messages.success(request, "'Thanks For Subcriber Us \n'  'You will be updated with our new sevices and offers' ")
            return redirect('/Health')
            
        except Exception as e:
            
            return HttpResponseNotFound(404)
    return render(request, "sub_category.html", data)


def fashion(request):
    category = Post.objects.filter(category = "4")
    cat = Post.objects.filter(category = "4")[:6]

    paginator=Paginator(category,6)
    page_number=request.GET.get('page')
    final=paginator.get_page(page_number)
    total=final.paginator.num_pages

    data = {
        'category' : category,
        'cat' : cat,
        'url' : "Fashion",
        'label' : 'Fashion',
        'servciesdata':final,
        'newsdata':category,
        'totalpage':[n+1 for n in range(total)]
    }
    if request.method == "POST":
        email = request.POST['email']
        try:
            if Subscriber.objects.filter( Email = email ).first():
                messages.success(request, "'You have alreday our subscriber' ")
                return redirect('/Fashion')

            subcriber = Subscriber.objects.create( Email = email )        
            subcriber.save()
            messages.success(request, "'Thanks For Subcriber Us \n'  'You will be updated with our new sevices and offers' ")
            return redirect('/Fashion')
            
        except Exception as e:
            
            return HttpResponseNotFound(404)
    return render(request, "sub_category.html", data)


def food(request):
    category = Post.objects.filter(category = "5")
    cat = Post.objects.filter(category = "5")[:6]

    paginator=Paginator(category,6)
    page_number=request.GET.get('page')
    final=paginator.get_page(page_number)
    total=final.paginator.num_pages

    data = {
        'category' : category,
        'cat' : cat,
        'url' : "Food",
        'label' : 'Food',
        'servciesdata':final,
        'newsdata':category,
        'totalpage':[n+1 for n in range(total)]
    }
    if request.method == "POST":
        email = request.POST['email']
        try:
            if Subscriber.objects.filter( Email = email ).first():
                messages.success(request, "'You have alreday our subscriber' ")
                return redirect('/Food')

            subcriber = Subscriber.objects.create( Email = email )        
            subcriber.save()
            messages.success(request, "'Thanks For Subcriber Us \n'  'You will be updated with our new sevices and offers' ")
            return redirect('/Food')
            
        except Exception as e:
            
            return HttpResponseNotFound(404)
    return render(request, "sub_category.html", data)


def education(request):
    category = Post.objects.filter(category = "9")
    cat = Post.objects.filter(category = "9")[:6]

    paginator=Paginator(category,6)
    page_number=request.GET.get('page')
    final=paginator.get_page(page_number)
    total=final.paginator.num_pages

    data = {
        'category' : category,
        'cat' : cat,
        'url' : "Education",
        'label' : 'Education',
        'servciesdata':final,
        'newsdata':category,
        'totalpage':[n+1 for n in range(total)]
    }
    if request.method == "POST":
        email = request.POST['email']
        try:
            if Subscriber.objects.filter( Email = email ).first():
                messages.success(request, "'You have alreday our subscriber' ")
                return redirect('/Education')

            subcriber = Subscriber.objects.create( Email = email )        
            subcriber.save()
            messages.success(request, "'Thanks For Subcriber Us \n'  'You will be updated with our new sevices and offers' ")
            return redirect('/Education')
            
        except Exception as e:
            
            return HttpResponseNotFound(404)
    return render(request, "sub_category.html", data)


def other(request):
    category = Post.objects.filter(category = "10")
    cat = Post.objects.filter(category = "10")[:6]

    paginator=Paginator(category,6)
    page_number=request.GET.get('page')
    final=paginator.get_page(page_number)
    total=final.paginator.num_pages

    data = {
        'category' : category,
        'cat' : cat,
        'url' : "Others",
        'label' : 'Others',
        'servciesdata':final,
        'newsdata':category,
        'totalpage':[n+1 for n in range(total)]
    }
    if request.method == "POST":
        email = request.POST['email']
        try:
            if Subscriber.objects.filter( Email = email ).first():
                messages.success(request, "'You have alreday our subscriber' ")
                return redirect('/Others')

            subcriber = Subscriber.objects.create( Email = email )        
            subcriber.save()
            messages.success(request, "'Thanks For Subcriber Us \n'  'You will be updated with our new sevices and offers' ")
            return redirect('/Others')
            
        except Exception as e:
            
            return HttpResponseNotFound(404)
    return render(request, "sub_category.html", data)


def footer(request):
    return render(request, "index.html")


def header(request):
    return render(request, "index.html")
