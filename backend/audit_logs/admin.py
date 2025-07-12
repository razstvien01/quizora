from django.contrib import admin
from audit_logs.models import AuditLog

admin.site.register(AuditLog)