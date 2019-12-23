from django.shortcuts import render

posts = [
    {
        'author': 'Jumpy',
        'title':'Blog Post 1',
        'content':'Nisi Lorem non sint sit exercitation reprehenderit laboris ut laborum. Nulla anim irure commodo sit consequat. Et cillum cupidatat proident enim tempor excepteur ullamco est amet irure et ipsum. Ad sint ut elit tempor ad occaecat culpa sit.',
        'date_posted':'August 27, 2019'
    },
    {
        'author': 'Zippy',
        'title':'Blog Post 2',
        'content':'Minim ea cupidatat ex Lorem ipsum duis aliquip sint deserunt voluptate. Consequat consectetur consequat magna laboris commodo amet adipisicing. Aliquip anim incididunt fugiat ex aliqua quis quis cillum ut. Laboris occaecat dolor culpa amet pariatur. Fugiat proident aliqua ut consectetur id in officia cillum irure. Lorem minim velit consequat quis duis. Ut pariatur anim adipisicing in proident sunt eiusmod.',
        'date_posted':'September 27, 2019'
    }
    
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')