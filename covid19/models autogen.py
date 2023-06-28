# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Announcements(models.Model):
    body = models.TextField(blank=True, null=True)
    date = models.TextField(blank=True, null=True)
    expire = models.TextField(blank=True, null=True)
    has_expired = models.IntegerField(blank=True, null=True)
    id = models.TextField(primary_key=True, blank=True, null=True)
    launch = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Announcements'


class Areas(models.Model):
    areacode = models.TextField(db_column='areaCode', blank=True, null=True)  # Field name made lowercase.
    areaname = models.TextField(db_column='areaName', blank=True, null=True)  # Field name made lowercase.
    areatype = models.TextField(db_column='areaType', blank=True, null=True)  # Field name made lowercase.
    id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Areas'


class Dates(models.Model):
    date = models.TextField(blank=True, null=True)
    weekending = models.TextField(db_column='weekEnding', blank=True, null=True)  # Field name made lowercase.
    monthending = models.TextField(db_column='monthEnding', blank=True, null=True)  # Field name made lowercase.
    monthname = models.TextField(db_column='monthName', blank=True, null=True)  # Field name made lowercase.
    dayname = models.TextField(db_column='dayName', blank=True, null=True)  # Field name made lowercase.
    year = models.IntegerField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Dates'


class Metricdetails(models.Model):
    category = models.TextField(blank=True, null=True)
    deprecated = models.TextField(blank=True, null=True)
    doc_last_modified = models.TextField(blank=True, null=True)
    metric = models.TextField(blank=True, null=True)
    metric_name = models.TextField(blank=True, null=True)
    tags = models.TextField(blank=True, null=True)
    id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MetricDetails'


class Metrics(models.Model):
    date = models.TextField(blank=True, null=True)
    areacode = models.TextField(db_column='areaCode', blank=True, null=True)  # Field name made lowercase.
    metricvalue = models.TextField(db_column='metricValue', blank=True, null=True)  # Field name made lowercase.
    metriccode = models.TextField(db_column='metricCode', blank=True, null=True)  # Field name made lowercase.
    areatype = models.TextField(db_column='areaType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Metrics'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
