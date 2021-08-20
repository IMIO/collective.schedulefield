# -*- coding: utf-8 -*-

from collective.schedulefield.behavior import IDateRange
from collective.schedulefield.behavior import IExceptionalClosureContent
from collective.schedulefield.behavior import IExceptionalClosureField
from collective.schedulefield.behavior import IMultiScheduledContent
from collective.schedulefield.behavior import IMultiScheduleField
from plone.restapi.interfaces import IFieldSerializer
from plone.restapi.interfaces import IJsonCompatible
from plone.restapi.serializer.converters import json_compatible
from plone.restapi.serializer.dxfields import DefaultFieldSerializer
from zope.component import adapter
from zope.interface import implementer
from zope.interface import Interface


@adapter(IExceptionalClosureField, IExceptionalClosureContent, Interface)
@implementer(IFieldSerializer)
class ExceptionalclosureSerializer(DefaultFieldSerializer):
    """ """

    def __call__(self):
        value = self.get_value()
        if value is None:
            return []
        closures = [json_compatible(v.__dict__) for v in value]
        return json_compatible(closures)


@adapter(IMultiScheduleField, IMultiScheduledContent, Interface)
@implementer(IFieldSerializer)
class MultiScheduleSerializer(DefaultFieldSerializer):
    """ """

    def __call__(self):
        value = self.get_value()
        if value is None:
            return []
        multischedules = [json_compatible(v.__dict__ )for v in value]
        return json_compatible(multischedules)


@adapter(IDateRange)
@implementer(IJsonCompatible)
def daterange_converter(value):
    if value is None:
        return {}
    return {
        "start_date": json_compatible(value.start_date),
        "end_date": json_compatible(value.end_date),
    }
