from users.permissions import AdminPanel


class BaseMixin:
    """
    Base mixin for api tasks
    """

    permission_classes = [AdminPanel]

    @property
    def user(self):
        """
        Retrieve user
        """

        return self.request.user if self.request else None

    @property
    def model(self):
        """
        Retrieve model used in serializer
        """

        return self.serializer_class.Meta.model

    def get_queryset(self):
        """
        Get all objects
        """

        if self.queryset:
            return self.queryset

        return self.model.objects.all()
