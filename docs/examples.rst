Examples
========


.. json:object:: Github Issue
   :showexample:

   Information about a Github issue.

   :property integer id: Github assigned issue ID
   :property url url: direct link to this issue
   :property url repository_url: direct link to the repository that
      this issue lives in
   :property url labels_url: retrieve and manipulate the labels
      associated with this issue
   :property url comments_url: retrieve and manipulate the comments
      associated with this issue
   :property url events_url: retrieve and manipulate the events associated
      with this issue
   :property html_url: HTML formatted information about this issue
   :proptype html_url: url
   :property integer number: raw issue number
   :property string state: current state of the issue
   :property string title: issue title
   :property string body: issue body
   :property user: embedded information about the user that created
      the issue
   :proptype user: :json:object:`Github User`

.. json:object:: Error
   :showexample: yaml

   What a normal JSON error body looks like.

   :property string type:
   :property string title:
   :property integer status:
   :property string detail:
   :property uri instance:

   The semantics of this data type is described in :rfc:`7807`.

.. json:object:: Github User
   :showexample:

   What Github's API thinks a user looks like.

   :property user_name login: the user's unique login
   :property integer id: Github assigned unique user identifier
   :property url avatar_url: url to user's selected avatar image
   :property url gravatar_url: url to the user's gravatar image or
      the empty string

.. http:get:: /

   Fetch a foo!

   :queryparam str id: foo to fetch

   :status 500: something went wrong, body is a :json:object:`Error`
