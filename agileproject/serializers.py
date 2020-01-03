from rest_framework import serializers

from manage_epic_capability.models import AR_EPIC_CAPABILITY
from manage_features.models import AR_FEATURE

class Ar_Epic_Serializer(serializers.ModelSerializer):
    class Meta:
        model = AR_EPIC_CAPABILITY
        fields = ('Cepic_key', 'Cepic_desc', 'Children_feature_list', 'PROJECT_ID', 'ORG_ID', 'created_by', 'create_dt', 'update_by', 'update_dt')


class Ar_Feature_Serializer(serializers.ModelSerializer):
    class Meta:
        model = AR_FEATURE
        fields = ('Feature_key', 'Feature_desc', 'CE_ID', 'ORG_ID', 'create_by', 'create_dt', 'update_by', 'update_dt')