"""
Owner Management
"""

from config import OWNER_NAME, OWNER_PASSWORD


_owner_mode = False


def login(password: str):

    global _owner_mode

    if password == OWNER_PASSWORD:
        _owner_mode = True
        return True

    return False


def logout():

    global _owner_mode

    _owner_mode = False


def is_owner():

    return _owner_mode


def owner_name():

    if _owner_mode:
        return OWNER_NAME

    return None


def owner_response():

    if _owner_mode:
        return f"🔓 حالت صاحب فعال است.\nصاحب من {OWNER_NAME} است."

    return "⛔ ابتدا رمز صاحب را وارد کنید."


def protect_private(question: str):

    private_words = [

        "صاحب",

        "رمز",

        "کد",

        "مالک",

        "owner",

        "password",

        "private"

    ]

    q = question.lower()

    for word in private_words:

        if word in q and not _owner_mode:

            return True

    return False
