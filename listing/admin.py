from listing.models import Group
from listing.models import Hyip
from listing.models import Paysystem
#from listing.models import Comment
from listing.models import Withdrawl
from listing.models import Plan
from django.contrib import admin
from imperavi.admin import ImperaviAdmin

admin.site.register(Group)

class WithdrawlInline(admin.TabularInline):
    model = Withdrawl
    extra = 1

class PlanInline(admin.TabularInline):
    model = Plan
    extra = 1

class HyipAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Info',            {'fields': ['name','group','url',
                            'status', 'rating','withdrawl_type','referral',
                            'RCB','support_email', 'date_start']}),
        ('Logo',            {'fields': ['img']}),
        ('Description',     {'fields': ['description','review']}), 
        ('Paymant',         {'fields': ['workday','withdrawl_time']}), 
    ]
    list_display = ('name', 'group', 'status', 'Total_Withdraw', 'ROI',
                    'Working_Time')
    list_filter = ['date_added']
    search_fields = ['name']
    date_hierarchy = 'date_added'
    inlines = [PlanInline,WithdrawlInline]


admin.site.register(Hyip, HyipAdmin)
admin.site.register(Paysystem)

class CommentAdmin(ImperaviAdmin):
    pass

#admin.site.register(Comment, CommentAdmin)

class WithdrawlAdmin(admin.ModelAdmin):
	list_display = ('hyip', 'type_paymant', 'summ', 'with_draw', 
                    'bantch', 'comments')
	list_filter = ['with_draw']

admin.site.register(Withdrawl, WithdrawlAdmin)



