from django.contrib import admin
from .models import Post , comment
from import_export.admin import ImportExportModelAdmin

@admin.register(Post)
class PostImportExport(ImportExportModelAdmin):
    pass
# admin.site.register(Post)

@admin.register(comment)
class CommentImportExport(ImportExportModelAdmin):
    pass
# admin.site.register(comment)