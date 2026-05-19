from app.extensions import db
from app.models.vendor_revenue import VendorRevenue

PLATFORM_COMMISSION = 0.20  # 20%

class RevenueService:

    @staticmethod
    def distribute(api, credits_used):

        total = credits_used

        fee = total * PLATFORM_COMMISSION
        vendor_share = total - fee

        revenue = VendorRevenue(
            vendor_id=api.vendor_id,
            api_id=api.id,
            amount=total,
            platform_fee=fee,
            vendor_earning=vendor_share
        )

        db.session.add(revenue)
        db.session.commit()
