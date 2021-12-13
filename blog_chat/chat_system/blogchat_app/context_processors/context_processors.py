from blogchat_app.models import LogoModel,NavbarModel
def header_and_footer(request):
    context = {}
    base_queryset = NavbarModel.objects.all()
    logo_queryset = LogoModel.objects.all()
    context['logo_queryset'] = logo_queryset
    context['base_queryset'] = base_queryset
    return context