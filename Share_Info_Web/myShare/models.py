from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ColsingPrice(models.Model):
    sclose = models.FloatField()
    sdate = models.DateField()
    smonth = models.IntegerField()
    sweek = models.IntegerField()
    sweekday = models.CharField(max_length=10)

    class Meta:
        db_table = "colsing_price"
        ordering = ["id"]

    @classmethod
    def createColsingPrice(cls, sclose, sdate, smonth, sweek, sweekday):
        # 若有装饰器，则可以用cls表示User类
        cprice = cls(
            sclose=sclose,
            sdate=sdate,
            smonth=smonth,
            sweek=sweek,
            sweekday=sweekday,
        )
        return cprice

# 自己创建的User模型
class UserInfo(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    onlinename = models.CharField(max_length=20)
    gender = models.CharField(default='男',max_length=5)
    mobilephone = models.CharField(max_length=15)
    uploadimg = models.ImageField(upload_to="myShare",default="media/myShare/profile_small.jpg")
    isDelete = models.BooleanField(default=False)
    class Meta:
        db_table = "userinfo"
        ordering = ['id']
    # @classmethod
    # def createUser(cls, username, password, onlinename, gender, mobilephone, email,
    #                   isD=False):
    #     # 若有装饰器，则可以用cls表示User类
    #     user = cls(
    #         username=username,
    #         password=password,
    #         onlinename=onlinename,
    #         gender=gender,
    #         mobilephone=mobilephone,
    #         email=email,
    #         # uploadimg=uploadimg,
    #         isDelete=isD,
    #     )
    #     return user

# 股票表
class Shares(models.Model):
    sname = models.CharField(max_length=20)
    snumber = models.CharField(max_length=10)
    issuenum = models.IntegerField()
    issuedate = models.DateTimeField(auto_now_add=True)
    hprice = models.FloatField()
    lprice = models.FloatField()
    nprice = models.FloatField()
    owner = models.ManyToManyField(User)
    isDelete = models.BooleanField(default=False)

    class Meta:
        db_table = "shares"
        ordering = ["id"]

# 股市开盘一天的信息
class ShareDailyInfo(models.Model):
    # 所属的股票对象
    share = models.ForeignKey(Shares)
    highestp = models.FloatField()
    lowestp = models.FloatField()
    startp = models.FloatField()
    closep = models.FloatField()
    # 第几次开盘的数据
    infotimes = models.IntegerField()
    class Meta:
        db_table = "sharedailyinfo"
        ordering = ["id"]


# 收益表
class Profit(models.Model):
    # 对应的股票
    share = models.ForeignKey(Shares)
    # 股票收益人
    owner = models.ForeignKey(User)
    # 买入时的价格
    buyrate = models.FloatField()
    # 当前价
    nowrate = models.FloatField()
    # 所持有的股票数
    sharenum = models.IntegerField()
    # # 该股票的当前总价值
    # totalvalue = models.FloatField()
    # # 该股票的总收益
    # profit = models.FloatField()
    class Meta:
        db_table = "profit"
        ordering = ["id"]

# 账户（余额，银行卡号）
class Account(models.Model):
    # 账户所有者
    owner = models.ForeignKey(User)
    # 绑定银行卡
    bankcard = models.CharField(max_length=20)
    # 支付密码
    paypassword = models.CharField(max_length=20)
    # 账户余额
    balance = models.FloatField(default=0)
    class Meta:
        db_table = "account"
        ordering = ["id"]

# 账户充值,提现记录
class Record(models.Model):
    # 记录所有者
    owner = models.ForeignKey(User)
    # 交易类型,False为提现，True为充值
    bstype = models.BooleanField(default=False)
    # 交易金额
    amount = models.FloatField()
    # 交易时间
    rdate = models.DateTimeField(auto_now_add=True)
    # 是否删除记录
    isdelete = models.BooleanField(default=False)
    class Meta:
        db_table = "actrecord"
        ordering = ["-rdate"]

# 购买订单
class BuyOrder(models.Model):
    owner = models.ForeignKey(User)
    share = models.ForeignKey(Shares)
    expectprice = models.FloatField()
    buynum = models.IntegerField()
    isSuccess = models.BooleanField(default=False)
    ordertime = models.DateTimeField(auto_now_add=True)
    remark = models.CharField(max_length=100)

    class Meta:
        db_table = "buyorder"
        ordering = ["id"]

# 卖出订单
class SellOrder(models.Model):
    owner = models.ForeignKey(User)
    share = models.ForeignKey(Shares)
    expectprice = models.FloatField()
    sellnum = models.IntegerField()
    isSuccess = models.BooleanField(default=False)
    ordertime = models.DateTimeField(auto_now_add=True)
    remark = models.CharField(max_length=100)

    class Meta:
        db_table = "sellorder"
        ordering = ["id"]