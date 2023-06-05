from .generator_services import generate_password


def home_view(request):
    """Main page"""
    return generate_password(
        request=request,
        template='generator/home.html',
        render_data={
            'title': 'SPG | Simple Password Generator',
            'password': None,
        },
    )
