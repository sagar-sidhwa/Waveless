from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('home/register/',views.addaefc,name='addaefc'),
    path('admin/',views.admin,name='admin'),
    path('employee/',views.employee,name='employee'),
    path('farmer/',views.farmer,name='farmer'),
    path('customer/',views.customer,name='customer'),
    path('contact/',views.contact,name='contact'),
    path('product/',views.product,name='product'),
    path('orderd/',views.orderd,name='orderd'),
    path('addp/',views.addp,name='addp'),
    path('addc/',views.addc,name='addc'),
    path('productv/',views.productv,name='productv'),

]

'''
    
    path('workerd/',views.workerd,name='workerd'),
    path('employeed/',views.employeed,name='employeed'),
    path('home/register/',views.addaew,name='addaew'),
    path('detailsi/',views.detailsi,name='detailsi'),
    path('home/employeed/detailsi/',views.edetailsi,name='edetailsi'),
    path('uploadi/',views.uploadi,name='uploadi'),
    path('home/detailsi/displayi/',views.displayi,name='displayi'),
    path('home/imaged/',views.imaged,name='imaged'),
'''