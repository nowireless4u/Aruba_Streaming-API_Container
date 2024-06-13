# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: presence.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0epresence.proto\x12\x08Presence\"\x1b\n\x0bmac_address\x12\x0c\n\x04\x61\x64\x64r\x18\x01 \x02(\x0c\"\x1a\n\nMacAddress\x12\x0c\n\x04\x61\x64\x64r\x18\x01 \x02(\x0c\"\xe2\x01\n\x15presence_client_state\x12\x10\n\x08is_label\x18\x02 \x01(\x08\x12\x10\n\x08label_id\x18\x03 \x01(\x04\x12\x19\n\x11label_category_id\x18\x04 \x01(\x04\x12;\n\x05state\x18\x05 \x01(\x0e\x32,.Presence.presence_client_state.client_state\x12\x15\n\ris_associated\x18\x06 \x01(\x08\"6\n\x0c\x63lient_state\x12\x0c\n\x08passerby\x10\x00\x12\x0b\n\x07visitor\x10\x01\x12\x0b\n\x07\x65ngaged\x10\x02\"Q\n\x0fpa_client_state\x12>\n\x15presence_client_state\x18\x01 \x03(\x0b\x32\x1f.Presence.presence_client_state\"<\n\x12pa_proximity_event\x12&\n\tproximity\x18\x01 \x03(\x0b\x32\x13.Presence.proximity\"\xda\x01\n\tproximity\x12\x11\n\tdevice_id\x18\x01 \x01(\t\x12*\n\x0bsta_eth_mac\x18\x02 \x01(\x0b\x32\x15.Presence.mac_address\x12(\n\tradio_mac\x18\x03 \x01(\x0b\x32\x15.Presence.mac_address\x12\x10\n\x08rssi_val\x18\x04 \x01(\x05\x12\x13\n\x0bnoise_floor\x18\x05 \x01(\r\x12\x12\n\nassociated\x18\x06 \x01(\x08\x12)\n\nap_eth_mac\x18\x07 \x01(\x0b\x32\x15.Presence.mac_address\"-\n\rpa_rssi_event\x12\x1c\n\x04rssi\x18\x01 \x03(\x0b\x32\x0e.Presence.rssi\"\xf1\x01\n\x04rssi\x12*\n\x0bsta_eth_mac\x18\x01 \x01(\x0b\x32\x15.Presence.mac_address\x12(\n\tradio_mac\x18\x02 \x01(\x0b\x32\x15.Presence.mac_address\x12\x10\n\x08rssi_val\x18\x03 \x01(\x05\x12\x13\n\x0bnoise_floor\x18\x04 \x01(\r\x12\x12\n\nassociated\x18\x05 \x01(\x08\x12\r\n\x05is_ap\x18\x06 \x01(\x08\x12\x0b\n\x03\x61ge\x18\x07 \x01(\r\x12\x11\n\tdevice_id\x18\x08 \x01(\t\x12)\n\nap_eth_mac\x18\t \x01(\x0b\x32\x15.Presence.mac_address\"\xe9\x02\n\x0epresence_event\x12\x11\n\ttimestamp\x18\x01 \x02(\x04\x12\x13\n\x0b\x63ustomer_id\x18\x02 \x02(\t\x12\r\n\x05\x65vent\x18\x03 \x02(\t\x12@\n\nevent_type\x18\x04 \x02(\x0e\x32,.Presence.presence_event.presence_event_type\x12\x32\n\x0fpa_client_state\x18\x05 \x01(\x0b\x32\x19.Presence.pa_client_state\x12.\n\rpa_rssi_event\x18\x06 \x01(\x0b\x32\x17.Presence.pa_rssi_event\x12\x38\n\x12pa_proximity_event\x18\x07 \x01(\x0b\x32\x1c.Presence.pa_proximity_event\"@\n\x13presence_event_type\x12\x10\n\x0c\x63lient_state\x10\x00\x12\x08\n\x04rssi\x10\x01\x12\r\n\tproximity\x10\x02')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'presence_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MAC_ADDRESS._serialized_start=28
  _MAC_ADDRESS._serialized_end=55
  _MACADDRESS._serialized_start=57
  _MACADDRESS._serialized_end=83
  _PRESENCE_CLIENT_STATE._serialized_start=86
  _PRESENCE_CLIENT_STATE._serialized_end=312
  _PRESENCE_CLIENT_STATE_CLIENT_STATE._serialized_start=258
  _PRESENCE_CLIENT_STATE_CLIENT_STATE._serialized_end=312
  _PA_CLIENT_STATE._serialized_start=314
  _PA_CLIENT_STATE._serialized_end=395
  _PA_PROXIMITY_EVENT._serialized_start=397
  _PA_PROXIMITY_EVENT._serialized_end=457
  _PROXIMITY._serialized_start=460
  _PROXIMITY._serialized_end=678
  _PA_RSSI_EVENT._serialized_start=680
  _PA_RSSI_EVENT._serialized_end=725
  _RSSI._serialized_start=728
  _RSSI._serialized_end=969
  _PRESENCE_EVENT._serialized_start=972
  _PRESENCE_EVENT._serialized_end=1333
  _PRESENCE_EVENT_PRESENCE_EVENT_TYPE._serialized_start=1269
  _PRESENCE_EVENT_PRESENCE_EVENT_TYPE._serialized_end=1333
# @@protoc_insertion_point(module_scope)