from rest_framework.routers import DefaultRouter

from accounts.views.accounts import AccountViewset
from accounts.views.transactions import TransactionViewset

router = DefaultRouter()

router.register(prefix='transactions', viewset=TransactionViewset, basename='transactions')
router.register(prefix='', viewset=AccountViewset, basename='accounts')
