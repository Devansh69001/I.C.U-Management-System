from patients.models import Patient

def critical_alerts(request):
    # Only show alerts for authenticated users
    if not request.user.is_authenticated:
        return {'alerts': []}
    
    # Exclude login, registration, and logout paths (handle both with and without trailing slashes)
    ignore_paths = [
        '/login/', '/login', '/accounts/login/', '/accounts/login',
        '/accounts/logout/', '/accounts/logout', '/logout/', '/logout',
        '/register/', '/register', '/accounts/register/', '/accounts/register'
    ]
    
    # Normalize path for comparison (remove trailing slash)
    normalized_path = request.path.rstrip('/') or '/'
    normalized_ignore = [p.rstrip('/') or '/' for p in ignore_paths]
    
    if normalized_path in normalized_ignore:
        return {'alerts': []}
    
    # Fetch critical patients only for authenticated users on allowed pages
    critical = Patient.objects.filter(status__iexact='critical')
    return {'alerts': critical}
