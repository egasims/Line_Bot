def transit(sp, ep):
    contents = {
        "type": "bubble",
        "size": "mega",
        "header": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "FROM",
                            "color": "#ffffff66",
                            "size": "sm"
                        },
                        {
                            "type": "text",
                            "text": sp,
                            "color": "#ffffff",
                            "size": "xl",
                            "flex": 4,
                            "weight": "bold"
                        }
                    ]
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "TO",
                            "color": "#ffffff66",
                            "size": "sm"
                        },
                        {
                            "type": "text",
                            "text": ep,
                            "color": "#ffffff",
                            "size": "xl",
                            "flex": 4,
                            "weight": "bold"
                        }
                    ]
                }
            ],
            "paddingAll": "20px",
            "backgroundColor": "#0367D3",
            "spacing": "md",
            "height": "154px",
            "paddingTop": "22px"
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": "Total: 1 hour",
                    "color": "#b7b7b7",
                    "size": "xs"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                        {
                            "type": "text",
                            "text": "20:30",
                            "size": "sm",
                            "gravity": "center"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "filler"
                                },
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [],
                                    "cornerRadius": "30px",
                                    "height": "12px",
                                    "width": "12px",
                                    "borderColor": "#EF454D",
                                    "borderWidth": "2px"
                                },
                                {
                                    "type": "filler"
                                }
                            ],
                            "flex": 0
                        },
                        {
                            "type": "text",
                            "text": sp,
                            "gravity": "center",
                            "flex": 4,
                            "size": "sm"
                        }
                    ],
                    "spacing": "lg",
                    "cornerRadius": "30px",
                    "margin": "xl"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                                {
                                    "type": "filler"
                                }
                            ],
                            "flex": 1
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                        {
                                            "type": "filler"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [],
                                            "width": "2px",
                                            "backgroundColor": "#B7B7B7"
                                        },
                                        {
                                            "type": "filler"
                                        }
                                    ],
                                    "flex": 1
                                }
                            ],
                            "width": "12px"
                        },
                        {
                            "type": "text",
                            "text": "Walk 4min",
                            "gravity": "center",
                            "flex": 4,
                            "size": "xs",
                            "color": "#8c8c8c"
                        }
                    ],
                    "spacing": "lg",
                    "height": "64px"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "20:34",
                                    "gravity": "center",
                                    "size": "sm"
                                }
                            ],
                            "flex": 1
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "filler"
                                },
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [],
                                    "cornerRadius": "30px",
                                    "width": "12px",
                                    "height": "12px",
                                    "borderWidth": "2px",
                                    "borderColor": "#6486E3"
                                },
                                {
                                    "type": "filler"
                                }
                            ],
                            "flex": 0
                        },
                        {
                            "type": "text",
                            "text": ep,
                            "gravity": "center",
                            "flex": 4,
                            "size": "sm"
                        }
                    ],
                    "spacing": "lg",
                    "cornerRadius": "30px"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                                {
                                    "type": "filler"
                                }
                            ],
                            "flex": 1
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                        {
                                            "type": "filler"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [],
                                            "width": "2px",
                                            "backgroundColor": "#6486E3"
                                        },
                                        {
                                            "type": "filler"
                                        }
                                    ],
                                    "flex": 1
                                }
                            ],
                            "width": "12px"
                        },
                        {
                            "type": "text",
                            "text": "Metro 1hr",
                            "gravity": "center",
                            "flex": 4,
                            "size": "xs",
                            "color": "#8c8c8c"
                        }
                    ],
                    "spacing": "lg",
                    "height": "64px"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                        {
                            "type": "text",
                            "text": "20:40",
                            "gravity": "center",
                            "size": "sm"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "filler"
                                },
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [],
                                    "cornerRadius": "30px",
                                    "width": "12px",
                                    "height": "12px",
                                    "borderColor": "#6486E3",
                                    "borderWidth": "2px"
                                },
                                {
                                    "type": "filler"
                                }
                            ],
                            "flex": 0
                        },
                        {
                            "type": "text",
                            "text": sp,
                            "gravity": "center",
                            "flex": 4,
                            "size": "sm"
                        }
                    ],
                    "spacing": "lg",
                    "cornerRadius": "30px"
                }
            ]
        }
    }
    return contents


