"""
Cache service using Redis for wardrobe items and other frequently accessed data.
"""

import os
import json
import hashlib
from typing import Optional, Any
from functools import wraps

try:
    import redis
    HAS_REDIS = True
except ImportError:
    HAS_REDIS = False
    print("⚠️  Redis not installed. Install with: pip install redis")

# Redis connection
redis_client = None

def init_redis():
    """Initialize Redis connection."""
    global redis_client
    if not HAS_REDIS:
        return False
    
    try:
        redis_url = os.getenv('REDIS_URL', 'redis://localhost:6379/0')
        redis_client = redis.from_url(redis_url, decode_responses=True)
        # Test connection
        redis_client.ping()
        print("✅ Redis cache initialized successfully!")
        return True
    except Exception as e:
        print(f"⚠️  Redis not available: {e}")
        redis_client = None
        return False

def get_cache_key(prefix: str, *args, **kwargs) -> str:
    """Generate a cache key from prefix and arguments."""
    key_parts = [prefix]
    if args:
        key_parts.extend(str(arg) for arg in args)
    if kwargs:
        sorted_kwargs = sorted(kwargs.items())
        key_parts.extend(f"{k}:{v}" for k, v in sorted_kwargs)
    
    key_string = ":".join(key_parts)
    # Hash if key is too long
    if len(key_string) > 200:
        key_string = hashlib.md5(key_string.encode()).hexdigest()
    
    return f"cameleon:{key_string}"

def get_cached(key: str, default: Optional[Any] = None) -> Optional[Any]:
    """Get value from cache."""
    if not redis_client:
        return default
    
    try:
        value = redis_client.get(key)
        if value:
            return json.loads(value)
        return default
    except Exception as e:
        print(f"⚠️  Cache get error: {e}")
        return default

def set_cached(key: str, value: Any, ttl: int = 3600) -> bool:
    """Set value in cache with TTL (default 1 hour)."""
    if not redis_client:
        return False
    
    try:
        redis_client.setex(key, ttl, json.dumps(value, default=str))
        return True
    except Exception as e:
        print(f"⚠️  Cache set error: {e}")
        return False

def delete_cached(key: str) -> bool:
    """Delete a key from cache."""
    if not redis_client:
        return False
    
    try:
        redis_client.delete(key)
        return True
    except Exception as e:
        print(f"⚠️  Cache delete error: {e}")
        return False

def delete_cached_pattern(pattern: str) -> int:
    """Delete all keys matching a pattern."""
    if not redis_client:
        return 0
    
    try:
        keys = redis_client.keys(pattern)
        if keys:
            return redis_client.delete(*keys)
        return 0
    except Exception as e:
        print(f"⚠️  Cache delete pattern error: {e}")
        return 0

def cache_result(ttl: int = 3600, key_prefix: str = "cache"):
    """Decorator to cache function results."""
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            # Generate cache key
            cache_key = get_cache_key(key_prefix, *args, **kwargs)
            
            # Try to get from cache
            cached = get_cached(cache_key)
            if cached is not None:
                return cached
            
            # Execute function
            result = await func(*args, **kwargs)
            
            # Store in cache
            set_cached(cache_key, result, ttl)
            
            return result
        return wrapper
    return decorator

# Initialize on import
if HAS_REDIS:
    init_redis()


