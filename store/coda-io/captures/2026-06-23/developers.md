<!--
source_url: https://coda.io/developers
captured: 2026-06-23
-->

[![Coda API](https://cdn.coda.io/external/img/apilogo.png)](https://coda.io/developers/apis/v1#)

- Introduction
- Getting Started
- Changes to the API
- Using the API
  - API Endpoint
  - Resource IDs and Links
  - Rate Limiting
  - Consistency
  - Volatile Formulas
  - Free and Paid Workspaces
  - Examples
  - OpenAPI/Swagger Spec
  - Client libraries
- Folders
  - Folders
    - getList folders
    - postCreate folder
    - getGet folder
    - patchUpdate folder
    - delDelete folder
- Docs
  - Docs
    - getList available docs
    - postCreate doc
    - getGet info about a doc
    - delDelete doc
    - patchUpdate doc
  - Permissions
    - getGet sharing metadata
    - getList permissions
    - postAdd permission
    - delDelete permission
    - getSearch principals
    - getGet ACL settings
    - patchUpdate ACL settings
  - Publishing
    - getGet doc categories
    - putPublish doc
    - delUnpublish doc
- Doc Structure
  - Pages
    - getList pages
    - postCreate a page
    - getGet a page
    - putUpdate a page
    - delDelete a page
    - getList page content
    - delDelete page content
    - postBegin content export
    - getContent export status
  - Automations
    - postTrigger automation
- Tables and Views
  - Tables
    - getList tables
    - getGet a table
  - Columns
    - getList columns
    - getGet a column
  - Rows
    - getList table rows
    - postInsert/upsert rows
    - delDelete multiple rows
    - getGet a row
    - putUpdate row
    - delDelete row
    - postPush a button
- Formulas & Controls
  - Formulas
    - getList formulas
    - getGet a formula
  - Controls
    - getList controls
    - getGet a control
- Miscellaneous
  - Account
    - getGet user info
  - Analytics
    - getList doc analytics
    - getList page analytics
    - getGet doc analytics summary
    - getList Pack analytics
    - getGet Pack analytics summary
    - getList Pack formula analytics
    - getGet analytics last updated day
  - Miscellaneous
    - getResolve browser link
    - getGet mutation status

[![redocly logo](https://cdn.redoc.ly/redoc/logo-mini.svg)API docs by Redocly](https://redocly.com/redoc/)

# Coda API (1.5.0)

API Support: [help+api@coda.io](mailto:help+api@coda.io)URL: [https://coda.io](https://coda.io/)License: [Coda Developer Terms](https://coda.io/trust/developer)[Terms of Service](https://coda.io/trust/tos)

## [section/Introduction](https://coda.io/developers/apis/v1\#section/Introduction) Introduction

The Coda API is a RESTful API that lets you programmatically interact with Coda docs:

- List and search Coda docs
- Create new docs and copy existing ones
- Share and publish docs
- Discover pages, tables, formulas, and controls
- Read, insert, upsert, update, and delete rows

If you plan to integrate Coda with an AI tool, you may also want to consider using the
[Coda MCP server](https://coda.io/resources/guides/getting_started_with_coda_mcp). It's optimized for LLM usage
patterns and often exposes more granular methods for accessing and modifying data.

## [section/Getting-Started](https://coda.io/developers/apis/v1\#section/Getting-Started) Getting Started

Our [Getting Started Guide](https://coda.io/@oleg/getting-started-guide-coda-api) helps you learn the
basic of working with the API and shows a few ways you can use it. Check it out, and learn how to:

- Read data from Coda tables and write back to them
- Build a one-way sync from one Coda doc to another
- Automate reminders
- Sync your Google Calendar to Coda

## [section/Changes-to-the-API](https://coda.io/developers/apis/v1\#section/Changes-to-the-API) Changes to the API

As we update and release newer versions of the API, we reserve the right to remove
older APIs and functionality with a 3-month deprecation notice. We will post about such changes as well as announce
new features in the [Developers Central](https://community.coda.io/c/developers-central) section of our Community,
and update the [API updates](https://coda.io/api-updates) doc.

## [section/Using-the-API](https://coda.io/developers/apis/v1\#section/Using-the-API) Using the API

Coda's REST API is designed to be straightforward to use. You can use the language and platform of your choice to
make requests. To get a feel for the API, you can also use a tool like [Postman](https://www.getpostman.com/) or
[Insomnia](https://insomnia.rest/).

## [section/Using-the-API/API-Endpoint](https://coda.io/developers/apis/v1\#section/Using-the-API/API-Endpoint) API Endpoint

This API uses a base path of `https://coda.io/apis/v1`.

## [section/Using-the-API/Resource-IDs-and-Links](https://coda.io/developers/apis/v1\#section/Using-the-API/Resource-IDs-and-Links) Resource IDs and Links

Each resource instance retrieved via the API has the following fields:

- `id`: The resource's immutable ID, which can be used to refer to it within its context
- `type`: The type of resource, useful for identifying it in a heterogenous collection of results
- `href`: A fully qualified URI that can be used to refer to and get the latest details on the resource

Most resources can be queried by their name or ID. We recommend sticking with IDs where possible, as names are
fragile and prone to being changed by your doc's users.

### List Endpoints

Endpoints supporting listing of resources have the following fields:

- `items`: An array containing the listed resources, limited by the `limit` or `pageToken` query parameters
- `nextPageLink`: If more results are available, an API link to the next page of results
- `nextPageToken`: If more results are available, a page token that can be passed into the `pageToken` query parameter

**The maximum page size may change at any time, and may be different for different endpoints.** Please do not rely on it
for any behavior of your application. If you pass a `limit` parameter that is larger than our maximum allowed limit,
we will only return as many results as our maximum limit. You should look for the presence of the `nextPageToken` on the
response to see if there are more results available, rather than relying on a result set that matches your provided limit.

To fetch a subsequent page of results, pass the `pageToken` parameter. Set this parameter to the value given to you as the `nextPageToken`
in a page response. If no value is provided, there are no more results available. You only need to pass the `pageToken` to get
the next page of results, you don't need to pass any of the parameters from your original request, as they are all
implied by the `pageToken`. Any other parameters provided alongside a `pageToken` will be ignored.

### Doc IDs

While most object IDs will have to be discovered via the API, you may find yourself frequently wanting to get the
ID of a specific Coda doc.

Here's a handy tool that will extract it for you. (See if you can find the pattern!)

Doc ID Extractor
Your doc ID is:


## [section/Using-the-API/Rate-Limiting](https://coda.io/developers/apis/v1\#section/Using-the-API/Rate-Limiting) Rate Limiting

The Coda API sets a reasonable limit on the number of requests that can be made per minute. Once this limit is
reached, calls to the API will start returning errors with an HTTP status code of 429.

These are the current rate limits. They are subject to change at any time without notice. For robustness,
all API scripts should check for HTTP 429 Too Many Requests errors and back off and retry the request.
Limits apply per-user across all endpoints that share the same limit and across all docs.

Reading data (with the exceptions below): 100 requests per 6 seconds

Writing data (POST/PUT/PATCH): 10 requests per 6 seconds

Writing doc content data (POST/PUT/PATCH): 5 requests per 10 seconds

Listing docs: 4 requests per 6 seconds

Reading analytics: 100 requests per 6 seconds

## [section/Using-the-API/Consistency](https://coda.io/developers/apis/v1\#section/Using-the-API/Consistency) Consistency

While edits made in Coda are shared with other collaborators in real-time, it can take a few seconds for them to
become available via the API. You may also notice that changes made via the API, such as updating a row, are not
immediate. These endpoints all return an HTTP 202 status code, instead of a standard 200, indicating that the
edit has been accepted and queued for processing. This generally takes a few seconds, and the edit may fail if
invalid. Each such edit will return a `requestId` in the response, and you can pass this `requestId` to the
[`#getMutationStatus`](https://coda.io/developers/apis/v1#operation/getMutationStatus) endpoint to find out if it has been applied.

Similarly, when you get doc data from the API (rows, pages, columns, etc), the data you receive comes from
the most recent "snapshot" of the doc, which might be slightly stale relative to the data you observe in
your browser. If you want to ensure that the data you receive is up to date and are ok getting an error if not,
you can pass this header in your request: `X-Coda-Doc-Version: latest`. If the API's view of the doc is
not up to date, the API will return an HTTP 400 response.

## [section/Using-the-API/Volatile-Formulas](https://coda.io/developers/apis/v1\#section/Using-the-API/Volatile-Formulas) Volatile Formulas

Coda exposes a number of "volatile" formulas, as as `Today()`, `Now()`, and `User()`. When used in a live Coda
doc, these formulas affect what's visible in realtime, tailored to the current user.

Such formulas behave differently with the API. Time-based values may only be current to the last edit made to the
doc. User-based values may be blank or invalid.

## [section/Using-the-API/Free-and-Paid-Workspaces](https://coda.io/developers/apis/v1\#section/Using-the-API/Free-and-Paid-Workspaces) Free and Paid Workspaces

We make the Coda API available to all of our users free of charge, in both free and paid workspaces. However, API
usage is subject to the role of the user associated with the API token in the workspace applicable to each API
request. What this means is:

- For the [`#createDoc`](https://coda.io/developers/apis/v1#operation/createDoc) endpoint specifically, the owner of the API token must be a Doc
Maker (or Admin) in the workspace. If the "Any member can create docs" option in enabled in the workspace
settings, they can be an Editor and will get auto-promoted to Doc Maker upon using this endpoint. Lastly, if in
addition, the API key owner matches the "Auto-join email domains" setting, they will be auto-added to the
workspace and promoted to Doc Maker upon using this endpoint

This behavior applies to the API as well as any integrations that may use it, such as Zapier.

## [section/Using-the-API/Examples](https://coda.io/developers/apis/v1\#section/Using-the-API/Examples) Examples

To help you get started, this documentation provides code examples in Python, Unix shell, and Google Apps Script.
These examples are based on a simple doc that looks something like this:

![](https://cdn.coda.io/external/img/api_example_doc.png)

### Python examples

These examples use Python 3.6+. If you don't already have the `requests` module, use `pip` or `easy_install` to
get it.

### Shell examples

The shell examples are intended to be run in a Unix shell. If you're on Windows, you will need to install
[WSL](https://docs.microsoft.com/en-us/windows/wsl/install-win10).

These examples use the standard cURL utility to pull from the API, and then process it with `jq` to extract and
format example output. If you don't already have it, you can either [install it](https://stedolan.github.io/jq/)
or run the command without it to see the raw JSON output.

### Google Apps Script examples

![](https://cdn.coda.io/external/img/api_gas.png)

[Google Apps Script](https://script.google.com/) makes it easy to write code in a JavaScript-like syntax and
easily access many Google products with built-in libraries. You can set up your scripts to run periodically,
which makes it a good environment for writing tools without maintaining your own server.

Coda provides a library for Google Apps Script. To use it, go into `Resources -> Libraries...` and enter the
following library ID: `15IQuWOk8MqT50FDWomh57UqWGH23gjsWVWYFms3ton6L-UHmefYHS9Vl`. If you want to see the
library's source code, it's available
[here](https://script.google.com/d/15IQuWOk8MqT50FDWomh57UqWGH23gjsWVWYFms3ton6L-UHmefYHS9Vl/edit).

Google provides autocomplete for API functions as well as generated docs. You can access these docs via the
Libraries dialog by clicking on the library name. Required parameters that would be included in the URL path are
positional arguments in each of these functions, followed by the request body, if applicable. All remaining
parameters can be specified in the options object.

## [section/Using-the-API/OpenAPISwagger-Spec](https://coda.io/developers/apis/v1\#section/Using-the-API/OpenAPISwagger-Spec) OpenAPI/Swagger Spec

In an effort to standardize our API and make it accessible, we offer an OpenAPI 3.0 specification:

- [OpenAPI 3.0 spec - YAML](https://coda.io/apis/v1/openapi.yaml)
- [OpenAPI 3.0 spec - JSON](https://coda.io/apis/v1/openapi.json)

#### Postman collection

To get started with prototyping the API quickly in Postman, you can use one of links above to import the Coda API
into a collection. You'll then need to set the [appropriate header](https://coda.io/developers/apis/v1#section/Authentication) and environment
variables.

## [section/Using-the-API/Client-libraries](https://coda.io/developers/apis/v1\#section/Using-the-API/Client-libraries) Client libraries

We do not currently support client libraries apart from Google Apps Script. To work with the Coda API, you can
either use standard network libraries for your language, or use the appropriate Swagger Generator tool to
auto-generate Coda API client libraries for your language of choice. We do not provide any guarantees that these
autogenerated libraries are compatible with our API (e.g., some libraries may not work with Bearer
authentication).

### OpenAPI 3.0

[Swagger Generator 3](https://generator3.swagger.io/) (that link takes you to the docs for the generator API) can
generate client libraries for [these languages](https://generator3.swagger.io/v2/clients). It's relatively new
and thus only has support for a limited set of languages at this time.

### Third-party client libraries

Some members of our amazing community have written libraries to work with our API. These aren't officially
supported by Coda, but are listed here for convenience. (Please let us know if you've written a library and would
like to have it included here.)

- [PHP](https://github.com/danielstieber/CodaPHP) by Daniel Stieber
- [Node-RED](https://github.com/serene-water/node-red-contrib-coda-io) by Mori Sugimoto
- [NodeJS](https://www.npmjs.com/package/coda-js) by Parker McMullin
- [Ruby](https://rubygems.org/gems/coda_docs/) by Carlos Muñoz at Getro
- [Python](https://github.com/Blasterai/codaio) by Mikhail Beliansky
- [Go](https://github.com/artsafin/coda-schema-generator) by Artur Safin

## [tag/Folders](https://coda.io/developers/apis/v1\#tag/Folders) Folders

Folders help you organize your docs within workspaces. This API lets you list, create, update, and delete folders.

## [tag/Folders/operation/listFolders](https://coda.io/developers/apis/v1\#tag/Folders/operation/listFolders) List folders

Returns a list of folders the user has access to.

##### Authorizations:

_Bearer_

##### query Parameters

|     |     |
| --- | --- |
| workspaceId | string<br>Example: workspaceId=ws-1Ab234<br>Show only folders belonging to the given workspace. |
| isStarred | boolean<br>If true, returns folders that are starred. If false, returns folders that are not starred. If not specified, returns all folders. |
| limit | integer >= 1 <br>Default: 25<br>Example: limit=10<br>Maximum number of results to return in this query. |
| pageToken | string<br>Example: pageToken=eyJsaW1pd<br>An opaque token used to fetch the next page of results. |

### Responses

**200**

List of folders.

##### Response Schema: application/json

|     |     |
| --- | --- |
| items<br>required | Array of objects (Folder) |
| href | string <url> <br>API link to these results. |
| nextPageToken | string (nextPageToken) <br>If specified, an opaque token used to fetch the next page of results. |
| nextPageLink | string <url> <br>If specified, a link that can be used to fetch the next page of results. |

**400**

The request parameters did not conform to expectations.

**401**

The API token is invalid or has expired.

**403**

The API token does not grant access to this resource.

**429**

The client has sent too many requests.

get/folders

Coda API (v1)

https://coda.io/apis/v1/folders

### Request samples

- Python 3.13
- Shell

Copy

```
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = 'https://coda.io/apis/v1/folders'
res = requests.get(uri, headers=headers).json()

for folder in res['items']:
    print(f'Folder: {folder["name"]}')
```

### Response samples

- 200
- 400
- 401
- 403
- 429

Content type

application/json

Copy
Expand all  Collapse all

`{"items": [{"id": "fl-1Ab234",\
\
"type": "folder",\
\
"name": "Projects",\
\
"browserLink": "https://coda.io/folders/fl-1Ab234",\
\
"description": "A collection of project docs.",\
\
"icon": {"name": "string",\
\
"type": "string",\
\
"browserLink": "https://cdn.coda.io/icons/png/color/icon-32.png"\
\
},\
\
"createdAt": "2018-04-11T00:18:57.946Z",\
\
"canEdit": true,\
\
"workspace": {"id": "ws-1Ab234",\
\
"type": "workspace",\
\
"organizationId": "org-2Bc456",\
\
"browserLink": "https://coda.io/docs?workspaceId=ws-1Ab234",\
\
"name": "My workspace"\
\
}\
\
}\
\
],

"href": "https://coda.io/apis/v1/folders?workspaceId=ws-1Ab234",

"nextPageToken": "eyJsaW1pd",

"nextPageLink": "https://coda.io/apis/v1/folders?pageToken=xyz"

}`

## [tag/Folders/operation/createFolder](https://coda.io/developers/apis/v1\#tag/Folders/operation/createFolder) Create folder

Creates a new folder.

##### Authorizations:

_Bearer_

##### Request Body schema: application/json  required

Parameters for creating the folder.

|     |     |
| --- | --- |
| name<br>required | string<br>Name of the folder. |
| workspaceId<br>required | string<br>ID of the workspace where the folder should be created. |
| description | string<br>Description of the folder. |

### Responses

**201**

The created folder.

##### Response Schema: application/json

|     |     |
| --- | --- |
| id<br>required | string<br>ID of the Coda folder. |
| type<br>required | string<br>Value:"folder"<br>The type of this resource. |
| name<br>required | string<br>The name of the folder. |
| browserLink<br>required | string <url> <br>Browser-friendly link to the folder. |
| workspace<br>required | object (WorkspaceReference) <br>Reference to a Coda workspace. |
| description | string<br>The description of the folder. |
| icon | object (Icon) <br>Info about the icon. |
| createdAt | string <date-time> <br>Timestamp for when the folder was created. |
| canEdit | boolean<br>Whether the folder settings can be edited. E.g., some folder types (like personal folders - "My Docs") cannot be edited. |

**400**

The request parameters did not conform to expectations.

**401**

The API token is invalid or has expired.

**403**

The API token does not grant access to this resource.

**429**

The client has sent too many requests.

post/folders

Coda API (v1)

https://coda.io/apis/v1/folders

### Request samples

- Payload
- Python 3.13
- Shell

Content type

application/json

Copy

`{"name": "Projects",

"workspaceId": "ws-1Ab234",

"description": "A collection of project docs."

}`

### Response samples

- 201
- 400
- 401
- 403
- 429

Content type

application/json

Copy
Expand all  Collapse all

`{"id": "fl-1Ab234",

"type": "folder",

"name": "Projects",

"browserLink": "https://coda.io/folders/fl-1Ab234",

"description": "A collection of project docs.",

"icon": {"name": "string",

"type": "string",

"browserLink": "https://cdn.coda.io/icons/png/color/icon-32.png"

},

"createdAt": "2018-04-11T00:18:57.946Z",

"canEdit": true,

"workspace": {"id": "ws-1Ab234",

"type": "workspace",

"organizationId": "org-2Bc456",

"browserLink": "https://coda.io/docs?workspaceId=ws-1Ab234",

"name": "My workspace"

}

}`

## [tag/Folders/operation/getFolder](https://coda.io/developers/apis/v1\#tag/Folders/operation/getFolder) Get folder

Returns the requested folder.

##### Authorizations:

_Bearer_

##### path Parameters

|     |     |
| --- | --- |
| folderId<br>required | string<br>Example: fl-1Ab234<br>ID of the folder. |

### Responses

**200**

The requested Coda folder.

##### Response Schema: application/json

|     |     |
| --- | --- |
| id<br>required | string<br>ID of the Coda folder. |
| type<br>required | string<br>Value:"folder"<br>The type of this resource. |
| name<br>required | string<br>The name of the folder. |
| browserLink<br>required | string <url> <br>Browser-friendly link to the folder. |
| workspace<br>required | object (WorkspaceReference) <br>Reference to a Coda workspace. |
| description | string<br>The description of the folder. |
| icon | object (Icon) <br>Info about the icon. |
| createdAt | string <date-time> <br>Timestamp for when the folder was created. |
| canEdit | boolean<br>Whether the folder settings can be edited. E.g., some folder types (like personal folders - "My Docs") cannot be edited. |

**400**

The request parameters did not conform to expectations.

**401**

The API token is invalid or has expired.

**403**

The API token does not grant access to this resource.

**404**

The resource could not be located with the current API token.

**429**

The client has sent too many requests.

get/folders/{folderId}

Coda API (v1)

https://coda.io/apis/v1/folders/{folderId}

### Request samples

- Python 3.13
- Shell

Copy

```
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = 'https://coda.io/apis/v1/folders/<your folder id>'
res = requests.get(uri, headers=headers).json()

print(f'Folder name is: {res["name"]}')
```

### Response samples

- 200
- 400
- 401
- 403
- 404
- 429

Content type

application/json

Copy
Expand all  Collapse all

`{"id": "fl-1Ab234",

"type": "folder",

"name": "Projects",

"browserLink": "https://coda.io/folders/fl-1Ab234",

"description": "A collection of project docs.",

"icon": {"name": "string",

"type": "string",

"browserLink": "https://cdn.coda.io/icons/png/color/icon-32.png"

},

"createdAt": "2018-04-11T00:18:57.946Z",

"canEdit": true,

"workspace": {"id": "ws-1Ab234",

"type": "workspace",

"organizationId": "org-2Bc456",

"browserLink": "https://coda.io/docs?workspaceId=ws-1Ab234",

"name": "My workspace"

}

}`

## [tag/Folders/operation/updateFolder](https://coda.io/developers/apis/v1\#tag/Folders/operation/updateFolder) Update folder

Updates metadata for a folder.

##### Authorizations:

_Bearer_

##### path Parameters

|     |     |
| --- | --- |
| folderId<br>required | string<br>Example: fl-1Ab234<br>ID of the folder. |

##### Request Body schema: application/json  required

Parameters for updating the folder.

|     |     |
| --- | --- |
| name | string<br>Name of the folder. |
| description | string<br>Description of the folder. |

### Responses

**200**

The updated folder.

##### Response Schema: application/json

|     |     |
| --- | --- |
| id<br>required | string<br>ID of the Coda folder. |
| type<br>required | string<br>Value:"folder"<br>The type of this resource. |
| name<br>required | string<br>The name of the folder. |
| browserLink<br>required | string <url> <br>Browser-friendly link to the folder. |
| workspace<br>required | object (WorkspaceReference) <br>Reference to a Coda workspace. |
| description | string<br>The description of the folder. |
| icon | object (Icon) <br>Info about the icon. |
| createdAt | string <date-time> <br>Timestamp for when the folder was created. |
| canEdit | boolean<br>Whether the folder settings can be edited. E.g., some folder types (like personal folders - "My Docs") cannot be edited. |

**400**

The request parameters did not conform to expectations.

**401**

The API token is invalid or has expired.

**403**

The API token does not grant access to this resource.

**404**

The resource could not be located with the current API token.

**429**

The client has sent too many requests.

patch/folders/{folderId}

Coda API (v1)

https://coda.io/apis/v1/folders/{folderId}

### Request samples

- Payload
- Python 3.13
- Shell

Content type

application/json

Copy

`{"name": "Projects",

"description": "A collection of project docs."

}`

### Response samples

- 200
- 400
- 401
- 403
- 404
- 429

Content type

application/json

Copy
Expand all  Collapse all

`{"id": "fl-1Ab234",

"type": "folder",

"name": "Projects",

"browserLink": "https://coda.io/folders/fl-1Ab234",

"description": "A collection of project docs.",

"icon": {"name": "string",

"type": "string",

"browserLink": "https://cdn.coda.io/icons/png/color/icon-32.png"

},

"createdAt": "2018-04-11T00:18:57.946Z",

"canEdit": true,

"workspace": {"id": "ws-1Ab234",

"type": "workspace",

"organizationId": "org-2Bc456",

"browserLink": "https://coda.io/docs?workspaceId=ws-1Ab234",

"name": "My workspace"

}

}`

## [tag/Folders/operation/deleteFolder](https://coda.io/developers/apis/v1\#tag/Folders/operation/deleteFolder) Delete folder

Deletes a folder. The folder must be empty (contain no docs).

##### Authorizations:

_Bearer_

##### path Parameters

|     |     |
| --- | --- |
| folderId<br>required | string<br>Example: fl-1Ab234<br>ID of the folder. |

### Responses

**200**

Folder was successfully deleted.

##### Response Schema: application/json

object (DeleteFolderResult)

The result of a folder deletion.

**400**

The request parameters did not conform to expectations.

**401**

The API token is invalid or has expired.

**403**

The API token does not grant access to this resource.

**404**

The resource could not be located with the current API token.

**429**

The client has sent too many requests.

delete/folders/{folderId}

Coda API (v1)

https://coda.io/apis/v1/folders/{folderId}

### Request samples

- Python 3.13
- Shell

Copy

```
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = 'https://coda.io/apis/v1/folders/<your folder id>'
res = requests.delete(uri, headers=headers)

print(f'Deleted: {res.status_code == 200}')
```

### Response samples

- 200
- 400
- 401
- 403
- 404
- 429

Content type

application/json

Copy

`{ }`

## [tag/Docs](https://coda.io/developers/apis/v1\#tag/Docs) Docs

Coda docs are foundational, top-level collaborative projects that contain pages. The API lets you list and search your docs to obtain basic metadata like titles and ownership information.

## [tag/Docs/operation/listDocs](https://coda.io/developers/apis/v1\#tag/Docs/operation/listDocs) List available docs

Returns a list of Coda docs accessible by the user, and which they have opened at least once. These are returned in the same order as on the docs page: reverse chronological by the latest event relevant to the user (last viewed, edited, or shared).

##### Authorizations:

_Bearer_

##### query Parameters

|     |     |
| --- | --- |
| isOwner | boolean<br>Show only docs owned by the user. |
| isPublished | boolean<br>Show only published docs. |
| query | string<br>Example: query=Supercalifragilisticexpialidocious<br>Search term used to filter down results. |
| sourceDoc | string<br>Show only docs copied from the specified doc ID. |
| isStarred | boolean<br>If true, returns docs that are starred. If false, returns docs that are not starred. |
| inGallery | boolean<br>Show only docs visible within the gallery. |
| workspaceId | string<br>Show only docs belonging to the given workspace. |
| folderId | string<br>Show only docs belonging to the given folder. |
| limit | integer >= 1 <br>Default: 25<br>Example: limit=10<br>Maximum number of results to return in this query. |
| pageToken | string<br>Example: pageToken=eyJsaW1pd<br>An opaque token used to fetch the next page of results. |

### Responses

**200**

List of Coda docs matching the query.

##### Response Schema: application/json

|     |     |
| --- | --- |
| items<br>required | Array of objects (Doc) |
| href | string <url> <br>API link to these results |
| nextPageToken | string (nextPageToken) <br>If specified, an opaque token used to fetch the next page of results. |
| nextPageLink | string <url> <br>If specified, a link that can be used to fetch the next page of results. |

**401**

The API token is invalid or has expired.

**403**

The API token does not grant access to this resource.

**404**

The resource could not be located with the current API token.

**429**

The client has sent too many requests.

get/docs

Coda API (v1)

https://coda.io/apis/v1/docs

### Request samples

- Python 3.13
- Shell
- Google Apps Script

Copy

```
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = 'https://coda.io/apis/v1/docs'
params = {
  'isOwner': True,
  'query': 'New',
}
res = requests.get(uri, headers=headers, params=params).json()

print(f'First doc is: {res["items"][0]["name"]}')
# => First doc is: New Document
```

### Response samples

- 200
- 401
- 403
- 404
- 429

Content type

application/json

Copy
Expand all  Collapse all

`{"items": [{"id": "AbCDeFGH",\
\
"type": "doc",\
\
"href": "https://coda.io/apis/v1/docs/AbCDeFGH",\
\
"browserLink": "https://coda.io/d/_dAbCDeFGH",\
\
"icon": {"name": "string",\
\
"type": "string",\
\
"browserLink": "https://cdn.coda.io/icons/png/color/icon-32.png"\
\
},\
\
"name": "Product Launch Hub",\
\
"owner": "user@example.com",\
\
"ownerName": "Some User",\
\
"docSize": {"totalRowCount": 31337,\
\
"tableAndViewCount": 42,\
\
"pageCount": 10,\
\
"overApiSizeLimit": false\
\
},\
\
"sourceDoc": {"id": "AbCDeFGH",\
\
"type": "doc",\
\
"href": "https://coda.io/apis/v1/docs/AbCDeFGH",\
\
"browserLink": "https://coda.io/d/_dAbCDeFGH"\
\
},\
\
"createdAt": "2018-04-11T00:18:57.946Z",\
\
"updatedAt": "2018-04-11T00:18:57.946Z",\
\
"published": {"description": "Hello World!",\
\
"browserLink": "https://coda.io/@coda/hello-world",\
\
"imageLink": "string",\
\
"discoverable": true,\
\
"earnCredit": true,\
\
"mode": "view",\
\
"categories": ["Project Management"\
\
]\
\
},\
\
"folder": {"id": "fl-1Ab234",\
\
"type": "folder",\
\
"browserLink": "https://coda.io/folders/fl-1Ab234",\
\
"name": "My docs"\
\
},\
\
"workspace": {"id": "ws-1Ab234",\
\
"type": "workspace",\
\
"organizationId": "org-2Bc456",\
\
"browserLink": "https://coda.io/docs?workspaceId=ws-1Ab234",\
\
"name": "My workspace"\
\
},\
\
"workspaceId": "ws-1Ab234",\
\
"folderId": "fl-1Ab234"\
\
}\
\
],

"href": "https://coda.io/apis/v1/docs?limit=20",

"nextPageToken": "eyJsaW1pd",

"nextPageLink": "https://coda.io/apis/v1/docs?pageToken=eyJsaW1pd"

}`

## [tag/Docs/operation/createDoc](https://coda.io/developers/apis/v1\#tag/Docs/operation/createDoc) Create doc

Creates a new Coda doc, optionally copying an existing doc. Note that creating a doc requires you to be a Doc Maker in the applicable workspace (or be auto-promoted to one).

##### Authorizations:

_Bearer_

##### Request Body schema: application/json  required

Parameters for creating the doc.

|     |     |
| --- | --- |
| title | string<br>Title of the new doc. Defaults to 'Untitled'. |
| sourceDoc | string<br>An optional doc ID from which to create a copy. |
| timezone | string<br>The timezone to use for the newly created doc. |
| folderId | string<br>The ID of the folder within which to create this doc. Defaults to your "My docs" folder in the oldest workspace you joined; this is subject to change. You can get this ID by opening the folder in the docs list on your computer and grabbing the `folderId` query parameter. |
| initialPage | object<br>The contents of the initial page of the doc. |

### Responses

**201**

Info about the created doc.

##### Response Schema: application/json

|     |     |
| --- | --- |
| id<br>required | string<br>ID of the Coda doc. |
| type<br>required | string<br>Value:"doc"<br>The type of this resource. |
| href<br>required | string <url> <br>API link to the Coda doc. |
| browserLink<br>required | string <url> <br>Browser-friendly link to the Coda doc. |
| name<br>required | string<br>Name of the doc. |
| owner<br>required | string <email> <br>Email address of the doc owner. |
| ownerName<br>required | string<br>Name of the doc owner. |
| createdAt<br>required | string <date-time> <br>Timestamp for when the doc was created. |
| updatedAt<br>required | string <date-time> <br>Timestamp for when the doc was last modified. |
| workspace<br>required | object (WorkspaceReference) <br>Reference to a Coda workspace. |
| folder<br>required | object (FolderReference) <br>Reference to a Coda folder. |
| workspaceId<br>required | string<br>Deprecated <br>ID of the Coda workspace containing this doc. |
| folderId<br>required | string<br>Deprecated <br>ID of the Coda folder containing this doc. |
| icon | object (Icon) <br>Info about the icon. |
| docSize | object (DocSize) <br>The number of components within a Coda doc. |
| sourceDoc | object<br>Reference to a Coda doc from which this doc was copied, if any. |
| published | object (DocPublished) <br>Information about the publishing state of the document. |
| requestId | string<br>An arbitrary unique identifier for this request. |

**400**

The request parameters did not conform to expectations.

**401**

The API token is invalid or has expired.

**403**

The API token does not grant access to this resource.

**429**

The client has sent too many requests.

post/docs

Coda API (v1)

https://coda.io/apis/v1/docs

### Request samples

- Payload
- Python 3.13
- Shell
- Google Apps Script

Content type

application/json

Copy
Expand all  Collapse all

`{"title": "Project Tracker",

"sourceDoc": "iJKlm_noPq",

"timezone": "America/Los_Angeles",

"folderId": "fl-ABcdEFgHJi",

"initialPage": {"name": "Launch Status",

"subtitle": "See the status of launch-related tasks.",

"iconName": "rocket",

"imageUrl": "https://example.com/image.jpg",

"parentPageId": "canvas-tuVwxYz",

"pageContent": {"type": "canvas",

"canvasContent": {"format": "html",

"content": "<p><b>This</b> is rich text</p>"

}

}

}

}`

### Response samples

- 201
- 400
- 401
- 403
- 429

Content type

application/json

Copy
Expand all  Collapse all

`{"id": "AbCDeFGH",

"type": "doc",

"href": "https://coda.io/apis/v1/docs/AbCDeFGH",

"browserLink": "https://coda.io/d/_dAbCDeFGH",

"icon": {"name": "string",

"type": "string",

"browserLink": "https://cdn.coda.io/icons/png/color/icon-32.png"

},

"name": "Product Launch Hub",

"owner": "user@example.com",

"ownerName": "Some User",

"docSize": {"totalRowCount": 31337,

"tableAndViewCount": 42,

"pageCount": 10,

"overApiSizeLimit": false

},

"sourceDoc": {"id": "AbCDeFGH",

"type": "doc",

"href": "https://coda.io/apis/v1/docs/AbCDeFGH",

"browserLink": "https://coda.io/d/_dAbCDeFGH"

},

"createdAt": "2018-04-11T00:18:57.946Z",

"updatedAt": "2018-04-11T00:18:57.946Z",

"published": {"description": "Hello World!",

"browserLink": "https://coda.io/@coda/hello-world",

"imageLink": "string",

"discoverable": true,

"earnCredit": true,

"mode": "view",

"categories": ["Project Management"\
\
]

},

"folder": {"id": "fl-1Ab234",

"type": "folder",

"browserLink": "https://coda.io/folders/fl-1Ab234",

"name": "My docs"

},

"workspace": {"id": "ws-1Ab234",

"type": "workspace",

"organizationId": "org-2Bc456",

"browserLink": "https://coda.io/docs?workspaceId=ws-1Ab234",

"name": "My workspace"

},

"workspaceId": "ws-1Ab234",

"folderId": "fl-1Ab234",

"requestId": "abc-123-def-456"

}`

## [tag/Docs/operation/getDoc](https://coda.io/developers/apis/v1\#tag/Docs/operation/getDoc) Get info about a doc

Returns metadata for the specified doc.

##### Authorizations:

_Bearer_

##### path Parameters

|     |     |
| --- | --- |
| docId<br>required | string<br>Example: AbCDeFGH<br>ID of the doc. |

### Responses

**200**

Basic Coda doc metadata.

##### Response Schema: application/json

|     |     |
| --- | --- |
| id<br>required | string<br>ID of the Coda doc. |
| type<br>required | string<br>Value:"doc"<br>The type of this resource. |
| href<br>required | string <url> <br>API link to the Coda doc. |
| browserLink<br>required | string <url> <br>Browser-friendly link to the Coda doc. |
| name<br>required | string<br>Name of the doc. |
| owner<br>required | string <email> <br>Email address of the doc owner. |
| ownerName<br>required | string<br>Name of the doc owner. |
| createdAt<br>required | string <date-time> <br>Timestamp for when the doc was created. |
| updatedAt<br>required | string <date-time> <br>Timestamp for when the doc was last modified. |
| workspace<br>required | object (WorkspaceReference) <br>Reference to a Coda workspace. |
| folder<br>required | object (FolderReference) <br>Reference to a Coda folder. |
| workspaceId<br>required | string<br>Deprecated <br>ID of the Coda workspace containing this doc. |
| folderId<br>required | string<br>Deprecated <br>ID of the Coda folder containing this doc. |
| icon | object (Icon) <br>Info about the icon. |
| docSize | object (DocSize) <br>The number of components within a Coda doc. |
| sourceDoc | object<br>Reference to a Coda doc from which this doc was copied, if any. |
| published | object (DocPublished) <br>Information about the publishing state of the document. |

**401**

The API token is invalid or has expired.

**403**

The API token does not grant access to this resource.

**404**

The resource could not be located with the current API token.

**429**

The client has sent too many requests.

get/docs/{docId}

Coda API (v1)

https://coda.io/apis/v1/docs/{docId}

### Request samples

- Python 3.13
- Shell
- Google Apps Script

Copy

```
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = f'https://coda.io/apis/v1/docs/<doc ID>'
res = requests.get(uri, headers=headers).json()

print(f'The name of the doc is {res["name"]}')
# => The name of the doc is New Document
```

### Response samples

- 200
- 401
- 403
- 404
- 429

Content type

application/json

Copy
Expand all  Collapse all

`{"id": "AbCDeFGH",

"type": "doc",

"href": "https://coda.io/apis/v1/docs/AbCDeFGH",

"browserLink": "https://coda.io/d/_dAbCDeFGH",

"icon": {"name": "string",

"type": "string",

"browserLink": "https://cdn.coda.io/icons/png/color/icon-32.png"

},

"name": "Product Launch Hub",

"owner": "user@example.com",

"ownerName": "Some User",

"docSize": {"totalRowCount": 31337,

"tableAndViewCount": 42,

"pageCount": 10,

"overApiSizeLimit": false

},

"sourceDoc": {"id": "AbCDeFGH",

"type": "doc",

"href": "https://coda.io/apis/v1/docs/AbCDeFGH",

"browserLink": "https://coda.io/d/_dAbCDeFGH"

},

"createdAt": "2018-04-11T00:18:57.946Z",

"updatedAt": "2018-04-11T00:18:57.946Z",

"published": {"description": "Hello World!",

"browserLink": "https://coda.io/@coda/hello-world",

"imageLink": "string",

"discoverable": true,

"earnCredit": true,

"mode": "view",

"categories": ["Project Management"\
\
]

},

"folder": {"id": "fl-1Ab234",

"type": "folder",

"browserLink": "https://coda.io/folders/fl-1Ab234",

"name": "My docs"

},

"workspace": {"id": "ws-1Ab234",

"type": "workspace",

"organizationId": "org-2Bc456",

"browserLink": "https://coda.io/docs?workspaceId=ws-1Ab234",

"name": "My workspace"

},

"workspaceId": "ws-1Ab234",

"folderId": "fl-1Ab234"

}`

## [tag/Docs/operation/deleteDoc](https://coda.io/developers/apis/v1\#tag/Docs/operation/deleteDoc) Delete doc

Deletes a doc.

##### Authorizations:

_Bearer_

##### path Parameters

|     |     |
| --- | --- |
| docId<br>required | string<br>Example: AbCDeFGH<br>ID of the doc. |

### Responses

**202**

A result indicating that the doc was deleted.

##### Response Schema: application/json

object (DocDelete)

The result of a doc deletion.

**401**

The API token is invalid or has expired.

**403**

The API token does not grant access to this resource.

**404**

The resource could not be located with the current API token.

**429**

The client has sent too many requests.

delete/docs/{docId}

Coda API (v1)

https://coda.io/apis/v1/docs/{docId}

### Request samples

- Python 3.13
- Shell
- Google Apps Script

Copy

```
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = f'https://coda.io/apis/v1/docs/<doc ID>'
res = requests.delete(uri, headers=headers).json()
```

### Response samples

- 202
- 401
- 403
- 404
- 429

Content type

application/json

Copy

`{ }`

## [tag/Docs/operation/updateDoc](https://coda.io/developers/apis/v1\#tag/Docs/operation/updateDoc) Update doc

Updates metadata for a doc. Note that updating a doc title requires you to be a Doc Maker in the applicable workspace.

##### Authorizations:

_Bearer_

##### path Parameters

|     |     |
| --- | --- |
| docId<br>required | string<br>Example: AbCDeFGH<br>ID of the doc. |

##### Request Body schema: application/json  required

Parameters for updating the doc.

|     |     |
| --- | --- |
| title | string<br>Title of the doc. |
| iconName | string<br>Name of the icon. |

### Responses

**200**

Basic Coda doc metadata.

##### Response Schema: application/json

object (DocUpdateResult)

The result of a doc update

**400**

The request parameters did not conform to expectations.

**401**

The API token is invalid or has expired.

**403**

The API token does not grant access to this resource.

**404**

The resource could not be located with the current API token.

**429**

The client has sent too many requests.

patch/docs/{docId}

Coda API (v1)

https://coda.io/apis/v1/docs/{docId}

### Request samples

- Payload
- Python 3.13
- Shell
- Google Apps Script

Content type

application/json

Copy

`{"title": "Project Tracker",

"iconName": "rocket"

}`

### Response samples

- 200
- 400
- 401
- 403
- 404
- 429

Content type

application/json

Copy

`{ }`

## [tag/Permissions](https://coda.io/developers/apis/v1\#tag/Permissions) Permissions

This API lets you manage sharing and permissions for your docs.

## [tag/Permissions/operation/getSharingMetadata](https://coda.io/developers/apis/v1\#tag/Permissions/operation/getSharingMetadata) Get sharing metadata

Returns metadata associated with sharing for this Coda doc.

##### Authorizations:

_Bearer_

##### path Parameters

|     |     |
| --- | --- |
| docId<br>required | string<br>Example: AbCDeFGH<br>ID of the doc. |

### Responses

**200**

Metadata associated with sharing permissions for a doc.

##### Response Schema: application/json

|     |     |
| --- | --- |
| canShare<br>required | boolean<br>When true, the user of the api can share |
| canShareWithWorkspace<br>required | boolean<br>When true, the user of the api can share with the workspace |
| canShareWithOrg<br>required | boolean<br>When true, the user of the api can share with the org |
| canCopy<br>required | boolean<br>When true, the user of the api can copy the doc |

**401**

The API token is invalid or has expired.

**403**

The API token does not grant access to this resource.

**404**

The resource could not be located with the current API token.

**429**

The client has sent too many requests.

get/docs/{docId}/acl/metadata

Coda API (v1)

https://coda.io/apis/v1/docs/{docId}/acl/metadata

### Request samples

- Python 3.13
- Shell
- Google Apps Script

Copy

```
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = f'https://coda.io/apis/v1/docs/<doc ID>/acl/metadata'
res = requests.get(uri, headers=headers).json()

print(f'Can I share this doc with others? {res["canShare"]}')
# => Can I share this doc with others? true
```

### Response samples

- 200
- 401
- 403
- 404
- 429

Content type

application/json

Copy

`{"canShare": true,

"canShareWithWorkspace": true,

"canShareWithOrg": true,

"canCopy": true

}`

## [tag/Permissions/operation/getPermissions](https://coda.io/developers/apis/v1\#tag/Permissions/operation/getPermissions) List permissions

Returns a list of permissions for this Coda doc.

##### Authorizations:

_Bearer_

##### path Parameters

|     |     |
| --- | --- |
| docId<br>required | string<br>Example: AbCDeFGH<br>ID of the doc. |

##### query Parameters

|     |     |
| --- | --- |
| limit | integer >= 1 <br>Default: 25<br>Example: limit=10<br>Maximum number of results to return in this query. |
| pageToken | string<br>Example: pageToken=eyJsaW1pd<br>An opaque token used to fetch the next page of results. |

### Responses

**200**

List of permissions for a doc.

##### Response Schema: application/json

|     |     |
| --- | --- |
| items<br>required | Array of objects (Permission) |
| href<br>required | string <url> <br>API link to these results |
| nextPageToken | string (nextPageToken) <br>If specified, an opaque token used to fetch the next page of results. |
| nextPageLink | string <url> <br>If specified, a link that can be used to fetch the next page of results. |

**401**

The API token is invalid or has expired.

**403**

The API token does not grant access to this resource.

**404**

The resource could not be located with the current API token.

**429**

The client has sent too many requests.

get/docs/{docId}/acl/permissions

Coda API (v1)

https://coda.io/apis/v1/docs/{docId}/acl/permissions

### Request samples

- Python 3.13
- Shell
- Google Apps Script

Copy

```
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = f'https://coda.io/apis/v1/docs/<doc ID>/acl/permissions'
res = requests.get(uri, headers=headers).json()

print(f'First user with access is {res["items"][0]["principal"]["email"]}')
# => First user with access is foo@bar.com
```

### Response samples

- 200
- 401
- 403
- 404
- 429

Content type

application/json

Copy
Expand all  Collapse all

`{"items": [{"principal": {"type": "email",\
\
"email": "example@domain.com"\
\
},\
\
"id": "string",\
\
"access": "readonly"\
\
}\
\
],

"href": "https://coda.io/apis/v1/docs/AbCDeFGH/acl?limit=20",

"nextPageToken": "eyJsaW1pd",

"nextPageLink": "https://coda.io/apis/v1/docs/AbCDeFGH/acl?pageToken=eyJsaW1pd"

}`

## [tag/Permissions/operation/addPermission](https://coda.io/developers/apis/v1\#tag/Permissions/operation/addPermission) Add permission

Adds a new permission to the doc.

##### Authorizations:

_Bearer_

##### path Parameters

|     |     |
| --- | --- |
| docId<br>required | string<br>Example: AbCDeFGH<br>ID of the doc. |

##### Request Body schema: application/json  required

Parameters for adding the new permission.

|     |     |
| --- | --- |
| access<br>required | string (AccessTypeNotNone) <br>Enum:"readonly""write""comment"<br>Type of access (excluding none). |
| principal<br>required | any (AddedPrincipal) <br>Metadata about a principal to add to a doc. |
| suppressEmail | boolean<br>When true suppresses email notification |

### Responses

**200**

Confirmation that the request was applied.

##### Response Schema: application/json

object (AddPermissionResult)

The result of sharing a doc.

**400**

The request parameters did not conform to expectations.

**401**

The API token is invalid or has expired.

**403**

The API token does not grant access to this resource.

**404**

The resource could not be located with the current API token.

**429**

The client has sent too many requests.

post/docs/{docId}/acl/permissions

Coda API (v1)

https://coda.io/apis/v1/docs/{docId}/acl/permissions

### Request samples

- Payload
- Python 3.13
- Shell
- Google Apps Script

Content type

application/json

Copy
Expand all  Collapse all

`{"access": "readonly",

"principal": {"type": "email",

"email": "example@domain.com"

},

"suppressEmail": true

}`

### Response samples

- 200
- 400
- 401
- 403
- 404
- 429

Content type

application/json

Copy

`{ }`

## [tag/Permissions/operation/deletePermission](https://coda.io/developers/apis/v1\#tag/Permissions/operation/deletePermission) Delete permission

Deletes an existing permission.

##### Authorizations:

_Bearer_

##### path Parameters

|     |     |
| --- | --- |
| docId<br>required | string<br>Example: AbCDeFGH<br>ID of the doc. |
| permissionId<br>required | string<br>Example: AbCDeFGH<br>ID of a permission on a doc. |

### Responses

**200**

Confirmation that the request was applied.

##### Response Schema: application/json

object (DeletePermissionResult)

The result of deleting a permission.

**400**

The request parameters did not conform to expectations.

**401**

The API token is invalid or has expired.

**403**

The API token does not grant access to this resource.

**404**

The resource could not be located with the current API token.

**429**

The client has sent too many requests.

delete/docs/{docId}/acl/permissions/{permissionId}

Coda API (v1)

https://coda.io/apis/v1/docs/{docId}/acl/permissions/{permissionId}

### Request samples

- Python 3.13
- Shell
- Google Apps Script

Copy

```
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = f'https://coda.io/apis/v1/docs/<doc ID>/acl/permissions/<permission ID>'
res = requests.delete(uri, headers=headers, json=payload)

# => Revoke access to the doc
```

### Response samples

- 200
- 400
- 401
- 403
- 404
- 429

Content type

application/json

Copy

`{ }`

## [tag/Permissions/operation/searchPrincipals](https://coda.io/developers/apis/v1\#tag/Permissions/operation/searchPrincipals) Search principals

Searches for user and group principals matching the query that this doc can be shared with.
At most 20 results will be returned for both users and groups. If no query is given then no results are returned.

##### Authorizations:

_Bearer_

##### path Parameters

|     |     |
| --- | --- |
| docId<br>required | string<br>Example: AbCDeFGH<br>ID of the doc. |

##### query Parameters

|     |     |
| --- | --- |
| query | string<br>Example: query=Supercalifragilisticexpialidocious<br>Search term used to filter down results. |

### Responses

**200**

Search results for the given query.

##### Response Schema: application/json

|     |     |
| --- | --- |
| users<br>required | Array of objects (UserSummary) |
| groups<br>required | Array of objects (GroupPrincipal) |

**400**

The request parameters did not conform to expectations.

**401**

The API token is invalid or has expired.

**403**

The API token does not grant access to this resource.

**404**

The resource could not be located with the current API token.

**429**

The client has sent too many requests.

get/docs/{docId}/acl/principals/search

Coda API (v1)

https://coda.io/apis/v1/docs/{docId}/acl/principals/search

### Request samples

- Python 3.13
- Shell
- Google Apps Script

Copy

```
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = f'https://coda.io/apis/v1/docs/<doc ID>/acl/principals/search?search=foo'
res = requests.get(uri, headers=headers).json()

print(f'First user with access is {res["users"][0]["email"]}')
# => First user with access is foo@bar.com
```

### Response samples

- 200
- 400
- 401
- 403
- 404
- 429

Content type

application/json

Copy
Expand all  Collapse all

`{"users": [{"name": "John Doe",\
\
"loginId": "user@example.com",\
\
"type": "user",\
\
"pictureLink": "https://cdn.coda.io/avatars/default_avatar.png"\
\
}\
\
],

"groups": [{"type": "group",\
\
"groupId": "grp-6SM9xrKcqW",\
\
"groupName": "Marketing team"\
\
}\
\
]

}`

## [tag/Permissions/operation/getAclSettings](https://coda.io/developers/apis/v1\#tag/Permissions/operation/getAclSettings) Get ACL settings

Returns settings associated with ACLs for this Coda doc.

##### Authorizations:

_Bearer_

##### path Parameters

|     |     |
| --- | --- |
| docId<br>required | string<br>Example: AbCDeFGH<br>ID of the doc. |

### Responses

**200**

Settings associated with access control for a doc.

##### Response Schema: application/json

|     |     |
| --- | --- |
| allowEditorsToChangePermissions<br>required | boolean<br>When true, allows editors to change doc permissions. When false, only doc owner can change doc permissions. |
| allowCopying<br>required | boolean<br>When true, allows doc viewers to copy the doc. |
| allowViewersToRequestEditing<br>required | boolean<br>When true, allows doc viewers to request editing permissions. |

**401**

The API token is invalid or has expired.

**403**

The API token does not grant access to this resource.

**404**

The resource could not be located with the current API token.

**429**

The client has sent too many requests.

get/docs/{docId}/acl/settings

Coda API (v1)

https://coda.io/apis/v1/docs/{docId}/acl/settings

### Request samples

- Python 3.13
- Shell
- Google Apps Script

Copy

```
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = f'https://coda.io/apis/v1/docs/<doc ID>/acl/settings'
res = requests.get(uri, headers=headers).json()

print(f'Can editors change sharing permissions? {res["allowEditorsToChangePermissions"]}')
# => Can editors change sharing permissions? false
```

### Response samples

- 200
- 401
- 403
- 404
- 429

Content type

application/json

Copy

`{"allowEditorsToChangePermissions": true,

"allowCopying": true,

"allowViewersToRequestEditing": true

}`

## [tag/Permissions/operation/updateAclSettings](https://coda.io/developers/apis/v1\#tag/Permissions/operation/updateAclSettings) Update ACL settings

Update settings associated with ACLs for this Coda doc.

##### Authorizations:

_Bearer_

##### path Parameters

|     |     |
| --- | --- |
| docId<br>required | string<br>Example: AbCDeFGH<br>ID of the doc. |

##### Request Body schema: application/json  required

Parameters for updating the ACL settings.

|     |     |
| --- | --- |
| allowEditorsToChangePermissions | boolean<br>When true, allows editors to change doc permissions. When false, only doc owner can change doc permissions. |
| allowCopying | boolean<br>When true, allows doc viewers to copy the doc. |
| allowViewersToRequestEditing | boolean<br>When true, allows doc viewers to request editing permissions. |

### Responses

**200**

Settings associated with access control for a doc.

##### Response Schema: application/json

|     |     |
| --- | --- |
| allowEditorsToChangePermissions<br>required | boolean<br>When true, allows editors to change doc permissions. When false, only doc owner can change doc permissions. |
| allowCopying<br>required | boolean<br>When true, allows doc viewers to copy the doc. |
| allowViewersToRequestEditing<br>required | boolean<br>When true, allows doc viewers to request editing permissions. |

**401**

The API token is invalid or has expired.

**403**

The API token does not grant access to this resource.

**404**

The resource could not be located with the current API token.

**429**

The client has sent too many requests.

patch/docs/{docId}/acl/settings

Coda API (v1)

https://coda.io/apis/v1/docs/{docId}/acl/settings

### Request samples

- Payload

Content type

application/json

Copy

`{"allowEditorsToChangePermissions": true,

"allowCopying": true,

"allowViewersToRequestEditing": true

}`

### Response samples

- 200
- 401
- 403
- 404
- 429

Content type

application/json

Copy

`{"allowEditorsToChangePermissions": true,

"allowCopying": true,

"allowViewersToRequestEditing": true

}`

## [tag/Publishing](https://coda.io/developers/apis/v1\#tag/Publishing) Publishing

Coda docs can be published publicly and associated with categories to help the world discover them. This API lets you manage the publishing settings of your docs.

## [tag/Publishing/operation/listCategories](https://coda.io/developers/apis/v1\#tag/Publishing/operation/listCategories) Get doc categories

Gets all available doc categories.

##### Authorizations:

_Bearer_

### Responses

**200**

List of doc categories

##### Response Schema: application/json

|     |     |
| --- | --- |
| items<br>required | Array of objects (DocCategory) <br>Categories for the doc. |

**401**

The API token is invalid or has expired.

**404**

The resource could not be located with the current API token.

**429**

The client has sent too many requests.

get/categories

Coda API (v1)

https://coda.io/apis/v1/categories

### Request samples

- Python 3.13
- Shell
- Google Apps Script

Copy

```
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = f'https://coda.io/apis/v1/categories'
res = requests.get(uri, headers=headers).json()

print(f'Category count: {res["categories"].length}')
# => Category count: 10
```

### Response samples

- 200
- 401
- 404
- 429

Content type

application/json

Copy
Expand all  Collapse all

`{"items": [{"name": "Project Management"\
\
}\
\
]

}`

## [tag/Publishing/operation/publishDoc](https://coda.io/developers/apis/v1\#tag/Publishing/operation/publishDoc) Publish doc

Update publish settings for a doc.

##### Authorizations:

_Bearer_

##### path Parameters

|     |     |
| --- | --- |
| docId<br>required | string<br>Example: AbCDeFGH<br>ID of the doc. |

##### Request Body schema: application/json  required

Parameters for changing publish settings.

|     |     |
| --- | --- |
| slug | string<br>Slug for the published doc. |
| discoverable | boolean<br>If true, indicates that the doc is discoverable. |
| earnCredit | boolean<br>If true, new users may be required to sign in to view content within this document. You will receive Coda credit for each user who signs up via your doc. |
| categoryNames | Array of strings<br>The names of categories to apply to the document. |
| mode | string (DocPublishMode) <br>Enum:"view""play""edit"<br>Which interaction mode the published doc should use. |

### Responses

**202**

Confirmation that the publish request was accepted.

##### Response Schema: application/json

|     |     |
| --- | --- |
| requestId<br>required | string<br>An arbitrary unique identifier for this request. |

**400**

The request parameters did not conform to expectations.

**401**

The API token is invalid or has expired.

**403**

The API token does not grant access to this resource.

**404**

The resource could not be located with the current API token.

**429**

The client has sent too many requests.

put/docs/{docId}/publish

Coda API (v1)

https://coda.io/apis/v1/docs/{docId}/publish

### Request samples

- Payload
- Python 3.13
- Shell
- Google Apps Script

Content type

application/json

Copy
Expand all  Collapse all

`{"slug": "my-doc",

"discoverable": true,

"earnCredit": true,

"categoryNames": ["Project management"\
\
],

"mode": "view"

}`

### Response samples

- 202
- 400
- 401
- 403
- 404
- 429

Content type

application/json

Copy

`{"requestId": "abc-123-def-456"

}`

## [tag/Publishing/operation/unpublishDoc](https://coda.io/developers/apis/v1\#tag/Publishing/operation/unpublishDoc) Unpublish doc

Unpublishes a doc.

##### Authorizations:

_Bearer_

##### path Parameters

|     |     |
| --- | --- |
| docId<br>required | string<br>Example: AbCDeFGH<br>ID of the doc. |

### Responses

**200**

A result indicating that the doc was unpublished.

##### Response Schema: application/json

object (UnpublishResult)

The result of unpublishing a doc.

**401**

The API token is invalid or has expired.

**403**

The API token does not grant access to this resource.

**404**

The resource could not be located with the current API token.

**429**

The client has sent too many requests.

delete/docs/{docId}/publish

Coda API (v1)

https://coda.io/apis/v1/docs/{docId}/publish

### Request samples

- Python 3.13
- Shell
- Google Apps Script

Copy

```
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = f'https://coda.io/apis/v1/docs/<doc ID>/publish'
res = requests.unpublishDoc(uri, headers=headers).json()
```

### Response samples

- 200
- 401
- 403
- 404
- 429

Content type

application/json

Copy

`{ }`

## [tag/Pages](https://coda.io/developers/apis/v1\#tag/Pages) Pages

Pages in Coda offer canvases containing rich text, tables, controls, and other objects. At this time, this API lets you list and access pages in a doc.

## [tag/Pages/operation/listPages](https://coda.io/developers/apis/v1\#tag/Pages/operation/listPages) List pages

Returns a list of pages in a Coda doc.

##### Authorizations:

_Bearer_

##### path Parameters

|     |     |
| --- | --- |
| docId<br>required | string<br>Example: AbCDeFGH<br>ID of the doc. |

##### query Parameters

|     |     |
| --- | --- |
| limit | integer >= 1 <br>Default: 25<br>Example: limit=10<br>Maximum number of results to return in this query. |
| pageToken | string<br>Example: pageToken=eyJsaW1pd<br>An opaque token used to fetch the next page of results. |

### Responses

**200**

List of pages.

##### Response Schema: application/json

|     |     |
| --- | --- |
| items<br>required | Array of objects (Page) |
| href | string <url> <br>API link to these results |
| nextPageToken | string (nextPageToken) <br>If specified, an opaque token used to fetch the next page of results. |
| nextPageLink | string <url> <br>If specified, a link that can be used to fetch the next page of results. |

**401**

The API token is invalid or has expired.

**403**

The API token does not grant access to this resource.

**404**

The resource could not be located with the current API token.

**429**

The client has sent too many requests.

get/docs/{docId}/pages

Coda API (v1)

https://coda.io/apis/v1/docs/{docId}/pages

### Request samples

- Python 3.13
- Shell
- Google Apps Script

Copy

```
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = f'https://coda.io/apis/v1/docs/<doc ID>/pages'
res = requests.get(uri, headers=headers).json()

print(f'The name of the first page is {res["items"][0]["name"]}')
# => The name of the first page is Page 1
```

### Response samples

- 200
- 401
- 403
- 404
- 429

Content type

application/json

Copy
Expand all  Collapse all

`{"items": [{"id": "canvas-IjkLmnO",\
\
"type": "page",\
\
"href": "https://coda.io/apis/v1/docs/AbCDeFGH/pages/canvas-IjkLmnO",\
\
"browserLink": "https://coda.io/d/_dAbCDeFGH/Launch-Status_sumnO",\
\
"name": "Launch Status",\
\
"subtitle": "See the status of launch-related tasks.",\
\
"icon": {"name": "string",\
\
"type": "string",\
\
"browserLink": "https://cdn.coda.io/icons/png/color/icon-32.png"\
\
},\
\
"image": {"browserLink": "https://codahosted.io/docs/nUYhlXysYO/blobs/bl-lYkYKNzkuT/3f879b9ecfa27448",\
\
"type": "string",\
\
"width": 800,\
\
"height": 600\
\
},\
\
"contentType": "canvas",\
\
"isHidden": true,\
\
"isEffectivelyHidden": true,\
\
"parent": {"id": "canvas-IjkLmnO",\
\
"type": "page",\
\
"href": "https://coda.io/apis/v1/docs/AbCDeFGH/pages/canvas-IjkLmnO",\
\
"browserLink": "https://coda.io/d/_dAbCDeFGH/Launch-Status_sumnO",\
\
"name": "Launch Status"\
\
},\
\
"children": [{"id": "canvas-IjkLmnO",\
\
"type": "page",\
\
"href": "https://coda.io/apis/v1/docs/AbCDeFGH/pages/canvas-IjkLmnO",\
\
"browserLink": "https://coda.io/d/_dAbCDeFGH/Launch-Status_sumnO",\
\
"name": "Launch Status"\
\
}\
\
],\
\
"authors": [{"@context": "http://schema.org/",\
\
"@type": "Person",\
\
"additionalType": "string",\
\
"name": "Alice Atkins",\
\
"email": "alice@atkins.com"\
\
}\
\
],\
\
"createdAt": "2018-04-11T00:18:57.946Z",\
\
"createdBy": {"@context": "http://schema.org/",\
\
"@type": "Person",\
\
"additionalType": "string",\
\
"name": "Alice Atkins",\
\
"email": "alice@atkins.com"\
\
},\
\
"updatedAt": "2018-04-11T00:18:57.946Z",\
\
"updatedBy": {"@context": "http://schema.org/",\
\
"@type": "Person",\
\
"additionalType": "string",\
\
"name": "Alice Atkins",\
\
"email": "alice@atkins.com"\
\
}\
\
}\
\
],

"href": "https://coda.io/apis/v1/docs/AbCDeFGH/pages?limit=20",

"nextPageToken": "eyJsaW1pd",

"nextPageLink": "https://coda.io/apis/v1/docs/AbCDeFGH/pages?pageToken=eyJsaW1pd"

}`

## [tag/Pages/operation/createPage](https://coda.io/developers/apis/v1\#tag/Pages/operation/createPage) Create a page

Create a new page in a doc. Note that creating a page requires you to be a Doc Maker in the applicable workspace.

##### Authorizations:

_Bearer_

##### path Parameters

|     |     |
| --- | --- |
| docId<br>required | string<br>Example: AbCDeFGH<br>ID of the doc. |

##### Request Body schema: application/json  required

Parameters for creating a page.

|     |     |
| --- | --- |
| name | string<br>Name of the page. |
| subtitle | string<br>Subtitle of the page. |
| iconName | string<br>Name of the icon. |
| imageUrl | string<br>Url of the cover image to use. |
| parentPageId | string<br>The ID of this new page's parent, if creating a subpage. |
| pageContent | any (PageCreateContent) <br>Content that can be added to a page at creation time, either text (or rich text) or a URL to create a full-page embed. |

### Responses

**202**

A result indicating that the creation request was queued for processing.

##### Response Schema: application/json

|     |     |
| --- | --- |
| requestId<br>required | string<br>An arbitrary unique identifier for this request. |
| id<br>required | string<br>ID of the created page. |

**400**

The request parameters did not conform to expectations.

**401**

The API token is invalid or has expired.

**403**

The API token does not grant access to this resource.

**404**

The resource could not be located with the current API token.

**429**

The client has sent too many requests.

post/docs/{docId}/pages

Coda API (v1)

https://coda.io/apis/v1/docs/{docId}/pages

### Request samples

- Payload
- Python 3.13
- Shell
- Google Apps Script

Content type

application/json

Copy
Expand all  Collapse all

`{"name": "Launch Status",

"subtitle": "See the status of launch-related tasks.",

"iconName": "rocket",

"imageUrl": "https://example.com/image.jpg",

"parentPageId": "canvas-tuVwxYz",

"pageContent": {"type": "canvas",

"canvasContent": {"format": "html",

"content": "<p><b>This</b> is rich text</p>"

}

}

}`

### Response samples

- 202
- 400
- 401
- 403
- 404
- 429

Content type

application/json

Copy

`{"requestId": "abc-123-def-456",

"id": "canvas-tuVwxYz"

}`

## [tag/Pages/operation/getPage](https://coda.io/developers/apis/v1\#tag/Pages/operation/getPage) Get a page

Returns details about a page.

##### Authorizations:

_Bearer_

##### path Parameters

|     |     |
| --- | --- |
| docId<br>required | string<br>Example: AbCDeFGH<br>ID of the doc. |
| pageIdOrName<br>required | string<br>Example: canvas-IjkLmnO<br>ID or name of the page. Names are discouraged because they're easily prone to being changed by users. If you're using a name, be sure to URI-encode it. If you provide a name and there are multiple pages with the same name, an arbitrary one will be selected. |

### Responses

**200**

Info about a page.

##### Response Schema: application/json

|     |     |
| --- | --- |
| id<br>required | string<br>ID of the page. |
| type<br>required | string<br>Value:"page"<br>The type of this resource. |
| href<br>required | string <url> <br>API link to the page. |
| name<br>required | string<br>Name of the page. |
| isHidden<br>required | boolean<br>Whether the page is hidden in the UI. |
| isEffectivelyHidden<br>required | boolean<br>Whether the page or any of its parents is hidden in the UI. |
| browserLink<br>required | string <url> <br>Browser-friendly link to the page. |
| children<br>required | Array of objects (PageReference) |
| contentType<br>required | string (PageType) <br>Enum:"canvas""embed""syncPage"<br>The type of a page in a doc. |
| subtitle | string<br>Subtitle of the page. |
| icon | object (Icon) <br>Info about the icon. |
| image | object (Image) <br>Info about the image. |
| parent | object (PageReference) <br>Reference to a page. |
| authors | Array of objects (PersonValue) <br>Authors of the page |
| createdAt | string <date-time> <br>Timestamp for when the page was created. |
| createdBy | object (PersonValue) <br>A named reference to a person, where the person is identified by email address. |
| updatedAt | string <date-time> <br>Timestamp for when page content was last modified. |
| updatedBy | object (PersonValue) <br>A named reference to a person, where the person is identified by email address. |

**401**

The API token is invalid or has expired.

**403**

The API token does not grant access to this resource.

**404**

The resource could not be located with the current API token.

**410**

The resource has been deleted.

**429**

The client has sent too many requests.

get/docs/{docId}/pages/{pageIdOrName}

Coda API (v1)

https://coda.io/apis/v1/docs/{docId}/pages/{pageIdOrName}

### Request samples

- Python 3.13
- Shell
- Google Apps Script

Copy

```
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = f'https://coda.io/apis/v1/docs/<doc ID>/pages/<page ID>'
res = requests.get(uri, headers=headers).json()

print(f'The name of this page is {res["name"]}')
# => The name of this page is Page 1
```

### Response samples

- 200
- 401
- 403
- 404
- 410
- 429

Content type

application/json

Copy
Expand all  Collapse all

`{"id": "canvas-IjkLmnO",

"type": "page",

"href": "https://coda.io/apis/v1/docs/AbCDeFGH/pages/canvas-IjkLmnO",

"browserLink": "https://coda.io/d/_dAbCDeFGH/Launch-Status_sumnO",

"name": "Launch Status",

"subtitle": "See the status of launch-related tasks.",

"icon": {"name": "string",

"type": "string",

"browserLink": "https://cdn.coda.io/icons/png/color/icon-32.png"

},

"image": {"browserLink": "https://codahosted.io/docs/nUYhlXysYO/blobs/bl-lYkYKNzkuT/3f879b9ecfa27448",

"type": "string",

"width": 800,

"height": 600

},

"contentType": "canvas",

"isHidden": true,

"isEffectivelyHidden": true,

"parent": {"id": "canvas-IjkLmnO",

"type": "page",

"href": "https://coda.io/apis/v1/docs/AbCDeFGH/pages/canvas-IjkLmnO",

"browserLink": "https://coda.io/d/_dAbCDeFGH/Launch-Status_sumnO",

"name": "Launch Status"

},

"children": [{"id": "canvas-IjkLmnO",\
\
"type": "page",\
\
"href": "https://coda.io/apis/v1/docs/AbCDeFGH/pages/canvas-IjkLmnO",\
\
"browserLink": "https://coda.io/d/_dAbCDeFGH/Launch-Status_sumnO",\
\
"name": "Launch Status"\
\
}\
\
],

"authors": [{"@context": "http://schema.org/",\
\
"@type": "Person",\
\
"additionalType": "string",\
\
"name": "Alice Atkins",\
\
"email": "alice@atkins.com"\
\
}\
\
],

"createdAt": "2018-04-11T00:18:57.946Z",

"createdBy": {"@context": "http://schema.org/",

"@type": "Person",

"additionalType": "string",

"name": "Alice Atkins",

"email": "alice@atkins.com"

},

"updatedAt": "2018-04-11T00:18:57.946Z",

"updatedBy": {"@context": "http://schema.org/",

"@type": "Person",

"additionalType": "string",

"name": "Alice Atkins",

"email": "alice@atkins.com"

}

}`

## [tag/Pages/operation/updatePage](https://coda.io/developers/apis/v1\#tag/Pages/operation/updatePage) Update a page

Update properties for a page. Note that updating a page title or icon requires you to be a Doc Maker in the applicable workspace.

##### Authorizations:

_Bearer_

##### path Parameters

|     |     |
| --- | --- |
| docId<br>required | string<br>Example: AbCDeFGH<br>ID of the doc. |
| pageIdOrName<br>required | string<br>Example: canvas-IjkLmnO<br>ID or name of the page. Names are discouraged because they're easily prone to being changed by users. If you're using a name, be sure to URI-encode it. If you provide a name and there are multiple pages with the same name, an arbitrary one will be selected. |

##### Request Body schema: application/json  required

Parameters for updating a page.

|     |     |
| --- | --- |
| name | string<br>Name of the page. |
| subtitle | string<br>Subtitle of the page. |
| iconName | string<br>Name of the icon. |
| imageUrl | string<br>Url of the cover image to use. |
| isHidden | boolean<br>Whether the page is hidden or not. Note that for pages that cannot be hidden, like the sole top-level page in a doc, this will be ignored. |
| contentUpdate | object<br>Content with which to update an existing page. |

### Responses

**202**

A result indicating that the update was queued for processing.

##### Response Schema: application/json

|     |     |
| --- | --- |
| requestId<br>required | string<br>An arbitrary unique identifier for this request. |
| id<br>required | string<br>ID of the updated page. |

**400**

The request parameters did not conform to expectations.

**401**

The API token is invalid or has expired.

**403**

The API token does not grant access to this resource.

**404**

The resource could not be located with the current API token.

**429**

The client has sent too many requests.

put/docs/{docId}/pages/{pageIdOrName}

Coda API (v1)

https://coda.io/apis/v1/docs/{docId}/pages/{pageIdOrName}

### Request samples

- Payload
- Python 3.13
- Shell
- Google Apps Script

Content type

application/json

Copy
Expand all  Collapse all

`{"name": "Launch Status",

"subtitle": "See the status of launch-related tasks.",

"iconName": "rocket",

"imageUrl": "https://example.com/image.jpg",

"isHidden": true,

"contentUpdate": {"insertionMode": "append",

"elementId": "cl-lzqh0Q0poT",

"canvasContent": {"format": "html",

"content": "<p><b>This</b> is rich text</p>"

}

}

}`

### Response samples

- 202
- 400
- 401
- 403
- 404
- 429

Content type

application/json

Copy

`{"requestId": "abc-123-def-456",

"id": "canvas-tuVwxYz"

}`

## [tag/Pages/operation/deletePage](https://coda.io/developers/apis/v1\#tag/Pages/operation/deletePage) Delete a page

Deletes the specified page.

##### Authorizations:

_Bearer_

##### path Parameters

|     |     |
| --- | --- |
| docId<br>required | string<br>Example: AbCDeFGH<br>ID of the doc. |
| pageIdOrName<br>required | string<br>Example: canvas-IjkLmnO<br>ID or name of the page. Names are discouraged because they're easily prone to being changed by users. If you're using a name, be sure to URI-encode it. If you provide a name and there are multiple pages with the same name, an arbitrary one will be selected. |

### Responses

**202**

A result indicating that the delete was queued for processing.

##### Response Schema: application/json

|     |     |
| --- | --- |
| requestId<br>required | string<br>An arbitrary unique identifier for this request. |
| id<br>required | string<br>ID of the page to be deleted. |

**400**

The request parameters did not conform to expectations.

**401**

The API token is invalid or has expired.

**403**

The API token does not grant access to this resource.

**404**

The resource could not be located with the current API token.

**429**

The client has sent too many requests.

delete/docs/{docId}/pages/{pageIdOrName}

Coda API (v1)

https://coda.io/apis/v1/docs/{docId}/pages/{pageIdOrName}

### Request samples

- Python 3.13
- Shell
- Google Apps Script

Copy

```
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = f'https://coda.io/apis/v1/docs/<doc ID>/pages/<page ID>'
req = requests.delete(uri, headers=headers)
req.raise_for_status() # Throw if there was an error.
res = req.json()

print(f'Deleted page')
# => Deleted page
```

### Response samples

- 202
- 400
- 401
- 403
- 404
- 429

Content type

application/json

Copy

`{"requestId": "abc-123-def-456",

"id": "canvas-tuVwxYz"

}`

## [tag/Pages/operation/listPageContent](https://coda.io/developers/apis/v1\#tag/Pages/operation/listPageContent) List page content

Returns a list of content elements in a page.

##### Authorizations:

_Bearer_

##### path Parameters

|     |     |
| --- | --- |
| docId<br>required | string<br>Example: AbCDeFGH<br>ID of the doc. |
| pageIdOrName<br>required | string<br>Example: canvas-IjkLmnO<br>ID or name of the page. Names are discouraged because they're easily prone to being changed by users. If you're using a name, be sure to URI-encode it. If you provide a name and there are multiple pages with the same name, an arbitrary one will be selected. |

##### query Parameters

|     |     |
| --- | --- |
| limit | integer \[ 1 .. 500 \] <br>Default: 50<br>Example: limit=50<br>Maximum number of content items to return in this query. |
| pageToken | string<br>Example: pageToken=eyJsaW1pd<br>An opaque token used to fetch the next page of results. |
| contentFormat | string<br>Default: "plainText"<br>Value:"plainText"<br>Example: contentFormat=plainText<br>The format to return content in. Defaults to plainText. |

### Responses

**200**

List of page content elements.

##### Response Schema: application/json

|     |     |
| --- | --- |
| items<br>required | Array of objects (PageContentItem) |
| href<br>required | string <url> <br>API link to these results |
| nextPageToken | string (nextPageToken) <br>If specified, an opaque token used to fetch the next page of results. |
| nextPageLink | string <url> <br>If specified, a link that can be used to fetch the next page of results. |

**401**

The API token is invalid or has expired.

**403**

The API token does not grant access to this resource.

**404**

The resource could not be located with the current API token.

**410**

The resource has been deleted.

**429**

The client has sent too many requests.

get/docs/{docId}/pages/{pageIdOrName}/content

Coda API (v1)

https://coda.io/apis/v1/docs/{docId}/pages/{pageIdOrName}/content

### Request samples

- Python 3.13
- Shell
- Google Apps Script

Copy

```
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = f'https://coda.io/apis/v1/docs/<doc ID>/pages/<page ID>/content'
res = requests.get(uri, headers=headers).json()

print(f'The page has {len(res["items"])} content elements')
# => The page has 10 content elements
```

### Response samples

- 200
- 401
- 403
- 404
- 410
- 429

Content type

application/json

Copy
Expand all  Collapse all

`{"items": [{"id": "cl-2ZUJuRhNuN",\
\
"type": "line",\
\
"itemContent": {"style": "blockQuote",\
\
"format": "plainText",\
\
"content": "This is a paragraph of text.",\
\
"lineLevel": 0\
\
}\
\
}\
\
],

"href": "https://coda.io/apis/v1/docs/AbCDeFGH/pages/canvas-IjkLmnO/content?limit=20",

"nextPageToken": "eyJsaW1pd",

"nextPageLink": "https://coda.io/apis/v1/docs/AbCDeFGH/pages/canvas-IjkLmnO/content?pageToken=eyJsaW1pd"

}`

## [tag/Pages/operation/deletePageContent](https://coda.io/developers/apis/v1\#tag/Pages/operation/deletePageContent) Delete page content

Delete content from a page. You can delete specific elements by providing their IDs, or delete all content from the page.

##### Authorizations:

_Bearer_

##### path Parameters

|     |     |
| --- | --- |
| docId<br>required | string<br>Example: AbCDeFGH<br>ID of the doc. |
| pageIdOrName<br>required | string<br>Example: canvas-IjkLmnO<br>ID or name of the page. Names are discouraged because they're easily prone to being changed by users. If you're using a name, be sure to URI-encode it. If you provide a name and there are multiple pages with the same name, an arbitrary one will be selected. |

##### Request Body schema: application/json  optional

Parameters for deleting page content.

|     |     |
| --- | --- |
| elementIds | Array of strings<br>IDs of the elements to delete from the page. If omitted or empty, all content will be deleted. |

### Responses

**202**

A result indicating that the deletion was queued for processing.

##### Response Schema: application/json

|     |     |
| --- | --- |
| requestId<br>required | string<br>An arbitrary unique identifier for this request. |
| id<br>required | string<br>ID of the page whose content was deleted. |

**400**

The request parameters did not conform to expectations.

**401**

The API token is invalid or has expired.

**403**

The API token does not grant access to this resource.

**404**

The resource could not be located with the current API token.

**429**

The client has sent too many requests.

delete/docs/{docId}/pages/{pageIdOrName}/content

Coda API (v1)

https://coda.io/apis/v1/docs/{docId}/pages/{pageIdOrName}/content

### Request samples

- Payload
- Python 3.13
- Shell
- Google Apps Script

Content type

application/json

Copy
Expand all  Collapse all

`{"elementIds": ["cl-lzqh0Q0poT",\
\
"cl-abc123def"\
\
]

}`

### Response samples

- 202
- 400
- 401
- 403
- 404
- 429

Content type

application/json

Copy

`{"requestId": "abc-123-def-456",

"id": "canvas-tuVwxYz"

}`

## [tag/Pages/operation/beginPageContentExport](https://coda.io/developers/apis/v1\#tag/Pages/operation/beginPageContentExport) Begin content export

Initiate an export of content for the given page.

##### Authorizations:

_Bearer_

##### path Parameters

|     |     |
| --- | --- |
| docId<br>required | string<br>Example: AbCDeFGH<br>ID of the doc. |
| pageIdOrName<br>required | string<br>Example: canvas-IjkLmnO<br>ID or name of the page. Names are discouraged because they're easily prone to being changed by users. If you're using a name, be sure to URI-encode it. If you provide a name and there are multiple pages with the same name, an arbitrary one will be selected. |

##### Request Body schema: application/json  required

Parameters for requesting a page content export.

|     |     |
| --- | --- |
| outputFormat<br>required | string (PageContentOutputFormat) <br>Enum:"html""markdown"<br>Supported output content formats that can be requested for getting content for an existing page. |

### Responses

**202**

Export page content response.

##### Response Schema: application/json

|     |     |
| --- | --- |
| id<br>required | string<br>The identifier of this export request. |
| status<br>required | string<br>The status of this export. |
| href<br>required | string<br>The URL that reports the status of this export. Poll this URL to get the content URL when the export has completed. |

**400**

The request parameters did not conform to expectations.

**401**

The API token is invalid or has expired.

**403**

The API token does not grant access to this resource.

**404**

The resource could not be located with the current API token.

**410**

The resource has been deleted.

**429**

The client has sent too many requests.

post/docs/{docId}/pages/{pageIdOrName}/export

Coda API (v1)

https://coda.io/apis/v1/docs/{docId}/pages/{pageIdOrName}/export

### Request samples

- Payload
- Python 3.13
- Shell
- Google Apps Script

Content type

application/json

Copy

`{"outputFormat": "html"

}`

### Response samples

- 202
- 400
- 401
- 403
- 404
- 410
- 429

Content type

application/json

Copy

`{"id": "AbCDeFGH",

"status": "complete",

"href": "https://coda.io/apis/v1/docs/somedoc/pages/somepage/export/some-request-id"

}`

## [tag/Pages/operation/getPageContentExportStatus](https://coda.io/developers/apis/v1\#tag/Pages/operation/getPageContentExportStatus) Content export status

Check the status of a page content export

##### Authorizations:

_Bearer_

##### path Parameters

|     |     |
| --- | --- |
| docId<br>required | string<br>Example: AbCDeFGH<br>ID of the doc. |
| pageIdOrName<br>required | string<br>Example: canvas-IjkLmnO<br>ID or name of the page. Names are discouraged because they're easily prone to being changed by users. If you're using a name, be sure to URI-encode it. If you provide a name and there are multiple pages with the same name, an arbitrary one will be selected. |
| requestId<br>required | string<br>Example: abc-123-def-456<br>ID of the request. |

### Responses

**200**

Info about the page content export request.

##### Response Schema: application/json

|     |     |
| --- | --- |
| id<br>required | string<br>The identifier of this export request. |
| status<br>required | string<br>The status of this export. |
| href<br>required | string<br>The URL that reports the status of this export. |
| downloadLink | string<br>Once the export completes, the location where the resulting export file can be downloaded; this link typically expires after a short time. Call this method again to get a fresh link. |
| error | string<br>Message describing an error, if this export failed. |

**401**

The API token is invalid or has expired.

**403**

The API token does not grant access to this resource.

**404**

The resource could not be located with the current API token.

**410**

The resource has been deleted.

**429**

The client has sent too many requests.

get/docs/{docId}/pages/{pageIdOrName}/export/{requestId}

Coda API (v1)

https://coda.io/apis/v1/docs/{docId}/pages/{pageIdOrName}/export/{requestId}

### Request samples

- Python 3.13
- Shell
- Google Apps Script

Copy

```
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = f'https://coda.io/apis/v1/docs/<doc ID>/pages/<page ID>/export/<request ID>'
res = requests.get(uri, headers=headers).json()

print(f'Request status: {res["status"]}')
# => Request status: completed
```

### Response samples

- 200
- 401
- 403
- 404
- 410
- 429

Content type

application/json

Copy

`{"id": "AbCDeFGH",

"status": "complete",

"href": "https://coda.io/apis/v1/docs/somedoc/pages/somepage/export/some-request-id",

"downloadLink": "https://coda.io/blobs/DOC_EXPORT_RENDERING/some-request-id",

"error": "string"

}`

## [tag/Automations](https://coda.io/developers/apis/v1\#tag/Automations) Automations

This API allows you to trigger automations.

## [tag/Automations/operation/triggerWebhookAutomation](https://coda.io/developers/apis/v1\#tag/Automations/operation/triggerWebhookAutomation) Trigger automation

Triggers webhook-invoked automation

##### Authorizations:

_Bearer_

##### path Parameters

|     |     |
| --- | --- |
| docId<br>required | string<br>Example: AbCDeFGH<br>ID of the doc. |
| ruleId<br>required | string<br>Example: grid-auto-b3Jmey6jBS<br>ID of the automation rule. |

##### Request Body schema:   application/jsonapplication/x-www-form-urlencodedtext/plainapplication/json

Payload for webhook

|     |     |
| --- | --- |
| property name\*<br>additional property | any |

### Responses

**202**

A result indicating that the automation trigger was queued for processing.

##### Response Schema: application/json

|     |     |
| --- | --- |
| requestId<br>required | string<br>An arbitrary unique identifier for this request. |

**400**

The request parameters did not conform to expectations.

**401**

The API token is invalid or has expired.

**403**

The API token does not grant access to this resource.

**404**

The resource could not be located with the current API token.

**422**

Unable to process the request.

**429**

The client has sent too many requests.

post/docs/{docId}/hooks/automation/{ruleId}

Coda API (v1)

https://coda.io/apis/v1/docs/{docId}/hooks/automation/{ruleId}

### Request samples

- Payload

Content type

application/jsonapplication/x-www-form-urlencodedtext/plainapplication/json

Copy

`{"message": "The doc that brings words, data, & teams together."

}`

### Response samples

- 202
- 400
- 401
- 403
- 404
- 422
- 429

Content type

application/json

Copy

`{"requestId": "abc-123-def-456"

}`

## [tag/Tables](https://coda.io/developers/apis/v1\#tag/Tables) Tables

## [tag/Tables/operation/listTables](https://coda.io/developers/apis/v1\#tag/Tables/operation/listTables) List tables

Returns a list of tables in a Coda doc.

##### Authorizations:

_Bearer_

##### path Parameters

|     |     |
| --- | --- |
| docId<br>required | string<br>Example: AbCDeFGH<br>ID of the doc. |

##### query Parameters

|     |     |
| --- | --- |
| limit | integer >= 1 <br>Default: 25<br>Example: limit=10<br>Maximum number of results to return in this query. |
| pageToken | string<br>Example: pageToken=eyJsaW1pd<br>An opaque token used to fetch the next page of results. |
| sortBy | string (SortBy) <br>Value:"name"<br>Example: sortBy=name<br>Determines how to sort the given objects. |
| tableTypes | Array of strings (TableType) <br>Items Enum:"table""view"<br>Example: tableTypes=table,view<br>Comma-separated list of table types to include in results. If omitted, includes both tables and views. |

### Responses

**200**

List of tables or views in a doc.

##### Response Schema: application/json

|     |     |
| --- | --- |
| items<br>required | Array of objects (TableReference) |
| href | string <url> <br>API link to these results |
| nextPageToken | string (nextPageToken) <br>If specified, an opaque token used to fetch the next page of results. |
| nextPageLink | string <url> <br>If specified, a link that can be used to fetch the next page of results. |

**401**

The API token is invalid or has expired.

**403**

The API token does not grant access to this resource.

**404**

The resource could not be located with the current API token.

**429**

The client has sent too many requests.

get/docs/{docId}/tables

Coda API (v1)

https://coda.io/apis/v1/docs/{docId}/tables

### Request samples

- Python 3.13
- Shell
- Google Apps Script

Copy

```
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = f'https://coda.io/apis/v1/docs/<doc ID>/tables'
res = requests.get(uri, headers=headers).json()

print(f'The name of the first table is {res["items"][0]["name"]}')
# => The name of the first table is To-do List
```

### Response samples

- 200
- 401
- 403
- 404
- 429

Content type

application/json

Copy
Expand all  Collapse all

`{"items": [{"id": "grid-pqRst-U",\
\
"type": "table",\
\
"tableType": "table",\
\
"href": "https://coda.io/apis/v1/docs/AbCDeFGH/tables/grid-pqRst-U",\
\
"browserLink": "https://coda.io/d/_dAbCDeFGH/#Teams-and-Tasks_tpqRst-U",\
\
"name": "Tasks",\
\
"parent": {"id": "canvas-IjkLmnO",\
\
"type": "page",\
\
"href": "https://coda.io/apis/v1/docs/AbCDeFGH/pages/canvas-IjkLmnO",\
\
"browserLink": "https://coda.io/d/_dAbCDeFGH/Launch-Status_sumnO",\
\
"name": "Launch Status"\
\
}\
\
}\
\
],

"href": "https://coda.io/apis/v1/docs/AbCDeFGH/tables?limit=20",

"nextPageToken": "eyJsaW1pd",

"nextPageLink": "https://coda.io/apis/v1/docs/AbCDeFGH/tables?pageToken=eyJsaW1pd"

}`

## [tag/Tables/operation/getTable](https://coda.io/developers/apis/v1\#tag/Tables/operation/getTable) Get a table

Returns details about a specific table or view.

##### Authorizations:

_Bearer_

##### path Parameters

|     |     |
| --- | --- |
| docId<br>required | string<br>Example: AbCDeFGH<br>ID of the doc. |
| tableIdOrName<br>required | string<br>Example: grid-pqRst-U<br>ID or name of the table. Names are discouraged because they're easily prone to being changed by users. If you're using a name, be sure to URI-encode it. |

##### query Parameters

|     |     |
| --- | --- |
| useUpdatedTableLayouts | boolean<br>Return "detail" and "form" for the `layout` field of detail and form layouts respectively (instead of "masterDetail" for both) |

### Responses

**200**

Info about a table.

##### Response Schema: application/json

|     |     |
| --- | --- |
| id<br>required | string<br>ID of the table. |
| type<br>required | string<br>Value:"table"<br>The type of this resource. |
| tableType<br>required | string (TableType) <br>Enum:"table""view" |
| href<br>required | string <url> <br>API link to the table. |
| name<br>required | string<br>Name of the table. |
| parent<br>required | object (PageReference) <br>Reference to a page. |
| browserLink<br>required | string <url> <br>Browser-friendly link to the table. |
| displayColumn<br>required | object (ColumnReference) <br>Reference to a column. |
| rowCount<br>required | integer<br>Total number of rows in the table. |
| sorts<br>required | Array of objects (Sort) <br>Any sorts applied to the table. |
| layout<br>required | string (Layout) <br>Enum:"default""areaChart""barChart""bubbleChart""calendar""card""detail""form""ganttChart""lineChart""masterDetail""pieChart""scatterChart""slide""wordCloud"<br>Layout type of the table or view. |
| createdAt<br>required | string <date-time> <br>Timestamp for when the table was created. |
| updatedAt<br>required | string <date-time> <br>Timestamp for when the table was last modified. |
| parentTable | object (TableReference) <br>Reference to a table or view. |
| filter | object<br>Detailed information about the filter formula for the table, if applicable. |

**401**

The API token is invalid or has expired.

**403**

The API token does not grant access to this resource.

**404**

The resource could not be located with the current API token.

**429**

The client has sent too many requests.

get/docs/{docId}/tables/{tableIdOrName}

Coda API (v1)

https://coda.io/apis/v1/docs/{docId}/tables/{tableIdOrName}

### Request samples

- Python 3.13
- Shell
- Google Apps Script

Copy

```
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = f'https://coda.io/apis/v1/docs/<doc ID>/tables/<table ID>'
res = requests.get(uri, headers=headers).json()

print(f'Table {res["name"]} has {res["rowCount"]} rows')
# => Table To-do List has 2 rows
```

### Response samples

- 200
- 401
- 403
- 404
- 429

Content type

application/json

Copy
Expand all  Collapse all

`{"id": "grid-pqRst-U",

"type": "table",

"tableType": "table",

"href": "https://coda.io/apis/v1/docs/AbCDeFGH/tables/grid-pqRst-U",

"browserLink": "https://coda.io/d/_dAbCDeFGH/#Teams-and-Tasks_tpqRst-U",

"name": "Tasks",

"parent": {"id": "canvas-IjkLmnO",

"type": "page",

"href": "https://coda.io/apis/v1/docs/AbCDeFGH/pages/canvas-IjkLmnO",

"browserLink": "https://coda.io/d/_dAbCDeFGH/Launch-Status_sumnO",

"name": "Launch Status"

},

"parentTable": {"id": "grid-pqRst-U",

"type": "table",

"tableType": "table",

"href": "https://coda.io/apis/v1/docs/AbCDeFGH/tables/grid-pqRst-U",

"browserLink": "https://coda.io/d/_dAbCDeFGH/#Teams-and-Tasks_tpqRst-U",

"name": "Tasks",

"parent": {"id": "canvas-IjkLmnO",

"type": "page",

"href": "https://coda.io/apis/v1/docs/AbCDeFGH/pages/canvas-IjkLmnO",

"browserLink": "https://coda.io/d/_dAbCDeFGH/Launch-Status_sumnO",

"name": "Launch Status"

}

},

"displayColumn": {"id": "c-tuVwxYz",

"type": "column",

"href": "https://coda.io/apis/v1/docs/AbCDeFGH/tables/grid-pqRst-U/columns/c-tuVwxYz"

},

"rowCount": 130,

"sorts": [{"column": {"id": "c-tuVwxYz",\
\
"type": "column",\
\
"href": "https://coda.io/apis/v1/docs/AbCDeFGH/tables/grid-pqRst-U/columns/c-tuVwxYz"\
\
},\
\
"direction": "ascending"\
\
}\
\
],

"layout": "default",

"filter": {"valid": true,

"isVolatile": false,

"hasUserFormula": false,

"hasTodayFormula": false,

"hasNowFormula": false

},

"createdAt": "2018-04-11T00:18:57.946Z",

"updatedAt": "2018-04-11T00:18:57.946Z"

}`

## [tag/Columns](https://coda.io/developers/apis/v1\#tag/Columns) Columns

While columns in Coda have user-friendly names, they also have immutable IDs that are used when reading and writing rows. These endpoints let you query the columns in a table and get basic information about them.

## [tag/Columns/operation/listColumns](https://coda.io/developers/apis/v1\#tag/Columns/operation/listColumns) List columns

Returns a list of columns in a table.

##### Authorizations:

_Bearer_

##### path Parameters

|     |     |
| --- | --- |
| docId<br>required | string<br>Example: AbCDeFGH<br>ID of the doc. |
| tableIdOrName<br>required | string<br>Example: grid-pqRst-U<br>ID or name of the table. Names are discouraged because they're easily prone to being changed by users. If you're using a name, be sure to URI-encode it. |

##### query Parameters

|     |     |
| --- | --- |
| limit | integer \[ 1 .. 100 \] <br>Default: 25<br>Example: limit=10<br>Maximum number of results to return in this query. |
| pageToken | string<br>Example: pageToken=eyJsaW1pd<br>An opaque token used to fetch the next page of results. |
| visibleOnly | boolean<br>Example: visibleOnly=true<br>If true, returns only visible columns for the table. This parameter only applies to base tables, and not views. |

### Responses

**200**

List of columns in the table.

##### Response Schema: application/json

|     |     |
| --- | --- |
| items<br>required | Array of objects (Column) |
| href | string <url> <br>API link to these results |
| nextPageToken | string (nextPageToken) <br>If specified, an opaque token used to fetch the next page of results. |
| nextPageLink | string <url> <br>If specified, a link that can be used to fetch the next page of results. |

**401**

The API token is invalid or has expired.

**403**

The API token does not grant access to this resource.

**404**

The resource could not be located with the current API token.

**429**

The client has sent too many requests.

get/docs/{docId}/tables/{tableIdOrName}/columns

Coda API (v1)

https://coda.io/apis/v1/docs/{docId}/tables/{tableIdOrName}/columns

### Request samples

- Python 3.13
- Shell
- Google Apps Script

Copy

```
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = f'https://coda.io/apis/v1/docs/<doc ID>/tables/<table ID>/columns'
res = requests.get(uri, headers=headers).json()

print(f'This table\'s columns: {", ".join(c["name"] for c in res["items"])}')
# => This table's columns: Task, Duration (hr), Duration (min)
```

### Response samples

- 200
- 401
- 403
- 404
- 429

Content type

application/json

Copy
Expand all  Collapse all

`{"items": [{"id": "c-tuVwxYz",\
\
"type": "column",\
\
"href": "https://coda.io/apis/v1/docs/AbCDeFGH/tables/grid-pqRst-U/columns/c-tuVwxYz",\
\
"name": "Completed",\
\
"display": true,\
\
"calculated": true,\
\
"formula": "thisRow.Created()",\
\
"defaultValue": "Test",\
\
"format": {"type": "text",\
\
"isArray": true,\
\
"label": "Click me",\
\
"disableIf": "False()",\
\
"action": "OpenUrl(\"www.google.com\")"\
\
}\
\
}\
\
],

"href": "https://coda.io/apis/v1/docs/AbCDeFGH/tables/grid-pqRst-U/columns?limit=20",

"nextPageToken": "eyJsaW1pd",

"nextPageLink": "https://coda.io/apis/v1/docs/AbCDeFGH/tables/grid-pqRst-U/columns?pageToken=eyJsaW1pd"

}`

## [tag/Columns/operation/getColumn](https://coda.io/developers/apis/v1\#tag/Columns/operation/getColumn) Get a column

Returns details about a column in a table.

##### Authorizations:

_Bearer_

##### path Parameters

|     |     |
| --- | --- |
| docId<br>required | string<br>Example: AbCDeFGH<br>ID of the doc. |
| tableIdOrName<br>required | string<br>Example: grid-pqRst-U<br>ID or name of the table. Names are discouraged because they're easily prone to being changed by users. If you're using a name, be sure to URI-encode it. |
| columnIdOrName<br>required | string<br>Example: c-tuVwxYz<br>ID or name of the column. Names are discouraged because they're easily prone to being changed by users. If you're using a name, be sure to URI-encode it. |

### Responses

**200**

Info about a column.

##### Response Schema: application/json

|     |     |
| --- | --- |
| id<br>required | string<br>ID of the column. |
| type<br>required | string<br>Value:"column"<br>The type of this resource. |
| href<br>required | string <url> <br>API link to the column. |
| name<br>required | string<br>Name of the column. |
| parent<br>required | object (TableReference) <br>Reference to a table or view. |
| format<br>required | any (ColumnFormat) <br>Format of a column. |
| display | boolean<br>Whether the column is the display column. |
| calculated | boolean<br>Whether the column has a formula set on it. |
| formula | string<br>Formula on the column. |
| defaultValue | string<br>Default value formula for the column. |

**401**

The API token is invalid or has expired.

**403**

The API token does not grant access to this resource.

**404**

The resource could not be located with the current API token.

**429**

The client has sent too many requests.

get/docs/{docId}/tables/{tableIdOrName}/columns/{columnIdOrName}

Coda API (v1)

https://coda.io/apis/v1/docs/{docId}/tables/{tableIdOrName}/columns/{columnIdOrName}

### Request samples

- Python 3.13
- Shell
- Google Apps Script

Copy

```
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = f'https://coda.io/apis/v1/docs/<doc ID>/tables/<table ID>/columns/<column ID>'
res = requests.get(uri, headers=headers).json()

is_default = res.get("display", False)
print(f'Column {res["name"]} {"is" if is_default else "is not"} the display column')
# => Column Task is the display column
```

### Response samples

- 200
- 401
- 403
- 404
- 429

Content type

application/json

Copy
Expand all  Collapse all

`{"id": "c-tuVwxYz",

"type": "column",

"href": "https://coda.io/apis/v1/docs/AbCDeFGH/tables/grid-pqRst-U/columns/c-tuVwxYz",

"name": "Completed",

"display": true,

"calculated": true,

"formula": "thisRow.Created()",

"defaultValue": "Test",

"format": {"type": "text",

"isArray": true,

"label": "Click me",

"disableIf": "False()",

"action": "OpenUrl(\"www.google.com\")"

},

"parent": {"id": "grid-pqRst-U",

"type": "table",

"tableType": "table",

"href": "https://coda.io/apis/v1/docs/AbCDeFGH/tables/grid-pqRst-U",

"browserLink": "https://coda.io/d/_dAbCDeFGH/#Teams-and-Tasks_tpqRst-U",

"name": "Tasks",

"parent": {"id": "canvas-IjkLmnO",

"type": "page",

"href": "https://coda.io/apis/v1/docs/AbCDeFGH/pages/canvas-IjkLmnO",

"browserLink": "https://coda.io/d/_dAbCDeFGH/Launch-Status_sumnO",

"name": "Launch Status"

}

}

}`

## [tag/Rows](https://coda.io/developers/apis/v1\#tag/Rows) Rows

You'll likely use this part of the API the most. These endpoints let you retrieve row data from tables in Coda as well as create, upsert, update, and delete them. Most of these endpoints work for both base tables and views, but for inserting/upsering rows, you must use a base table.

## [tag/Rows/operation/listRows](https://coda.io/developers/apis/v1\#tag/Rows/operation/listRows) List table rows

Returns a list of rows in a table.

### Value results

The `valueFormat` parameter dictates in what format the API should return values for individual cells.

- `simple` (default): Returns cell values as the following JSON values: `string`, `number`, or `boolean`. Array values (like multiselects) are returned as comma-delimited strings.
- `simpleWithArrays`: Singleton values are returned as `simple`. Array values are returned as JSON arrays and the values within are `simple` values (including nested arrays).
- `rich`: If applicable, returns many values with further encoding, allowing API users to have lossless access to data in Coda.

  - For `text` values, returns data in Markdown syntax. If the text field is simple text (e.g. has no formatting),
    the field will be fully escaped with triple-ticks. E.g
    \`

`This is plain text`
\`

  - For `currency`, `lookup`, `image`, `person` and `hyperlink` values, the value will be encoded in [JSON-LD](https://json-ld.org/) format.

```
  // Currency
  {
    "@context": "http://schema.org",
    "@type": "MonetaryAmount",
    "currency": "USD",
    "amount": 42.42
  }

  // Lookup
  {
    "@context": "http://schema.org",
    "@type": "StructuredValue",
    "additionalType": "row",
    "name": "Row Name",
    "rowId": "i-123456789",
    "tableId": "grid-123456789",
    "tableUrl": "https://coda.io/d/_d123456789/grid-123456789",
    "url": "https://coda.io/d/_d123456789/grid-123456789#_r42",
  }

  // Hyperlink
  {
    "@context": "http://schema.org",
    "@type": "WebPage",
    "name": "Coda",
    "url": "https://coda.io"
  }

  // Image
  {
    "@context": "http://schema.org",
    "@type": "ImageObject",
    "name": "Coda logo",
    "url": "https://coda.io/logo.jpg"
  }

  // People
  {
    "@context": "http://schema.org",
    "@type": "Person",
    "name": "Art Vandalay",
    "email": "art@vandalayindustries.com"
  }
```

##### Authorizations:

_Bearer_

##### path Parameters

|     |     |
| --- | --- |
| docId<br>required | string<br>Example: AbCDeFGH<br>ID of the doc. |
| tableIdOrName<br>required | string<br>Example: grid-pqRst-U<br>ID or name of the table. Names are discouraged because they're easily prone to being changed by users. If you're using a name, be sure to URI-encode it. |

##### query Parameters

|     |     |
| --- | --- |
| query | string<br>Example: query=c-tuVwxYz:"Apple"<br>Query used to filter returned rows, specified as `<column_id_or_name>:<value>`. If you'd like to use a column name instead of an ID, you must quote it (e.g., `"My Column":123`). Also note that `value` is a JSON value; if you'd like to use a string, you must surround it in quotes (e.g., `"groceries"`). |
| sortBy | string (RowsSortBy) <br>Enum:"createdAt""natural""updatedAt"<br>Specifies the sort order of the rows returned. If left unspecified, rows are returned by creation time ascending. "UpdatedAt" sort ordering is the order of rows based upon when they were last updated. This does not include updates to calculated values. "Natural" sort ordering is the order that the rows appear in the table view in the application. This ordering is only meaningfully defined for rows that are visible (unfiltered). Because of this, using this sort order will imply visibleOnly=true, that is, to only return visible rows. If you pass sortBy=natural and visibleOnly=false explicitly, this will result in a Bad Request error as this condition cannot be satisfied. |
| useColumnNames | boolean<br>Example: useColumnNames=true<br>Use column names instead of column IDs in the returned output. This is generally discouraged as it is fragile. If columns are renamed, code using original names may throw errors. |
| valueFormat | string (ValueFormat) <br>Enum:"simple""simpleWithArrays""rich"<br>The format that cell values are returned as. |
| visibleOnly | boolean<br>Example: visibleOnly=true<br>If true, returns only visible rows and columns for the table. |
| limit | integer >= 1 <br>Default: 25<br>Example: limit=10<br>Maximum number of results to return in this query. |
| pageToken | string<br>Example: pageToken=eyJsaW1pd<br>An opaque token used to fetch the next page of results. |
| syncToken | string<br>Example: syncToken=eyJsaW1pd<br>An opaque token returned from a previous call that can be used to return results that are relevant to the query since the call where the syncToken was generated. |

### Responses

**200**

List of rows in the table.

##### Response Schema: application/json

|     |     |
| --- | --- |
| items<br>required | Array of objects (Row) |
| href | string <url> <br>API link to these results |
| nextPageToken | string (nextPageToken) <br>If specified, an opaque token used to fetch the next page of results. |
| nextPageLink | string <url> <br>If specified, a link that can be used to fetch the next page of results. |
| nextSyncToken | string (nextSyncToken) <br>If specified, an opaque token that can be passed back later to retrieve new results that match the parameters specified when the sync token was created. |

**400**

The request parameters did not conform to expectations.

**401**

The API token is invalid or has expired.

**403**

The API token does not grant access to this resource.

**404**

The resource could not be located with the current API token.

**429**

The client has sent too many requests.

get/docs/{docId}/tables/{tableIdOrName}/rows

Coda API (v1)

https://coda.io/apis/v1/docs/{docId}/tables/{tableIdOrName}/rows

### Request samples

- Python 3.13
- Shell
- Google Apps Script

Copy

```
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = f'https://coda.io/apis/v1/docs/<doc ID>/tables/<table ID>/rows'
params = {
  'query': '<column ID>:"Work out"',
}
req = requests.get(uri, headers=headers, params=params)
req.raise_for_status() # Throw if there was an error.
res = req.json()

print(f'Matching rows: {len(res["items"])}')
# => Matching rows: 1
```

### Response samples

- 200
- 400
- 401
- 403
- 404
- 429

Content type

application/json

Copy
Expand all  Collapse all

`{"items": [{"id": "i-tuVwxYz",\
\
"type": "row",\
\
"href": "https://coda.io/apis/v1/docs/AbCDeFGH/tables/grid-pqRst-U/rows/i-RstUv-W",\
\
"name": "Apple",\
\
"index": 7,\
\
"browserLink": "https://coda.io/d/_dAbCDeFGH#Teams-and-Tasks_tpqRst-U/_rui-tuVwxYz",\
\
"createdAt": "2018-04-11T00:18:57.946Z",\
\
"updatedAt": "2018-04-11T00:18:57.946Z",\
\
"values": {"c-tuVwxYz": "Apple",\
\
"c-bCdeFgh": ["$12.34",\
\
"$56.78"\
\
]\
\
}\
\
}\
\
],

"href": "https://coda.io/apis/v1/docs/AbCDeFGH/tables/grid-pqRst-U/rows?limit=20",

"nextPageToken": "eyJsaW1pd",

"nextPageLink": "https://coda.io/apis/v1/docs/AbCDeFGH/tables/grid-pqRst-U/rows?pageToken=eyJsaW1pd",

"nextSyncToken": "eyJsaW1pd"

}`

## [tag/Rows/operation/upsertRows](https://coda.io/developers/apis/v1\#tag/Rows/operation/upsertRows) Insert/upsert rows

Inserts rows into a table, optionally updating existing rows if any upsert key columns are provided. This endpoint will always return a 202, so long as the doc and table exist and are accessible (and the update is structurally valid). Row inserts/upserts are generally processed within several seconds. Note: this endpoint only works for base tables, not views.
When upserting, if multiple rows match the specified key column(s), they will all be updated with the specified value.

##### Authorizations:

_Bearer_

##### path Parameters

|     |     |
| --- | --- |
| docId<br>required | string<br>Example: AbCDeFGH<br>ID of the doc. |
| tableIdOrName<br>required | string<br>Example: grid-pqRst-U<br>ID or name of the table. Names are discouraged because they're easily prone to being changed by users. If you're using a name, be sure to URI-encode it. |

##### query Parameters

|     |     |
| --- | --- |
| disableParsing | boolean<br>Example: disableParsing=true<br>If true, the API will not attempt to parse the data in any way. |

##### Request Body schema: application/json  required

Rows to insert or upsert.

|     |     |
| --- | --- |
| rows<br>required | Array of objects (RowEdit) |
| keyColumns | Array of strings<br>Optional column IDs, URLs, or names (fragile and discouraged), specifying columns to be used as upsert keys. |

### Responses

**202**

A result indicating that the upsert was queued for processing.

##### Response Schema: application/json

|     |     |
| --- | --- |
| requestId<br>required | string<br>An arbitrary unique identifier for this request. |
| addedRowIds | Array of strings<br>Row IDs for rows that will be added. Only applicable when keyColumns is not set or empty. |

**400**

The request parameters did not conform to expectations.

**401**

The API token is invalid or has expired.

**403**

The API token does not grant access to this resource.

**404**

The resource could not be located with the current API token.

**429**

The client has sent too many requests.

post/docs/{docId}/tables/{tableIdOrName}/rows

Coda API (v1)

https://coda.io/apis/v1/docs/{docId}/tables/{tableIdOrName}/rows

### Request samples

- Payload
- Python 3.13
- Shell
- Google Apps Script

Content type

application/json

Copy
Expand all  Collapse all

`{"rows": [{"cells": [{"column": "c-tuVwxYz",\
\
"value": "$12.34"\
\
}\
\
]\
\
}\
\
],

"keyColumns": ["c-bCdeFgh"\
\
]

}`

### Response samples

- 202
- 400
- 401
- 403
- 404
- 429

Content type

application/json

Copy
Expand all  Collapse all

`{"requestId": "abc-123-def-456",

"addedRowIds": ["i-bCdeFgh",\
\
"i-CdEfgHi"\
\
]

}`

## [tag/Rows/operation/deleteRows](https://coda.io/developers/apis/v1\#tag/Rows/operation/deleteRows) Delete multiple rows

Deletes the specified rows from the table or view. This endpoint will always return a 202. Row deletions are generally processed within several seconds.

##### Authorizations:

_Bearer_

##### path Parameters

|     |     |
| --- | --- |
| docId<br>required | string<br>Example: AbCDeFGH<br>ID of the doc. |
| tableIdOrName<br>required | string<br>Example: grid-pqRst-U<br>ID or name of the table. Names are discouraged because they're easily prone to being changed by users. If you're using a name, be sure to URI-encode it. |

##### Request Body schema: application/json  required

Rows to delete.

|     |     |
| --- | --- |
| rowIds<br>required | Array of strings<br>Row IDs to delete. |

### Responses

**202**

A result indicating that the delete was queued for processing.

##### Response Schema: application/json

|     |     |
| --- | --- |
| requestId<br>required | string<br>An arbitrary unique identifier for this request. |
| rowIds<br>required | Array of strings<br>Row IDs to delete. |

**400**

The request parameters did not conform to expectations.

**401**

The API token is invalid or has expired.

**403**

The API token does not grant access to this resource.

**404**

The resource could not be located with the current API token.

**429**

The client has sent too many requests.

delete/docs/{docId}/tables/{tableIdOrName}/rows

Coda API (v1)

https://coda.io/apis/v1/docs/{docId}/tables/{tableIdOrName}/rows

### Request samples

- Payload
- Python 3.13
- Shell
- Google Apps Script

Content type

application/json

Copy
Expand all  Collapse all

`{"rowIds": ["i-bCdeFgh",\
\
"i-CdEfgHi"\
\
]

}`

### Response samples

- 202
- 400
- 401
- 403
- 404
- 429

Content type

application/json

Copy
Expand all  Collapse all

`{"requestId": "abc-123-def-456",

"rowIds": ["i-bCdeFgh",\
\
"i-CdEfgHi"\
\
]

}`

## [tag/Rows/operation/getRow](https://coda.io/developers/apis/v1\#tag/Rows/operation/getRow) Get a row

Returns details about a row in a table.

##### Authorizations:

_Bearer_

##### path Parameters

|     |     |
| --- | --- |
| docId<br>required | string<br>Example: AbCDeFGH<br>ID of the doc. |
| tableIdOrName<br>required | string<br>Example: grid-pqRst-U<br>ID or name of the table. Names are discouraged because they're easily prone to being changed by users. If you're using a name, be sure to URI-encode it. |
| rowIdOrName<br>required | string<br>Example: i-tuVwxYz<br>ID or name of the row. Names are discouraged because they're easily prone to being changed by users. If you're using a name, be sure to URI-encode it. If there are multiple rows with the same value in the identifying column, an arbitrary one will be selected. |

##### query Parameters

|     |     |
| --- | --- |
| useColumnNames | boolean<br>Example: useColumnNames=true<br>Use column names instead of column IDs in the returned output. This is generally discouraged as it is fragile. If columns are renamed, code using original names may throw errors. |
| valueFormat | string (ValueFormat) <br>Enum:"simple""simpleWithArrays""rich"<br>The format that cell values are returned as. |

### Responses

**200**

Info about a row. If this row was retrieved by name, only one matching row will be returned, with no guarantees as to which one it is.

##### Response Schema: application/json

|     |     |
| --- | --- |
| id<br>required | string<br>ID of the row. |
| type<br>required | string<br>Value:"row"<br>The type of this resource. |
| href<br>required | string <url> <br>API link to the row. |
| name<br>required | string<br>The display name of the row, based on its identifying column. |
| index<br>required | integer<br>Index of the row within the table. |
| browserLink<br>required | string <url> <br>Browser-friendly link to the row. |
| createdAt<br>required | string <date-time> <br>Timestamp for when the row was created. |
| updatedAt<br>required | string <date-time> <br>Timestamp for when the row was last modified. |
| values<br>required | object<br>Values for a specific row, represented as a hash of column IDs (or names with `useColumnNames`) to values. |
| parent<br>required | object (TableReference) <br>Reference to a table or view. |

**401**

The API token is invalid or has expired.

**403**

The API token does not grant access to this resource.

**404**

The resource could not be located with the current API token.

**429**

The client has sent too many requests.

get/docs/{docId}/tables/{tableIdOrName}/rows/{rowIdOrName}

Coda API (v1)

https://coda.io/apis/v1/docs/{docId}/tables/{tableIdOrName}/rows/{rowIdOrName}

### Request samples

- Python 3.13
- Shell
- Google Apps Script

Copy

```
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = f'https://coda.io/apis/v1/docs/<doc ID>/tables/<table ID>/rows/<row ID>'
req = requests.get(uri, headers=headers)
req.raise_for_status() # Throw if there was an error.
res = req.json()

print(f'Row values are: {", ".join(str(v) for v in res["values"].values())}')
# => Row values are: Get groceries, 1, 60
```

### Response samples

- 200
- 401
- 403
- 404
- 429

Content type

application/json

Copy
Expand all  Collapse all

`{"id": "i-tuVwxYz",

"type": "row",

"href": "https://coda.io/apis/v1/docs/AbCDeFGH/tables/grid-pqRst-U/rows/i-RstUv-W",

"name": "Apple",

"index": 7,

"browserLink": "https://coda.io/d/_dAbCDeFGH#Teams-and-Tasks_tpqRst-U/_rui-tuVwxYz",

"createdAt": "2018-04-11T00:18:57.946Z",

"updatedAt": "2018-04-11T00:18:57.946Z",

"values": {"c-tuVwxYz": "Apple",

"c-bCdeFgh": ["$12.34",\
\
"$56.78"\
\
]

},

"parent": {"id": "grid-pqRst-U",

"type": "table",

"tableType": "table",

"href": "https://coda.io/apis/v1/docs/AbCDeFGH/tables/grid-pqRst-U",

"browserLink": "https://coda.io/d/_dAbCDeFGH/#Teams-and-Tasks_tpqRst-U",

"name": "Tasks",

"parent": {"id": "canvas-IjkLmnO",

"type": "page",

"href": "https://coda.io/apis/v1/docs/AbCDeFGH/pages/canvas-IjkLmnO",

"browserLink": "https://coda.io/d/_dAbCDeFGH/Launch-Status_sumnO",

"name": "Launch Status"

}

}

}`

## [tag/Rows/operation/updateRow](https://coda.io/developers/apis/v1\#tag/Rows/operation/updateRow) Update row

Updates the specified row in the table. This endpoint will always return a 202, so long as the row exists and is accessible (and the update is structurally valid). Row updates are generally processed within several seconds. When updating using a name as opposed to an ID, an arbitrary row will be affected.

##### Authorizations:

_Bearer_

##### path Parameters

|     |     |
| --- | --- |
| docId<br>required | string<br>Example: AbCDeFGH<br>ID of the doc. |
| tableIdOrName<br>required | string<br>Example: grid-pqRst-U<br>ID or name of the table. Names are discouraged because they're easily prone to being changed by users. If you're using a name, be sure to URI-encode it. |
| rowIdOrName<br>required | string<br>Example: i-tuVwxYz<br>ID or name of the row. Names are discouraged because they're easily prone to being changed by users. If you're using a name, be sure to URI-encode it. If there are multiple rows with the same value in the identifying column, an arbitrary one will be selected. |

##### query Parameters

|     |     |
| --- | --- |
| disableParsing | boolean<br>Example: disableParsing=true<br>If true, the API will not attempt to parse the data in any way. |

##### Request Body schema: application/json  required

Row update.

|     |     |
| --- | --- |
| row<br>required | object (RowEdit) <br>An edit made to a particular row. |

### Responses

**202**

A result indicating that the update was queued for processing.

##### Response Schema: application/json

|     |     |
| --- | --- |
| requestId<br>required | string<br>An arbitrary unique identifier for this request. |
| id<br>required | string<br>ID of the updated row. |

**400**

The request parameters did not conform to expectations.

**401**

The API token is invalid or has expired.

**403**

The API token does not grant access to this resource.

**404**

The resource could not be located with the current API token.

**429**

The client has sent too many requests.

put/docs/{docId}/tables/{tableIdOrName}/rows/{rowIdOrName}

Coda API (v1)

https://coda.io/apis/v1/docs/{docId}/tables/{tableIdOrName}/rows/{rowIdOrName}

### Request samples

- Payload
- Python 3.13
- Shell
- Google Apps Script

Content type

application/json

Copy
Expand all  Collapse all

`{"row": {"cells": [{"column": "c-tuVwxYz",\
\
"value": "$12.34"\
\
}\
\
]

}

}`

### Response samples

- 202
- 400
- 401
- 403
- 404
- 429

Content type

application/json

Copy

`{"requestId": "abc-123-def-456",

"id": "i-tuVwxYz"

}`

## [tag/Rows/operation/deleteRow](https://coda.io/developers/apis/v1\#tag/Rows/operation/deleteRow) Delete row

Deletes the specified row from the table or view. This endpoint will always return a 202, so long as the row exists and is accessible (and the update is structurally valid). Row deletions are generally processed within several seconds. When deleting using a name as opposed to an ID, an arbitrary row will be removed.

##### Authorizations:

_Bearer_

##### path Parameters

|     |     |
| --- | --- |
| docId<br>required | string<br>Example: AbCDeFGH<br>ID of the doc. |
| tableIdOrName<br>required | string<br>Example: grid-pqRst-U<br>ID or name of the table. Names are discouraged because they're easily prone to being changed by users. If you're using a name, be sure to URI-encode it. |
| rowIdOrName<br>required | string<br>Example: i-tuVwxYz<br>ID or name of the row. Names are discouraged because they're easily prone to being changed by users. If you're using a name, be sure to URI-encode it. If there are multiple rows with the same value in the identifying column, an arbitrary one will be selected. |

### Responses

**202**

A result indicating that the deletion was queued for processing.

##### Response Schema: application/json

|     |     |
| --- | --- |
| requestId<br>required | string<br>An arbitrary unique identifier for this request. |
| id<br>required | string<br>ID of the row to be deleted. |

**401**

The API token is invalid or has expired.

**403**

The API token does not grant access to this resource.

**404**

The resource could not be located with the current API token.

**429**

The client has sent too many requests.

delete/docs/{docId}/tables/{tableIdOrName}/rows/{rowIdOrName}

Coda API (v1)

https://coda.io/apis/v1/docs/{docId}/tables/{tableIdOrName}/rows/{rowIdOrName}

### Request samples

- Python 3.13
- Shell
- Google Apps Script

Copy

```
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = f'https://coda.io/apis/v1/docs/<doc ID>/tables/<table ID>/rows/<row ID>'
req = requests.delete(uri, headers=headers)
req.raise_for_status() # Throw if there was an error.
res = req.json()

print(f'Deleted row {res["id"]}')
# => Deleted row <row ID>
```

### Response samples

- 202
- 401
- 403
- 404
- 429

Content type

application/json

Copy

`{"requestId": "abc-123-def-456",

"id": "i-tuVwxYz"

}`

## [tag/Rows/operation/pushButton](https://coda.io/developers/apis/v1\#tag/Rows/operation/pushButton) Push a button

Pushes a button on a row in a table.
Authorization note: This action is available to API tokens that are authorized to write to the table. However, the underlying button can perform any action on the document, including writing to other tables and performing Pack actions.

##### Authorizations:

_Bearer_

##### path Parameters

|     |     |
| --- | --- |
| docId<br>required | string<br>Example: AbCDeFGH<br>ID of the doc. |
| tableIdOrName<br>required | string<br>Example: grid-pqRst-U<br>ID or name of the table. Names are discouraged because they're easily prone to being changed by users. If you're using a name, be sure to URI-encode it. |
| rowIdOrName<br>required | string<br>Example: i-tuVwxYz<br>ID or name of the row. Names are discouraged because they're easily prone to being changed by users. If you're using a name, be sure to URI-encode it. If there are multiple rows with the same value in the identifying column, an arbitrary one will be selected. |
| columnIdOrName<br>required | string<br>Example: c-tuVwxYz<br>ID or name of the column. Names are discouraged because they're easily prone to being changed by users. If you're using a name, be sure to URI-encode it. |

### Responses

**202**

A result indicating that the push button action was queued for processing.

##### Response Schema: application/json

|     |     |
| --- | --- |
| requestId<br>required | string<br>An arbitrary unique identifier for this request. |
| rowId<br>required | string<br>ID of the row where the button exists. |
| columnId<br>required | string<br>ID of the column where the button exists. |

**400**

The request parameters did not conform to expectations.

**401**

The API token is invalid or has expired.

**403**

The API token does not grant access to this resource.

**404**

The resource could not be located with the current API token.

**429**

The client has sent too many requests.

post/docs/{docId}/tables/{tableIdOrName}/rows/{rowIdOrName}/buttons/{columnIdOrName}

Coda API (v1)

https://coda.io/apis/v1/docs/{docId}/tables/{tableIdOrName}/rows/{rowIdOrName}/buttons/{columnIdOrName}

### Request samples

- Python 3.13
- Shell
- Google Apps Script

Copy

```
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = f'https://coda.io/apis/v1/docs/<doc ID>/tables/<table ID>/rows/<row ID>/buttons/<column ID>'
req = requests.post(uri, headers=headers)
req.raise_for_status() # Throw if there was an error.
res = req.json()
print(f'Pushed button')
# => Pushed button
```

### Response samples

- 202
- 400
- 401
- 403
- 404
- 429

Content type

application/json

Copy

`{"requestId": "abc-123-def-456",

"rowId": "i-tuVwxYz",

"columnId": "i-tuVwxYz"

}`

## [tag/Formulas](https://coda.io/developers/apis/v1\#tag/Formulas) Formulas

Formulas can be great for performing one-off computations, or used with tables and other formulas to compute a single value. With this API, you can discover formulas in a doc and obtain computed results.

## [tag/Formulas/operation/listFormulas](https://coda.io/developers/apis/v1\#tag/Formulas/operation/listFormulas) List formulas

Returns a list of named formulas in a Coda doc.

##### Authorizations:

_Bearer_

##### path Parameters

|     |     |
| --- | --- |
| docId<br>required | string<br>Example: AbCDeFGH<br>ID of the doc. |

##### query Parameters

|     |     |
| --- | --- |
| limit | integer >= 1 <br>Default: 25<br>Example: limit=10<br>Maximum number of results to return in this query. |
| pageToken | string<br>Example: pageToken=eyJsaW1pd<br>An opaque token used to fetch the next page of results. |
| sortBy | string (SortBy) <br>Value:"name"<br>Example: sortBy=name<br>Determines how to sort the given objects. |

### Responses

**200**

List of formulas that have names in a doc.

##### Response Schema: application/json

|     |     |
| --- | --- |
| items<br>required | Array of objects (FormulaReference) |
| href | string <url> <br>API link to these results |
| nextPageToken | string (nextPageToken) <br>If specified, an opaque token used to fetch the next page of results. |
| nextPageLink | string <url> <br>If specified, a link that can be used to fetch the next page of results. |

**401**

The API token is invalid or has expired.

**403**

The API token does not grant access to this resource.

**404**

The resource could not be located with the current API token.

**429**

The client has sent too many requests.

get/docs/{docId}/formulas

Coda API (v1)

https://coda.io/apis/v1/docs/{docId}/formulas

### Request samples

- Python 3.13
- Shell
- Google Apps Script

Copy

```
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = f'https://coda.io/apis/v1/docs/<doc ID>/formulas'
res = requests.get(uri, headers=headers).json()

print(f'This doc\'s formulas are: {", ".join(i["name"] for i in res["items"])}')
# => This doc's formulas are: Total Duration, Time Now
```

### Response samples

- 200
- 401
- 403
- 404
- 429

Content type

application/json

Copy
Expand all  Collapse all

`{"items": [{"id": "f-fgHijkLm",\
\
"type": "formula",\
\
"href": "https://coda.io/apis/v1/docs/AbCDeFGH/formulas/f-fgHijkLm",\
\
"name": "Sum of expenses",\
\
"parent": {"id": "canvas-IjkLmnO",\
\
"type": "page",\
\
"href": "https://coda.io/apis/v1/docs/AbCDeFGH/pages/canvas-IjkLmnO",\
\
"browserLink": "https://coda.io/d/_dAbCDeFGH/Launch-Status_sumnO",\
\
"name": "Launch Status"\
\
}\
\
}\
\
],

"href": "https://coda.io/apis/v1/docs/AbCDeFGH/formulas?limit=20",

"nextPageToken": "eyJsaW1pd",

"nextPageLink": "https://coda.io/apis/v1/docs/AbCDeFGH/formulas?pageToken=eyJsaW1pd"

}`

## [tag/Formulas/operation/getFormula](https://coda.io/developers/apis/v1\#tag/Formulas/operation/getFormula) Get a formula

Returns info on a formula.

##### Authorizations:

_Bearer_

##### path Parameters

|     |     |
| --- | --- |
| docId<br>required | string<br>Example: AbCDeFGH<br>ID of the doc. |
| formulaIdOrName<br>required | string<br>Example: f-fgHijkLm<br>ID or name of the formula. Names are discouraged because they're easily prone to being changed by users. If you're using a name, be sure to URI-encode it. |

### Responses

**200**

Details about a formula.

##### Response Schema: application/json

|     |     |
| --- | --- |
| id<br>required | string<br>ID of the formula. |
| type<br>required | string<br>Value:"formula"<br>The type of this resource. |
| href<br>required | string <url> <br>API link to the formula. |
| name<br>required | string<br>Name of the formula. |
| value<br>required | (ScalarValue (ScalarValue (string) or ScalarValue (number) or ScalarValue (boolean))) or (Array of (ScalarValue (ScalarValue (string) or ScalarValue (number) or ScalarValue (boolean))) or (Array of ScalarValue (strings or numbers or booleans))) (Value) <br>A Coda result or entity expressed as a primitive type, or array of primitive types. |
| parent | object (PageReference) <br>Reference to a page. |

**401**

The API token is invalid or has expired.

**403**

The API token does not grant access to this resource.

**404**

The resource could not be located with the current API token.

**429**

The client has sent too many requests.

get/docs/{docId}/formulas/{formulaIdOrName}

Coda API (v1)

https://coda.io/apis/v1/docs/{docId}/formulas/{formulaIdOrName}

### Request samples

- Python 3.13
- Shell
- Google Apps Script

Copy

```
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = f'https://coda.io/apis/v1/docs/<doc ID>/formulas/<formula ID>'
res = requests.get(uri, headers=headers).json()

print(f'It will take {res["value"]} hours to complete everything')
# => It will take 3 hours to complete everything
```

### Response samples

- 200
- 401
- 403
- 404
- 429

Content type

application/json

Copy
Expand all  Collapse all

`{"id": "f-fgHijkLm",

"type": "formula",

"href": "https://coda.io/apis/v1/docs/AbCDeFGH/formulas/f-fgHijkLm",

"name": "Sum of expenses",

"parent": {"id": "canvas-IjkLmnO",

"type": "page",

"href": "https://coda.io/apis/v1/docs/AbCDeFGH/pages/canvas-IjkLmnO",

"browserLink": "https://coda.io/d/_dAbCDeFGH/Launch-Status_sumnO",

"name": "Launch Status"

},

"value": "$12.34"

}`

## [tag/Controls](https://coda.io/developers/apis/v1\#tag/Controls) Controls

Controls provide a user-friendly way to input a value that can affect other parts of the doc. This API lets you list controls and get their current values.

## [tag/Controls/operation/listControls](https://coda.io/developers/apis/v1\#tag/Controls/operation/listControls) List controls

Returns a list of controls in a Coda doc.

##### Authorizations:

_Bearer_

##### path Parameters

|     |     |
| --- | --- |
| docId<br>required | string<br>Example: AbCDeFGH<br>ID of the doc. |

##### query Parameters

|     |     |
| --- | --- |
| limit | integer >= 1 <br>Default: 25<br>Example: limit=10<br>Maximum number of results to return in this query. |
| pageToken | string<br>Example: pageToken=eyJsaW1pd<br>An opaque token used to fetch the next page of results. |
| sortBy | string (SortBy) <br>Value:"name"<br>Example: sortBy=name<br>Determines how to sort the given objects. |

### Responses

**200**

List of controls in a doc.

##### Response Schema: application/json

|     |     |
| --- | --- |
| items<br>required | Array of objects (ControlReference) |
| href | string <url> <br>API link to these results |
| nextPageToken | string (nextPageToken) <br>If specified, an opaque token used to fetch the next page of results. |
| nextPageLink | string <url> <br>If specified, a link that can be used to fetch the next page of results. |

**401**

The API token is invalid or has expired.

**403**

The API token does not grant access to this resource.

**404**

The resource could not be located with the current API token.

**429**

The client has sent too many requests.

get/docs/{docId}/controls

Coda API (v1)

https://coda.io/apis/v1/docs/{docId}/controls

### Request samples

- Python 3.13
- Shell
- Google Apps Script

Copy

```
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = f'https://coda.io/apis/v1/docs/<doc ID>/controls'
res = requests.get(uri, headers=headers).json()

print(f'Controls here are: {", ".join(i["name"] for i in res["items"])}')
# => Controls here are: Control 1, Control 2
```

### Response samples

- 200
- 401
- 403
- 404
- 429

Content type

application/json

Copy
Expand all  Collapse all

`{"items": [{"id": "ctrl-cDefGhij",\
\
"type": "control",\
\
"href": "https://coda.io/apis/v1/docs/AbCDeFGH/controls/ctrl-cDefGhij",\
\
"name": "Cost",\
\
"parent": {"id": "canvas-IjkLmnO",\
\
"type": "page",\
\
"href": "https://coda.io/apis/v1/docs/AbCDeFGH/pages/canvas-IjkLmnO",\
\
"browserLink": "https://coda.io/d/_dAbCDeFGH/Launch-Status_sumnO",\
\
"name": "Launch Status"\
\
}\
\
}\
\
],

"href": "https://coda.io/apis/v1/docs/AbCDeFGH/controls?limit=20",

"nextPageToken": "eyJsaW1pd",

"nextPageLink": "https://coda.io/apis/v1/docs/AbCDeFGH/controls?pageToken=eyJsaW1pd"

}`

## [tag/Controls/operation/getControl](https://coda.io/developers/apis/v1\#tag/Controls/operation/getControl) Get a control

Returns info on a control.

##### Authorizations:

_Bearer_

##### path Parameters

|     |     |
| --- | --- |
| docId<br>required | string<br>Example: AbCDeFGH<br>ID of the doc. |
| controlIdOrName<br>required | string<br>Example: ctrl-cDefGhij<br>ID or name of the control. Names are discouraged because they're easily prone to being changed by users. If you're using a name, be sure to URI-encode it. |

### Responses

**200**

Details about a control.

##### Response Schema: application/json

|     |     |
| --- | --- |
| id<br>required | string<br>ID of the control. |
| type<br>required | string<br>Value:"control"<br>The type of this resource. |
| href<br>required | string <url> <br>API link to the control. |
| name<br>required | string<br>Name of the control. |
| controlType<br>required | string (ControlType) <br>Enum:"aiBlock""button""checkbox""datePicker""dateRangePicker""dateTimePicker""lookup""multiselect""select""scale""slider""reaction""textbox""timePicker"<br>Type of the control. |
| value<br>required | (ScalarValue (ScalarValue (string) or ScalarValue (number) or ScalarValue (boolean))) or (Array of (ScalarValue (ScalarValue (string) or ScalarValue (number) or ScalarValue (boolean))) or (Array of ScalarValue (strings or numbers or booleans))) (Value) <br>A Coda result or entity expressed as a primitive type, or array of primitive types. |
| parent | object (PageReference) <br>Reference to a page. |

**401**

The API token is invalid or has expired.

**403**

The API token does not grant access to this resource.

**404**

The resource could not be located with the current API token.

**429**

The client has sent too many requests.

get/docs/{docId}/controls/{controlIdOrName}

Coda API (v1)

https://coda.io/apis/v1/docs/{docId}/controls/{controlIdOrName}

### Request samples

- Python 3.13
- Shell
- Google Apps Script

Copy

```
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = f'https://coda.io/apis/v1/docs/<doc ID>/controls/<control ID>'
res = requests.get(uri, headers=headers).json()

print(f'The control is a {res["controlType"]}')
# => The control is a slider
```

### Response samples

- 200
- 401
- 403
- 404
- 429

Content type

application/json

Copy
Expand all  Collapse all

`{"id": "ctrl-cDefGhij",

"type": "control",

"href": "https://coda.io/apis/v1/docs/AbCDeFGH/controls/ctrl-cDefGhij",

"name": "Cost",

"parent": {"id": "canvas-IjkLmnO",

"type": "page",

"href": "https://coda.io/apis/v1/docs/AbCDeFGH/pages/canvas-IjkLmnO",

"browserLink": "https://coda.io/d/_dAbCDeFGH/Launch-Status_sumnO",

"name": "Launch Status"

},

"controlType": "slider",

"value": "$12.34"

}`

## [tag/Account](https://coda.io/developers/apis/v1\#tag/Account) Account

At this time, the API exposes some limited information about your account. However, `/whoami` is a good endpoint to hit to verify that you're hitting the API correctly and that your token is working as expected.

## [tag/Account/operation/whoami](https://coda.io/developers/apis/v1\#tag/Account/operation/whoami) Get user info

Returns basic info about the current user.

##### Authorizations:

_Bearer_

### Responses

**200**

Info about the current user.

##### Response Schema: application/json

|     |     |
| --- | --- |
| name<br>required | string<br>Name of the user. |
| loginId<br>required | string<br>Email address of the user. |
| type<br>required | string<br>Value:"user"<br>The type of this resource. |
| scoped<br>required | boolean<br>True if the token used to make this request has restricted/scoped access to the API. |
| tokenName<br>required | string<br>Returns the name of the token used for this request. |
| href<br>required | string <url> <br>API link to the user. |
| workspace<br>required | object (WorkspaceReference) <br>Reference to a Coda workspace. |
| pictureLink | string <url> <br>Browser-friendly link to the user's avatar image. |

**401**

The API token is invalid or has expired.

**429**

The client has sent too many requests.

get/whoami

Coda API (v1)

https://coda.io/apis/v1/whoami

### Request samples

- Python 3.13
- Shell
- Google Apps Script

Copy

```
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = 'https://coda.io/apis/v1/whoami'
res = requests.get(uri, headers=headers).json()

print(f'Your name is {res["name"]}')
# => Your name is John Doe
```

### Response samples

- 200
- 401
- 429

Content type

application/json

Copy
Expand all  Collapse all

`{"name": "John Doe",

"loginId": "user@example.com",

"type": "user",

"pictureLink": "https://cdn.coda.io/avatars/default_avatar.png",

"scoped": false,

"tokenName": "My API token",

"href": "https://coda.io/apis/v1beta/whoami",

"workspace": {"id": "ws-1Ab234",

"type": "workspace",

"organizationId": "org-2Bc456",

"browserLink": "https://coda.io/docs?workspaceId=ws-1Ab234",

"name": "My workspace"

}

}`

## [tag/Analytics](https://coda.io/developers/apis/v1\#tag/Analytics) Analytics

This API offers analytics data for your docs and Packs over time.

## [tag/Analytics/operation/listDocAnalytics](https://coda.io/developers/apis/v1\#tag/Analytics/operation/listDocAnalytics) List doc analytics

Returns analytics data for available docs per day.

##### Authorizations:

_Bearer_

##### query Parameters

|     |     |
| --- | --- |
| docIds | Array of strings<br>List of docIds to fetch. |
| workspaceId | string<br>Example: workspaceId=ws-1Ab234<br>ID of the workspace. |
| query | string<br>Example: query=Supercalifragilisticexpialidocious<br>Search term used to filter down results. |
| isPublished | boolean<br>Limit results to only published items. |
| sinceDate | string <date> <br>Example: sinceDate=2020-08-01<br>Limit results to activity on or after this date. |
| untilDate | string <date> <br>Example: untilDate=2020-08-05<br>Limit results to activity on or before this date. |
| scale | string (AnalyticsScale) <br>Enum:"daily""cumulative"<br>Example: scale=daily<br>Quantization period over which to view analytics. Defaults to daily. |
| pageToken | string<br>Example: pageToken=eyJsaW1pd<br>An opaque token used to fetch the next page of results. |
| orderBy | string (DocAnalyticsOrderBy) <br>Enum:"date""docId""title""createdAt""publishedAt""likes""copies""views""sessionsDesktop""sessionsMobile""sessionsOther""totalSessions""aiCreditsChat""aiCreditsBlock""aiCreditsColumn""aiCreditsAssistant""aiCreditsReviewer""aiCredits"<br>Use this parameter to order the doc analytics returned. |
| direction | string (SortDirection) <br>Enum:"ascending""descending"<br>Direction to sort results in. |
| limit | integer \[ 1 .. 5000 \] <br>Default: 1000<br>Example: limit=10<br>Maximum number of results to return in this query. |

### Responses

**200**

List of Coda doc analytics.

##### Response Schema: application/json

|     |     |
| --- | --- |
| items<br>required | Array of objects (DocAnalyticsItem) |
| nextPageToken | string (nextPageToken) <br>If specified, an opaque token used to fetch the next page of results. |
| nextPageLink | string <url> <br>If specified, a link that can be used to fetch the next page of results. |

**401**

The API token is invalid or has expired.

**429**

The client has sent too many requests.

get/analytics/docs

Coda API (v1)

https://coda.io/apis/v1/analytics/docs

### Request samples

- Python 3.13
- Shell

Copy

```
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = 'https://coda.io/apis/v1/analytics/docs'
params = {
  'limit': 10,
}
res = requests.get(uri, headers=headers, params=params).json()

print(f'First doc is: {res["items"][0]["doc"]["title"]}')
# => First doc is: New Document
```

### Response samples

- 200
- 401
- 429

Content type

application/json

Copy
Expand all  Collapse all

`{"items": [{"doc": {"id": "AbCDeFGH",\
\
"type": "doc",\
\
"href": "https://coda.io/apis/v1/docs/AbCDeFGH",\
\
"browserLink": "https://coda.io/d/_dAbCDeFGH",\
\
"title": "Cool Geometry Formulas",\
\
"icon": {"name": "string",\
\
"type": "string",\
\
"browserLink": "https://cdn.coda.io/icons/png/color/icon-32.png"\
\
},\
\
"createdAt": "2022-04-11T00:18:57.946Z",\
\
"publishedAt": "2022-04-12T00:18:57.946Z"\
\
},\
\
"metrics": [{"date": "2020-09-02",\
\
"views": 980,\
\
"copies": 24,\
\
"likes": 342,\
\
"sessionsMobile": 530,\
\
"sessionsDesktop": 212,\
\
"sessionsOther": 10,\
\
"totalSessions": 1000,\
\
"aiCreditsChat": 10,\
\
"aiCreditsBlock": 10,\
\
"aiCreditsColumn": 10,\
\
"aiCreditsAssistant": 10,\
\
"aiCreditsReviewer": 10,\
\
"aiCredits": 50\
\
}\
\
]\
\
}\
\
],

"nextPageToken": "eyJsaW1pd",

"nextPageLink": "https://coda.io/apis/v1/analytics/docs?pageToken=xyz"

}`

## [tag/Analytics/operation/listPageAnalytics](https://coda.io/developers/apis/v1\#tag/Analytics/operation/listPageAnalytics) List page analytics

Returns analytics data for a given doc within the day.
This method will return a 401 if the given doc is not in an Enterprise workspace.

##### Authorizations:

_Bearer_

##### path Parameters

|     |     |
| --- | --- |
| docId<br>required | string<br>Example: AbCDeFGH<br>ID of the doc. |

##### query Parameters

|     |     |
| --- | --- |
| sinceDate | string <date> <br>Example: sinceDate=2020-08-01<br>Limit results to activity on or after this date. |
| untilDate | string <date> <br>Example: untilDate=2020-08-05<br>Limit results to activity on or before this date. |
| pageToken | string<br>Example: pageToken=eyJsaW1pd<br>An opaque token used to fetch the next page of results. |
| limit | integer \[ 1 .. 5000 \] <br>Default: 1000<br>Example: limit=10<br>Maximum number of results to return in this query. |

### Responses

**200**

List of page analytics for the given Coda doc.

##### Response Schema: application/json

|     |     |
| --- | --- |
| items<br>required | Array of objects (PageAnalyticsItem) |
| nextPageToken | string (nextPageToken) <br>If specified, an opaque token used to fetch the next page of results. |
| nextPageLink | string <url> <br>If specified, a link that can be used to fetch the next page of results. |

**401**

The API token is invalid or has expired.

**429**

The client has sent too many requests.

get/analytics/docs/{docId}/pages

Coda API (v1)

https://coda.io/apis/v1/analytics/docs/{docId}/pages

### Request samples

- Python 3.13
- Shell

Copy

```
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = 'https://coda.io/apis/v1/analytics/docs/abcdefghi/pages'
params = {
  'limit': 10,
}
res = requests.get(uri, headers=headers, params=params).json()

print(f'First page is: {res["items"][0]["page"]["name"]}')
# => First page is: My Page
```

### Response samples

- 200
- 401
- 429

Content type

application/json

Copy
Expand all  Collapse all

`{"items": [{"page": {"id": "section-IjkLmnO",\
\
"name": "Launch Status",\
\
"icon": {"name": "string",\
\
"type": "string",\
\
"browserLink": "https://cdn.coda.io/icons/png/color/icon-32.png"\
\
}\
\
},\
\
"metrics": [{"date": "2022-06-03",\
\
"views": 980,\
\
"sessions": 24,\
\
"users": 42,\
\
"averageSecondsViewed": 42,\
\
"medianSecondsViewed": 42,\
\
"tabs": 10\
\
}\
\
]\
\
}\
\
],

"nextPageToken": "eyJsaW1pd",

"nextPageLink": "https://coda.io/apis/v1/analytics/docs/DOC_ID/pages?pageToken=xyz"

}`

## [tag/Analytics/operation/listDocAnalyticsSummary](https://coda.io/developers/apis/v1\#tag/Analytics/operation/listDocAnalyticsSummary) Get doc analytics summary

Returns summarized analytics data for available docs.

##### Authorizations:

_Bearer_

##### query Parameters

|     |     |
| --- | --- |
| isPublished | boolean<br>Limit results to only published items. |
| sinceDate | string <date> <br>Example: sinceDate=2020-08-01<br>Limit results to activity on or after this date. |
| untilDate | string <date> <br>Example: untilDate=2020-08-05<br>Limit results to activity on or before this date. |
| workspaceId | string<br>Example: workspaceId=ws-1Ab234<br>ID of the workspace. |

### Responses

**200**

Response of Coda doc summary analytics.

##### Response Schema: application/json

|     |     |
| --- | --- |
| totalSessions<br>required | integer<br>Total number of sessions across all docs. |

**401**

The API token is invalid or has expired.

**429**

The client has sent too many requests.

get/analytics/docs/summary

Coda API (v1)

https://coda.io/apis/v1/analytics/docs/summary

### Response samples

- 200
- 401
- 429

Content type

application/json

Copy

`{"totalSessions": 1337

}`

## [tag/Analytics/operation/listPackAnalytics](https://coda.io/developers/apis/v1\#tag/Analytics/operation/listPackAnalytics) List Pack analytics

Returns analytics data for Packs the user can edit.

##### Authorizations:

_Bearer_

##### query Parameters

|     |     |
| --- | --- |
| packIds | Array of integers<br>Which Pack IDs to fetch. |
| workspaceId | string<br>Example: workspaceId=ws-1Ab234<br>ID of the workspace. |
| query | string<br>Example: query=Supercalifragilisticexpialidocious<br>Search term used to filter down results. |
| sinceDate | string <date> <br>Example: sinceDate=2020-08-01<br>Limit results to activity on or after this date. |
| untilDate | string <date> <br>Example: untilDate=2020-08-05<br>Limit results to activity on or before this date. |
| scale | string (AnalyticsScale) <br>Enum:"daily""cumulative"<br>Example: scale=daily<br>Quantization period over which to view analytics. Defaults to daily. |
| pageToken | string<br>Example: pageToken=eyJsaW1pd<br>An opaque token used to fetch the next page of results. |
| orderBy | string (PackAnalyticsOrderBy) <br>Enum:"date""packId""name""createdAt""docInstalls""workspaceInstalls""numFormulaInvocations""numActionInvocations""numSyncInvocations""numMetadataInvocations""docsActivelyUsing""docsActivelyUsing7Day""docsActivelyUsing30Day""docsActivelyUsing90Day""docsActivelyUsingAllTime""workspacesActivelyUsing""workspacesActivelyUsing7Day""workspacesActivelyUsing30Day""workspacesActivelyUsing90Day""workspacesActivelyUsingAllTime""workspacesWithActiveSubscriptions""workspacesWithSuccessfulTrials""revenueUsd"<br>Use this parameter to order the Pack analytics returned. |
| direction | string (SortDirection) <br>Enum:"ascending""descending"<br>Direction to sort results in. |
| isPublished | boolean<br>Limit results to only published items. If false or unspecified, returns all items including published ones. |
| limit | integer \[ 1 .. 5000 \] <br>Default: 1000<br>Example: limit=10<br>Maximum number of results to return in this query. |

### Responses

**200**

Response of Coda Pack analytics.

##### Response Schema: application/json

|     |     |
| --- | --- |
| items<br>required | Array of objects (PackAnalyticsItem) |
| nextPageToken | string (nextPageToken) <br>If specified, an opaque token used to fetch the next page of results. |
| nextPageLink | string <url> <br>If specified, a link that can be used to fetch the next page of results. |

**401**

The API token is invalid or has expired.

**429**

The client has sent too many requests.

get/analytics/packs

Coda API (v1)

https://coda.io/apis/v1/analytics/packs

### Request samples

- Python 3.13
- Shell

Copy

```
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = 'https://coda.io/apis/v1/analytics/packs'
params = {
  'limit': 10,
}
res = requests.get(uri, headers=headers, params=params).json()

print(f'First Pack is: {res["items"][0]["pack"]["name"]}')
# => First Pack is: New Pack
```

### Response samples

- 200
- 401
- 429

Content type

application/json

Copy
Expand all  Collapse all

`{"items": [{"pack": {"id": 1003,\
\
"name": "Cool Geometry Formulas",\
\
"logoUrl": "string",\
\
"createdAt": "2022-04-11T00:18:57.946Z"\
\
},\
\
"metrics": [{"date": "2020-09-02",\
\
"docInstalls": 100,\
\
"workspaceInstalls": 10,\
\
"numFormulaInvocations": 100,\
\
"numActionInvocations": 100,\
\
"numSyncInvocations": 100,\
\
"numMetadataInvocations": 100,\
\
"docsActivelyUsing": 50,\
\
"docsActivelyUsing7Day": 100,\
\
"docsActivelyUsing30Day": 200,\
\
"docsActivelyUsing90Day": 300,\
\
"docsActivelyUsingAllTime": 500,\
\
"workspacesActivelyUsing": 10,\
\
"workspacesActivelyUsing7Day": 15,\
\
"workspacesActivelyUsing30Day": 20,\
\
"workspacesActivelyUsing90Day": 30,\
\
"workspacesActivelyUsingAllTime": 50,\
\
"workspacesActivelyTrialing": 0,\
\
"workspacesActivelyTrialing7Day": 0,\
\
"workspacesActivelyTrialing30Day": 0,\
\
"workspacesActivelyTrialing90Day": 0,\
\
"workspacesActivelyTrialingAllTime": 0,\
\
"workspacesNewlySubscribed": 0,\
\
"workspacesWithActiveSubscriptions": 0,\
\
"workspacesWithSuccessfulTrials": 0,\
\
"revenueUsd": "string"\
\
}\
\
]\
\
}\
\
],

"nextPageToken": "eyJsaW1pd",

"nextPageLink": "https://coda.io/apis/v1/analytics/packs?pageToken=xyz"

}`

## [tag/Analytics/operation/listPackAnalyticsSummary](https://coda.io/developers/apis/v1\#tag/Analytics/operation/listPackAnalyticsSummary) Get Pack analytics summary

Returns summarized analytics data for Packs the user can edit.

##### Authorizations:

_Bearer_

##### query Parameters

|     |     |
| --- | --- |
| packIds | Array of integers<br>Which Pack IDs to fetch. |
| workspaceId | string<br>Example: workspaceId=ws-1Ab234<br>ID of the workspace. |
| isPublished | boolean<br>Limit results to only published items. If false or unspecified, returns all items including published ones. |
| sinceDate | string <date> <br>Example: sinceDate=2020-08-01<br>Limit results to activity on or after this date. |
| untilDate | string <date> <br>Example: untilDate=2020-08-05<br>Limit results to activity on or before this date. |

### Responses

**200**

Response of Coda Pack summary analytics.

##### Response Schema: application/json

|     |     |
| --- | --- |
| totalDocInstalls<br>required | integer<br>The number of times this Pack was installed in docs. |
| totalWorkspaceInstalls<br>required | integer<br>The number of times this Pack was installed in workspaces. |
| totalInvocations<br>required | integer<br>The number of times formulas in this Pack were invoked. |

**401**

The API token is invalid or has expired.

**429**

The client has sent too many requests.

get/analytics/packs/summary

Coda API (v1)

https://coda.io/apis/v1/analytics/packs/summary

### Response samples

- 200
- 401
- 429

Content type

application/json

Copy

`{"totalDocInstalls": 0,

"totalWorkspaceInstalls": 0,

"totalInvocations": 0

}`

## [tag/Analytics/operation/listPackFormulaAnalytics](https://coda.io/developers/apis/v1\#tag/Analytics/operation/listPackFormulaAnalytics) List Pack formula analytics

Returns analytics data for Pack formulas.

##### Authorizations:

_Bearer_

##### path Parameters

|     |     |
| --- | --- |
| packId<br>required | integer >= 1 <br>Example: 123<br>ID of a Pack |

##### query Parameters

|     |     |
| --- | --- |
| packFormulaNames | Array of strings<br>Example: packFormulaNames=SquareRoot,CubeRoot<br>A list of Pack formula names (case-sensitive) for which to retrieve analytics. |
| packFormulaTypes | Array of strings (PackFormulaType) <br>Items Enum:"action""formula""sync""metadata"<br>Example: packFormulaTypes=action,formula<br>A list of Pack formula types corresponding to the `packFormulaNames`. If specified, this must have the same length as `packFormulaNames`. |
| sinceDate | string <date> <br>Example: sinceDate=2020-08-01<br>Limit results to activity on or after this date. |
| untilDate | string <date> <br>Example: untilDate=2020-08-05<br>Limit results to activity on or before this date. |
| scale | string (AnalyticsScale) <br>Enum:"daily""cumulative"<br>Example: scale=daily<br>Quantization period over which to view analytics. Defaults to daily. |
| pageToken | string<br>Example: pageToken=eyJsaW1pd<br>An opaque token used to fetch the next page of results. |
| orderBy | string (PackFormulaAnalyticsOrderBy) <br>Enum:"date""formulaName""formulaType""formulaInvocations""medianLatencyMs""medianResponseSizeBytes""errors""docsActivelyUsing""docsActivelyUsing7Day""docsActivelyUsing30Day""docsActivelyUsing90Day""docsActivelyUsingAllTime""workspacesActivelyUsing""workspacesActivelyUsing7Day""workspacesActivelyUsing30Day""workspacesActivelyUsing90Day""workspacesActivelyUsingAllTime"<br>Use this parameter to order the Pack formula analytics returned. |
| direction | string (SortDirection) <br>Enum:"ascending""descending"<br>Direction to sort results in. |
| limit | integer \[ 1 .. 5000 \] <br>Default: 1000<br>Example: limit=10<br>Maximum number of results to return in this query. |

### Responses

**200**

Response of Coda Pack formula analytics.

##### Response Schema: application/json

|     |     |
| --- | --- |
| items<br>required | Array of objects (PackFormulaAnalyticsItem) |
| nextPageToken | string (nextPageToken) <br>If specified, an opaque token used to fetch the next page of results. |
| nextPageLink | string <url> <br>If specified, a link that can be used to fetch the next page of results. |

**401**

The API token is invalid or has expired.

**429**

The client has sent too many requests.

get/analytics/packs/{packId}/formulas

Coda API (v1)

https://coda.io/apis/v1/analytics/packs/{packId}/formulas

### Response samples

- 200
- 401
- 429

Content type

application/json

Copy
Expand all  Collapse all

`{"items": [{"formula": {"name": "SquareRoot",\
\
"type": "action"\
\
},\
\
"metrics": [{"date": "2020-09-02",\
\
"formulaInvocations": 123,\
\
"errors": 5,\
\
"medianLatencyMs": 500,\
\
"medianResponseSizeBytes": 300,\
\
"docsActivelyUsing": 50,\
\
"docsActivelyUsing7Day": 100,\
\
"docsActivelyUsing30Day": 200,\
\
"docsActivelyUsing90Day": 300,\
\
"docsActivelyUsingAllTime": 500,\
\
"workspacesActivelyUsing": 10,\
\
"workspacesActivelyUsing7Day": 15,\
\
"workspacesActivelyUsing30Day": 20,\
\
"workspacesActivelyUsing90Day": 30,\
\
"workspacesActivelyUsingAllTime": 50,\
\
"workspacesActivelyTrialing": 0,\
\
"workspacesActivelyTrialing7Day": 0,\
\
"workspacesActivelyTrialing30Day": 0,\
\
"workspacesActivelyTrialing90Day": 0,\
\
"workspacesActivelyTrialingAllTime": 0,\
\
"workspacesNewlySubscribed": 0,\
\
"workspacesWithActiveSubscriptions": 0,\
\
"workspacesWithSuccessfulTrials": 0,\
\
"revenueUsd": "string"\
\
}\
\
]\
\
}\
\
],

"nextPageToken": "eyJsaW1pd",

"nextPageLink": "https://coda.io/apis/v1/analytics/packs/:packId/formulas?pageToken=xyz"

}`

## [tag/Analytics/operation/getAnalyticsLastUpdated](https://coda.io/developers/apis/v1\#tag/Analytics/operation/getAnalyticsLastUpdated) Get analytics last updated day

Returns days based on Pacific Standard Time when analytics were last updated.

##### Authorizations:

_Bearer_

### Responses

**200**

Response of analytics last updated days.

##### Response Schema: application/json

|     |     |
| --- | --- |
| docAnalyticsLastUpdated<br>required | string <date> <br>Date that doc analytics were last updated. |
| packAnalyticsLastUpdated<br>required | string <date> <br>Date that Pack analytics were last updated. |
| packFormulaAnalyticsLastUpdated<br>required | string <date> <br>Date that Pack formula analytics were last updated. |

**429**

The client has sent too many requests.

get/analytics/updated

Coda API (v1)

https://coda.io/apis/v1/analytics/updated

### Response samples

- 200
- 429

Content type

application/json

Copy

`{"docAnalyticsLastUpdated": "2022-05-01",

"packAnalyticsLastUpdated": "2022-05-01",

"packFormulaAnalyticsLastUpdated": "2022-05-01"

}`

## [tag/Miscellaneous](https://coda.io/developers/apis/v1\#tag/Miscellaneous) Miscellaneous

These endpoints wouldn't fit anywhere else, but you may find them useful when working with Coda.

## [tag/Miscellaneous/operation/resolveBrowserLink](https://coda.io/developers/apis/v1\#tag/Miscellaneous/operation/resolveBrowserLink) Resolve browser link

Given a browser link to a Coda object, attempts to find it and return metadata that can be used to get more info on it. Returns a 400 if the URL does not appear to be a Coda URL or a 404 if the resource cannot be located with the current credentials.

##### Authorizations:

_Bearer_

##### query Parameters

|     |     |
| --- | --- |
| url<br>required | string <url> <br>Example: url=https://coda.io/d/\_dAbCDeFGH/Launch-Status\_sumnO<br>The browser link to try to resolve. |
| degradeGracefully | boolean<br>Example: degradeGracefully=true<br>By default, attempting to resolve the Coda URL of a deleted object will result in an error. If this flag is set, the next-available object, all the way up to the doc itself, will be resolved. |

### Responses

**200**

Metadata for the resolved resource.

##### Response Schema: application/json

|     |     |
| --- | --- |
| type<br>required | string<br>Value:"apiLink"<br>The type of this resource. |
| href<br>required | string <url> <br>Self link to this query. |
| resource<br>required | object (ApiLinkResolvedResource) <br>Reference to the resolved resource. |
| browserLink | string <url> <br>Canonical browser-friendly link to the resolved resource. |

**400**

The request parameters did not conform to expectations.

**401**

The API token is invalid or has expired.

**403**

The API token does not grant access to this resource.

**404**

The resource could not be located with the current API token.

**429**

The client has sent too many requests.

get/resolveBrowserLink

Coda API (v1)

https://coda.io/apis/v1/resolveBrowserLink

### Request samples

- Python 3.13
- Shell
- Google Apps Script

Copy

```
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = 'https://coda.io/apis/v1/resolveBrowserLink'
params = {
  'url': 'https://coda.io/d/Some-Doc_d<doc ID>/#To-do-List_tu<table ID>',
}
res = requests.get(uri, headers=headers, params=params).json()
resolved_uri = res["resource"]["href"]

res = requests.get(resolved_uri, headers=headers).json()
print(f'This link points to a {res["type"]} named {res["name"]}')
# => This link points to a table named To-do List
```

### Response samples

- 200
- 400
- 401
- 403
- 404
- 429

Content type

application/json

Copy
Expand all  Collapse all

`{"type": "apiLink",

"href": "https://coda.io/apis/v1/resolveBrowserLink?url=https%3A%2F%2Fcoda.io%2Fd%2F_dAbCDeFGH%2FLaunch-Status_sumnO",

"browserLink": "https://coda.io/d/_dAbCDeFGH/Launch-Status_sumnO",

"resource": {"type": "aclMetadata",

"id": "canvas-IjkLmnO",

"name": "My Page",

"href": "https://coda.io/apis/v1/docs/AbCDeFGH/pages/canvas-IjkLmnO"

}

}`

## [tag/Miscellaneous/operation/getMutationStatus](https://coda.io/developers/apis/v1\#tag/Miscellaneous/operation/getMutationStatus) Get mutation status

Get the status for an asynchronous mutation to know whether or not it has been completed. Each API endpoint that mutates a document will return a request id that you can pass to this endpoint to check the completion status. Status information is not guaranteed to be available for more than one day after the mutation was completed. It is intended to be used shortly after the request was made.

##### Authorizations:

_Bearer_

##### path Parameters

|     |     |
| --- | --- |
| requestId<br>required | string<br>Example: abc-123-def-456<br>ID of the request. |

### Responses

**200**

Info about the mutation.

##### Response Schema: application/json

|     |     |
| --- | --- |
| completed<br>required | boolean<br>Returns whether the mutation has completed. |
| warning | string<br>A warning if the mutation completed but with caveats. |

**401**

The API token is invalid or has expired.

**404**

The resource could not be located with the current API token.

**429**

The client has sent too many requests.

get/mutationStatus/{requestId}

Coda API (v1)

https://coda.io/apis/v1/mutationStatus/{requestId}

### Request samples

- Python 3.13
- Shell
- Google Apps Script

Copy

```
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = 'https://coda.io/apis/v1/mutationStatus/some-request-id'
res = requests.get(uri, headers=headers).json()

print(f'Request has completed? {res["completed"]}')
# => Request has completed? false
```

### Response samples

- 200
- 401
- 404
- 429

Content type

application/json

Copy

`{"completed": true,

"warning": "Initial page HTML was invalid."

}`