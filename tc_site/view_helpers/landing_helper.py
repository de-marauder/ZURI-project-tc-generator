# This file should only be edited by people working on the landing view
# ! If you must change this file inform them or de-marauder

from django.shortcuts import render

def landing_helper(request):
    # Write your logic here
    return render(request, 'tc_site/pages/index.html') # Make sure to return a valid response