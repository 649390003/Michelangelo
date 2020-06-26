from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Shares,UserInfo
# 上传文件需要的包
from django.conf import settings
import os
# 限制未登录用户的访问
from django.contrib.auth.decorators import login_required
# 引入表单
from .forms import UserInfoForm,AccountForm
from django.contrib import messages

# Create your views here.
# 父模板
# def base(request):
#     return render(request, "myShare/base.html" )
# 首页
def index(request):
    # 取session
    # onlinename = request.session.get('onlinename', '游客')
    # print(request.session['user_id'])
    if request.user.id:
        user = User.objects.get(id=request.user.id)
        uinfo = user.userinfo_set.first()
        userimg = user.userinfo_set.first().uploadimg
        onlinename = uinfo.onlinename
        # 此功能已在前台base模板实现
        # if request.user.is_superuser:
        #     issu = "管理员"
        # else:
        #     issu = "用户"
        shares = Shares.objects.all()
        context = {'shares':shares,'userimg':userimg,'onlinename':onlinename}
        return render(request, "myShare/index.html",context)
    return render(request, "myShare/index.html")

# 注册视图
def showregist(request):
    return render(request,'myShare/regist.html')

def regist(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        onlinename = request.POST['onlinename']
        gender = request.POST['gender']
        mobilephone = request.POST['mobilephone']
        email = request.POST['email']
        # 获取路径
        f = request.FILES["file"]
        # 文件在服务器端的路径
        filePath = os.path.join(settings.MEDIA_ROOT,f.name)
        # 将本地文件复制到服务器
        with open(filePath,'wb') as fp:
            for info in f.chunks():
                # 以文件流的形式接收文件
                fp.write(info)
        # print(username + "+" + password + "+" + onlinename + "+" + gender+ "+" + mobilephone + "+" + email+" + "+ filePath)
        # user = Users.createUser(username,password,onlinename,gender,mobilephone,email)
        # user.save()
        return redirect('/login')
    else:
        return redirect('/showregist')


# 主页视图
# def main(request):
#     # 取session
#     onlinename = request.session.get('onlinename','游客')
#     return render(request,"myShare/index.html",{'onlinename':onlinename})


# def login(request):
#     # 如果是POST请求，则说明是点击登录按扭 FORM表单跳转到此的，那么就要验证密码，并进行保存session
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         if username and password:
#             # 去除空格
#             username = username.strip()
#             try:
#                 user = Users.objects.get(username=username)
#                 if user.password == password:
#                     # 存储session
#                     request.session['onlinename'] = user.onlinename
#                     # 设置session的过期时间
#                     request.session.set_expiry(0)
#                     return redirect('/')
#                 else:
#                     msg = "密码错误"
#                     # return render(request,"myShare/login.html",{'msg':msg})
#             except:
#                 msg = "账号不存在"
#                 # return render(request,"myShare/login.html",{'msg':msg})
#         else:
#             msg = "账号或密码为空"
#             # return render(request, "myShare/login.html", {'msg': msg})
#     # 如果是GET请求，就说明是用户刚开始登录，使用URL直接进入登录页面的
#     else:
#         msg = "请先登录"
#     return render(request, "myShare/login.html", {'msg': msg})
# 登录视图
# def login(request):
#     return render(request,"myShare/login.html")


# 清除session

from django.contrib.auth import logout
def quit(request):
    # 第一种清除方式
    logout(request)
    return redirect('/users/login')

# 收益页面
@login_required
def shouyi1(request):
    user = User.objects.get(id=request.user.id)
    uinfo = user.userinfo_set.first()
    userimg = user.userinfo_set.first().uploadimg
    onlinename = uinfo.onlinename
    profits = []
    # 全部的收益订单
    orprofits = user.profit_set.all()
    sharecount = user.profit_set.count()
    # 总价值
    allvalue = 0
    # 总收益
    allprofit = 0
    for p in orprofits:
        p.value = p.nowrate * p.sharenum
        # 加入总价值
        allvalue+=p.value
        p.profit = round((p.nowrate - p.buyrate) * p.sharenum,2)
        # 加入总收益
        allprofit+=p.profit
        profits.append(p)
    # print(profits[0].profit)
    # print(profits[0].value)
    context = {'profits':profits,'allvalue':allvalue,'allprofit':allprofit,'sharecount':sharecount,'userimg': userimg, 'onlinename': onlinename,'shouyi':'active','shouyi1' : 'active'}
    return render(request,"myShare/shouyi-1.html",context)
@login_required
def shouyi2(request):
    user = User.objects.get(id=request.user.id)
    uinfo = user.userinfo_set.first()
    userimg = user.userinfo_set.first().uploadimg
    onlinename = uinfo.onlinename
    context = {'userimg': userimg, 'onlinename': onlinename, 'shouyi': 'active', 'shouyi2': 'active'}
    return render(request, "myShare/shouyi-2.html", context)
@login_required
def shouyi3(request):
    user = User.objects.get(id=request.user.id)
    uinfo = user.userinfo_set.first()
    userimg = user.userinfo_set.first().uploadimg
    onlinename = uinfo.onlinename
    context = {'userimg': userimg, 'onlinename': onlinename, 'shouyi': 'active', 'shouyi3': 'active'}
    return render(request, "myShare/shouyi-3.html", context)

# 分析页面
@login_required
def fenxi1(request):
    user = User.objects.get(id=request.user.id)
    uinfo = user.userinfo_set.first()
    userimg = user.userinfo_set.first().uploadimg
    onlinename = uinfo.onlinename
    context = {'userimg': userimg, 'onlinename': onlinename, 'fenxi': 'active', 'fenxi1': 'active'}
    return render(request, "myShare/fenxi1.html", context)
@login_required
def fenxi2(request):
    # 获取全部信息
    # shares = Shares.objects.all()
    # 获取登录用户自己的信息
    shares = Shares.objects.filter(owner__id=request.user.id)
    user = User.objects.get(id=request.user.id)
    uinfo = user.userinfo_set.first()
    userimg = user.userinfo_set.first().uploadimg
    onlinename = uinfo.onlinename
    context = {'shares':shares,'userimg': userimg, 'onlinename': onlinename, 'fenxi': 'active', 'fenxi2': 'active'}
    return render(request, "myShare/fenxi2.html", context)
@login_required
def fenxi3(request):
    user = User.objects.get(id=request.user.id)
    uinfo = user.userinfo_set.first()
    userimg = user.userinfo_set.first().uploadimg
    onlinename = uinfo.onlinename
    context = {'userimg': userimg, 'onlinename': onlinename, 'fenxi': 'active', 'fenxi3': 'active'}
    return render(request, "myShare/fenxi3.html", context)
@login_required
def fenxi4(request):
    user = User.objects.get(id=request.user.id)
    uinfo = user.userinfo_set.first()
    userimg = user.userinfo_set.first().uploadimg
    onlinename = uinfo.onlinename
    context = {'userimg': userimg, 'onlinename': onlinename, 'fenxi': 'active', 'fenxi4': 'active'}
    return render(request, "myShare/fenxi4.html", context)

# 财务
@login_required
def caiwu(request):
    user = User.objects.get(id=request.user.id)
    uinfo = user.userinfo_set.first()
    # 用户头像
    userimg = user.userinfo_set.first().uploadimg
    # 用户昵称
    onlinename = uinfo.onlinename
    if user.account_set.first():
        # 账户余额
        uact = user.account_set.first()
        # 充值/提现记录
        records = user.record_set.filter(isdelete=False)
        # print(records[0].rdate)
        # 账户总流水金额
        zdls = 0
        for r in records:
            zdls += r.amount
        context = {'zdls': zdls,'uact': uact, 'records': records,'userimg': userimg, 'onlinename': onlinename, 'caiwu': 'active'}
        return render(request, "myShare/caiwu.html", context)
    else:
        context = {'userimg': userimg, 'onlinename': onlinename, 'caiwu': 'active'}
        return render(request, "myShare/caiwu.html", context)

# 客户
@login_required
def kehu(request):
    user = User.objects.get(id=request.user.id)
    uinfo = user.userinfo_set.first()
    userimg = user.userinfo_set.first().uploadimg
    onlinename = uinfo.onlinename
    context = {'userimg': userimg, 'onlinename': onlinename, 'kehu': 'active'}
    return render(request, "myShare/kehu.html", context)

# 服务
@login_required
def fuwu(request):
    user = User.objects.get(id=request.user.id)
    uinfo = user.userinfo_set.first()
    userimg = user.userinfo_set.first().uploadimg
    onlinename = uinfo.onlinename
    context = {'userimg': userimg, 'onlinename': onlinename, 'fuwu': 'active'}
    return render(request, "myShare/fuwu.html", context)

# 消息
@login_required
def xiaoxi(request):
    user = User.objects.get(id=request.user.id)
    uinfo = user.userinfo_set.first()
    userimg = user.userinfo_set.first().uploadimg
    onlinename = uinfo.onlinename
    context = {'userimg': userimg, 'onlinename': onlinename, 'xiaoxi': 'active'}
    return render(request, "myShare/xiaoxi.html", context)

# 设置
@login_required
def shezhi1(request):
    user = User.objects.get(id=request.user.id)
    uinfo = user.userinfo_set.first()
    userimg = user.userinfo_set.first().uploadimg
    onlinename = uinfo.onlinename
    if request.method != 'POST':
        form = UserInfoForm(instance=uinfo)
    else:
        form = UserInfoForm(instance=uinfo,data=request.POST)
        if form.is_valid():
            if request.POST.get("uploadimg","file")=="":
                form.save()
                return HttpResponseRedirect(reverse('myShare:index'))
            else:
                uinfo = form.save(commit=False)
                # f为文件名
                f = request.FILES["uploadimg"]
                uinfo.uploadimg = f
                print(uinfo.uploadimg)
                uinfo.save()
                return HttpResponseRedirect(reverse('myShare:index'))
    context = {'form':form,'userimg': userimg, 'onlinename': onlinename, 'shezhi':'active', 'shezhi1': 'active'}
    return render(request, "myShare/shezhi1.html", context)
@login_required
def shezhi2(request):
    user = User.objects.get(id=request.user.id)
    uinfo = user.userinfo_set.first()
    userimg = user.userinfo_set.first().uploadimg
    onlinename = uinfo.onlinename
    context = {'userimg': userimg, 'onlinename': onlinename, 'shezhi': 'active', 'shezhi2': 'active'}
    return render(request, "myShare/shezhi2.html", context)

# 用户的股票交易记录
@login_required
def order(request):
    user = User.objects.get(id=request.user.id)
    uinfo = user.userinfo_set.first()
    userimg = user.userinfo_set.first().uploadimg
    onlinename = uinfo.onlinename
    mairudingdan = user.buyorder_set.all()
    # print(mairudingdan)
    maichudingdan = user.sellorder_set.all()
    # print(maichudingdan)
    context = {'mairudingdan':mairudingdan,'maichudingdan':maichudingdan,'userimg': userimg, 'onlinename': onlinename, 'kehu': 'active'}
    return render(request,"myShare/order.html", context)

from django.contrib.auth.models import User
import random
def createshare(request):
    share = ["小米","京东","阿里","魅族","腾讯","网易","微软"]
    for i in range(0,7):
        name = share[i]
        owner = User.objects.get(pk=2)
        snumber = str(100000+i)
        print(snumber)
        issuenum = 5000
        hp = random.randint(50,100)
        lp = random.randint(10,30)
        np = random.randint(lp,hp)
        s = Shares(sname=name,snumber=snumber,issuenum=issuenum,hprice=hp,lprice=lp,nprice=np)
        s.save()
        s.owner.add(owner)
    return HttpResponse("create successfully")

# 加入自选股
@login_required
def addshare(request,share_id):
    # 要加入自选股的用户
    owner = User.objects.get(id=request.user.id)
    # 用户拥有的全部股票
    # shares = Shares.objects.filter(owner__id=request.user.id)
    share = Shares.objects.get(id=share_id)
    # 该股票的全部买家
    users = share.owner.all()
    if owner in users:
        messages.error(request,"请勿重复添加！")
    else:
        share.owner.add(owner)
        messages.success(request, "添加成功！")
    return redirect("/")

@login_required
def userinfo(request):
    user = User.objects.get(id=request.user.id)
    uinfo = user.userinfo_set.first()
    # print(uinfo)
    if request.method != 'POST':
        form = UserInfoForm(instance=uinfo)
    else:
        form = UserInfoForm(instance=uinfo,data=request.POST)
        if form.is_valid():
            if request.POST.get("uploadimg","file")=="":
                form.save()
            else:
                uinfo = form.save(commit=False)
                # f为文件名
                f = request.FILES["uploadimg"]
                uinfo.uploadimg = f
                print(uinfo.uploadimg)
                uinfo.save()
                return HttpResponseRedirect(reverse('myShare:index'))
    userimg = user.userinfo_set.first().uploadimg
    onlinename = uinfo.onlinename
    context = {'form':form,'userimg': userimg, 'onlinename': onlinename}
    return render(request,"myShare/userinfo.html",context)

def adduserinfo(request):
    if request.user.id:
        user = User.objects.get(id=request.user.id)
        if user.userinfo_set.first():
            return HttpResponseRedirect(reverse('myShare:index'))
        else:
            if request.method != 'POST':
                form = UserInfoForm()
            else:
                form = UserInfoForm(data=request.POST)
                if form.is_valid():
                    uinfo = form.save(commit=False)
                    uinfo.user = user
                    f = request.FILES["uploadimg"]
                    uinfo.uploadimg = f
                    uinfo.save()
                    return HttpResponseRedirect(reverse('myShare:index'))
        context = {'form':form}
        return render(request,"myShare/adduserinfo.html",context)
    return redirect('/users/login')

@login_required
def addaccount(request):
    if request.user.id:
        user = User.objects.get(id=request.user.id)
        if request.method != 'POST':
            form = AccountForm()
        else:
            form = AccountForm(data=request.POST)
            if form.is_valid():
                # 此处uacc.bankcard保存的值错误,会将所有POST值都传递进来
                # 已解决，自定义验证方法的返回值错误
                uacc = form.save(commit=False)
                uacc.owner = user
                # uacc.bankcard = request.POST['bankcard']
                uacc.save()
                messages.info(request,"开通成功！")
                return HttpResponseRedirect(reverse('myShare:index'))
        uinfo = user.userinfo_set.first()
        userimg = user.userinfo_set.first().uploadimg
        onlinename = uinfo.onlinename
        context = {'form': form, 'userimg': userimg, 'onlinename': onlinename, }
        return render(request,"myShare/addaccount.html",context)
    return redirect('/users/login')

# 账户充值界面
from .forms import ChargeForm
from .models import Record
@login_required
def recharge(request):
    if request.user.id:
        user = User.objects.get(id=request.user.id)
        uaccount = user.account_set.first()
        if request.method != 'POST':
            form = ChargeForm(instance=uaccount)
        else:
            form = ChargeForm(data=request.POST)
            if form.is_valid():
                if uaccount.bankcard == request.POST['bankcard']:
                    if uaccount.paypassword == request.POST['ppassword']:
                        uaccount.balance = uaccount.balance + float(request.POST["ramount"])
                        uaccount.save()
                        # 将充值记录保存
                        rcrecord = Record(owner=user,bstype=True,amount=float(request.POST["ramount"]))
                        rcrecord.save()
                        messages.info(request,"充值成功")
                        return HttpResponseRedirect(reverse('myShare:caiwu'))
                    else:
                        messages.error(request,"密码错误，请重新输入！")
                else:
                    messages.error(request, "银行账号不正确")
        uinfo = user.userinfo_set.first()
        userimg = user.userinfo_set.first().uploadimg
        onlinename = uinfo.onlinename
        context = {'form': form,'userimg': userimg, 'onlinename': onlinename, }
        return render(request, "myShare/recharge.html", context)
    return redirect('/users/login')

# 账户提现界面
from .forms import ToCashForm
@login_required
def tocash(request):
    if request.user.id:
        user = User.objects.get(id=request.user.id)
        uaccount = user.account_set.first()
        if request.method != 'POST':
            form = ToCashForm(instance=uaccount)
        else:
            form = ToCashForm(data=request.POST)
            if form.is_valid():
                if uaccount.bankcard == request.POST['bankcard']:
                    if uaccount.paypassword == request.POST['ppassword']:
                        # 判断余额是否充足
                        print(uaccount.balance)
                        if uaccount.balance >= float(request.POST["tcamount"]):
                            uaccount.balance = uaccount.balance - float(request.POST["tcamount"])
                            uaccount.save()
                            # 将充值记录保存
                            rcrecord = Record(owner=user,bstype=False,amount=float(request.POST["tcamount"]))
                            rcrecord.save()
                            messages.info(request,"提现成功")
                            return HttpResponseRedirect(reverse('myShare:caiwu'))
                        else:
                            messages.error(request, "账户余额不足！")
                    else:
                        messages.error(request,"密码错误，请重新输入！")
                else:
                    messages.error(request, "银行账号错误")
        uinfo = user.userinfo_set.first()
        userimg = user.userinfo_set.first().uploadimg
        onlinename = uinfo.onlinename
        context = {'form': form, 'userimg': userimg, 'onlinename': onlinename, }
        return render(request, "myShare/tocash.html", context)
    return redirect('/users/login')

# 删除提现/充值记录
def delrtrecord(request,record_id):
    # print(record_id)
    record = Record.objects.get(id=record_id)
    # print(record.amount)
    record.isdelete = True
    record.save()
    return redirect('/caiwu')

# 股票详细信息显示
@login_required
def shareinfo(request,share_id):
    share = Shares.objects.get(id=share_id)
    # 股票的第几次开盘
    # shareinfo_infotimes = ShareDailyInfo.objects.filter(share=share).count() + 1
    # print(shareinfo_infotimes)
    context = {'share':share}
    return render(request,"myShare/shareinfo.html",context)

# 股票开盘后信息ajax传递
from django.http import JsonResponse
from .models import ShareDailyInfo
import random
@login_required
def shareinfoajax(request):
    sid = request.POST.get('sid',0)
    print(sid)
    share = Shares.objects.get(id=sid)
    # 开盘价
    startprice = share.nprice
    # 涨停价
    ztprice = 1.1*startprice
    # 跌停价
    dtprice = 0.9*startprice
    # 初始变动价等于开盘价
    flowprice = startprice
    # 价格变化列表
    plist = []
    for i in range(10):
        # 设置涨停跌停flag
        flag = True
        if flag:
            # 股票每次波动
            flow = random.randint(-2, 2)*0.01*flowprice
            # 股票波动后的价格
            flowprice += flow
        if flowprice >= ztprice:
            # 关闭价格变动
            flag = False
            # 固定为传递涨停价
            plist.append(ztprice)
        elif flowprice <= dtprice:
            # 关闭价格变动
            flag = False
            # 固定为传递跌停价
            plist.append(dtprice)
        elif flowprice < ztprice and flowprice>dtprice:
            # 将价格保留两位小数并传入列表
            plist.append(round(flowprice,2))
        else:
            plist.append(0)
    # print(plist)
    # 每日最高价
    highestp = max(plist)
    # 每日最低价
    lowestp = min(plist)
    # 收盘价
    closep = plist[-1]
    sdinfo_count = ShareDailyInfo.objects.filter(share=share).count()
    sdinfo = ShareDailyInfo(
        share=share,
        highestp=highestp,
        lowestp=lowestp,
        startp=startprice,
        closep=closep,
        infotimes=int(sdinfo_count)+1,
    )
    # 关于股票基本信息的保存
    # 将今天的收盘价保存到现价
    share.nprice = closep
    # 若历史最高价比今日最高价低，则更新历史最高价
    if share.hprice < highestp:
        share.hprice = highestp
    # 若历史最低价比今日最低价高，则更新历史最低价
    if share.lprice > lowestp:
        share.lprice = lowestp
    # 将一天的开盘信息保存
    # sdinfo.save()
    # 将股票基本信息保存
    # share.save()
    return JsonResponse({'plist':plist})

# 股票买入订单
from .forms import BuyOrderForm
from .models import BuyOrder,Shares,ShareDailyInfo,Profit
@login_required
def buyorder(request,share_id):
    if request.user.id:
        # 获取当前用户
        user = User.objects.get(id=request.user.id)
        # 获取当前用户的账户信息
        uaccount = user.account_set.first()
        # 获取要买入的股票信息,并作为默认数据传入前台
        share = Shares.objects.get(id=share_id)
        if request.method != 'POST':
            form = BuyOrderForm()
        else:
            form = BuyOrderForm(data=request.POST)
            if form.is_valid():
                order = form.save(commit=False)
                order.owner = user
                order.share = share
                payment = order.expectprice * order.buynum
                # print(payment)
                # print(uaccount.balance)
                if payment <= uaccount.balance:
                    uaccount.balance -= payment
                    # 如果买入的股票数小于等于剩余股票数
                    if order.buynum <= share.issuenum:
                        # 修改剩余的股票数
                        share.issuenum -= order.buynum
                        # 获取这是该股票的第几次模拟数据
                        # sdinfo = ShareDailyInfo.objects.last()
                        sdinfos = ShareDailyInfo.objects.filter(share=share)
                        # print(sdinfos)
                        sdinfo = sdinfos[len(sdinfos) - 1]
                        # print(sdinfo.infotimes)
                        # 只要输入价格在本次模拟的最高价与最低价之间，则可以购买成功
                        if order.expectprice <= sdinfo.highestp and order.expectprice >= sdinfo.lowestp:
                            order.isSuccess = True
                            # 添加成功备注
                            order.remark = "购买成功"
                            # 保存订单（购买成功）
                            order.save()
                            # 股票保存
                            share.save()
                            # 支付金额
                            uaccount.save()
                            # 购买成功后创建用户的收益信息
                            # 如果创建一个表则买入价无法处理,只能创建多个profit表来存储信息
                            profit = Profit(
                                share=share,
                                owner=user,
                                # 买入价
                                buyrate=order.expectprice,
                                # 当前价等于今日股票的收盘价
                                nowrate=sdinfo.closep,
                                sharenum=order.buynum,
                                # totalvalue=sdinfo.closep * order.buynum,
                                # # 当前价乘以买入数目 减去 买入价乘以买入数目
                                # profit=sdinfo.closep * order.buynum - order.expectprice * order.buynum,
                            )
                            profit.save()
                            upinfos = user.profit_set.filter(share=share)
                            for pinfo in upinfos:
                                pinfo.nowrate = sdinfo.closep
                                pinfo.save()
                            messages.info(request, "已为您下单请等待")
                            return HttpResponseRedirect(reverse('myShare:shareinfo', args=[share_id]))
                        else:
                            order.remark = "股票价格未达到您的购买价"
                    else:
                        order.remark = "市场没有足够的股票数"
                    # 保存订单（购买失败）
                    order.isSuccess = False
                    order.save()
                    messages.info(request,"已为您下单请等待")
                else:
                    messages.error(request,"账户余额不足!")
        uinfo = user.userinfo_set.first()
        userimg = user.userinfo_set.first().uploadimg
        onlinename = uinfo.onlinename
        context = {"share":share,'form': form, 'userimg': userimg, 'onlinename': onlinename, }
        # context = {"share":share,"form":form}
        return render(request, "myShare/buyorder.html", context)
    return redirect('/users/login')

# 股票卖出订单
from .forms import SellOrderForm
from .models import SellOrder,Shares,ShareDailyInfo
@login_required
def sellorder(request,share_id):
    if request.user.id:
        # 获取当前用户
        user = User.objects.get(id=request.user.id)
        # 获取当前用户的账户信息
        uaccount = user.account_set.first()
        # 获取要买入的股票信息,并作为默认数据传入前台
        share = Shares.objects.get(id=share_id)
        if request.method != 'POST':
            form = SellOrderForm()
        else:
            form = SellOrderForm(data=request.POST)
            if form.is_valid():
                # 将订单信息存入order
                order = form.save(commit=False)
                order.owner = user
                order.share = share
                # 获取该用户已拥有的该股票的信息
                uprofit = user.profit_set.filter(share=share)
                ownsharenum = 0
                # 将用户拥有的该股票的数目存入ownsharenum
                for up in uprofit:
                    ownsharenum += up.sharenum
                # print(ownsharenum)
                # 若用户所持股票数小于要卖出股票数，则弹窗
                if ownsharenum >= order.sellnum:
                    # 获取这是该股票的第几次模拟数据
                    sdinfos = ShareDailyInfo.objects.filter(share=share)
                    # print(sdinfos)
                    sdinfo = sdinfos[len(sdinfos)-1]
                    # print(sdinfo.infotimes)
                    # 只要输入价格在本次模拟的最高价与最低价之间，则可以卖出成功
                    if order.expectprice <= sdinfo.highestp and order.expectprice >= sdinfo.lowestp:
                        # 要卖出的股票数目初始值为订单数
                        sellsharenum = order.sellnum
                        # 从第一个收益数据开始卖，判断股票数是否充足
                        for up in uprofit:
                            if sellsharenum - up.sharenum >= 0:
                                sellsharenum -= up.sharenum
                                up.sharenum = 0
                                # print(up.sharenum)
                                up.save()
                                # 将sharenum等于0的收益数据删除
                                up.delete()
                            else:
                                up.sharenum -= sellsharenum
                                # print(up.sharenum)
                                up.save()
                                break
                        # 订单是否成功
                        order.isSuccess = True
                        # 添加成功备注
                        order.remark = "出售成功"
                        # 保存订单（出售成功）
                        order.save()

                        # 卖出后可获得的收入
                        income = order.expectprice * order.sellnum
                        # print(income)
                        # 更改账户余额
                        uaccount.balance += income
                        print(uaccount.balance)
                        # 保存账户信息
                        uaccount.save()

                        # 更改该股票的剩余票数(总数目加上卖出的数目)
                        share.issuenum += order.sellnum
                        share.save()
                        messages.info(request,"已为您下单请等待")
                        return HttpResponseRedirect(reverse('myShare:shareinfo', args=[share_id]))
                    else:
                        # 订单未成功
                        order.isSuccess = False
                        order.remark = "股票价格未达到您的卖出价"
                        # 未售出的订单保存
                        order.save()
                        messages.info(request, "已为您下单请等待")
                else:
                    messages.error(request, "账户股票数目小于卖出数目")
        uinfo = user.userinfo_set.first()
        userimg = user.userinfo_set.first().uploadimg
        onlinename = uinfo.onlinename
        context = {"share": share, 'form': form, 'userimg': userimg, 'onlinename': onlinename, }
        # context = {"share": share, "form": form}
        return render(request, "myShare/sellorder.html", context)
    return redirect('/users/login')

# 显示股票卖出订单（若未持有该股票，则进不去股票卖出页）
@login_required
def showsellorder(request,share_id):
    user = User.objects.get(id=request.user.id)
    share = Shares.objects.get(id=share_id)
    # 判断用户是否是股票的拥有者
    if user.profit_set.filter(share=share):
        return HttpResponseRedirect(reverse('myShare:sellorder', args=[share_id]))
    else:
        messages.error(request,"您的账户没有该股票，无法卖出！")
        return HttpResponseRedirect(reverse('myShare:shareinfo', args=[share_id]))