def AtoB(title, a, b):
    contents = {
        "type": "carousel",
        "contents": [
            {
                "type": "bubble",
                "size": "mega",
                "header": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "icon",
                                            "url": "https://i.imgur.com/ahkcJcq.png",
                                            "size": "65px"
                                        }
                                    ],
                                    "width": "100px"
                                },
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": title,
                                            "size": "3xl",
                                            "weight": "bold",
                                            "align": "center",
                                            "color": "#019858",
                                            "decoration": "underline"
                                        },
                                        {
                                            "type": "text",
                                            "text": "(2024/12/27更新)",
                                            "size": "xl",
                                            "weight": "bold",
                                            "align": "center",
                                            "color": "#FF0000",
                                            "margin": "md"
                                        }
                                    ],
                                    "offsetEnd": "xl"
                                }
                            ]
                        },
                        {
                            "type": "separator",
                            "margin": "xl"
                        }
                    ]
                },
                "hero": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [
                                                {
                                                    "type": "text",
                                                    "text": "【去程】",
                                                    "weight": "bold",
                                                    "align": "end",
                                                    "size": "xl"
                                                }
                                            ],
                                            "width": "100px"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [
                                                {
                                                    "type": "text",
                                                    "text": a,
                                                    "weight": "bold",
                                                    "align": "center",
                                                    "size": "xl"
                                                }
                                            ],
                                            "width": "70px"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [
                                                {
                                                    "type": "text",
                                                    "text": "→",
                                                    "weight": "bold",
                                                    "align": "center",
                                                    "size": "xl"
                                                }
                                            ],
                                            "width": "50px"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [
                                                {
                                                    "type": "text",
                                                    "text": b,
                                                    "weight": "bold",
                                                    "align": "center",
                                                    "size": "xl"
                                                }
                                            ],
                                            "width": "70px"
                                        }
                                    ],
                                    "alignItems": "center",
                                    "action": {
                                        "type": "message",
                                        "label": a + " to " + b + "(新)",
                                        "text": a + " to " + b + "(新)"
                                    },
                                    "margin": "xl"
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [
                                                {
                                                    "type": "text",
                                                    "text": "【回程】",
                                                    "weight": "bold",
                                                    "align": "end",
                                                    "size": "xl"
                                                }
                                            ],
                                            "width": "100px"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [
                                                {
                                                    "type": "text",
                                                    "text": b,
                                                    "weight": "bold",
                                                    "align": "center",
                                                    "size": "xl"
                                                }
                                            ],
                                            "width": "70px"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [
                                                {
                                                    "type": "text",
                                                    "text": "→",
                                                    "weight": "bold",
                                                    "align": "center",
                                                    "size": "xl"
                                                }
                                            ],
                                            "width": "50px"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [
                                                {
                                                    "type": "text",
                                                    "text": a,
                                                    "weight": "bold",
                                                    "align": "center",
                                                    "size": "xl"
                                                }
                                            ],
                                            "width": "70px"
                                        }
                                    ],
                                    "alignItems": "center",
                                    "margin": "25px",
                                    "action": {
                                        "type": "message",
                                        "label": b + " to " + a + "(新)",
                                        "text": b + " to " + a + "(新)"
                                    }
                                }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [],
                            "margin": "30px"
                        }
                    ],
                    "margin": "150px"
                }
            }
        ]
    }
    return contents


