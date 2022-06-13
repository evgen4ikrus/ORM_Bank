from datacenter.models import Passcard, Visit, get_duration, format_duration, verify_visit
from django.shortcuts import render


def storage_information_view(request):
    
    non_closed_visits = []
    active_visits = Visit.objects.filter(leaved_at=None)
    
    for active_visit in active_visits:
        duration_in_seconds = get_duration(active_visit)
        visit_duration = format_duration(duration_in_seconds)
        is_strange = verify_visit(duration_in_seconds)
        non_closed_visit = {
                'who_entered': active_visit.passcard.owner_name,
                'entered_at': active_visit.entered_at,
                'duration': visit_duration,
                'is_strange': is_strange
        }
        non_closed_visits.append(non_closed_visit)
        
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
