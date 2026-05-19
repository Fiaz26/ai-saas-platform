from app.extensions import redis_client

class AbuseService:

    @staticmethod
    def track(user_id):

        key = f"abuse:{user_id}"

        count = redis_client.incr(key)

        redis_client.expire(key, 60)

        return count