def gigaPage():
    contents = {
        "type": "bubble",
        "size": "giga",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": "交通路線",
                    "weight": "bold",
                    "size": "xxl",
                    "margin": "md",
                    "gravity": "center",
                    "align": "center"
                },
                {
                    "type": "separator",
                    "margin": "lg"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "image",
                                    "url": "https://i.imgur.com/2QNQMPC.png",
                                    "size": "full",
                                    "action": {
                                        "type": "message",
                                        "label": "廠辦線",
                                        "text": "廠辦線"
                                    }
                                }
                            ],
                            "cornerRadius": "xl"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "image",
                                    "url": "https://i.imgur.com/F1b2MrV.png",
                                    "size": "full",
                                    "action": {
                                        "type": "message",
                                        "label": "長興線",
                                        "text": "長興線"
                                    }
                                }
                            ],
                            "cornerRadius": "xl"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "image",
                                    "url": "https://i.imgur.com/CCchyXk.png",
                                    "size": "full",
                                    "action": {
                                        "type": "message",
                                        "label": "A15線",
                                        "text": "A15線"
                                    }
                                }
                            ],
                            "cornerRadius": "xl"
                        }
                    ],
                    "cornerRadius": "xl"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "image",
                                    "url": "https://i.imgur.com/2wFRJo0.png",
                                    "align": "center",
                                    "size": "full",
                                    "action": {
                                        "type": "message",
                                        "label": "T2Walk",
                                        "text": "T2Walk"
                                    }
                                }
                            ],
                            "cornerRadius": "xl"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "image",
                                    "url": "https://i.imgur.com/nNPwA2S.png",
                                    "size": "full",
                                    "action": {
                                        "type": "message",
                                        "label": "EGASwalk",
                                        "text": "EGASwalk"
                                    }
                                }
                            ],
                            "cornerRadius": "xl"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "image",
                                    "url": "https://i.imgur.com/81NRLeL.png",
                                    "size": "full",
                                    "action": {
                                        "type": "uri",
                                        "label": "map",
                                        "uri": "https://maps.app.goo.gl/b2UUMqVDuy8oBJDQ8"
                                    }
                                }
                            ],
                            "cornerRadius": "xl"
                        }
                    ],
                    "cornerRadius": "xl"
                }
            ]
        },
        "styles": {
            "footer": {
                "separator": True
            }
        }
    }
    return contents


def positionPage():
    contents = {
        "type": "bubble",
        "header": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                        {
                            "type": "image",
                            "url": "https://i.imgur.com/tqTCfWQ.jpg",
                            "size": "full",
                            "aspectMode": "cover",
                            "gravity": "center",
                            "flex": 1,
                            "align": "center",
                            "action": {
                                "type": "message",
                                "label": "長興線",
                                "text": "長興線"
                            }
                        }
                    ]
                },
                {
                    "type": "separator"
                }
            ],
            "paddingAll": "0px"
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                                {
                                    "type": "icon",
                                    "url": "https://i.imgur.com/Oswmift.png",
                                    "size": "4xl"
                                },
                                {
                                    "type": "text",
                                    "text": "廠辦大樓大門口",
                                    "weight": "bold",
                                    "align": "start",
                                    "gravity": "center"
                                }
                            ],
                            "action": {
                                "type": "uri",
                                "label": "action",
                                "uri": "https://maps.app.goo.gl/XnvP3gGwHwh8WkQv9"
                            }
                        }
                    ]
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                                {
                                    "type": "icon",
                                    "url": "https://i.imgur.com/Oswmift.png",
                                    "size": "4xl"
                                },
                                {
                                    "type": "text",
                                    "text": "廠辦大樓大門口",
                                    "weight": "bold",
                                    "align": "start",
                                    "gravity": "center"
                                }
                            ],
                            "action": {
                                "type": "uri",
                                "label": "action",
                                "uri": "https://maps.app.goo.gl/XnvP3gGwHwh8WkQv9"
                            }
                        }
                    ]
                }
            ]
        }
    }
    return contents


