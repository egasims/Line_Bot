from linebot.models import (TextSendMessage, ImageSendMessage, FlexSendMessage)
from Module.flexModule import AtoB, multilePage2, trainsitPage, four_page, video_page


def return_flex(alt_text, contents):
    return FlexSendMessage(alt_text=alt_text, contents=contents)


def return_img(original_content_url, preview_image_url):
    return ImageSendMessage(original_content_url=original_content_url, preview_image_url=preview_image_url)


def return_text(text):
    return TextSendMessage(text=text)


mesDic = dict({"交通資訊": return_flex("交通資訊", trainsitPage()),
               "廠辦線": return_flex("廠辦線", AtoB("廠辦線", "EGAS", "T2")),
               "EGAS to T2(新)": return_flex("EGAS to T2(新)",
                                             four_page("https://i.imgur.com/nYUuBw1.jpg", "廠辦G1(新)",
                                                       "https://i.imgur.com/78qfQot.jpg", "廠辦G2(新)",
                                                       "https://i.imgur.com/OrhX4WE.jpg", "廠辦G3(新)",
                                                       "https://i.imgur.com/3CoLg32.jpg", "廠辦G4(新)")),
               "T2 to EGAS(新)": return_flex("T2 to EGAS(新)",
                                             four_page("https://i.imgur.com/IVREYxX.jpg", "廠辦G5(新)",
                                                       "https://i.imgur.com/EKJVnNJ.jpg", "廠辦G6(新)",
                                                       "https://i.imgur.com/3pC9q96.jpg", "廠辦G7(新)",
                                                       "https://i.imgur.com/CAgjj9h.jpg", "廠辦G8(新)")),
               "廠辦G1(新)": return_img("https://i.imgur.com/nYUuBw1.jpg", "https://i.imgur.com/nYUuBw1.jpg"),
               "廠辦G2(新)": return_img("https://i.imgur.com/78qfQot.jpg", "https://i.imgur.com/78qfQot.jpg"),
               "廠辦G3(新)": return_img("https://i.imgur.com/OrhX4WE.jpg", "https://i.imgur.com/OrhX4WE.jpg"),
               "廠辦G4(新)": return_img("https://i.imgur.com/3CoLg32.jpg", "https://i.imgur.com/3CoLg32.jpg"),
               "廠辦G5(新)": return_img("https://i.imgur.com/IVREYxX.jpg", "https://i.imgur.com/IVREYxX.jpg"),
               "廠辦G6(新)": return_img("https://i.imgur.com/EKJVnNJ.jpg", "https://i.imgur.com/EKJVnNJ.jpg"),
               "廠辦G7(新)": return_img("https://i.imgur.com/3pC9q96.jpg", "https://i.imgur.com/3pC9q96.jpg"),
               "廠辦G8(新)": return_img("https://i.imgur.com/CAgjj9h.jpg", "https://i.imgur.com/CAgjj9h.jpg"),
               "長興線": return_flex("長興線", multilePage2("https://i.imgur.com/rLSIn5g.jpg", "每日行駛",
                                                            "https://i.imgur.com/M7d8Mh7.jpg", "工作日行駛")),
               "每日行駛": return_img("https://i.imgur.com/rLSIn5g.jpg", "https://i.imgur.com/rLSIn5g.jpg"),
               "工作日行駛": return_img("https://i.imgur.com/M7d8Mh7.jpg", "https://i.imgur.com/M7d8Mh7.jpg"),
               "A15線": return_flex("A15線", multilePage2("https://i.imgur.com/HDwDhvC.jpg", "A15線去程",
                                                          "https://i.imgur.com/byBAbBm.jpg", "A15線回程")),
               "A15線去程": return_img("https://i.imgur.com/HDwDhvC.jpg", "https://i.imgur.com/HDwDhvC.jpg"),
               "A15線回程": return_img("https://i.imgur.com/byBAbBm.jpg", "https://i.imgur.com/byBAbBm.jpg"),
               "EGASflex": return_flex("EGAS to A14a 交通路線",
                                       video_page("https://i.imgur.com/0xOfojx.png", "EGAS <-> A14a", "#a5a552",
                                                  "EGASwalk",
                                                  "https://youtu.be/i_LqwGNfAmM")),
               "T2flex": return_flex("T2 to A13 交通路線",
                                     video_page("https://i.imgur.com/Lxu9u7L.png", "T2 <-> A13", "#9f4d95",
                                                "T2walk",
                                                "https://youtu.be/z72EmsAsqQ0")),
               "T2walk": return_img("https://i.imgur.com/VclCNxR.jpg", "https://i.imgur.com/VclCNxR.jpg"),
               "EGASwalk": return_img("https://i.imgur.com/zeyrBUj.jpg", "https://i.imgur.com/zeyrBUj.jpg"),
               "03-3916058": return_text("03-3916058"),
               "03-3916126": return_text("03-3916126"),
               "其它資訊": return_text("功能開發中!")})


def chk_mes(ukey):
    if ukey in mesDic:
        return mesDic[ukey]
    else:
        return return_text("本系統僅供查詢，無回覆功能; 若有問題請洽總務部!!")
