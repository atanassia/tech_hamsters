from django.shortcuts import render


def page_not_found(request, exception = None):
    return render(request, 'error_pages/404.html')

def server_error(request):
    return render(request, 'error_pages/500.html')

def main_page(request):
    return render(request, 'main/main_page.html')
