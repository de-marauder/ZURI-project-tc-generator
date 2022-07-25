from django.shortcuts import render

# Helper imports
from .view_helpers.landing_helper import landing_helper
from .view_helpers.signin_helper import signin_helper
from .view_helpers.signup_helper import signup_helper
from .view_helpers.gen_form_helper import gen_form_helper
from .view_helpers.gen_file_helper import gen_file_helper
from .view_helpers.embed_helper import embed_helper
from .view_helpers.download_helper import download_helper
from .view_helpers.share_helper import share_helper
from .view_helpers.export_helper import export_helper

# Create your views here.

def landing (request):
    return landing_helper(request)

def signin (request):
    return signin_helper(request)

def signup (request):
    return signup_helper(request)

def logut (request):
    return signup_helper(request)

def gen_form (request):
    return gen_form_helper(request)

def gen_file (request):
    return gen_file_helper(request)

def embed (request):
    return embed_helper(request)

def download (request):
    return download_helper(request)

def share (request):
    return share_helper(request)

def export (request):
    return export_helper(request)
