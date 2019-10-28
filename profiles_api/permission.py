from rest_framework import permissions

class updateOwnProfile (permissions.BasePermission):
    """Allow user to edit Own profile """

    def has_object_permission(self, request, view, obj):
        """ Check user is tying to edit their own profile """
        if request.methods in permissions.SAFE_METHODS:
            return True

        return obj.id == request.use.id
