from flask import Blueprint, jsonify

from app.models.vendor_revenue import VendorRevenue

analytics_bp = Blueprint(
    "vendor_analytics",
    __name__
)

@analytics_bp.route("/vendor/<int:vendor_id>")
def vendor_stats(vendor_id):

    revenues = VendorRevenue.query.filter_by(
        vendor_id=vendor_id
    ).all()

    total = sum(r.vendor_earning for r in revenues)

    return jsonify({
        "total_earnings": total,
        "transactions": len(revenues)
    })
