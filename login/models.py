from django.db import models

# Create your models here.
class User(models.Model):
    #用户表
    gender = (
        ('male', '男'),
        ('female', '女'),
    )

    #name必填，最长不超过128个字符，并且唯一，问题：必填在哪体现的？
    name = models.CharField(max_length=128, unique=True)
    #password必填，最长不超过256个字符
    password = models.CharField(max_length=256)
    #email使用django内置的邮箱类型，并且唯一
    email = models.EmailField(unique=True)
    #性能使用了一个choice，不能选择男或女，默认为男
    sex = models.CharField(max_length=32, choices=gender, default='男')
    c_time = models.DateTimeField(auto_now_add=True)

    #使用__str__帮助人性显示对象信息
    def __str__(self):
        return self.name

    #元数据里定义用户按创建时间的倒序排列，也就是最近的最先显示
    class Meta:
        ordering = ['c_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'