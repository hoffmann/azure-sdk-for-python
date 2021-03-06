# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class B2BPartnerContent(Model):
    """B2BPartnerContent.

    :param business_identities: The list of partner business identities.
    :type business_identities: list of :class:`BusinessIdentity
     <azure.mgmt.logic.models.BusinessIdentity>`
    """ 

    _attribute_map = {
        'business_identities': {'key': 'businessIdentities', 'type': '[BusinessIdentity]'},
    }

    def __init__(self, business_identities=None):
        self.business_identities = business_identities
