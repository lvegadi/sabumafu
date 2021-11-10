import random
from django.utils.text import slugify

def slugify_instance_title(instance, save=False, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.nombre)
        Klass = instance.__class__
    qs = Klass.objects.filter(slug=slug).exclude(id=instance.id)
    if qs.exists():
        # auto genera un nuevo slug
        rand_int = random.randint(300_000,500_000)
        slug = f"{slug}-{rand_int}"
        return slugify_instance_title(instance,save=save)
    instance.slug = slug
    if save:
        instance.save()
    return instance
