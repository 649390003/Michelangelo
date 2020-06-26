from django.conf.urls import url
from . import views

urlpatterns=[
    # url(r'^base/$',views.base),
    # 首页
    url(r'^$',views.index,name="index"),
    # 注册
    url(r'^showregist/$',views.showregist,name="showregist"),
    url(r'^regist/$',views.regist,name="regist"),
    # 主页
    # url(r'^main/$',views.main,name="main"),
    # url(r'^showmain/$',views.showmain,name="showmain"),
    # 登录
    # url(r'^login/$',views.login,name="login"),
    url(r'^quit/$',views.quit,name="quit"),
    # 收益三个页面
    url(r'^shouyi1/$',views.shouyi1,name="shouyi1"),
    url(r'^shouyi2/$',views.shouyi2,name="shouyi2"),
    url(r'^shouyi3/$',views.shouyi3,name="shouyi3"),
    # 分析四个页面
    url(r'^fenxi1/$',views.fenxi1,name="fenxi1"),
    url(r'^fenxi2/$',views.fenxi2,name="fenxi2"),
    url(r'^fenxi3/$',views.fenxi3,name="fenxi3"),
    url(r'^fenxi4/$',views.fenxi4,name="fenxi4"),
    # 财务
    url(r'^caiwu/$',views.caiwu,name="caiwu"),
    # 用户交易订单
    url(r'order/$',views.order,name="order"),
    # 客户
    url(r'^kehu/$',views.kehu,name="kehu"),
    # 服务
    url(r'^fuwu/$',views.fuwu,name="fuwu"),
    # 消息
    url(r'^xiaoxi/$',views.xiaoxi,name="xiaoxi"),
    # 设置
    url(r'^shezhi1/$',views.shezhi1,name="shezhi1"),
    url(r'^shezhi2/$',views.shezhi2,name="shezhi2"),
    # 生成股票基础信息
    url(r'^createshare/$',views.createshare,name='createshare'),
    # 添加个人详细信息
    url(r'^adduserinfo/$',views.adduserinfo,name='adduserinfo'),
    # 修改个人详细信息
    url(r'^userinfo/$',views.userinfo,name='userinfo'),
    # 添加账户信息
    url(r'^addaccount/$',views.addaccount,name='addaccount'),
    # 账户充值
    url(r'^recharge/$',views.recharge,name='recharge'),
    # 账户提现
    url(r'^tocash/$',views.tocash,name='tocash'),
    # 充值/提现记录删除
    url(r'^delrtrecord/(?P<record_id>\d+)/$',views.delrtrecord,name='delrtrecord'),
    # 股票详细信息
    url(r'^shareinfo/(?P<share_id>\d+)/$',views.shareinfo,name='shareinfo'),
    # 加入至自选股
    url(r'^addshare/(?P<share_id>\d+)/$',views.addshare,name='addshare'),
    # 股票价格动态变动
    url(r'^shareinfoajax/$',views.shareinfoajax,name='shareinfoajax'),
    # 股票买入订单
    url(r'^buyorder/(?P<share_id>\d+)/$',views.buyorder,name='buyorder'),
    # 股票卖出订单
    url(r'^sellorder/(?P<share_id>\d+)/$',views.sellorder,name='sellorder'),
    # 是否显示股票卖出订单
    url(r'^showsellorder/(?P<share_id>\d+)/$',views.showsellorder,name='showsellorder'),
]