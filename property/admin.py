from django.contrib import admin

from .models import Complaint, Flat, Owner


class FlatOwnersInline(admin.TabularInline):
    model = Flat.owners.through
    raw_id_fields = ('owner', 'flat',)


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address',)
    readonly_fields = ['created_at']
    list_display = [
        'address',
        'price',
        'new_building',
        'construction_year',
        'town',
        ]
    list_editable = ['new_building']
    list_filter = ('new_building',)
    raw_id_fields = ('liked_by', 'owners')
    inlines = [
        FlatOwnersInline,
    ]


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ['author', 'flat', 'text']
    raw_id_fields = ('author', 'flat')


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ['name', 'phonenumber', 'owner_pure_phone']
    inlines = [
        FlatOwnersInline,
    ]
