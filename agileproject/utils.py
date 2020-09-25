import random
import string
from django.utils.text import slugify

def random_string_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def slug_generator_for_backlog_parent(instance,new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.Color_name)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(backlog_slug=slug).exists()
    if qs_exists:
        new_slug = "{backlog_slug}-{rendstr}".format(backlog_slug=slug,rendstr=random_string_generator(size=4))
        return slug_generator_for_user_story(instance,new_slug=new_slug)
    return slug



def slug_generator_for_user_story(instance,new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(user_story_slug=slug).exists()
    if qs_exists:
        new_slug = "{user_story_slug}-{rendstr}".format(user_story_slug=slug,rendstr=random_string_generator(size=4))
        return slug_generator_for_user_story(instance,new_slug=new_slug)
    return slug