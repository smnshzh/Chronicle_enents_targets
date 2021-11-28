from .models import Access
from targets.models import TargetAccess

def access(request):
    if request.user.is_authenticated:
        return {"event_access": Access.objects.filter(user=request.user).first(),
                "target_access":TargetAccess.objects.filter(user=request.user).first(),
                }
    else:
        return {"event_access":False,
                "target_access" :False
                }

