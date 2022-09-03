import requests,json,base64,hashlib
bot_url="https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=XXXX"
def send_work_msg(content, webhook_url):
    data = {"msgtype": "markdown", 
            "markdown": 
            {"content": content}}
    r = requests.post(webhook_url, data=json.dumps(data))
    # return r.text, r.status_code
send_work_msg("聚宽环境测试:企业微信群发",bot_url)

name,holding,vr,max_vr,pct_chg,max_pct_chg,min_pct_chg,pnl,pnl_pct,dt="贵州茅台",1032000,3,15,0.01,0.09,-0.02,1030,0.03,"2000-09-01"
mkd_msg=''' 
#### ** 盘中！**<font color=\"warning\">**{0}**</font> \n
            > **总持仓:{1}** 
            > 盈亏：<font color=\"warning\">{7}/{8}</font>                     
            > 量比/最高：<font color=\"info\">{2} / {3}</font> 
            > 变/高/低：<font color=\"warning\">{4} , {5}, {6}</font>
            > 时间：<font color=\"comment\">{9}</font> 
    '''.format(name,holding,vr,max_vr,pct_chg,max_pct_chg,min_pct_chg,pnl,pnl_pct,dt)
def sent_work_markdown(webhook_url=bot_url,mkd_msg=mkd_msg):
    mkd={
        "msgtype": "markdown",
        "markdown": {
            "content": mkd_msg
            }
        }

    body = json.dumps(mkd)
    res = requests.post(webhook_url,data=body)
    return res.text, res.status_code
sent_work_markdown(bot_url,mkd_msg)

def sent_work_img(img,webhook_url=bot_url):
    with open(img, 'rb') as file:
        #转换图片成base64格式
        data = file.read()
        encodestr = base64.b64encode(data)
        image_data = str(encodestr, 'utf-8')

    #图片的MD5值
    with open(img, 'rb') as file:
        md = hashlib.md5()
        md.update(file.read())
        image_md5 = md.hexdigest()
        
    mkt = {"msgtype": "image",
            "image": {"base64": image_data,
                      "md5": image_md5
                     }
            }
    
    body = json.dumps(mkt)
    res = requests.post(webhook_url,data=body)
sent_work_img('work.jpg')
