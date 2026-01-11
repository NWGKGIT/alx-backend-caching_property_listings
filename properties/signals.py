from django.core.cache import cache
from .models import Property

def get_all_properties():
    cache_key = 'all_properties'
    properties = cache.get(cache_key)

    if properties is None:
        properties = list(Property.objects.all())  # Evaluate QuerySet before caching
        cache.set(cache_key, properties, 3600)  # Store for 1 hour
    
    return properties