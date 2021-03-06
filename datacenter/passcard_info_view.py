from django.shortcuts import render

from datacenter.models import (Passcard, Visit, format_duration, get_duration,
                               verify_visit)


def passcard_info_view(request, passcode):
    
    passcard = Passcard.objects.get(passcode=passcode)
    passcard_visits = Visit.objects.filter(passcard=passcard)
    serialized_passcard_visits = []
    
    for visit in passcard_visits:
        duration_in_seconds = get_duration(visit)
        duration = format_duration(duration_in_seconds)
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
