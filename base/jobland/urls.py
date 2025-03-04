from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

# user, admin and job paths
urlpatterns = [
    # url path to the admin page
    path('admin/', admin.site.urls),
    # url path to the user app - empty path hence the default path, or the root path
    path('', include('user.urls')),
    # url path to the job app - /job path
    path('job/', include('job.urls')),
]

# server media files to production directory
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
