from authy.api import AuthyApiClient


def send_otp(authy_id):
    # Your API key from twilio.com/console/authy/applications
    authy_api = AuthyApiClient('KkwniIQT73oh3ua6fnmc8eWQxsHA97S9')
    sms = authy_api.users.request_sms(authy_id, {'force': True})

    if sms.ok():
        print(sms.content)


def verify_otp(authy_id, token_id):
    # Your API key from twilio.com/console/authy/applications
    authy_api = AuthyApiClient('KkwniIQT73oh3ua6fnmc8eWQxsHA97S9')
    verification = authy_api.tokens.verify(authy_id, token=token_id)
    print(verification.ok())
    return verification.ok()


def add_user(email, phone):
    authy_api = AuthyApiClient('KkwniIQT73oh3ua6fnmc8eWQxsHA97S9')
    user = authy_api.users.create(
        email=str(email),
        phone=str(phone),
        country_code=91)

    if user.ok():
        return user.id
        # user.id is the `authy_id` needed for future requests
    else:
        print(user.errors())
