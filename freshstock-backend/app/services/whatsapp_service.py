import os
from twilio.rest import Client

def send_supplier_order(product_name: str, quantity: float, to_number: str = "+1234567890") -> dict:
    account_sid = os.getenv("TWILIO_ACCOUNT_SID", "mock_sid")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN", "mock_token")
    from_number = os.getenv("TWILIO_PHONE_NUMBER", "+1234567890")
    
    message_body = f"URGENT ORDER: Need {quantity}kg/L of {product_name} delivered to Warehouse A. Authorized by AI Manager."
    
    # Mock behavior if keys aren't set yet during development
    if account_sid == "mock_sid":
        print(f"[MOCK WHATSAPP] To: {to_number} | Body: {message_body}")
        return {"status": "success", "message_sid": "mock_12345"}

    try:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=message_body,
            from_=from_number,
            to=to_number
        )
        return {"status": "success", "message_sid": message.sid}
    except Exception as e:
        return {"status": "error", "error": str(e)}