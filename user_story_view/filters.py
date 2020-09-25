from user_story_view.models import AR_USER_STORY
import django_filters

class UserStoryViewFilter(django_filters.FilterSet):

    class Meta:
        model = AR_USER_STORY
        fields = ['backlog_parent','BV_ID','UST_ID','user_story_status', ]
