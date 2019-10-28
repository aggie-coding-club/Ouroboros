from django import forms
from django.utils.safestring import mark_safe

from application import models as application_models


class ApplicationModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["agree_to_coc"].label = mark_safe(
            'I agree to the <a href="https://static.mlh.io/docs/mlh-code-of-conduct.pdf">MLH Code of Conduct</a>'
        )

        # HACK: Disable the form if there's not an active wave
        if not application_models.Wave.objects.active_wave():
            for field_name in self.fields.keys():
                self.fields[field_name].widget.attrs["disabled"] = "disabled"

    def is_valid(self) -> bool:
        """
        Checks to ensure that a wave is currently active.
        """
        if not application_models.Wave.objects.active_wave():
            self.add_error(
                None,
                "Applications may only be submitted during an active registration wave.",
            )
        return super().is_valid()

    class Meta:
        model = application_models.Application
        widgets = {
            "is_adult": forms.CheckboxInput,
            "agree_to_coc": forms.CheckboxInput,
            "extra_links": forms.TextInput(
                attrs={
                    "placeholder": "ex. GitHub, Devpost, personal website, LinkedIn, etc."
                }
            ),
        }
        fields = [
            "first_name",
            "last_name",
            "major",
            "classification",
            "grad_term",
            "gender",
            "race",
            "num_hackathons_attended",
            "transport_needed",
            "resume",
            "extra_links",
            "question1",
            "question2",
            "question3",
            "agree_to_coc",
            "is_adult",
            "additional_accommodations",
            "notes",
        ]
