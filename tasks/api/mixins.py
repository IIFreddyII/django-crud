from base.mixins import BaseMixin


class TaskMixin(BaseMixin):
    """
    Task mixin
    """

    def perform_create(self, serializer):
        """
        When saving serializer add user to data
        if model needs it
        """

        serializer.save(author=self.user)

    def get_queryset(self):
        """
        Get all objects
        """

        if self.queryset:
            return self.queryset

        return self.model.objects.filter(author=self.user)
