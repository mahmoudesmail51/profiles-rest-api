from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """ Allow User to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""


        """ READ ONLY """
        if request.method in permissions.SAFE_METHODS:
            return True

        """ CHECK ON WRITE OPERATIONS """
        return obj.id == request.user.id
