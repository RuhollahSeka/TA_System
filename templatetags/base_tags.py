from django import template

register = template.Library()


@register.inclusion_tag('account/partials/active_navbar.html')
def active_link(request, link_name, content, classes):
    return {
        "request": request,
        "link_name": link_name,
        "link": f"account:{link_name}",
        "content": content,
        "classes": classes,
    }


@register.inclusion_tag('account/partials/simple-form.html')
def simple_form(form, card_title):
    return {
        "form": form,
        "card_title": card_title,
    }


@register.inclusion_tag('account/partials/modal.html')
def create_modal(modal_type, object, action_url, form=None):
    if modal_type == 'Update' or modal_type == 'Create':
        assert form is not None
    return {
        "modal_type": modal_type,
        'object': None if isinstance(object, str) else object,
        'action_url': action_url,
        'form': form
    }
