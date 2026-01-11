import logging
from django.core.cache import cache
from django_redis import get_redis_connection
from .models import Property

logger = logging.getLogger(__name__)

def get_all_properties():
    properties = cache.get('all_properties')
    if properties is None:
        properties = list(Property.objects.all())
        cache.set('all_properties', properties, 3600)
    return properties

def get_redis_cache_metrics():
    con = get_redis_connection("default")
    info = con.info()
    
    keyspace_hits = info.get('keyspace_hits', 0)
    keyspace_misses = info.get('keyspace_misses', 0)
    total_requests = keyspace_hits + keyspace_misses
    
    # Specific regex requirement:
    hit_ratio = keyspace_hits / total_requests if total_requests > 0 else 0
    
    metrics = {
        'keyspace_hits': keyspace_hits,
        'keyspace_misses': keyspace_misses,
        'hit_ratio': hit_ratio
    }
    
    # Logging metrics as requested without using logger.error
    logger.info(f"Cache metrics: {metrics}")
    
    return metrics