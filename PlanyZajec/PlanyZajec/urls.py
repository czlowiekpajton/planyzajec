from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'', include('SubjectList.urls')),
    url(r'^SubjectList/', include('SubjectList.urls')),
    url(r'^AddSubject/', include('AddSubject.urls'))
    # url(r'^$', 'PlanyZajec.views.home', name='home'),
    # url(r'^PlanyZajec/', include('PlanyZajec.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
## JEBAC DZIWKO