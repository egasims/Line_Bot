from linebot.models import (TextSendMessage, ImageSendMessage, FlexSendMessage)
from Module.flexModule import transit, AtoB, gigaPage, positionPage, carouselPage, multilePage, multilePage2, \
    trainsitPage


def return_flex(alt_text, contents):
    return FlexSendMessage(alt_text=alt_text, contents=contents)


def return_img(original_content_url, preview_image_url):
    return ImageSendMessage(original_content_url=original_content_url, preview_image_url=preview_image_url)


def return_text(text):
    return TextSendMessage(text=text)


mesDic = dict({"交通資訊": return_flex("交通資訊", trainsitPage()),
               "廠辦線": return_flex("廠辦線", AtoB("廠辦線", "【去程】EGAS to T2", "EGAS to T2",
                                                    "【回程】T2 to EGAS", "T2 to EGAS")),
               "EGAS to T2": return_flex("EGAS to T2", multilePage("https://i.imgur.com/AIJFOT5.jpg", "廠辦G1",
                                                                   "https://i.imgur.com/E4lcfhq.jpg", "廠辦G2",
                                                                   "https://i.imgur.com/wV36c3T.jpg", "廠辦G3")),
               "T2 to EGAS": return_flex("T2 to EGAS", multilePage("https://i.imgur.com/LX9holP.jpg", "廠辦G4",
                                                                   "https://i.imgur.com/xURs7oN.jpg", "廠辦G5",
                                                                   "https://i.imgur.com/rQAabxd.jpg", "廠辦G6")),
               "廠辦G1": return_img("廠辦線", "https://i.imgur.com/AIJFOT5.jpg"),
               "廠辦G2": return_img("廠辦線", "https://i.imgur.com/E4lcfhq.jpg"),
               "廠辦G3": return_img("廠辦線", "https://i.imgur.com/wV36c3T.jpg"),
               "廠辦G4": return_img("廠辦線", "https://i.imgur.com/LX9holP.jpg"),
               "廠辦G5": return_img("廠辦線", "https://i.imgur.com/xURs7oN.jpg"),
               "廠辦G6": return_img("廠辦線", "https://i.imgur.com/rQAabxd.jpg"),
               "長興線": return_flex("長興線", multilePage2("https://i.imgur.com/HuOQci5.jpg", "每日行駛",
                                                            "https://i.imgur.com/hIkHelU.jpg", "工作日行駛")),
               "每日行駛": return_img("長興線每日行駛", "https://i.imgur.com/HuOQci5.jpg"),
               "工作日行駛": return_img("長興線工作日行駛", "https://i.imgur.com/hIkHelU.jpg"),
               "A15線": return_flex("A15線", multilePage2("https://i.imgur.com/HDwDhvC.jpg", "A15線去程",
                                                          "https://i.imgur.com/byBAbBm.jpg", "A15線回程")),
               "A15線去程": return_img("A15線去程", "https://i.imgur.com/HDwDhvC.jpg"),
               "A15線回程": return_img("A15線回程", "https://i.imgur.com/byBAbBm.jpg"),
               "T2walk": return_img("T2walk", "https://i.imgur.com/uSfw5fO.jpg"),
               "EGASwalk": return_img("EGASwalk", "https://i.imgur.com/zeyrBUj.jpg")})


def chk_mes(ukey):
    if ukey in mesDic:
        return mesDic[ukey]
    else:
        return return_text("功能開發中!!")
