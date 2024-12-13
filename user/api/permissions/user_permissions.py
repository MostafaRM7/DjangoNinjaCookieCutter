def user_list_create_permission(request, *args, **kwargs):
    print(request.user)
    user = request.user
    # return True
    return user.is_staff or user.is_superuser


def user_detail_permission(request, *args, **kwargs):
    user = request.user
    user_id = kwargs.get('user_id')
    return user.is_staff or user.is_superuser or user.id == user_id
