from django.contrib import admin
from account.models import Account
from authent.models import User
from import_export.admin import ImportExportModelAdmin

# Register your models here.





class AccountAdminModel(ImportExportModelAdmin): 
    list_editable = ['account_status', "account_balance"]
    list_display = ['user', 'account_number', 'account_status', 'account_balance']
    list_filter = ['account_status']

admin.site.register(Account, AccountAdminModel)
# admin.site.register(KYC,KYCAdmin)