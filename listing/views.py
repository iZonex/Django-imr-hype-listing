from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from listing.models import Group, Hyip,Paysystem, Withdrawl
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    latest_hyip_list = Hyip.objects.all()[:10]
    return render_to_response('index.html', {'hyip': hyip})

def detail(request, name):
    #p = get_object_or_404(Hyip, pk=hyip_id)
    p = Hyip.objects.get(name=name)
    return render_to_response('detail.html', {'hyip': p},
                               context_instance=RequestContext(request))

def premium(request):
    premium_hyip_list = Hyip.objects.all()
    paginator = Paginator(premium_hyip_list, 25) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        hyips = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        hyips = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        hyips = paginator.page(paginator.num_pages)

    return render_to_response('list.html', {"hyips": hyips})