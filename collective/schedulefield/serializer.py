# -*- coding: utf-8 -*-
from plone.dexterity.interfaces import IDexterityContent
from collective.schedulefield.schedule import ISchedule
from collective.schedulefield.behavior import IExceptionalClosureContent
from collective.schedulefield.behavior import IExceptionalClosure
from plone.restapi.interfaces import IFieldSerializer
from plone.restapi.serializer.converters import json_compatible
from plone.restapi.serializer.dxfields import DefaultFieldSerializer
from zope.component import adapter
from zope.interface import Interface
from zope.interface import implementer
from zope.schema.interfaces import IField


@adapter(IExceptionalClosure, IExceptionalClosureContent, Interface)
@implementer(IFieldSerializer)
class ExceptionalclosureSerializer(DefaultFieldSerializer):
    """"""
    def __call__(self):
        value = self.get_value()


@adapter(ISchedule, IDexterityContent, Interface)
@implementer(IFieldSerializer)
class MultiScheduleSerializer(DefaultFieldSerializer):
    """"""
    def __call__(self):
        value = self.get_value()