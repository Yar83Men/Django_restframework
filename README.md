# Django_restframework
#### Приложение Car, APIView, url car/apiview/ список всех авотобилей
#### Приложение Collage, viewsets.ModelViewSet, модель ManyToMany, url collage/
#### Приложение Posts, viewsets.ModelViewSet, модель OneToOneField, url  posts/
#### Приложение Racing, viewsets.ModelViewSet, url racing/
#### /rest-auth/login/ (POST)
#### username
#### email
#### password
#### Returns Token key
##############################
#### /rest-auth/logout/ (POST)
##############################
#### /rest-auth/password/reset/ (POST)
#### email
##############################
#### /rest-auth/password/reset/confirm/ (POST)
#### uid and token are sent in email after calling /rest-auth/password/reset/
#### uid
#### token
#### new_password1
#### new_password2
##############################
#### /rest-auth/password/change/ (POST)
#### new_password1
#### new_password2
#### old_password
##############################
#### /rest-auth/user/ (GET, PUT, PATCH)
#### username
#### first_name
#### last_name
#### Returns pk, username, email, first_name, last_name
##############################
#### Registration
#### /rest-auth/registration/ (POST)
#### username
#### password1
####### password2
#### email
#### /rest-auth/registration/verify-email/ (POST)
#### key
