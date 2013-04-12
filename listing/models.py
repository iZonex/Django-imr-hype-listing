from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.db.models import Avg
from django.db.models import Sum
import datetime
import time
import urllib2
from time import gmtime,strftime
from django.utils import timezone
import pywhois
from datetime import timedelta
from django.utils.timezone import utc

class Group(models.Model):
    group_name = models.CharField(max_length=200, verbose_name=_('name'))
    GROUP_TYPE = (
        ('41', 'UserListing'),
        ('42', 'OurListing'),
        ('43', 'AutoAdded'),
        ('44', 'NoListing'),
        )
    group_type = models.CharField(max_length=200, choices=GROUP_TYPE, 
                                  verbose_name=_('type'))
    GROUP_SORTING = (
        ('31', 'Rating'),
        ('32', 'Votes'),
        ('33', 'Payout Ratio'),
        ('34', 'Date Added'),
        ('35', 'Date Start'),
        ('36', 'In Traffic'),
        ('37', 'Out Traffic'),
        ('38', 'Traffic Ratio'),
        ('39', 'Listing name'),
        )
    group_sorting = models.CharField(max_length=200, choices=GROUP_SORTING,
                                     verbose_name=_('sorting'))
    group_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('price'))
    group_price_fee = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('price_fee'))
    group_discount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('disscount'))
    def __unicode__(self):
        return self.group_name

class Paysystem(models.Model):
    paysystem_name = models.CharField(max_length=200, verbose_name=_('paysystem_name'))
    paysystem_url = models.CharField(max_length=200, verbose_name=_('paysystem_url'))
    def __unicode__(self):
        return self.paysystem_name

class Hyip(models.Model):
    name = models.CharField(max_length=200, verbose_name=_('name'))
    group = models.ForeignKey(Group, related_name="name", null=True,
                              verbose_name=_('group'))
    url = models.CharField(max_length=200, null=True, blank=True,
                           verbose_name=_('url'))
    img = models.ImageField(upload_to="uploads", null=True, 
                            blank=True, verbose_name=_('img'))
    STATUS = (
        ('10', 'Waiting'),
        ('20', 'Paying'),
        ('30', 'No Paying'),
        ('40', 'Problem'),
        )
    status = models.CharField(max_length=2, choices=STATUS, 
                              verbose_name=_('status'))
    RATING = (
        ('1', 'Risky'),
        ('2', 'Not much Risky'),
        ('3', 'Normal'),
        ('4', 'Good'),
        ('5', 'Fine'),
        ('6', 'No Ranking'),
        )
    rating = models.CharField(max_length=2, choices=RATING, 
                              verbose_name=_('rating'))
    WITHDRAWL_TYPE = (
        ('11', 'Automatic'),
        ('12', 'Manual'),
        ('13', 'Instant'),
        )
    withdrawl_type = models.CharField(max_length=2, choices=WITHDRAWL_TYPE,
                                      verbose_name=_('withdrawl_type'))
    referral = models.CharField(max_length=200, null=True, blank=True,
                                verbose_name=_('referral'))
    RCB = models.CharField(max_length=200, null=True, blank=True, 
                           verbose_name=_('RCB'))
    support_email = models.EmailField(max_length=200, null=True, blank=True,
                                      verbose_name=_('support_email'))
    date_added = models.DateTimeField(default=datetime.datetime.now, 
                                      verbose_name=_('date_added'),auto_now_add=True)
    date_start = models.DateField(verbose_name=_('date_start'))
    description = models.TextField(help_text=('Description information about HYIP Project.'),
                                   null=True, blank=True, verbose_name=_('description'))
    review = models.TextField(help_text=('Our review this HYIP Project.'), 
                              null=True, blank=True, verbose_name=_('review'))
    workday = models.CharField(max_length=200, verbose_name=_('workday'))
    withdrawl_time = models.CharField(max_length=200, verbose_name=_('withdrawl_time'))
    
    def Total_Withdraw(self):
        x = self.withdrawl_set.filter(type_paymant='84')
        return x.aggregate(Sum('summ'))['summ__sum']
    
    def Total_Invest(self):
        x = self.withdrawl_set.filter(type_paymant='83')
        return x.aggregate(Sum('summ'))['summ__sum']
    
    def Working_Time(self):
        if self.date_start == None:
            raise ValueError
        return (datetime.date.today() - self.date_start).days # pokazatb chasi esli menshe dnya

    def New_status(self):
        New_status = (datetime.date.today() - self.date_start).days
        if New_status <= 4: #Dopisat Stroky v grupu, i dat vozmognostb menyat status.
            return "[ New ]"
        return

    def Day_start(self):
        '''Show name of week day, when start Hyip Project'''
        return self.date_start.strftime("%A")

    def ROI(self):
        roi_withdraw = self.withdrawl_set.filter(type_paymant='84')
        all_withdraw = roi_withdraw.aggregate(Sum('summ'))['summ__sum']
        roi_invest = self.withdrawl_set.filter(type_paymant='83')
        all_invest = roi_invest.aggregate(Sum('summ'))['summ__sum']
        if all_withdraw >= 1 and all_invest >= 1:
            x = (all_withdraw * 100) / all_invest
            return '%.2f' % x
        else:
            return 0

    def check_online(self):
        check_result = "Offline"
        try:
            connection = urllib2.urlopen(self.url, timeout=1)
            connection.close()
        except (urllib2.URLError), e:
            pass
        else:
            check_result = "Online"
        now = datetime.datetime.now().strftime('%c')
        return "{0} {1}".format(check_result, now)

    def expiration(self):
        return pywhois.whois(self.url).expiration_date

    def admin_email(self):
        return pywhois.whois(self.url).emails

    #def Show_Paysystem(self):
    #    paysystem_withdraw = self.withdrawl_set.filter()
    #    return paysystem_withdraw('paysystems')['paysystems__paysystems']

    def status_hyip(self):
        # status_hyip
        date_invest = self.withdrawl_set.values('summ').filter(type_paymant='83').latest('with_draw')['summ']
        x_withdraw = self.withdrawl_set.filter(type_paymant='84')
        withdraw = x_withdraw.values('summ')['summ']
        date_withdrawl = self.withdrawl_set.values('with_draw').filter(type_paymant='84').latest('with_draw')['with_draw']
        x_invest = self.withdrawl_set.filter(type_paymant='83')
        invest = x_invest.values('summ')['summ']
        date_invest = self.withdrawl_set.values('with_draw').filter(type_paymant='83').latest('with_draw')['with_draw']
        timenow = datetime.datetime.utcnow().replace(tzinfo=utc)
        constanttime = 1
        #timewite = timedelta(days=self.withdrawl_time + constanttime) 
        timewite = timedelta(days=1)
        scamwite = timedelta(days=2)
        #scamwite = timedelta(days=constanttime + (self.withdrawl_time * 2))
        if invest > 0 and withdraw <= 0:
            if date_invest + scamwite < timenow:
                return 'Scam'
            elif date_invest + timewite < timenow:
                return 'No Paying'
            else:
                return 'Waiting'
        elif invest >= 0 and withdraw > 0:
            if date_withdrawl + scamwite < timenow:
                return 'Scam'
            elif date_withdrawl + timewite < timenow:
                return 'Problem'
            else:
                return 'Paying'
        else:
            return 'No Monitoring'

    def Show_status(self):
        return self.get_status_display()

    def Show_rating(self):
        return self.get_rating_display()

    def Show_withdrawl_type(self):
        return self.get_withdrawl_type_display()

    def get_test(self):
        x = self.withdrawl_set.filter(type_paymant='83')
        if x.values('summ') == None:
            return x.values('summ')['summ_summ']
        else:
            return x.values('summ')['summ_summ']

    def __unicode__(self):
    	return self.name

