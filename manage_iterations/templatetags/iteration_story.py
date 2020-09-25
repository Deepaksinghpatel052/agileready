from django.shortcuts import get_object_or_404
from manage_iterations.models import ArIterations
from account.models import AR_organization
from user_story_points.models import ArUserStoryPoints
from django import template
register = template.Library()

@register.simple_tag
def iter_score(pk, id):
    org_ins = get_object_or_404(AR_organization, pk=int(pk))
    backlog_data = ArIterations.objects.filter(ORG_ID=org_ins).filter(pk=id)
    for data in backlog_data:
        QS = 0
        num = 0
        UTP = 0
        if data.UserStory.all().count() != 0:
            for val in data.UserStory.all():
                num = num +1
                QS = QS + val.readiness_quality_score
            TOT = QS + UTP
            num = num
            if num != 0 :
                tot = TOT/num
                return (int(tot))
        else:
            tot = 0
            return (round(tot,2))


@register.simple_tag
def size(pk, id):
    org_ins = get_object_or_404(AR_organization, pk=int(pk))
    backlog_data = ArIterations.objects.filter(ORG_ID=org_ins).filter(pk=id)
    for data in backlog_data:
        UTP = 0
        point_num = 0
        if data.UserStory.all().count() != 0:
            for val in data.UserStory.all():
                if val.story_points_id is not None:
                    point_num = point_num + 1
                    UTP_val = get_object_or_404(ArUserStoryPoints, pk=val.story_points_id)
                    UTP = UTP + UTP_val.Point_score
        return (UTP)