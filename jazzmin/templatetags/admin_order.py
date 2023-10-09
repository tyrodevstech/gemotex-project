from copy import deepcopy

from django.conf import settings
from django.contrib import admin
from django.core.exceptions import ImproperlyConfigured

try:
    from django.urls import resolve, Resolver404
except ModuleNotFoundError:
    # Deprecated since Django 1.10, removed in Django 2.0
    from django.urls.urlresolvers import resolve, Resolver404

try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    # Not required for Django <= 1.9, see:
    # https://docs.djangoproject.com/en/1.10/topics/http/middleware/#upgrading-pre-django-1-10-style-middleware
    MiddlewareMixin = object


class ModelAdminReorder():

    def __init__(self, app_list):
        self.app_list = app_list

        self.config = getattr(settings, 'ADMIN_REORDER', None)
        
        self.models_list = []
        for app in app_list:
            for model in app['models']:
                model['model_name'] = self.get_model_name(
                    app['app_label'], model['object_name'])
                self.models_list.append(model)

    def get_app_list(self):
        ordered_app_list = []
        for app_config in self.config:
            app = self.make_app(app_config)
            if app:
                ordered_app_list.append(app)
        return ordered_app_list

    def make_app(self, app_config):
        if not isinstance(app_config, (dict, str)):
            raise TypeError('ADMIN_REORDER list item must be '
                            'dict or string. Got %s' % repr(app_config))

        if isinstance(app_config, str):
            # Keep original label and models
            return self.find_app(app_config)
        else:
            return self.process_app(app_config)

    def find_app(self, app_label):
        for app in self.app_list:
            if app['app_label'] == app_label:
                return app

    def get_model_name(self, app_name, model_name):
        if '.' not in model_name:
            model_name = '%s.%s' % (app_name, model_name)
        return model_name

    def process_app(self, app_config):
        if 'app' not in app_config:
            raise NameError('ADMIN_REORDER list item must define '
                            'a "app" name. Got %s' % repr(app_config))

        app = self.find_app(app_config['app'])
        if app:
            app = deepcopy(app)
            # Rename app
            if 'label' in app_config:
                app['name'] = app_config['label']

            # Process app models
            if 'models' in app_config:
                models_config = app_config.get('models')
                models = self.process_models(models_config)
                if models:
                    app['models'] = models
                else:
                    return None
            return app

    def process_models(self, models_config):
        if not isinstance(models_config, (dict, list, tuple)):
            raise TypeError('"models" config for ADMIN_REORDER list '
                            'item must be dict or list/tuple. '
                            'Got %s' % repr(models_config))

        ordered_models_list = []
        for model_config in models_config:
            model = None
            if isinstance(model_config, dict):
                model = self.process_model(model_config)
            else:
                model = self.find_model(model_config)

            if model:
                ordered_models_list.append(model)

        return ordered_models_list

    def find_model(self, model_name):
        for model in self.models_list:
            if model['model_name'] == model_name:
                return model

    def process_model(self, model_config):
        # Process model defined as { model: 'model', 'label': 'label' }
        for key in ('model', 'label', ):
            if key not in model_config:
                return
        model = self.find_model(model_config['model'])
        if model:
            model['name'] = model_config['label']
            return model



