from linebot.models import (TextSendMessage, ImageSendMessage, FlexSendMessage)
from Module.flexModule import AtoB, multilePage2, trainsitPage, four_page, video_page


# 回傳 Flex Message 物件，用於顯示複雜排版訊息
def return_flex(alt_text, contents):
    return FlexSendMessage(alt_text=alt_text, contents=contents)


# 回傳 Image Message 物件，用於顯示圖片
def return_img(original_content_url, preview_image_url):
    return ImageSendMessage(original_content_url=original_content_url, preview_image_url=preview_image_url)


# 回傳 Text Message 物件，用於顯示純文字
def return_text(text):
    return TextSendMessage(text=text)


# 集中管理圖片連結，方便維護與重複使用
img_urls = {
    "廠辦G1(新)": "https://imgur.com/a/wdYDHUj#c3J2NXR",
    "廠辦G2(新)": "https://imgur.com/a/wdYDHUj#2aN2XCi",
    "廠辦G3(新)": "https://imgur.com/a/wdYDHUj#bVsSfbR",
    "廠辦G4(新)": "https://imgur.com/a/wdYDHUj#dU4O0EC",
    "廠辦G5(新)": "https://imgur.com/a/wdYDHUj#LEHotVA",
    "廠辦G6(新)": "https://imgur.com/a/wdYDHUj#8ZdgTk1",
    "廠辦G7(新)": "https://imgur.com/a/wdYDHUj",
    "廠辦G8(新)": "https://imgur.com/a/wdYDHUj#qNpE9Yi",
    "每日行駛": "https://imgur.com/a/wdYDHUj#LJrZv0E",
    "工作日行駛": "https://imgur.com/a/wdYDHUj#0fAUFd3",
    "A15線去程": "https://imgur.com/a/wdYDHUj#XA2fdpC", #A1
    "A15線回程": "https://imgur.com/a/wdYDHUj#ACpaF3l", #A2
    "T2walk": "https://i.imgur.com/VclCNxR.jpg",
    "EGASwalk": "https://i.imgur.com/zeyrBUj.jpg",
}

# 建立訊息字典，定義關鍵字與對應的回覆訊息 (Flex Message 或 Text Message)
mesDic = {
    "交通資訊": return_flex("交通資訊", trainsitPage()),
    "廠辦線": return_flex("廠辦線", AtoB("廠辦線", "EGAS", "T2")),
    "EGAS to T2(新)": return_flex("EGAS to T2(新)",
                                  four_page(img_urls["廠辦G1(新)"], "廠辦G1(新)",
                                            img_urls["廠辦G2(新)"], "廠辦G2(新)",
                                            img_urls["廠辦G3(新)"], "廠辦G3(新)",
                                            img_urls["廠辦G4(新)"], "廠辦G4(新)")),
    "T2 to EGAS(新)": return_flex("T2 to EGAS(新)",
                                  four_page(img_urls["廠辦G5(新)"], "廠辦G5(新)",
                                            img_urls["廠辦G6(新)"], "廠辦G6(新)",
                                            img_urls["廠辦G7(新)"], "廠辦G7(新)",
                                            img_urls["廠辦G8(新)"], "廠辦G8(新)")),
    "長興線": return_flex("長興線", multilePage2(img_urls["每日行駛"], "每日行駛",
                                                img_urls["工作日行駛"], "工作日行駛")),
    "A15線": return_flex("A15線", multilePage2(img_urls["A15線去程"], "A15線去程",
                                              img_urls["A15線回程"], "A15線回程")),
    "EGASflex": return_flex("EGAS to A14a 交通路線",
                            video_page("https://i.imgur.com/0xOfojx.png", "EGAS <-> A14a", "#a5a552",
                                       "EGASwalk",
                                       "https://youtu.be/i_LqwGNfAmM")),
    "T2flex": return_flex("T2 to A13 交通路線",
                          video_page("https://i.imgur.com/Lxu9u7L.png", "T2 <-> A13", "#9f4d95",
                                     "T2walk",
                                     "https://youtu.be/z72EmsAsqQ0")),
    "03-3916058": return_text("03-3916058"),
    "03-3916126": return_text("03-3916126"),
    "其它資訊": return_text("功能開發中!!")
}

# 自動將 img_urls 中的項目加入 mesDic 作為圖片訊息 (Image Message)
# 這樣當使用者輸入圖片名稱 (如 "廠辦G1(新)") 時，可以直接回傳對應的圖片
for key, url in img_urls.items():
    mesDic[key] = return_img(url, url)


# 檢查使用者輸入的關鍵字 (ukey) 是否存在於 mesDic 中
# 若存在則回傳對應的訊息物件，否則回傳預設的提示文字
def chk_mes(ukey):
    if ukey in mesDic:
        return mesDic[ukey]
    else:
        return return_text("本系統僅供查詢，無回覆功能; 若有問題請洽總務部!!")
