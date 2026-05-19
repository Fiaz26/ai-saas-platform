from app.extensions import db
from app.models.vendor_revenue import VendorRevenue
from app.models.vendor_wallet import VendorWallet
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
wallet = VendorWallet.query.filter_by(
    vendor_id=api.vendor_id
).first()

if not wallet:

    wallet = VendorWallet(
        vendor_id=api.vendor_id
    )

    db.session.add(wallet)

wallet.balance += vendor_share
wallet.lifetime_earnings += vendor_share
        db.session.add(revenue)
        db.session.commit()