def carouselPage():
    contents = {
        "type": "carousel",
        "contents": [
            {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "image",
                            "url": "https://i.imgur.com/tqTCfWQ.jpg",
                            "size": "full",
                            "aspectMode": "cover",
                            "aspectRatio": "8:15",
                            "gravity": "top"
                        }
                    ],
                    "paddingAll": "0px",
                    "background": {
                        "type": "linearGradient",
                        "angle": "0deg",
                        "startColor": "#E6E6F2",
                        "endColor": "#ffffff"
                    }
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "搭車地點",
                            "margin": "none",
                            "weight": "bold",
                            "align": "center",
                            "gravity": "center",
                            "size": "xl"
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                                {
                                    "type": "image",
                                    "url": "https://i.imgur.com/3TJ1ggr.jpg",
                                    "align": "center",
                                    "gravity": "top",
                                    "size": "full",
                                    "aspectMode": "cover"
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "icon",
                                            "url": "https://i.imgur.com/Oswmift.png",
                                            "size": "lg",
                                            "offsetStart": "md"
                                        },
                                        {
                                            "type": "text",
                                            "text": "廠辦門口",
                                            "weight": "bold",
                                            "offsetStart": "md",
                                            "size": "lg"
                                        }
                                    ],
                                    "alignItems": "center",
                                    "action": {
                                        "type": "uri",
                                        "label": "廠辦門口",
                                        "uri": "https://maps.app.goo.gl/KRtZwWuzuQ5aAw3m7"
                                    }
                                }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                                {
                                    "type": "image",
                                    "url": "https://i.imgur.com/gW3GN82.jpg",
                                    "gravity": "top",
                                    "align": "center",
                                    "size": "full",
                                    "aspectMode": "cover"
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "icon",
                                            "url": "https://i.imgur.com/Oswmift.png",
                                            "size": "lg",
                                            "offsetStart": "md"
                                        },
                                        {
                                            "type": "text",
                                            "text": "T2航廈",
                                            "weight": "bold",
                                            "offsetStart": "md",
                                            "size": "lg"
                                        }
                                    ],
                                    "alignItems": "center",
                                    "action": {
                                        "type": "uri",
                                        "label": "T2航廈",
                                        "uri": "https://maps.app.goo.gl/GyRYnfMkX2xYgMXz8"
                                    }
                                }
                            ],
                            "margin": "md"
                        }
                    ],
                    "background": {
                        "type": "linearGradient",
                        "angle": "0deg",
                        "startColor": "#ffffff",
                        "endColor": "#E6E6F2"
                    },
                    "margin": "none"
                }
            },
            {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "image",
                            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/flexsnapshot/clip/clip2.jpg",
                            "size": "full",
                            "aspectMode": "cover",
                            "aspectRatio": "2:3",
                            "gravity": "top"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "Cony's T-shirts",
                                            "size": "xl",
                                            "color": "#ffffff",
                                            "weight": "bold"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "¥35,800",
                                            "color": "#ebebeb",
                                            "size": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "¥75,000",
                                            "color": "#ffffffcc",
                                            "decoration": "line-through",
                                            "gravity": "bottom",
                                            "flex": 0,
                                            "size": "sm"
                                        }
                                    ],
                                    "spacing": "lg"
                                },
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "filler"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "baseline",
                                            "contents": [
                                                {
                                                    "type": "filler"
                                                },
                                                {
                                                    "type": "icon",
                                                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/flexsnapshot/clip/clip14.png"
                                                },
                                                {
                                                    "type": "text",
                                                    "text": "Add to cart",
                                                    "color": "#ffffff",
                                                    "flex": 0,
                                                    "offsetTop": "-2px"
                                                },
                                                {
                                                    "type": "filler"
                                                }
                                            ],
                                            "spacing": "sm"
                                        },
                                        {
                                            "type": "filler"
                                        }
                                    ],
                                    "borderWidth": "1px",
                                    "cornerRadius": "4px",
                                    "spacing": "sm",
                                    "borderColor": "#ffffff",
                                    "margin": "xxl",
                                    "height": "40px"
                                }
                            ],
                            "position": "absolute",
                            "offsetBottom": "0px",
                            "offsetStart": "0px",
                            "offsetEnd": "0px",
                            "backgroundColor": "#9C8E7Ecc",
                            "paddingAll": "20px",
                            "paddingTop": "18px"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "SALE",
                                    "color": "#ffffff",
                                    "align": "center",
                                    "size": "xs",
                                    "offsetTop": "3px"
                                }
                            ],
                            "position": "absolute",
                            "cornerRadius": "20px",
                            "offsetTop": "18px",
                            "backgroundColor": "#ff334b",
                            "offsetStart": "18px",
                            "height": "25px",
                            "width": "53px"
                        }
                    ],
                    "paddingAll": "0px"
                }
            }
        ]
    }
    return contents


