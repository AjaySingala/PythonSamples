from external_dependency import dark_magic

def is_credit_card_fraud(transaction):
    print(transaction)
    fraud_probability = dark_magic(transaction)
    print(fraud_probability)
    if fraud_probability > 0.99:
        return True
    else:
        return False

if __name__ == '__main__':
    transaction = {"amount_usd": "9999.99", "overnight_shipping": True}
    is_credit_card_fraud(transaction)
