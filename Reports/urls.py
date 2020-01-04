from django.urls import path
from . import views


urlpatterns = [

    #path('create/',views.create_report,name='sdvx' ),
    path('create-report/',views.create_report,name='sdvdvx' ),
    path('generate-report/',views.FilterDetails ,name='sd4545dvx' ),
    path('quarterlly-create-report/',views.QFull_Summary_Generate,name='sdrgdvxyy' ),

    path('quarterlly-report/<int:id>/',views.Q_ReportDetails,name='qdetail' ),
    path('search-reports/',views.SearchFormView,name='gdvx' ),
    path('myactivities/',views.myActivitiesView),
    path('filter-by-topic/',views.FilterTopicDetails),
    path('filter-by-topic-me/',views.FilterTopicByMe),
    path('all-activities/',views.Activities),
    path('filter-by-spoc-consultant/',views.FilterByConsultant),
    path('search-subject-topic/',views.FilterBySubjectDocType),
    path('search-subject-topic-me/',views.FilterBySubjectDocTypeByMe),
    path('search-reports-bank-date-range-me/',views.SearchFormViewByMe ),
    path('quarterlly-reports/',views.QReportList ),

    


]