def multilePage(a, at, b, bt, c, ct, d, dt):
    contents = {
        "type": "carousel",
        "contents": [
            {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "image",
                            "url": a,
                            "size": "full",
                            "aspectMode": "cover",
                            "gravity": "top",
                            "aspectRatio": "8.5:20"
                        }
                    ],
                    "paddingAll": "0px",
                    "action": {
                        "type": "message",
                        "label": at,
                        "text": at
                    }
                }
            },
            {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "image",
                            "url": b,
                            "size": "full",
                            "aspectMode": "cover",
                            "gravity": "top",
                            "aspectRatio": "8.5:20"
                        }
                    ],
                    "paddingAll": "0px",
                    "action": {
                        "type": "message",
                        "label": bt,
                        "text": bt
                    }
                }
            },
            {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "image",
                            "url": c,
                            "size": "full",
                            "aspectMode": "cover",
                            "gravity": "top",
                            "aspectRatio": "8.5:20"
                        }
                    ],
                    "paddingAll": "0px",
                    "action": {
                        "type": "message",
                        "label": ct,
                        "text": ct
                    }
                }
            },
            {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "image",
                            "url": d,
                            "size": "full",
                            "aspectMode": "cover",
                            "gravity": "top",
                            "aspectRatio": "8.5:20"
                        }
                    ],
                    "paddingAll": "0px",
                    "action": {
                        "type": "message",
                        "label": dt,
                        "text": dt
                    }
                }
            }
        ]
    }
    return contents


def multilePage2(a, at, b, bt):
    contents = {
        "type": "carousel",
        "contents": [
            {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "image",
                            "url": a,
                            "size": "full",
                            "aspectMode": "cover",
                            "gravity": "top",
                            "aspectRatio": "8.5:20"
                        }
                    ],
                    "paddingAll": "0px",
                    "action": {
                        "type": "message",
                        "label": at,
                        "text": at
                    }
                }
            },
            {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "image",
                            "url": b,
                            "size": "full",
                            "aspectMode": "cover",
                            "gravity": "top",
                            "aspectRatio": "8.5:20"
                        }
                    ],
                    "paddingAll": "0px",
                    "action": {
                        "type": "message",
                        "label": bt,
                        "text": bt
                    }
                }
            }
        ]
    }
    return contents


def trainsitPage():
    contents = {
        "type": "bubble",
        "size": "mega",
        "hero": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "image",
                    "url": "https://i.imgur.com/gwi2hnz.png",
                    "size": "full",
                    "aspectMode": "cover"
                },
                {
                    "type": "separator"
                }
            ],
            "height": "100px"
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                        {
                            "type": "icon",
                            "url": "https://i.imgur.com/ahkcJcq.png",
                            "size": "4xl",
                            "offsetStart": "lg"
                        },
                        {
                            "type": "text",
                            "text": "廠辦線",
                            "size": "xxl",
                            "weight": "bold",
                            "color": "#00A600",
                            "align": "center",
                            "gravity": "center",
                            "decoration": "underline",
                            "offsetBottom": "xxl",
                            "margin": "1px"
                        }
                    ],
                    "alignItems": "center",
                    "justifyContent": "center",
                    "action": {
                        "type": "message",
                        "label": "廠辦線",
                        "text": "廠辦線"
                    },
                    "spacing": "xxl"
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                        {
                            "type": "icon",
                            "url": "https://i.imgur.com/yDuhMfq.png",
                            "size": "4xl",
                            "offsetStart": "lg"
                        },
                        {
                            "type": "text",
                            "text": "長興線",
                            "size": "xxl",
                            "weight": "bold",
                            "color": "#EAC100",
                            "gravity": "center",
                            "align": "center",
                            "decoration": "underline",
                            "offsetBottom": "xxl",
                            "margin": "1px"
                        }
                    ],
                    "alignItems": "center",
                    "justifyContent": "center",
                    "action": {
                        "type": "message",
                        "label": "長興線",
                        "text": "長興線"
                    },
                    "spacing": "xxl",
                    "margin": "lg"
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                        {
                            "type": "icon",
                            "url": "https://i.imgur.com/7cuHLc7.png",
                            "size": "4xl",
                            "offsetStart": "lg"
                        },
                        {
                            "type": "text",
                            "text": "A15線",
                            "size": "xxl",
                            "weight": "bold",
                            "color": "#46A3FF",
                            "align": "center",
                            "gravity": "center",
                            "decoration": "underline",
                            "offsetBottom": "xxl",
                            "margin": "1px"
                        }
                    ],
                    "alignItems": "center",
                    "justifyContent": "center",
                    "action": {
                        "type": "message",
                        "label": "A15線",
                        "text": "A15線"
                    },
                    "spacing": "xxl",
                    "margin": "lg"
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                        {
                            "type": "icon",
                            "url": "https://i.imgur.com/Lxu9u7L.png",
                            "size": "4xl",
                            "offsetStart": "lg"
                        },
                        {
                            "type": "text",
                            "text": "T2 <-> A13",
                            "size": "xxl",
                            "weight": "bold",
                            "color": "#9F4D95",
                            "gravity": "center",
                            "align": "center",
                            "decoration": "underline",
                            "offsetBottom": "xxl",
                            "margin": "1px"
                        }
                    ],
                    "alignItems": "center",
                    "justifyContent": "center",
                    "action": {
                        "type": "message",
                        "label": "T2flex",
                        "text": "T2flex"
                    },
                    "spacing": "xxl",
                    "margin": "lg"
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                        {
                            "type": "icon",
                            "url": "https://i.imgur.com/0xOfojx.png",
                            "size": "4xl",
                            "offsetStart": "lg"
                        },
                        {
                            "type": "text",
                            "text": "EGAS <-> A14a",
                            "size": "xxl",
                            "weight": "bold",
                            "color": "#A5A552",
                            "gravity": "center",
                            "align": "center",
                            "decoration": "underline",
                            "offsetBottom": "xxl",
                            "margin": "1px"
                        }
                    ],
                    "alignItems": "center",
                    "justifyContent": "center",
                    "action": {
                        "type": "message",
                        "label": "EGASflex",
                        "text": "EGASflex"
                    },
                    "spacing": "xxl",
                    "margin": "lg"
                }
            ]
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "separator"
                },
                {
                    "type": "text",
                    "text": "接駁車誤點通報-聯絡電話",
                    "margin": "lg",
                    "weight": "bold",
                    "align": "center",
                    "size": "lg"
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                        {
                            "type": "text",
                            "text": "工作日(08:30-17:30)",
                            "weight": "bold",
                            "size": "md",
                            "align": "center"
                        }
                    ],
                    "margin": "xxl"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "請洽總務部：03-3916058",
                                    "align": "center",
                                    "size": "md",
                                    "action": {
                                        "type": "message",
                                        "label": "連絡電話",
                                        "text": "03-3916058"
                                    },
                                    "decoration": "underline"
                                }
                            ]
                        }
                    ],
                    "alignItems": "center",
                    "margin": "xl"
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                        {
                            "type": "text",
                            "text": "其餘時間",
                            "weight": "bold",
                            "size": "md",
                            "align": "center"
                        }
                    ],
                    "margin": "xxl"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "請洽OCC：03-3916126~6128",
                                    "align": "center",
                                    "size": "md",
                                    "action": {
                                        "type": "message",
                                        "label": "連絡電話",
                                        "text": "03-3916126"
                                    },
                                    "decoration": "underline"
                                }
                            ]
                        }
                    ],
                    "alignItems": "center",
                    "margin": "xl"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [],
                    "margin": "lg"
                }
            ]
        }
    }
    return contents


