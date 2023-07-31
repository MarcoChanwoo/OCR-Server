from django.db import models
# python terminal에서 python manage.py startapp (앱이름)하면
# (앱이름)으로 정의된 파일이 생성됨
class Board(models.Model) :
    # 글번호
    no = models.AutoField(primary_key=True, auto_created=1000)
    # 제목
    title = models.CharField(max_length=100)
    # 내용
    contents = models.TextField(null=True, blank=True)
    # 작성자
    author = models.ForeignKey("users.User", on_delete=models.SET_NULL, null=True, related_name='boards')
    # 파일-?
    loaded_file = models.FileField(null=True, blank=True)
    # 등록일
    created_at = models.DateTimeField(auto_now_add=True)
    # 수정일
    modified_at = models.DateTimeField(auto_now=True)