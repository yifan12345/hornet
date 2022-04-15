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


class TestCase(models.Model):
    """测试用例表"""

    module = models.ForeignKey(Module,on_delete=models.CASCADE)
    name = models.CharField("名称",max_length=50,null=False)
    url = models.TextField("URL",null=False)
    method = models.CharField("请求方法",max_length=10,null=False)
    header = models.TextField("请求体",null=True,default="{}")
    params_type = models.CharField("参数类型",max_length=10,null=False)
    params_body = models.TextField("参数内容",null=True,default="{}")
    response = models.TextField("结果",null=True,default="{}")
    assert_type = models.CharField("断言类型",max_length=10,null=True)
    assert_text = models.TextField("断言结果",null=True,default="{}")
    is_Delete = models.BooleanField("状态",default=False)
    create_time = models.DateField("创建时间",auto_now_add=True)
    update_time = models.DateField("更新时间",auto_now=True)

    def __str__(self):
        return self.name
