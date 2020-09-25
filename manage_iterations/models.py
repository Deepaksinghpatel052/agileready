from django.db import models
from account.models import Ar_user,AR_organization
from manage_product.models import AR_team,AR_product
from manage_backlogs.models import AR_BACKLOG
from user_story_view.models import AR_USER_STORY
import django

from autoslug import AutoSlugField
# Create your models here.



class ArIterations(models.Model):
    IterationName  = models.CharField(max_length=50,blank=True)
    iteration_slug = AutoSlugField(populate_from='IterationName', always_update=True, unique_with='create_dt__month', null=True, blank=True)
    # owner  = models.CharField(max_length=50,blank=True)
    owner  = models.ForeignKey(Ar_user,  default="",null=True , on_delete=models.SET_NULL)
    IterationId    = models.TextField(max_length=50)
    StartDate      = models.DateField()
    EndDate        = models.DateField()
    Description    = models.TextField()
    Product        = models.ForeignKey(AR_product,default="",null=True , on_delete=models.SET_NULL,related_name='productArIterations')
    Backlog        = models.ForeignKey(AR_BACKLOG,default="",null=True , on_delete=models.SET_NULL,related_name='backlogArIterations')
    UserStory = models.ManyToManyField(AR_USER_STORY, default="", blank=True,related_name='userstoryArIterations')
    Team           = models.ForeignKey(AR_team,default="",null=True , on_delete=models.SET_NULL,related_name='teamArIterations')
    IterationScore = models.FloatField(blank=True, null=True)
    IterationSize = models.IntegerField(blank=True, null=True)
    ORG_ID         = models.ForeignKey(AR_organization,default="",null=True , on_delete=models.SET_NULL,related_name='teamArIterations')
    create_by = models.ForeignKey(Ar_user, on_delete=models.SET_NULL,related_name='create_by_iterations',null=True ,blank=True)
    create_dt = models.DateTimeField(default=django.utils.timezone.now)
    update_by = models.ForeignKey(Ar_user, on_delete=models.SET_NULL,related_name='update_by_iterations',null=True ,blank=True)
    update_dt = models.DateTimeField(default=django.utils.timezone.now)
    data_Type = models.CharField(max_length=50, default="ORG Data",blank=True)
    def __str__(self):
        return str(self.IterationName)
    class Meta:
        verbose_name_plural = "Ar iterations"