"""
Offline Brain
جواب های بدون اینترنت ربات
"""


def offline_answer(message):

    text = message.strip().lower()


    # سلام

    if any(x in text for x in [
        "سلام",
        "درود",
        "hello",
        "hi"
    ]):

        return "سلام امیر 👋 من آماده‌ام."


    # احوالپرسی

    if any(x in text for x in [
        "خوبی",
        "حالت چطوره",
        "چه خبر"
    ]):

        return "من خوبم 🤖 آماده کمک هستم."


    # معرفی

    if any(x in text for x in [
        "اسمت چیه",
        "تو کی هستی",
        "معرفی کن"
    ]):

        return "من Tobi هستم، ربات شخصی امیر."


    # تشکر

    if any(x in text for x in [
        "ممنون",
        "مرسی",
        "تشکر"
    ]):

        return "خواهش می‌کنم امیر."


    # خداحافظی

    if any(x in text for x in [
        "خداحافظ",
        "فعلا",
        "بای"
    ]):

        return "خداحافظ امیر 👋"


    # زمان

    if "ساعت" in text:

        return "برای ساعت دقیق باید به اینترنت وصل شوم."


    # هوا

    if "هوا" in text:

        return "برای وضعیت هوا باید از سرویس آنلاین استفاده کنم."


    # صاحب

    if "صاحب" in text:

        return "برای اطلاعات صاحب، ابتدا حالت صاحب را فعال کن."


    # پیش فرض

    return None



def has_offline_answer(message):

    return offline_answer(message) is not None
