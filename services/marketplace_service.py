from app.models.ai_api import AIAPI

class MarketplaceService:

    @staticmethod
    def get_all_apis():

        return AIAPI.query.filter_by(active=True).all()
