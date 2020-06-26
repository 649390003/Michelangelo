from django import forms
from .models import UserInfo,Account,BuyOrder,SellOrder
from django.forms import fields,widgets,ValidationError

# 用户详细信息
class UserInfoForm(forms.ModelForm):
    gender = fields.ChoiceField(
        label='性别',
        choices=((1, '男'), (2, '女'),),
        initial=1,
        widget=widgets.RadioSelect
    )
    mobilephone = fields.NumberInput()
    class Meta:
        model = UserInfo
        fields = ['uploadimg','onlinename','gender','mobilephone']
        labels = {'onlinename':'用户昵称','gender':'性别','mobilephone':'联系方式','uploadimg':'上传头像'}
        widgets={
            'uploadimg':forms.FileInput(attrs={'class':'fileInput','id':'uploadimg'}),
            "onlinename":forms.TextInput(attrs={'class':'shurunic'}),
            "mobilephone": forms.TextInput(attrs={'class': 'shurunic'})
        }

# 账户表单
class AccountForm(forms.ModelForm):
    bankcard = fields.CharField(
        required=True,
        max_length=15,
        min_length=10,
        label='银行卡号',
        error_messages={
            'required': '银行账户不能为空',
            'invalid': '数据格式不正确',
        },
        widget=forms.NumberInput(attrs={'class': 'form-control',})
    )
    paypassword = fields.CharField(
        required=True,
        max_length=15,
        min_length=6,
        label='支付密码',
        error_messages={'required': '密码不能为空', 'invalid': '输入不合规定'},
        widget=widgets.PasswordInput(attrs={'class': 'form-control loon lpass', 'value': ''})
    )
    repassword = fields.CharField(
        required=True,
        max_length=15,
        min_length=6,
        label='确认密码',
        error_messages={'required': '密码不能为空', 'invalid': '输入不合规定'},
        widget=widgets.PasswordInput(attrs={'class': 'form-control loon lpass', 'value': ''})
    )
    class Meta:
        model = Account
        fields = "__all__"
        exclude = ["owner","balance"]

    # 方法名自定义的是哪个字段，就return哪个字段的值
    def clean_repassword(self):
        print(self.cleaned_data['paypassword'])
        print(self.cleaned_data['repassword'])
        if self.cleaned_data['paypassword'] == self.cleaned_data['repassword']:
            return self.cleaned_data['repassword']
        else:
            self.add_error('repassword', ValidationError('密码不一致'))
            return self.cleaned_data['repassword']
    def clean_bankcard(self):
        if self.cleaned_data['bankcard'].isdigit():
            return self.cleaned_data['bankcard']
        else:
            self.add_error('bankcard', ValidationError('请输入纯数字'))
            return self.cleaned_data['bankcard']

# 充值表单
class ChargeForm(forms.ModelForm):
    bankcard = fields.CharField(
        required=True,
        max_length=15,
        min_length=10,
        label='银行卡号',
        help_text='请确认的您的银行账户',
        error_messages={
            'required': '银行账户不能为空',
            'invalid': '数据格式不正确',
        },
        widget=forms.NumberInput(attrs={'class': 'form-control','readonly':'true', })
    )
    ramount = fields.DecimalField(
        required=True,
        min_value = 10,
        decimal_places= 2,
        label = "充值金额",
        error_messages={
            'required': '金额不能为空',
            'min_value': '充值订单至少为10元',
            'decimal_places': '金额保留两位小数',
            'invalid': '输入不合规定',
        },
        widget=widgets.NumberInput(attrs={'class': 'form-control','placeholder':"每次充值订单不少于¥10"})
    )
    ppassword = fields.CharField(
        required=True,
        max_length=15,
        min_length=6,
        label='交易密码',
        error_messages={'required': '密码不能为空', 'invalid': '输入不合规定'},
        widget=widgets.PasswordInput(attrs={'class': 'form-control', 'value': ''})
    )
    class Meta:
        model = Account
        fields = ["bankcard"]

# 提现表单
class ToCashForm(forms.ModelForm):
    bankcard = fields.CharField(
        required=True,
        max_length=15,
        min_length=10,
        label='银行卡号',
        help_text='请确认的您的银行账户',
        error_messages={
            'required': '银行账户不能为空',
            'invalid': '数据格式不正确',
        },
        widget=forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'true', })
    )
    tcamount = fields.DecimalField(
        required=True,
        max_value=20000000,
        min_value=10,
        decimal_places= 2,
        label="提现金额",
        error_messages={
            'required': '金额不能为空',
            'max_value': '每次最多提现2000元',
            'min_value': '提现订单至少为10元',
            'decimal_places': '金额保留两位小数',
            'invalid': '输入不合规定',
        },
        widget=widgets.NumberInput(attrs={'class': 'form-control', 'placeholder': "每次提现订单不少于¥10"})
    )
    ppassword = fields.CharField(
        required=True,
        max_length=15,
        min_length=6,
        label='交易密码',
        error_messages={'required': '密码不能为空', 'invalid': '输入不合规定'},
        widget=widgets.PasswordInput(attrs={'class': 'form-control', 'value': ''})
    )
    class Meta:
        model = Account
        fields = ["bankcard"]

# 买入股票表单
class BuyOrderForm(forms.ModelForm):
    expectprice = fields.DecimalField(
        required=True,
        max_value=1000,
        min_value=1,
        decimal_places=2,
        label="买入价",
        error_messages={
            'required': '买入价格不能为空',
            'max_value': '请输入合理的买入价格',
            'min_value': '请输入合理的买入价格',
            'decimal_places': '金额保留两位小数',
            'invalid': '请输入不带小数点的整数',
        },
    )
    buynum = fields.IntegerField(
        required=True,
        max_value=5000,
        min_value=50,
        label="买入股票数",
        error_messages={
            'required': '金额不能为空',
            'max_value': '买入不能超过发行的股票数',
            'min_value': '至少买入50股',
            'invalid': '输入不合规定',
        },
    )
    class Meta:
        model = BuyOrder
        fields = "__all__"
        exclude = ["owner", "isSuccess","ordertime","share","remark"]

# 卖出股票表单
class SellOrderForm(forms.ModelForm):
    expectprice = fields.DecimalField(
        required=True,
        max_value=1000,
        min_value=1,
        decimal_places=2,
        label="卖出价",
        error_messages={
            'required': '卖出价格不能为空',
            'max_value': '请输入合理的买入卖出',
            'min_value': '请输入合理的买入卖出',
            'decimal_places': '金额保留两位小数',
            'invalid': '输入不合规定',
        },
    )
    sellnum = fields.IntegerField(
        required=True,
        max_value=5000,
        label="卖出股票数",
        error_messages={
            'required': '金额不能为空',
            'max_value': '卖出不能超过发行的股票数',
            'invalid': '输入不合规定',
        },
    )
    class Meta:
        model = SellOrder
        fields = "__all__"
        exclude = ["owner", "isSuccess","ordertime","share","remark"]