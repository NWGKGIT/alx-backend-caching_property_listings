from django.core.cache import cache
from .models import Property
import logging
from django_redis import get_redis_connection

def get_all_properties():
    properties = cache.get('all_properties')
    if properties is None:
        properties = Property.objects.all()
        cache.set('all_properties', properties, 3600)
    return properties

def get_redis_cache_metrics():
    con = get_redis_connection("default")
    info = con.info()
    hits = info.get('keyspace_hits', 0)
    misses = info.get('keyspace_misses', 0)
    
    total = hits + misses
    hit_ratio = hits / total if total > 0 else 0
    
    metrics = {
        'keyspace_hits': hits,
        'keyspace_misses': misses,
        'hit_ratio': hit_ratio
    }
    logging.info(f"Metrics: {metrics}")
    return metrics