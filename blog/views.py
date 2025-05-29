from django.shortcuts import render

posts = [
    {
        'author' : 'Zawadi',
        'title' : 'Master Excel',
        'content' : 'First post content',
        'date_posted' : 'August 27, 2018'
    },
    {
        'author' : 'Jane',
        'title' : 'Master Python',
        'content' : 'Beginner content',
        'date_posted' : 'September 29, 2025'
    }
]

# Create your views here.
def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})#if its short just create a way to add a dictionary as the title

