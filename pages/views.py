from django.shortcuts import render

# Create your views here.
def home(request):
    welcome_message = "Welcome to George's portfolio website!"
    summary = "I am a web developer with expertise in Django, Python, and HTML/CSS."
    return render(request, 'pages/home.html', {'welcome_message': welcome_message, 'summary': summary})

def about(request):
    bio = "Hello, my name is George Cancino. I am a passionate web developer pursuing a Bachelor's Degree in Computer Science at the University of Memphis."
    skills = ["Ruby on Rails", "JavaScript", "HTML/CSS"]
    education = "Bachelor's Degree in Computer Science, University of Memphis"
    achievements = ["Completed multiple web development projects", "Received awards for excellence in coding"]
    return render(request, 'pages/about.html', {'bio': bio, 'skills': skills, 'education': education, 'achievements': achievements})

def work(request):
    projects = [
        { 'title': "Project 1", 'description': "Logo I made for a class project website.", 'image_url': '/images/woof-sitters-logo.png' },
        { 'title': "Project 2", 'description': "Home page I made for a class project website.", 'image_url': '/images/home.png' }
    ]
    return render(request, 'pages/work.html', {'projects': projects})

def contact(request):
    email = "gcancino@memphis.edu"
    phone = "123-456-7890"
    social_media_links = { 'twitter': "https://twitter.com/example", 'linkedin': "https://linkedin.com/in/example" }
    return render(request, 'pages/contact.html', {'email': email, 'phone': phone, 'social_media_links': social_media_links})