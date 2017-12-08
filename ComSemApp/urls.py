from django.conf.urls import url

from . import views, admin_views, teacher_views, student_views, corpus_views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^initiate_roles/$', views.initiate_roles, name='initiate_roles'),

    # ADMIN
    url(r'^admin/$', admin_views.admin, name='admin'),

    # TEACHER
    url(r'^teacher/$', teacher_views.teacher, name='teacher'),
    url(r'^teacher/course/([0-9]+)/$', teacher_views.teacher_course, name='teacher_course'),
    url(r'^teacher/course/([0-9]+)/worksheet/([0-9]+)/$', teacher_views.teacher_worksheet, name='teacher_worksheet'),

    url(r'^ajax/course_students/$', teacher_views.course_students, name='course_students'),
    url(r'^ajax/save_worksheet/$', teacher_views.save_worksheet, name='save_worksheet'),
    url(r'^ajax/delete_worksheet/$', teacher_views.delete_worksheet, name='delete_worksheet'),
    url(r'^ajax/release_worksheet/$', teacher_views.release_worksheet, name='release_worksheet'),

    # STUDENT
    url(r'^student/$', student_views.student, name='student'),

    # CORPUS
    url(r'^corpus/$', corpus_views.corpus_search, name='corpus_search'),
    url(r'^ajax/populate_word_tag/$', corpus_views.populate_word_tag, name='populate_word_tag'),
    url(r'^ajax/search_results/$', corpus_views.search_results, name='search_results'),
]