def three_page(a, at, b, bt, c, ct):
    contents = {
        "type": "carousel",
        "contents": [
            {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "image",
                            "url": a,
                            "size": "full",
                            "aspectMode": "cover",
                            "gravity": "top",
                            "aspectRatio": "8.5:20"
                        }
                    ],
                    "paddingAll": "0px",
                    "action": {
                        "type": "message",
                        "label": at,
                        "text": at
                    }
                }
            },
            {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "image",
                            "url": b,
                            "size": "full",
                            "aspectMode": "cover",
                            "gravity": "top",
                            "aspectRatio": "8.5:20"
                        }
                    ],
                    "paddingAll": "0px",
                    "action": {
                        "type": "message",
                        "label": bt,
                        "text": bt
                    }
                }
            },
            {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "image",
                            "url": c,
                            "size": "full",
                            "aspectMode": "cover",
                            "gravity": "top",
                            "aspectRatio": "8.5:20"
                        }
                    ],
                    "paddingAll": "0px",
                    "action": {
                        "type": "message",
                        "label": ct,
                        "text": ct
                    }
                }
            }
        ]
    }
    return contents


def four_page(a, at, b, bt, c, ct, d, dt):
    contents = {
        "type": "carousel",
        "contents": [
            {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "image",
                            "url": a,
                            "size": "full",
                            "aspectMode": "cover",
                            "gravity": "top",
                            "aspectRatio": "8.5:20"
                        }
                    ],
                    "paddingAll": "0px",
                    "action": {
                        "type": "message",
                        "label": at,
                        "text": at
                    }
                }
            },
            {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "image",
                            "url": b,
                            "size": "full",
                            "aspectMode": "cover",
                            "gravity": "top",
                            "aspectRatio": "8.5:20"
                        }
                    ],
                    "paddingAll": "0px",
                    "action": {
                        "type": "message",
                        "label": bt,
                        "text": bt
                    }
                }
            },
            {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "image",
                            "url": c,
                            "size": "full",
                            "aspectMode": "cover",
                            "gravity": "top",
                            "aspectRatio": "8.5:20"
                        }
                    ],
                    "paddingAll": "0px",
                    "action": {
                        "type": "message",
                        "label": ct,
                        "text": ct
                    }
                }
            },
            {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "image",
                            "url": d,
                            "size": "full",
                            "aspectMode": "cover",
                            "gravity": "top",
                            "aspectRatio": "8.5:20"
                        }
                    ],
                    "paddingAll": "0px",
                    "action": {
                        "type": "message",
                        "label": dt,
                        "text": dt
                    }
                }
            }
        ]
    }
    return contents


