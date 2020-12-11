# Copyright 2023 Clivern
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.utils.translation import gettext as _

from app.exceptions.access_forbidden import AccessForbidden


def stop_request_if_authenticated(function):
    def wrap(controller, request, *args, **kwargs):
        if request.user and request.user.is_authenticated:
            raise AccessForbidden(_("Error! Access forbidden for authenticated users."))
        return function(controller, request, *args, **kwargs)
    return wrap


def prevent_if_not_authenticated(function):
    def wrap(controller, request, *args, **kwargs):
        if not request.user or not request.user.is_authenticated:
            raise AccessForbidden(_("Oops! Access forbidden."))
        return function(controller, request, *args, **kwargs)
    return wrap


def push_metric(metric, count):
    def wrapper(function):
        def wrap(controller, request, *args, **kwargs):
            return function(controller, request, *args, **kwargs)
        return wrap
    return wrapper
