# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: location.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0elocation.proto\x12\x08Location\"\x1b\n\x0bmac_address\x12\x0c\n\x04\x61\x64\x64r\x18\x01 \x01(\x0c\"h\n\x06record\x12\x11\n\ttimestamp\x18\x01 \x02(\r\x12(\n\tradio_mac\x18\x02 \x02(\x0b\x32\x15.Location.mac_address\x12\x10\n\x08rssi_val\x18\x03 \x02(\x05\x12\x0f\n\x07\x63hannel\x18\x04 \x01(\r\"\xb4\x04\n\x0fstream_location\x12\x16\n\x0esta_location_x\x18\x01 \x01(\x02\x12\x16\n\x0esta_location_y\x18\x02 \x01(\x02\x12\x13\n\x0b\x65rror_level\x18\x03 \x01(\r\x12\x1a\n\x12hashed_sta_eth_mac\x18\x07 \x01(\t\x12\x14\n\x0cgeofence_ids\x18\x08 \x03(\t\x12*\n\rloc_algorithm\x18\t \x01(\x0e\x32\x13.Location.algorithm\x12\x11\n\tlongitude\x18\x0b \x01(\x01\x12\x10\n\x08latitude\x18\x0c \x01(\x01\x12\x10\n\x08\x61ltitude\x18\r \x01(\x01\x12(\n\x04unit\x18\x0e \x01(\x0e\x32\x1a.Location.measurement_unit\x12*\n\x0bsta_eth_mac\x18\x0f \x02(\x0b\x32\x15.Location.mac_address\x12\x18\n\x10\x63\x61mpus_id_string\x18\x10 \x01(\t\x12\x1a\n\x12\x62uilding_id_string\x18\x11 \x01(\t\x12\x17\n\x0f\x66loor_id_string\x18\x12 \x01(\t\x12\x43\n\x0btarget_type\x18\x13 \x01(\x0e\x32\x19.Location.target_dev_type:\x13TARGET_TYPE_UNKNOWN\x12\x12\n\nassociated\x18\x14 \x01(\x08\x12&\n\x08\x65rr_code\x18\x15 \x01(\x0e\x32\x14.Location.error_code\x12!\n\x07records\x18\x16 \x03(\x0b\x32\x10.Location.record\"\xe5\x01\n\x16stream_geofence_notify\x12,\n\x0egeofence_event\x18\x01 \x01(\x0e\x32\x14.Location.zone_event\x12\x13\n\x0bgeofence_id\x18\x02 \x01(\x0c\x12\x15\n\rgeofence_name\x18\x03 \x01(\t\x12*\n\x0bsta_eth_mac\x18\x04 \x01(\x0b\x32\x15.Location.mac_address\x12\x12\n\nassociated\x18\x05 \x01(\x08\x12\x15\n\ndwell_time\x18\x06 \x01(\r:\x01\x30\x12\x1a\n\x12hashed_sta_eth_mac\x18\x07 \x01(\t*o\n\x0ftarget_dev_type\x12\x17\n\x13TARGET_TYPE_UNKNOWN\x10\x00\x12\x17\n\x13TARGET_TYPE_STATION\x10\x01\x12\x13\n\x0fTARGET_TYPE_TAG\x10\x02\x12\x15\n\x11TARGET_TYPE_ROGUE\x10\x03*\x94\x01\n\talgorithm\x12\x1b\n\x17\x41LGORITHM_TRIANGULATION\x10\x00\x12\x1a\n\x16\x41LGORITHM_AP_PLACEMENT\x10\x01\x12\x19\n\x15\x41LGORITHM_CALIBRATION\x10\x02\x12\x18\n\x14\x41LGORITHM_ESTIMATION\x10\x03\x12\x19\n\x15\x41LGORITHM_LOW_DENSITY\x10\x04*4\n\x10measurement_unit\x12\n\n\x06METERS\x10\x00\x12\x08\n\x04\x46\x45\x45T\x10\x01\x12\n\n\x06PIXELS\x10\x02*\xf2\x01\n\nerror_code\x12\x17\n\x13\x45RROR_CODE_NO_ERROR\x10\x00\x12\x15\n\x11\x45RROR_CODE_0_RSSI\x10\x01\x12\x1a\n\x16\x45RROR_CODE_ONLY_1_RSSI\x10\x02\x12\x1a\n\x16\x45RROR_CODE_ONLY_2_RSSI\x10\x03\x12\x1b\n\x17\x45RROR_CODE_RSSI_QUALITY\x10\x04\x12!\n\x1d\x45RROR_CODE_RSSI_OLD_TIMESTAMP\x10\x08\x12#\n\x1f\x45RROR_CODE_RSSI_CLOSE_TIMESTAMP\x10\x10\x12\x17\n\x11\x45RROR_CODE_LEGACY\x10\xff\xff?*\'\n\nzone_event\x12\x0b\n\x07ZONE_IN\x10\x00\x12\x0c\n\x08ZONE_OUT\x10\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'location_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_TARGET_DEV_TYPE']._serialized_start=962
  _globals['_TARGET_DEV_TYPE']._serialized_end=1073
  _globals['_ALGORITHM']._serialized_start=1076
  _globals['_ALGORITHM']._serialized_end=1224
  _globals['_MEASUREMENT_UNIT']._serialized_start=1226
  _globals['_MEASUREMENT_UNIT']._serialized_end=1278
  _globals['_ERROR_CODE']._serialized_start=1281
  _globals['_ERROR_CODE']._serialized_end=1523
  _globals['_ZONE_EVENT']._serialized_start=1525
  _globals['_ZONE_EVENT']._serialized_end=1564
  _globals['_MAC_ADDRESS']._serialized_start=28
  _globals['_MAC_ADDRESS']._serialized_end=55
  _globals['_RECORD']._serialized_start=57
  _globals['_RECORD']._serialized_end=161
  _globals['_STREAM_LOCATION']._serialized_start=164
  _globals['_STREAM_LOCATION']._serialized_end=728
  _globals['_STREAM_GEOFENCE_NOTIFY']._serialized_start=731
  _globals['_STREAM_GEOFENCE_NOTIFY']._serialized_end=960
# @@protoc_insertion_point(module_scope)