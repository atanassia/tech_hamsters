from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('main.urls', namespace = '')),
    path('', include('accounts.urls', namespace = '')),
    path('blog/', include('blog.urls', namespace = '')),
    path('admin/', admin.site.urls),
]

handler404 = 'main.views.page_not_found'
handler500 = 'main.views.server_error'