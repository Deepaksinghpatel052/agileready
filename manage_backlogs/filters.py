from manage_backlogs.models import AR_BACKLOG
import django_filters

class BacklogFilter(django_filters.FilterSet):

    class Meta:
        model = AR_BACKLOG
        fields = ['product_parent', ]
