# importing path from django.urls
from django.urls import path

# reset password library - provided by django by default
from django.contrib.auth import views as auth_views

# importing views form the views.py file in this directory
from . import views

# from . import views

urlpatterns = [
     # Home page
    path('', views.home, name='home'),

    # user login and logout url - adding the additional account text to the path
    path('account/login', views.login_page, name='login'),
    path('account/logout', views.logout_user, name='logout'),

    # applicant and company registration url
    path('account/applicant-registration', views.applicant_register, name='applicant-register'),
    path('account/company-registration', views.company_register, name='company-register'),

    # applicant feed url
    path('applicant/applicant-feed', views.applicant_feed, name='applicant-feed'),
    path('applicant/search-result', views.search_result, name='search-result'),

    # applicant profile, public profile and company profile url
    path('applicant/applicant-profile/<str:pk>/', views.applicant_profile, name='applicant-profile'),
    path('applicant/applicant-public-profile/<str:pk>', views.applicant_public_profile, name='applicant-public-profile'),
    path('company/company-profile/<str:pk>/', views.company_profile, name='company-profile'),

    # applicant and company profile edit url
    # path('create-resume', create_resume, name='create-resume'),
    path('pdf', views.pdf_view, name='pdf-view'),
    path('applicant/applicant-edit-profile', views.applicant_edit_profile, name='applicant-edit-profile'),
    path('applicant/applicant-add-social', views.applicant_add_social, name='applicant-add-social'),
    path('applicant/applicant-add-phone', views.applicant_add_phone, name='applicant-add-phone'),
    path('applicant/applicant-add-resume', views.applicant_add_resume, name='applicant-add-resume'),
    path('company/company-edit-profile', views.company_edit_profile, name='company-edit-profile'),

    # add, edit, and delete work experience url
    path('applicant/applicant-profile/add-experience', views.add_experience, name='add-experience'),
    path('applicant/applicant-profile/edit-experience/<str:pk>', views.edit_experience, name='edit-experience'),
    path('applicant/applicant-profile/delete-experience/<str:pk>', views.delete_experience, name='delete-experience'),

    # add, edit, and delete education url
    path('applicant/applicant-profile/add-education', views.add_education, name='add-education'),
    path('applicant/applicant-profile/edit-education/<str:pk>', views.edit_education, name='edit-education'),
    path('applicant/applicant-profile/delete-education/<str:pk>', views.delete_education, name='delete-education'),

    # add, edit, and delete skill url
    path('applicant/applicant-profile/add-skill', views.add_skill, name='add-skill'),
    path('applicant/applicant-profile/edit-skill/<str:pk>/', views.edit_skill, name='edit-skill'),
    path('applicant/applicant-profile/delete-skill/<str:pk>/', views.delete_skill, name='delete-skill'),

    # add, edit, and delete language url
    path('applicant/applicant-profile/add-language', views.add_language, name='add-language'),
    path('applicant/applicant-profile/edit-language/<str:pk>/', views.edit_language, name='edit-language'),
    path('applicant/applicant-profile/delete-language/<str:pk>/', views.delete_language, name='delete-language'),

    # add, edit, and delete reference url
    path('applicant/applicant-profile/add-reference', views.add_reference, name='add-reference'),
    path('applicant/applicant-profile/edit-reference/<str:pk>', views.edit_reference, name='edit-reference'),
    path('applicant/applicant-profile/delete-reference/<str:pk>', views.delete_reference, name='delete-reference'),

    # add, edit, and delete award url
    path('applicant/applicant-profile/add-award', views.add_award, name='add-award'),
    path('applicant/applicant-profile/edit-award/<str:pk>', views.edit_award, name='edit-award'),
    path('applicant/applicant-profile/delete-award/<str:pk>', views.delete_award, name='delete-award'),

    # add, edit, and delete preferred job url
    path('applicant/applicant-profile/add-preferred-job', views.add_preferred_job, name='add-preferred-job'),
    path('applicant/applicant-profile/edit-preferred-job/<str:pk>', views.edit_preferred_job, name='edit-preferred-job'),
    path('applicant/applicant-profile/delete-preferred-jobs/<str:pk>', views.delete_preferred_jobs,
         name='delete-preferred-jobs'),

    # utilities
    path('confirm-email-password', views.authentication_view, name='authentication'),
    path('account-settings/<str:pk>/', views.account_settings, name='account-settings'),
    path('deactivation-successful/', views.deactivation_successful_view, name='deactivation-successful'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    # first help is the url pattern, second help is the name of the function in view.py and third help is the referecing name in the templates/ unique identifier
    path('help', help, name='help'),

     # Password reset views
    path('reset-password/',
         auth_views.PasswordResetView.as_view(template_name="user/password-reset.html"),
         name="reset-password"),
    path('reset-password-sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="user/password-reset-sent.html"),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="user/password-reset-form.html"),
         name="password_reset_confirm"),

    path('reset-password-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="user/password-reset-done.html"),
         name="password_reset_complete"),
]
