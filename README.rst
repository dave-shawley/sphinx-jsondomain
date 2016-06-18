Sphinx JSON Domain
==================
I was surprised that this didn't already exist somewhere when I wanted to
describe a JSON document outside of using `sphinxcontrib-httpdomain`_ to
document one of my APIs.  This extension simplifies describing structured
JSON documents using a new `Sphinx domain`_.

.. code-block:: rst

   .. json:object:: Github User

      What Github's API thinks a user looks like.

      :property string login: the user's login
      :property integer id: Github assigned unique user identifier
      :property string avatar_url: url to user's selected avatar image
         or the empty string
      :property string gravatar_url: url to the user's gravatar image
         or the empty string

This will format to something pretty and make references to
`:json:object:`Github User`` work as expected.

.. _sphinxcontrib-httpdomain: https://pythonhosted.org/sphinxcontrib-httpdomain/
.. _sphinx domain: http://www.sphinx-doc.org/en/stable/domains.html#what-is-a-domain