def video_page(titleimg, title, titlecolor, flat, video):
    contents = {
        "type": "carousel",
        "contents": [
            {
                "type": "bubble",
                "size": "mega",
                "header": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "icon",
                                            "url": titleimg,
                                            "size": "70px"
                                        }
                                    ],
                                    "width": "70px"
                                },
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": title,
                                            "weight": "bold",
                                            "align": "center",
                                            "color": titlecolor,
                                            "decoration": "underline",
                                            "gravity": "center",
                                            "size": "27px"
                                        }
                                    ],
                                    "offsetEnd": "xl",
                                    "alignItems": "center",
                                    "justifyContent": "center",
                                    "width": "220px"
                                }
                            ],
                            "maxHeight": "80px"
                        }
                    ],
                    "maxHeight": "100px"
                },
                "hero": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                        {
                                            "type": "box",
                                            "layout": "baseline",
                                            "contents": [
                                                {
                                                    "type": "icon",
                                                    "url": "https://i.imgur.com/BmOoACT.png",
                                                    "size": "50px"
                                                }
                                            ],
                                            "maxWidth": "80px",
                                            "justifyContent": "center"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [
                                                {
                                                    "type": "text",
                                                    "text": "行走路線平面圖",
                                                    "weight": "bold",
                                                    "align": "center",
                                                    "size": "xl",
                                                    "decoration": "underline",
                                                    "action": {
                                                        "type": "message",
                                                        "label": "action",
                                                        "text": flat
                                                    },
                                                    "gravity": "center",
                                                    "margin": "xl",
                                                    "offsetBottom": "md"
                                                }
                                            ],
                                            "maxWidth": "200px"
                                        }
                                    ],
                                    "alignItems": "center",
                                    "action": {
                                        "type": "message",
                                        "label": "atob",
                                        "text": "atob"
                                    },
                                    "cornerRadius": "50px",
                                    "offsetTop": "10px",
                                    "margin": "15px"
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                        {
                                            "type": "box",
                                            "layout": "baseline",
                                            "contents": [
                                                {
                                                    "type": "icon",
                                                    "url": "https://i.imgur.com/cYKPlO2.png",
                                                    "size": "50px"
                                                }
                                            ],
                                            "justifyContent": "center",
                                            "maxWidth": "80px"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [
                                                {
                                                    "type": "text",
                                                    "text": "行走路線影片",
                                                    "align": "center",
                                                    "size": "xl",
                                                    "weight": "bold",
                                                    "decoration": "underline",
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "action",
                                                        "uri": video,
                                                        "altUri": {
                                                            "desktop": video
                                                        }
                                                    },
                                                    "gravity": "center",
                                                    "margin": "xl",
                                                    "offsetBottom": "md",
                                                    "color": "#FF5151"
                                                }
                                            ],
                                            "maxWidth": "200px"
                                        }
                                    ],
                                    "alignItems": "center",
                                    "margin": "20px",
                                    "action": {
                                        "type": "message",
                                        "label": "atob",
                                        "text": "atob"
                                    },
                                    "cornerRadius": "50px",
                                    "offsetTop": "10px"
                                }
                            ],
                            "height": "160px"
                        }
                    ]
                },
                "styles": {
                    "hero": {
                        "backgroundColor": "#FFF3EE"
                    }
                }
            }
        ]
    }
    return contents
