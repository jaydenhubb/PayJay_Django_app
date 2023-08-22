from django.db import models
import uuid
from authent.models import User
from shortuuid.django_fields import ShortUUIDField
from django.db.models.signals import post_save



ACCOUNT_STATUS = (
    ("active", "Active"),
    ("in-active", "in-active"),
)
GENDER=(
    ('male','Male'),('female', 'Female')
)
STATE_OF_ORIGIN=(
    ('edo','Edo'),('lagos','Lagos')
)
TYPE_OF_ID=(
    ('national id card','National ID Card'),("passport","Passport"), ("drivers_license","Drivers License")
)
# Create your models here.
def user_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '%s_%s_' % (instance.id, ext)
    return "user_{0}/{1}".format(instance.user.id, filename)


class Account(models.Model):
    id= models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_balance= models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    account_number = ShortUUIDField(unique=True, length=10, max_length=25, prefix="419", alphabet= "1234567890")
    account_id = ShortUUIDField(unique=True, length=7, max_length=25, prefix="JAY", alphabet= "1234567890")
    pin_number = ShortUUIDField(unique=True,length=4, max_length=7, alphabet= "1234567890")
    ref_code =ShortUUIDField(unique=True, length=10, max_length=25, alphabet= "abcdefgh1234567890")
    account_status =models.CharField(max_length=100, choices=ACCOUNT_STATUS, default="in-active")
    date = models.DateTimeField(auto_now_add=True)
    kyc_submitted = models.BooleanField(default=False)
    kyc_approved = models.BooleanField(default=False)
    # referred_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True )


    class Meta :
        ordering = ['-date']

    def __str__(self):
        return f"{self.user}"
        


def create_account(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(user=instance)

def save_account(sender, instance, **kwargs):
    instance.account.save()

post_save.connect(create_account, sender=User)
post_save.connect(save_account, sender=User)