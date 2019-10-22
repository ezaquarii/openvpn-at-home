from django.conf import settings
from rest_framework import serializers

from .models import Settings, BlockListUrl


class SettingsSerializer(serializers.ModelSerializer):

    email_from = serializers.SerializerMethodField()
    email_smtp_server = serializers.SerializerMethodField()
    email_smtp_port = serializers.SerializerMethodField()
    email_smtp_login = serializers.SerializerMethodField()
    email_smtp_password = serializers.SerializerMethodField()
    client_config_file_extension_choices = serializers.SerializerMethodField()
    server_config_file_extension_choices = serializers.SerializerMethodField()

    class Meta:
        model = Settings
        fields = ('client_config_file_extension_choices',
                  'server_config_file_extension_choices',
                  'email_enabled',
                  'client_config_file_extension',
                  'server_config_file_extension',
                  'registration_enabled',
                  'email_from',
                  'email_smtp_server',
                  'email_smtp_port',
                  'email_smtp_login',
                  'email_smtp_password')

    def get_email_from(self, instance):
        return settings.SERVER_EMAIL

    def get_email_smtp_server(self, instance):
        return settings.EMAIL_HOST

    def get_email_smtp_port(self, instance):
        return settings.EMAIL_PORT

    def get_email_smtp_login(self, instance):
        return settings.EMAIL_HOST_USER

    def get_email_smtp_password(self, instance):
        return 'hidden'

    def serialize_choices(self, FILE_EXTENSION_CHOICES):
        serialized_choices = []
        for choice in FILE_EXTENSION_CHOICES:
            serialized_choices.append({'value': choice[0], 'name': choice[1]})

        return serialized_choices

    def get_client_config_file_extension_choices(self, instance):
        return self.serialize_choices(Settings.CLIENT_FILE_EXTENSION_CHOICES)

    def get_server_config_file_extension_choices(self, instance):
        return self.serialize_choices(Settings.SERVER_FILE_EXTENSION_CHOICES)


class BlockListUrlUpdateSerializer(serializers.ModelSerializer):
    """
    This serializer optionally validates id field, which is required
    to match model instances with update data, when performing
    bulk updates.

    Undesired side effect of id validation is that it is writable, but
    it is DRF limitation.
    """
    class Meta:
        model = BlockListUrl
        fields = ('id', 'enabled')

    def __init__(self, *args, **kwargs):
        """
        :param args: passed to super constructor
        :param kwargs: passed to super constructor
        :param require_id: If true, serializer id field writable and validated
        """
        self.__require_id = kwargs.pop('require_id', False)
        super().__init__(*args, **kwargs)
        if self.__require_id and 'id' in self.fields:
            self.fields['id'].read_only = False
            self.fields['id'].required = True

    def update(self, instance, validated_data):
        if self.__require_id:
            raise RuntimeError("You should not update when id is enabled")
        return super().update(instance, validated_data)


class BlockListUrlSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlockListUrl
        fields = '__all__'
