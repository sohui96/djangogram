from django.db import models
from djangogram.users import models as user_model

# Create your models here.

# >> 데이터 생성날짜, 변경날짜 <<
class TimeStamedModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    # 이 옵션을 주면 TimeStamedModels는 단독으로 테이블이 만들어지지 않을 것임
    class Meta:
        abstract = True

# >> 포스트 모델 <<
class Post(TimeStamedModel):
    author = models.ForeignKey(
                user_model.User,
                null=True,
                on_delete=models.CASCADE, # 외래키를 갖는 특정유저가 삭제되면 어떻게 처리가 될 것인가를 알려주는 옵션
                related_name='post_author'
            )
    image = models.ImageField(blank=True)
    caption = models.TextField(blank=True)
    image_likes = models.ManyToManyField(user_model.User, related_name='post_image_likes')

# >> 댓글 모델 <<
class Comment(TimeStamedModel):
    author = models.ForeignKey(
                user_model.User,
                null=True,
                on_delete=models.CASCADE, # 외래키를 갖는 특정유저가 삭제되면 어떻게 처리가 될 것인가를 알려주는 옵션
                related_name='post_author'
            )
    posts = models.ForeignKey(
                Post,
                null=True,
                on_delete=models.CASCADE, # 외래키를 갖는 특정포스트가 삭제되면 어떻게 처리가 될 것인가를 알려주는 옵션
                related_name='comment_post'
            )
    contents = models.TextField(blank=True)
