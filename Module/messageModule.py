from linebot.models import (TextSendMessage, ImageSendMessage, FlexSendMessage)
from Module.flexModule import AtoB, multilePage, multilePage2, trainsitPage, three_page, four_page


def return_flex(alt_text, contents):
    return FlexSendMessage(alt_text=alt_text, contents=contents)


def return_img(original_content_url, preview_image_url):
    return ImageSendMessage(original_content_url=original_content_url, preview_image_url=preview_image_url)


def return_text(text):
    return TextSendMessage(text=text)


mesDic = dict({"交通資訊": return_flex("交通資訊", trainsitPage()),
               "廠辦線": return_flex("廠辦線", AtoB("廠辦線", "EGAS", "T2")),
               "EGAS to T2": return_flex("EGAS to T2", three_page("https://i.imgur.com/vmnJenZ.jpg", "廠辦G1",
                                                                  "https://i.imgur.com/ga31aK5.jpg", "廠辦G2",
                                                                  "https://i.imgur.com/c87o95S.jpg", "廠辦G3")),
               "T2 to EGAS": return_flex("EGAS to T2", three_page("https://i.imgur.com/yy6pf3C.jpg", "廠辦G4",
                                                                  "https://i.imgur.com/iCr63se.jpg", "廠辦G5",
                                                                  "https://i.imgur.com/hQm4bJR.jpg", "廠辦G6")),
               "廠辦G1": return_img("https://i.imgur.com/vmnJenZ.jpg", "https://i.imgur.com/vmnJenZ.jpg"),
               "廠辦G2": return_img("https://i.imgur.com/ga31aK5.jpg", "https://i.imgur.com/ga31aK5.jpg"),
               "廠辦G3": return_img("https://i.imgur.com/c87o95S.jpg", "https://i.imgur.com/c87o95S.jpg"),
               "廠辦G4": return_img("https://i.imgur.com/yy6pf3C.jpg", "https://i.imgur.com/yy6pf3C.jpg"),
               "廠辦G5": return_img("https://i.imgur.com/iCr63se.jpg", "https://i.imgur.com/iCr63se.jpg"),
               "廠辦G6": return_img("https://i.imgur.com/hQm4bJR.jpg", "https://i.imgur.com/hQm4bJR.jpg"),
               "EGAS to T2(新)": return_flex("EGAS to T2(新)",
                                             four_page("https://i.imgur.com/HNMsYsL.jpg", "廠辦G1(新)",
                                                       "https://i.imgur.com/AQ4JjJQ.jpg", "廠辦G2(新)",
                                                       "https://i.imgur.com/fkif50U.jpg", "廠辦G3(新)",
                                                       "https://i.imgur.com/hbDO7pl.jpg", "廠辦G4(新)")),
               "T2 to EGAS(新)": return_flex("T2 to EGAS(新)",
                                             four_page("https://i.imgur.com/vcVEDNs.jpg", "廠辦G5(新)",
                                                       "https://i.imgur.com/5rifrtL.jpg", "廠辦G6(新)",
                                                       "https://i.imgur.com/635SCW5.jpg", "廠辦G7(新)",
                                                       "https://i.imgur.com/eWTKvs0.jpg", "廠辦G8(新)")),
               "廠辦G1(新)": return_img("https://i.imgur.com/HNMsYsL.jpg", "https://i.imgur.com/HNMsYsL.jpg"),
               "廠辦G2(新)": return_img("https://i.imgur.com/AQ4JjJQ.jpg", "https://i.imgur.com/AQ4JjJQ.jpg"),
               "廠辦G3(新)": return_img("https://i.imgur.com/fkif50U.jpg", "https://i.imgur.com/fkif50U.jpg"),
               "廠辦G4(新)": return_img("https://i.imgur.com/hbDO7pl.jpg", "https://i.imgur.com/hbDO7pl.jpg"),
               "廠辦G5(新)": return_img("https://i.imgur.com/vcVEDNs.jpg", "https://i.imgur.com/vcVEDNs.jpg"),
               "廠辦G6(新)": return_img("https://i.imgur.com/5rifrtL.jpg", "https://i.imgur.com/5rifrtL.jpg"),
               "廠辦G7(新)": return_img("https://i.imgur.com/635SCW5.jpg", "https://i.imgur.com/635SCW5.jpg"),
               "廠辦G8(新)": return_img("https://i.imgur.com/eWTKvs0.jpg", "https://i.imgur.com/eWTKvs0.jpg"),
               "長興線": return_flex("長興線", multilePage2("https://i.imgur.com/HsCcU0D.jpg", "每日行駛",
                                                            "https://i.imgur.com/kOrJYYI.jpg", "工作日行駛")),
               "每日行駛": return_img("https://i.imgur.com/HsCcU0D.jpg", "https://i.imgur.com/HsCcU0D.jpg"),
               "工作日行駛": return_img("https://i.imgur.com/kOrJYYI.jpg", "https://i.imgur.com/kOrJYYI.jpg"),
               "A15線": return_flex("A15線", multilePage2("https://i.imgur.com/HDwDhvC.jpg", "A15線去程",
                                                          "https://i.imgur.com/byBAbBm.jpg", "A15線回程")),
               "A15線去程": return_img("https://i.imgur.com/HDwDhvC.jpg", "https://i.imgur.com/HDwDhvC.jpg"),
               "A15線回程": return_img("https://i.imgur.com/byBAbBm.jpg", "https://i.imgur.com/byBAbBm.jpg"),
               "T2walk": return_img("https://i.imgur.com/uSfw5fO.jpg", "https://i.imgur.com/uSfw5fO.jpg"),
               "EGASwalk": return_img("https://i.imgur.com/zeyrBUj.jpg", "https://i.imgur.com/zeyrBUj.jpg"),
               "03-3916058": return_text("03-3916058"),
               "03-3916126": return_text("03-3916126"),
               "其它資訊": return_text("功能開發中!")})


def chk_mes(ukey):
    if ukey in mesDic:
        return mesDic[ukey]
    else:
        return return_text("本系統僅供查詢，無回覆功能; 若有問題請洽總務部!!")
