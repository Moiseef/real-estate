from django.contrib import admin
from .models import Home_articl, Home_slide, Logo, About_articl, About_slide, Title_contact, Call_us, Email_us, Social_us, Contact_form, Product, Image, Subscrib, AboutSlideDown, ReviewMy, News_articl 

# Register your models here.
admin.site.register(Home_articl)
admin.site.register(Home_slide)
admin.site.register(Logo)
admin.site.register(About_articl)
admin.site.register(About_slide)
admin.site.register(AboutSlideDown)
admin.site.register(ReviewMy)
admin.site.register(Title_contact)
admin.site.register(Call_us)
admin.site.register(Email_us)
admin.site.register(Social_us)
admin.site.register(Contact_form)
admin.site.register(Image)
class ProductImageInline(admin.TabularInline):
    model = Image
    extra = 1
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]

@admin.register(Subscrib)
class SubscribAdmin(admin.ModelAdmin):
    list_display = ("email", "date")


admin.site.register(News_articl)