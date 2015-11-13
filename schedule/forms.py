from six.moves.builtins import object
from django import forms
from django.utils.translation import ugettext_lazy as _
from schedule.models import Event, Occurrence


forms.DateInput.input_type="date"

forms.TimeInput.input_type="time"

class SpanForm(forms.ModelForm):
    start = forms.DateTimeField(label=_("Incio"),
                                widget=forms.SplitDateTimeWidget)
    end = forms.DateTimeField(label=_("Fin"),
                              widget=forms.SplitDateTimeWidget,
                              help_text=_(u"The end time must be later than start time."))

    def clean(self):
        if 'end' in self.cleaned_data and 'start' in self.cleaned_data:
            if self.cleaned_data['end'] <= self.cleaned_data['start']:
                raise forms.ValidationError(_(u"The end time must be later than start time."))
        return self.cleaned_data


class EventForm(SpanForm):
    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)

    end_recurring_period = forms.DateTimeField(label=_(u"Periodo de Recurrencia"),
                                               help_text=_(u"Esta fecha se ignora si es un evento de una unica ocurrencia"),
                                               required=False)

    class Meta(object):
        model = Event
        exclude = ('creator', 'created_on', 'calendar','end_recurring_period')


class OccurrenceForm(SpanForm):
    class Meta(object):
        model = Occurrence
        exclude = ('original_start', 'original_end', 'event', 'cancelled','end_recurring_period')
