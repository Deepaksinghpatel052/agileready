from ar_scenario.models import AR_SCENARIO
import django_filters

class ScenarioFilter(django_filters.FilterSet):

    class Meta:
        model = AR_SCENARIO
        fields = ['product_id', ]
