from core.models import CompanyInfo


def default(request):
    companyinfo = CompanyInfo.objects.first()
    return {
        'companyinfo': companyinfo,
    }