class Plan(models.Model):
    hyip = models.ForeignKey(Hyip)
    name = models.CharField(max_length=15, verbose_name=_('Name'))
    term = models.CharField(max_length=15, verbose_name=_('Term'))
    withdrawl = models.CharField(max_length=15, verbose_name=_('Withdrawl'))
    min_invest = models.CharField(max_length=15, verbose_name=_('Minimal'))
    max_invest = models.CharField(max_length=15, verbose_name=_('Maximal'))
    profit = models.CharField(max_length=15, verbose_name=_('Total Profit'))
    def __unicode__(self):
        return self.name
    
class Withdrawl(models.Model):
    hyip = models.ForeignKey(Hyip)
    TYPE_PAYMANT = (
        ('81', 'Banner'),
        ('82', 'Listing place'),
        ('83', 'Spend'),
        ('84', 'Payouts'),
        ('85', 'RCB_Back'),
        )
    type_paymant = models.CharField(max_length=3, choices=TYPE_PAYMANT,
                                  verbose_name=_('paylisting'))
    paysystems = models.ForeignKey(Paysystem, related_name="paysystems", null=True)
    account = models.CharField(max_length=15, verbose_name=_('account'))
    bantch = models.CharField(max_length=15, verbose_name=_('bantch'))
    with_draw = models.DateTimeField(default=datetime.datetime.now,
                                     verbose_name=_('with_draw'))
    summ = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('summ'))
    comments = models.CharField(max_length=200, verbose_name=_('comments'))

    def Show_TypePamant(self):
        return self.get_type_paymant_display()
    
    def __unicode__(self):
        return self.bantch

#class Comment(models.Model):
#	user = models.CharField(max_length=200, verbose_name=_('user'))
#    ucomments = models.TextField(help_text=('User comments'),null=True, blank=True, verbose_name=_('ucomments'))
#	rating = models.CharField(max_length=200, verbose_name=_('rating'))
#	hyip_name = models.CharField(max_length=200, verbose_name=_('hyip_name'))
#	def __unicode__(self):
#		return self.ucomments
#
