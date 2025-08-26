from django.db import models
from django.utils.text import slugify


class Post(models.Model):
    title = models.CharField(max_length=140)
    # slug 필드에서 unique=True를 잠시 제거합니다.
    # unique 제약은 save 메서드에서 직접 관리합니다.
    slug = models.SlugField(allow_unicode=True, blank=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    # ✅ 업그레이드된 save 메서드
    def save(self, *args, **kwargs):
        if not self.id:  # 객체가 처음 생성될 때
            # 먼저 slug 없이 객체를 저장하여 id를 부여받습니다.
            super().save(*args, **kwargs)

        if not self.slug:  # slug가 비어있다면
            # id와 title을 조합하여 고유한 slug를 생성합니다.
            self.slug = f'{slugify(self.title, allow_unicode=True)}-{self.id}'

        # 최종적으로 slug와 함께 다시 저장합니다.
        super().save(*args, **kwargs)