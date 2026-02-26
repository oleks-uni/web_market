from rest_framework.response import Response
from rest_framework.exceptions import ValidationError, NotFound

# from django shortcuts.py
def _get_queryset(klass):
    """
    Return a QuerySet or a Manager.
    Duck typing in action: any class with a `get()` method (for
    get_object_or_404) or a `filter()` method (for get_list_or_404) might do
    the job.
    """
    # If it is a model class or anything else with ._default_manager
    if hasattr(klass, "_default_manager"):
        return klass._default_manager.all()
    return klass


def get_object_or_404(klass, *args, **kwargs):

    queryset = _get_queryset(klass)
    if not hasattr(queryset, "get"):
        raise ValidationError({
            "error": "Cannot procced the request"
        })
    try:
        return queryset.get(*args, **kwargs)
    except queryset.model.DoesNotExist:
        raise NotFound({
            "error": "Not found"
        })