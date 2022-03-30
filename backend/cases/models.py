from django.db import models
from projects.models import Project

# Create your models here.
class Module(models.Model):
    """
    模块管理表
    """
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    name = models.CharField("名称",max_length=100,null=False,default="")
    parent_id = models.IntegerField("父级ID",default=0)
    is_delete = models.BooleanField("删除状态",default=False)
    create_time = models.DateField("创建时间",auto_now_add=True)
    update_time = models.DateField("更新时间",auto_now=True)

    def __str__(self):
        return self.name
