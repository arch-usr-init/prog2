from django.shortcuts import render

def home(request):
    """
    Project-level home view.
    Demonstrates XSS protection with auto-escaping.
    """
    context = {
        'user_input': '<script>alert("XSS Attack!")</script>',
    }
    return render(request, 'home.html', context)

def post_list(request):

    """
    Blog post list view.
    Will display all published posts once we create the Post model in Step 2.

    Currently returns empty list for demonstration purposes.
    """
    context = {

        'posts': [], # Empty for now - will populate in Step 2

    }

    return render(request, 'blog/blog_list.html', context)

def post_detail(request, slug):
    """
    Blog post detail view.
    Will display a single post once we create the Post model in Step 2.

    Currently returns mock data for demonstration purposes.
    In Step 2, this will use: get_object_or_404(Post, slug=slug)
    """
    context = {
        'post': {
        'title': 'Sample Post',
        'slug': slug,
        'content': 'This is sample content. Real data coming in Step 2!',
        'author': {'username': 'demo_user'},
        'published_date': None,
        'categories': {'all': []},
        'tags': {'all': []},
        }
    }

    return render(request, 'blog/blog_detail.html', context)