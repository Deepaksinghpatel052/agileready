from rest_framework import serializers
from manage_epic_capability.models import AR_EPIC_CAPABILITY
from manage_features.models import AR_FEATURE
from account.models import ArUserProfilePermission
from user_story_view.models import AR_USER_STORY,Help_Text


class Ar_Epic_Serializer(serializers.ModelSerializer):
    class Meta:
        model = AR_EPIC_CAPABILITY
        fields = ('Cepic_key', 'Cepic_desc', 'Children_feature_list', 'PROJECT_ID', 'ORG_ID', 'created_by', 'create_dt', 'update_by', 'update_dt')


class Ar_Feature_Serializer(serializers.ModelSerializer):
    class Meta:
        model = AR_FEATURE
        fields = ('Feature_key', 'Feature_desc', 'CE_ID', 'ORG_ID', 'create_by', 'create_dt', 'update_by', 'update_dt')

class Help_Text_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Help_Text
        fields = ('page_name', 'page_slug', 'topic', 'description', 'information', 'create_by', 'create_dt', 'update_by','update_dt')


class ArUserProfilePermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArUserProfilePermission
        fields = (
        'profile_key', 'ORG_ID', 'activites', 'editor', 'viewer', 'create_by', 'create_dt', 'update_by', 'update_dt')
#


class ArUserStoryViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = AR_USER_STORY
        fields = (
        'owner', 'title', 'story_tri_part_text')