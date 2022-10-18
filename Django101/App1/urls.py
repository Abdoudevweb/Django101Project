from django.urls import path
from . import views
import App1.views


urlpatterns = [path('', App1.views.homme),
               path('FAQ/', App1.views.faq),
               path('Actu/', App1.views.actu),
               path('prof/', App1.views.show_prof),
               path('module/', App1.views.show_module),
               path('siq/', App1.views.show_sqi),
               path('isil/', App1.views.show_isil)

               ]
