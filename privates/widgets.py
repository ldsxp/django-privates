from typing import Optional, Union

from django.contrib.admin.widgets import AdminFileWidget
from django.core.files.uploadedfile import UploadedFile
from django.db.models.fields.files import FieldFile
from django.urls import reverse


class PrivateFileWidgetMixin:
    def __init__(self, *args, **kwargs):
        self.url_name = kwargs.pop("url_name")
        self.download_allowed = kwargs.pop("download_allowed")
        super().__init__(*args, **kwargs)

    def get_context(
        self, name: str, value: Optional[Union[FieldFile, UploadedFile]], attrs: dict
    ):
        """
        Return value-related substitutions.
        """
        context = super().get_context(name, value, attrs)
        if self.is_initial(value):
            if self.download_allowed:
                context["url"] = reverse(
                    self.url_name, kwargs={"pk": value.instance.pk}
                )
                context["download_allowed"] = True
            else:
                context["url"] = ""
                context["download_allowed"] = False
            context["display_value"] = self.get_display_value(value)
        return context

    def get_display_value(self, value):
        return value


class PrivateFileWidget(PrivateFileWidgetMixin, AdminFileWidget):
    template_name = "admin/widgets/clearable_private_file_input.html"
