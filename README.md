## 青龙 app 签到

```
ql repo https://github.com/sorry510/auto_sign.git
```

### 河南移动签到(hnmcc_sign.py)
> 进入河南移动app，点击签到，使用手机抓取域名为`h5.ha.chinamobile.com`的完整 `cookie`


- 配置变量

```
export hnmcc_cookie="xxx"
```

### 郑州移动微信签到
> 微信进入郑州移动YD66 公众号，使用手机抓取域名为`zxkwx-boot.hacitd.com`的get参数中的openId和userId

```
export yd66_query="openId=xxx&userId=xxx"
```

### freedom 自动续签

```
export freedom_username="xxx"
export freedom_password="xxx"
```

### 云闪付签到
> 进入云闪付app，使用手机抓取域名为`youhui.95516.com`的地址，找到带`header`部分带有`Authorization`的接口, 提取 `Bearer` 之后的部分

```
export ysfAuthorization='xxx' # 多个账号用@符号隔开
```

### 饿了么10点抢5，10元红包

```
export elmck='xxx' # 抓包 h5.ele.me 域名下的任何url 请求头中的Cookie，多个账号用@符号隔开
export elmdh='false' # 兑换设置，默认为false,开启兑换，如需开启兑换，请设置为true
export SM_STARTTIME=60 # 当为60时，9点59分运行脚本，10点准时开枪，如果网络慢可以设置为59，则9点59分59秒开抢
```