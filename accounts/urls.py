from rest_framework.routers import DefaultRouter

from accounts.views import AccountViewset, TransactionViewset

router = DefaultRouter()

router.register(prefix='transactions', viewset=TransactionViewset, basename='transactions')
router.register(prefix='', viewset=AccountViewset)