from django.views.generic.simple import direct_to_template

def template_path(request, path=None, template="prd/index.html"):

    if path is not None:
        template = "prd/" + path

    return direct_to_template(request, template)

