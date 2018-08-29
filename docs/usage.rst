Usage
=====
Before you can use this extension, you need to install the
`sphinx-jsondomain <https://pypi.python.org/pypi/sphinx-jsondomain>`_
Python package and then add the :mod:`sphinxjsondomain` module to
:data:`extensions` list in your Sphinx configuration file (:file:`conf.py`)::

   extensions = ['sphinxjsondomain']

Then you can use the :rst:dir:`json:object` directive to document
your JSON documents.

ReStructuredText Usage
----------------------

.. rst:directive:: .. json:object:: Object Name

   Documents the structure of a JSON document using the name ``Object Name``.
   The description is referenceable using the :rst:role:`json:object` role.
   Each property of the JSON document is described using a separate

   **:property** *[type]* *identifier* **:** *description*
      Documents the property named *identifier*.  The property's type can be
      specified inline or as a separate ``:proptype:`` option.  The type is
      shown in the rendered output and linked if the type is something
      recognizable.  It is also used to generate sample data, if the
      ``:showexample:`` option is included.

   **:property-opt** *[type]* *identifier* **:** *description*
      Same as above, but add an '(optional)' string at the end.

   **:proptype** *identifier* **:** *type*
      Set's the type of the property named *identifier*.  This is
      necessary if you are setting the property type to a hyperlinked
      value (e.g., :rst:role:`json:object` role instance).

   **:propexample** *identifier* **:** *example*
      Set's the example showed when the *showexample* option is enabled.

   **:showexample:**
      If this option is specified, then the rendered output will contain
      a generated example.  The example data is generated using the
      Python `fake-factory`_ library.  See :ref:`recognized_types` for
      more details.

   **:noindex:**
      Do not include this object in the general index.

   **:options** *identifier* **:** *option-list*
      Options are a comma-separated list of values that are rendered in
      italics after the property's description.  The extension does not
      interpret the option values in any way.

      .. note::

         The ``:options:`` option will be used to in the near future
         to enable additional functionality such as adding constraints
         when generating a JSON Schema for types.

.. rst:role:: json:object

   Links to the named :rst:dir:`json:object` directive.

.. _recognized_types:

Recognized Types
----------------
Types are used for two distinct purposes in this extension.  First of all,
they are linked to appropriate documentation.  Secondly, they are used to
generate example snippets if the *:showexample:* option is included.

**uri**, **url** links to the relevant IETF RFC that describes URL
   syntax.  Examples are generated using `faker.providers.internet`_.

**boolean** links to the definition for the Python :class:`bool` type.
   Examples are generated using `faker.providers.python`_.

**string**, **str** links to the definition for the Python :class:`str`
   type.  Examples are generated using `faker.providers.python`_.

**integer**, **int** links to the definition for the Python :class:`int`
   type.  Examples are generated using `faker.providers.python`_.

**float**, **number** links to the definition for the Python :class:`float`
   type.  Examples are generated using `faker.providers.python`_.

**null** links to the definition for the Python :data:`None` value.

**email** links to :rfc:`2822` since it is the formal definition of an
   email address.  Examples are generated using `faker.providers.internet`_.

**iso8601** links to :rfc:`3339` since it is a good (and freely available)
   description of the ISO-8601 format.  Examples are generated using
   `faker.providers.date_time`_.

**uuid4** links to :rfc:`4122` since it is the definitive specification
   for UUIDv4 values.  Examples are generated using `faker.providers.misc`_.

**md5** links to :rfc:`1321`.  Examples are generated using
   `faker.providers.misc`_.

**sha1** links to :rfc:`3174`.  Examples are generated using
   `faker.providers.misc`_.

**sha256** links to :rfc:`6234`.  Examples are generated using
   `faker.providers.misc`_.

**user_name** links to the defintion for the Python :class:`str` type.
   Examples are generated using `faker.providers.internet`_.

**[type]** by enclosing any type into [], it indicate a json array.

Example Generation
------------------
As mentioned elsewhere, this extensions uses the `fake-factory`_ library
to generate sample data.  If the "type" of the property is an attribute
of a ``faker.Factory`` instance, then the method is called to generate
the sample value.  Otherwise, the extension will handle integer, float,
boolean, string, and :data:`None` values by calling the appropriate faker
methods.

The other interesting case is the one of embedded objects.  If you set
the property type to a :rst:role:`json:object` reference, then the
documented object is included recursively.  Let's look at a simple
example.

.. code-block:: rst
   :linenos:

   .. json:object:: Contact
      :showexample:

      :property name preferred_name: contact's preferred name in
         correspondance
      :property address: mailing address of contact
      :proptype address: :json:object:`Address`

   .. json:object:: Address
      :showexample:

      :property street_address street: street address for this
         location
      :property city city: city name
      :propexample city: New York
      :property state_abbr state: abbreviated state name
      :property postalcode zip: postal code for this address

And this is the rendered version.  Pay particular attention to the
handling of the ``address`` property.  The property type is specified
using the ``:proptype:`` option so that we can use a link to another
JSON object (e.g., ``:json:object`Address``` on line 7).  The extension
recognizes linked objects and embeds an instance of them in the generated
example.

.. json:object:: Contact
   :showexample:

   :property name preferred_name: contact's preferred name in
      correspondance
   :property address: mailing address of contact
   :proptype address: :json:object:`Address`

.. json:object:: Address
   :showexample:

   :property street_address street: street address for this
      location
   :property city city: city name
   :property state_abbr state: abbreviated state name
   :property postalcode zip: postal code for this address

Index Generation
----------------
:rst:dir:`json:object` directives are added to the general index as
children of the ``JSON Objects`` entry.  You can inhibit this on a
directive-by-directive basis by including the ``:noindex:`` option.

.. _fake-factory: http://fake-factory.readthedocs.io/en/latest/
.. _faker.providers.date_time: http://fake-factory.readthedocs.io/en/latest
   /providers/faker.providers.date_time.html
.. _faker.providers.internet: http://fake-factory.readthedocs.io/en/latest
   /providers/faker.providers.internet.html
.. _faker.providers.misc: http://fake-factory.readthedocs.io/en/latest
   /providers/faker.providers.misc.html
.. _faker.providers.python: http://fake-factory.readthedocs.io/en/latest
   /providers/faker.providers.python.html
