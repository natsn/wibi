class TitleMixin():
    def __unicode__(self):
        return self.title

class TranslatedModelMixin(object):
    """
    Given a translated model, overwrites the original language with
    the one requested.

    view:      thing.set_language('es')
    template:  {{ thing.attribute }}
    """

    def set_language(self, language_code):
        if language_code == 'en':
            return

        self.language_code = language_code

        for field in self.translated_fields:
            translated_field_key = language_code + '_' + field
            translated_field = getattr(self, translated_field_key)
            setattr(self, field, translated_field)

class HelperMixin(object):
    # Add some helpful but fancy generic properties to your classes.
    @property
    def get_fields(self):
        # return [(field.name, field.value_to_string(self)) for field in self.__class__._meta.fields]
        return [(field.name, field.value_to_string(self)) for field in self._meta.fields]
