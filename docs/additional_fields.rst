Additional Fields
=================

This page describes the format of the output returned by the ``additionalfields`` CLI command and Python API.

The output format is a JSON object in which each key is the JSON path of the additional field. The value of each key is an object with the following properties:

* ``count`` (``number``): The number of occurrences of the additional field.
* ``examples`` (``array`` of ``string``, ``number``, ``boolean`` or ``null``): The values of the first three occurrences of the additional field.
* ``root_additional_field`` (``boolean``): Whether the additional field's parent is an OFDS field.
* ``additional_field_descendance`` (``object``): An object in which each key is the JSON path of a child of the additional field and the value of each key is an object describing the child with the properties described on this page.
* ``path`` (``string``): The JSON path to the parent of the additional field.
* ``field_name`` (``string``): The name of the additional field.
