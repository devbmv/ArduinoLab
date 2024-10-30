from django.shortcuts import render


# 404 - Page Not Found
def handler404(request, exception):
    """Error Handler 404 - Page Not Found"""
    return render(request, "404.html", status=404)


# 403 - Forbidden
def handler403(request, exception):
    """Error Handler 403 - Forbidden"""
    return render(request, "403.html", status=403)


# 500 - Internal Server Error
def handler500(request):
    """Error Handler 500 - Internal Server Error"""
    return render(request, "500.html", status=500)


# 400 - Bad Request
def handler400(request, exception):
    """Error Handler 400 - Bad Request"""
    return render(request, "400.html", status=400)
