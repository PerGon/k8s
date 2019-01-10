#!/usr/bin/env python
# -*- coding: utf-8
from __future__ import absolute_import

import six

from k8s.base import Model
from k8s.fields import Field, ListField, RequiredField
from k8s.models.v1_9.apimachinery.apis.meta.v1 import LabelSelector, ListMeta, ObjectMeta


###############################################################################
# This file is auto-generated! Do not edit!
#
# Codestyle checking is disabled for this file
# flake8: noqa
###############################################################################


class NetworkPolicyPort(Model):
    """
    NetworkPolicyPort describes a port to allow traffic on
    """

    port = Field(six.text_type, alt_type=int)
    protocol = Field(six.text_type)


class IPBlock(Model):
    """
    IPBlock describes a particular CIDR (Ex. '192.168.1.1/24') that is allowed to
    the pods matched by a NetworkPolicySpec's podSelector. The except entry
    describes CIDRs that should not be included within this rule.
    """

    _except = ListField(six.text_type)
    cidr = RequiredField(six.text_type)


class NetworkPolicyPeer(Model):
    """
    NetworkPolicyPeer describes a peer to allow traffic from. Exactly one of its
    fields must be specified.
    """

    ipBlock = Field(IPBlock)
    namespaceSelector = Field(LabelSelector)
    podSelector = Field(LabelSelector)


class NetworkPolicyIngressRule(Model):
    """
    NetworkPolicyIngressRule describes a particular set of traffic that is allowed
    to the pods matched by a NetworkPolicySpec's podSelector. The traffic must
    match both ports and from.
    """

    _from = ListField(NetworkPolicyPeer)
    ports = ListField(NetworkPolicyPort)


class NetworkPolicyEgressRule(Model):
    """
    NetworkPolicyEgressRule describes a particular set of traffic that is allowed
    out of pods matched by a NetworkPolicySpec's podSelector. The traffic must
    match both ports and to. This type is beta-level in 1.8
    """

    ports = ListField(NetworkPolicyPort)
    to = ListField(NetworkPolicyPeer)


class NetworkPolicySpec(Model):
    """
    NetworkPolicySpec provides the specification of a NetworkPolicy
    """

    egress = ListField(NetworkPolicyEgressRule)
    ingress = ListField(NetworkPolicyIngressRule)
    podSelector = RequiredField(LabelSelector)
    policyTypes = ListField(six.text_type)


class NetworkPolicy(Model):
    """
    NetworkPolicy describes what network traffic is allowed for a set of Pods
    """
    class Meta:
        create_url = "/apis/networking.k8s.io/v1/namespaces/{namespace}/networkpolicies"
        delete_url = "/apis/networking.k8s.io/v1/namespaces/{namespace}/networkpolicies/{name}"
        get_url = "/apis/networking.k8s.io/v1/namespaces/{namespace}/networkpolicies/{name}"
        list_all_url = "/apis/networking.k8s.io/v1/networkpolicies"
        list_ns_url = "/apis/networking.k8s.io/v1/namespaces/{namespace}/networkpolicies"
        update_url = "/apis/networking.k8s.io/v1/namespaces/{namespace}/networkpolicies/{name}"
        watch_url = "/apis/networking.k8s.io/v1/watch/namespaces/{namespace}/networkpolicies/{name}"
        watchlist_all_url = "/apis/networking.k8s.io/v1/watch/networkpolicies"
        watchlist_ns_url = "/apis/networking.k8s.io/v1/watch/namespaces/{namespace}/networkpolicies"
    
    apiVersion = Field(six.text_type, "networking.k8s.io/v1")
    kind = Field(six.text_type, "NetworkPolicy")

    metadata = Field(ObjectMeta)
    spec = Field(NetworkPolicySpec)


class NetworkPolicyList(Model):
    """
    NetworkPolicyList is a list of NetworkPolicy objects.
    """
    apiVersion = Field(six.text_type, "networking.k8s.io/v1")
    kind = Field(six.text_type, "NetworkPolicyList")

    items = ListField(NetworkPolicy)
    metadata = Field(ListMeta)
