# Sphinx JSON Domain

![https://pypi.python.org/pypi/sphinx-jsondomain](https://img.shields.io/pypi/v/sphinx-jsondomain.svg?maxAge=2592000)
![http://sphinx-jsondomain.readthedocs.io/en/latest/?badge=latest](https://readthedocs.org/projects/sphinx-jsondomain/badge/?version=latest)
![https://travis-ci.org/dave-shawley/sphinx-jsondomain](https://travis-ci.org/dave-shawley/sphinx-jsondomain.svg?branch=master)

> I was surprised that this didn't already exist somewhere when I wanted to
> describe a JSON document outside of using [sphinxcontrib-httpdomain](https://pythonhosted.org/sphinxcontrib-httpdomain/)
> to document one of my APIs.  This extension simplifies describing structured
> JSON documents using a new [Sphinx domain](http://www.sphinx-doc.org/en/stable/domains.html#what-is-a-domain).
>
> -- [Dave Shawley](mailto:daveshawley@gmail.com)

```rst
   .. json:object:: Github User

      What Github's API thinks a user looks like.

      :property string login: the user's login
      :property integer id: Github assigned unique user identifier
      :property string avatar_url: url to user's selected avatar image
         or the empty string
      :property string gravatar_url: url to the user's gravatar image
         or the empty string
```

This will format to something pretty and make references to the JSON object work as expected.

```rst
:json:object:`Github User`
```

See the [online examples](https://sphinx-jsondomain.readthedocs.io/en/latest/examples.html)
for a better idea of what is possible.

## Quick Start

Install sphinx and the ``sphinx-jsondomain`` package with [Pipenv](https://pipenv.pypa.io/en/latest/index.html).

```sh
pipenv install
pipenv shell
```

### Documentation

1. Set up the sphinx documentation root and build your documentation set.

   ```sh
   sphinx-quickstart
   sphinx-build docs docs/_build/html
   ```

2. Add `sphinxjsondomain` to the list of extensions in your configuration file.
3. Add an object directive to one of your source files and run `sphinx-build` again to see the results.

   ```rst
   .. json:object:: GitHub
   ```
