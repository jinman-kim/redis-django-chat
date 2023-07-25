from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("chat/", include("chat.urls")), # 이 부분 추가. localhost:8000/chat/ 으로 호출이 되면 chat.urls 파일로 가라는 뜻
    path("admin/", admin.site.urls),
]