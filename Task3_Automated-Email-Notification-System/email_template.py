def create_email(name):
    subject = "Order Confirmation"

    body = f"""
Hello {name},

Thank you for your order.

Your confirmation has been successfully received.

We appreciate your business.

Best Regards,
Customer Support Team
"""

    return subject, body