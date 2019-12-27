# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: messages.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='messages.proto',
  package='train',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=b'\n\x0emessages.proto\x12\x05train\"*\n\nEvaluation\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x0e\n\x06values\x18\x02 \x03(\x02\"j\n\x05Model\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x16\n\x07version\x18\x03 \x01(\t:\x05\x30.0.1\x12&\n\x0b\x65valuations\x18\x04 \x03(\x0b\x32\x11.train.Evaluation'
)




_EVALUATION = _descriptor.Descriptor(
  name='Evaluation',
  full_name='train.Evaluation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='train.Evaluation.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='values', full_name='train.Evaluation.values', index=1,
      number=2, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=25,
  serialized_end=67,
)


_MODEL = _descriptor.Descriptor(
  name='Model',
  full_name='train.Model',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='train.Model.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='train.Model.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='train.Model.version', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=b"0.0.1".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='evaluations', full_name='train.Model.evaluations', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=69,
  serialized_end=175,
)

_MODEL.fields_by_name['evaluations'].message_type = _EVALUATION
DESCRIPTOR.message_types_by_name['Evaluation'] = _EVALUATION
DESCRIPTOR.message_types_by_name['Model'] = _MODEL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Evaluation = _reflection.GeneratedProtocolMessageType('Evaluation', (_message.Message,), {
  'DESCRIPTOR' : _EVALUATION,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:train.Evaluation)
  })
_sym_db.RegisterMessage(Evaluation)

Model = _reflection.GeneratedProtocolMessageType('Model', (_message.Message,), {
  'DESCRIPTOR' : _MODEL,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:train.Model)
  })
_sym_db.RegisterMessage(Model)


# @@protoc_insertion_point(module_scope)