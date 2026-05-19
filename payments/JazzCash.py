import hashlib
import urllib.parse
from config import Config
import logging
logging.info(f"JazzCash callback received: {data}")
def generate_jazzcash_payload(amount, order_id):

    data = {
        "pp_Version": "1.1",
        "pp_TxnType": "MWALLET",
        "pp_Language": "EN",
        "pp_MerchantID": Config.JAZZCASH_MERCHANT_ID,
        "pp_Password": "",
        "pp_BillReference": order_id,
        "pp_Amount": str(amount * 100),  # paisa
        "pp_TxnCurrency": "PKR",
        "pp_TxnDateTime": "",
        "pp_TxnExpiryDateTime": "",
        "pp_ReturnURL": Config.JAZZCASH_RETURN_URL,
    }

    # Create secure hash
    sorted_string = "&".join([f"{k}={v}" for k, v in sorted(data.items())])
    hash_string = Config.JAZZCASH_INTEGRITY_SALT + "&" + sorted_string

    secure_hash = hashlib.sha256(hash_string.encode()).hexdigest().upper()

    data["pp_SecureHash"] = secure_hash

    return data
