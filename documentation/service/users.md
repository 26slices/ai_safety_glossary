# Users

## Overview

There will be two types of users in the system:

1. **Admin Users**: These users will have access to an admin interface where they can manage the system. This access will be limited to a number of functions, e.g. approving or rejecting terms, etc. Admin users will access the admin interface using a secure username and password.

2. **Pipeline Users**: These users will be able to access the web service endpoints, e.g. `create-term`, `list-terms`, etc. They will not have access to the admin interface. See [Pipeline Authentication](pipeline-authentication.md) for more details on how the data pipeline will authenticate to the web service.

End users of the website will not be required to register or log in. **Note**, this implies that the website will not have any write access.

## Admin Users

John and Tim will be the admin users. Even though we are trusted users, we will still limit the functionality of the admin interface to only the functions that we expect to perform regularly. This will help to reduce the risk of accidental changes to the system.

Other changes will have to be handled through code changes and deployments. This will ensure that the system is stable and that changes are tracked in version control.

## Pipeline Users

For now, there will only be one pipeline user.
