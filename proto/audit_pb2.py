# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: audit.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0b\x61udit.proto\x12\x05\x41udit\"\x1b\n\x0bmac_address\x12\x0c\n\x04\x61\x64\x64r\x18\x01 \x01(\x0c\"\x99\x01\n\nip_address\x12)\n\x02\x61\x66\x18\x01 \x01(\x0e\x32\x1d.Audit.ip_address.addr_family\x12\x0c\n\x04\x61\x64\x64r\x18\x02 \x01(\x0c\"R\n\x0b\x61\x64\x64r_family\x12\x16\n\x12\x41\x44\x44R_FAMILY_UNSPEC\x10\x00\x12\x14\n\x10\x41\x44\x44R_FAMILY_INET\x10\x01\x12\x15\n\x11\x41\x44\x44R_FAMILY_INET6\x10\x02\"-\n\x06\x63onfig\x12\x0c\n\x04\x64\x61ta\x18\x01 \x02(\t\x12\x15\n\rdetailed_data\x18\x02 \x01(\t\"/\n\x08\x66irmware\x12\x0c\n\x04\x64\x61ta\x18\x01 \x02(\t\x12\x15\n\rdetailed_data\x18\x02 \x01(\t\"8\n\x11\x64\x65vice_management\x12\x0c\n\x04\x64\x61ta\x18\x01 \x02(\t\x12\x15\n\rdetailed_data\x18\x02 \x01(\t\"\xb2\x02\n\raudit_message\x12\x13\n\x0b\x63ustomer_id\x18\x01 \x02(\t\x12\x11\n\ttimestamp\x18\x02 \x02(\r\x12&\n\x07service\x18\x03 \x02(\x0e\x32\x15.Audit.classification\x12\x12\n\ngroup_name\x18\x04 \x02(\t\x12\x0e\n\x06target\x18\x05 \x02(\t\x12$\n\tclient_ip\x18\x06 \x02(\x0b\x32\x11.Audit.ip_address\x12\x10\n\x08username\x18\x07 \x02(\t\x12\"\n\x0b\x63onfig_info\x18\x08 \x01(\x0b\x32\r.Audit.config\x12&\n\rfirmware_info\x18\t \x01(\x0b\x32\x0f.Audit.firmware\x12)\n\x07\x64m_info\x18\x10 \x01(\x0b\x32\x18.Audit.device_management*B\n\x0e\x63lassification\x12\x11\n\rCONFIGURATION\x10\x00\x12\x0c\n\x08\x46IRMWARE\x10\x01\x12\x0f\n\x0b\x44\x45VICE_MGMT\x10\x02')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'audit_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CLASSIFICATION._serialized_start=670
  _CLASSIFICATION._serialized_end=736
  _MAC_ADDRESS._serialized_start=22
  _MAC_ADDRESS._serialized_end=49
  _IP_ADDRESS._serialized_start=52
  _IP_ADDRESS._serialized_end=205
  _IP_ADDRESS_ADDR_FAMILY._serialized_start=123
  _IP_ADDRESS_ADDR_FAMILY._serialized_end=205
  _CONFIG._serialized_start=207
  _CONFIG._serialized_end=252
  _FIRMWARE._serialized_start=254
  _FIRMWARE._serialized_end=301
  _DEVICE_MANAGEMENT._serialized_start=303
  _DEVICE_MANAGEMENT._serialized_end=359
  _AUDIT_MESSAGE._serialized_start=362
  _AUDIT_MESSAGE._serialized_end=668
# @@protoc_insertion_point(module_scope)