from django.shortcuts import get_object_or_404
from manage_backlogs.models import AR_BACKLOG
from account.models import AR_organization
from manage_product.models import AR_product,AR_team
from user_story_points.models import ArUserStoryPoints
from django import template
register = template.Library()

@register.simple_tag
def team_add(pk, id):
    team_data_get = ""
    product_data = AR_product.objects.filter(pk=id)
    for data in product_data:
        for val in data.backlog_by_product.all():
            for team_data in val.team_list.all():
                team_name = team_data_get.split(" | ")
                if team_data_get != "":
                    if str(team_data) not in team_name:
                        team_data_get = team_data_get + " | " + str(team_data)
                else:
                    team_data_get = str(team_data)
        return (team_data_get)

@register.simple_tag
def team_edit(id):
    team_data_get = ""
    product_data = AR_product.objects.filter(pk=id)
    for data in product_data:
        for val in data.backlog_by_product.all():
            for team_data in val.team_list.all():
                team_name = team_data_get.split(" | ")
                if team_data_get != "":
                    if str(team_data) not in team_name:
                        team_data_get = team_data_get + " | " + str(team_data)
                else:
                    team_data_get = str(team_data)
        return (team_data_get)


@register.simple_tag
def mul_add(pk, id):
    org_ins = get_object_or_404(AR_organization, pk=int(pk))
    product_data = AR_product.objects.filter(pk=id)
    num2 = 0
    TOT1 = 0
    for data in product_data:
        num1=0
        for val in data.backlog_by_product.all():
            num1=num1+1
            val_id = val.id
            backlog_data = AR_BACKLOG.objects.filter(ORG_ID=org_ins).filter(pk=val_id)
            for data in backlog_data:
                QS = 0
                num = 0
                UTP = 0
                TOT = 0
                point_num = 0
                if data.story_by_backlog.all().count() != 0:
                    for val in data.story_by_backlog.all():
                        num = num + 1
                        QS = QS + val.readiness_quality_score
                        # if val.story_points_id is not None:
                        #     point_num = point_num + 1
                        #     UTP_val = get_object_or_404(ArUserStoryPoints, pk=val.story_points_id)
                        #     UTP = UTP + UTP_val.Point_score
                    TOT = QS + UTP
                    num = num + point_num
                else:
                    num = 0
            num2 = num2 + num
            TOT1 = TOT1 + TOT
    if num2 != 0:
        tot = TOT1 / num2
        return (int(tot))
    else:
        tot = 0
        return (round(tot,2))

@register.simple_tag
def product_add(id):
    product_data_get = ""
    team_data = AR_team.objects.filter(pk=id)
    for data in team_data:
        for val in data.backlog_team.all():
            product_name = product_data_get.split(" | ")
            if product_data_get != "":
                if str(val.product_parent) not in product_name:
                    product_data_get = product_data_get + " | " + str(val.product_parent)
            else:
                product_data_get = str(val.product_parent)
    return (product_data_get)




#
# @register.simple_tag
# def size(pk, id):
#     org_ins = get_object_or_404(AR_organization, organization_name=str(pk))
#     backlog_data = AR_BACKLOG.objects.filter(ORG_ID=org_ins).filter(pk=id)
#     for data in backlog_data:
#         UTP = 0
#         if data.story_by_backlog.all().count() != 0:
#             for val in data.story_by_backlog.all():
#                 if val.story_points_id is not None:
#                     UTP_val = get_object_or_404(ArUserStoryPoints, pk=val.story_points_id)
#                     if UTP_val.Point_score is not None:
#                         UTP = UTP + UTP_val.Point_score
#         return (UTP)


@register.simple_tag
def size(pk, id):
    org_ins = get_object_or_404(AR_organization, pk=int(pk))
    product_data = AR_product.objects.filter(pk=id)
    for data in product_data:
        num1=0
        UTP = 0
        if data.backlog_by_product.all().count() != 0:
            for val in data.backlog_by_product.all():
                num1=num1+1
                val_id = val.id
                backlog_data = AR_BACKLOG.objects.filter(ORG_ID=org_ins).filter(pk=val_id)
                for data in backlog_data:
                    # UTP = 0
                    if data.story_by_backlog.all().count() != 0:
                        for val in data.story_by_backlog.all():
                            if val.story_points_id is not None:
                                UTP_val = get_object_or_404(ArUserStoryPoints, pk=val.story_points_id)
                                UTP = UTP + UTP_val.Point_score
        return (UTP)
