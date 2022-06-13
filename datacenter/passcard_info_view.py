from datacenter.models import Passcard, Visit, get_duration, format_duration, verify_visit, get_active_visit_duration
from django.shortcuts import render


def passcard_info_view(request, passcode):
    
    passcard = Passcard.objects.get(passcode=passcode)
    passcard_visits = Visit.objects.filter(passcard=passcard)
    serialized_passcard_visits = []
    
    for visit in passcard_visits:
        duration_in_seconds = get_duration(visit)
        if duration_in_seconds is None:
            duration_in_seconds = get_active_visit_duration(visit)
        duration = format_duration(int(duration_in_seconds))
        is_strange = verify_visit(duration_in_seconds)
        this_passcard_visit = {
                'entered_at': visit.entered_at,
                'duration': duration,
                'is_strange': is_strange
        }
        serialized_passcard_visits.append(this_passcard_visit)
        
    context = {
        'passcard': passcard,
        'this_passcard_visits': serialized_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
