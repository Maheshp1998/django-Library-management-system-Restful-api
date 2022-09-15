from rest_framework import routers
from library.views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('Books', BookView )
router.register('Category',CategoryView)
router.register('Signup', SignupView,basename='test')
router.register('Students',StudentsView)

