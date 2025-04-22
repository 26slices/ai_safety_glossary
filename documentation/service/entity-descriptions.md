# Entity Descriptions

**Note**: All entities also include the following fields:

- `id`: Unique identifier for the entity.
- `created_at`: Timestamp of when the entity was created.
- `updated_at`: Timestamp of when the entity was last updated.
- `created_by`: User ID of the user who created the entity.
- `updated_by`: User ID of the user who last updated the entity.

Additionally, any entity that has a `reviewed` field will also have the following fields:

- `reviewed_by`: User ID of the user who reviewed the entity.
- `reviewed_at`: Timestamp of when the entity was reviewed.

## Term

`Term` is representation of a term relating to AI safety and alignment.

### Fields

- `name`: Name of the term, e.g., "Alignment". **Note**: There can be only one approved or pending term with a given name. There can be multiple rejected terms with the same name.

- `justification`: Justification for the term's relevance to AI safety and alignment. This is added by the pipeline user. This is used to help admin users understand the reasoning behind the LLM's suggestions.

- `status`: Either "pending", "rejected" or "approved". Indicates if the term is relevant to AI safety and alignment. We include terms that are not relevant to prevent our pipeline from repeatedly adding terms which are not relevant. The pipeline user will suggest whether a term is relevant or not and the admin user will approve or reject the term. When created, this is set to `pending`.

- `review`: Justification for the approval or rejection of the term. This is added by the admin user. This is used to help the LLM understand which terms are relevant to AI safety and alignment and which are not.

## Term Alias

`TermAlias` is a representation of an alias for a term. This is used to prevent duplicate information in the service. For example, "AI alignment" and "Alignment" are the same term.

### Fields

- `term_id`: Foreign key to the term. This is used to link the alias to the term.

- `name`: Name of the alias, e.g., "AI alignment".

## Term Enrichment

`TermEnrichment` is a separate entity that stores additional information about a term. The enrichment of a term is carried out during a separate process to the term creation. Additionally, the enrichment process for a term is carried out multiple times to prevent the term enrichment from becoming stale. Representing `TermEnrichment` as a separate entity allows us to replace enrichments without having to modify the term itself.

### Fields

- `term_id`: Foreign key to the term. This is used to link the enrichment to the term.

- `description`: Description of the term. This is used to provide additional information about the term. This is added by the pipeline user and reviewed by an admin user.

- `status`: Either "pending", "rejected" or "approved". Indicates if the enrichment is good.

- `review`: Justification for the approval or rejection of the term enrichment. This is added by the admin user. This is used to help the LLM understand why a term enrichment is good or bad.

## Tag

`Tag` is a representation of a tag that can be used to categorize terms. This is used to help users understand the relationships between terms and to present the information in a more user-friendly way. Tags are added by admin users.

### Fields

- `name`: Name of the tag, e.g., "Foundational". (unique)

- `description`: Description of the tag. This is used to provide additional information about the tag. This is useful for the LLM to determine whether a tag is relevant to a term or not.

## Term Tag

`TermTag` is a representation of a tag that is associated with a term, i.e. a through table/many-to-many relationship. Term tags are created by the pipeline user.

### Fields

- `term_id`: Foreign key to the term. This is used to link the tag to the term.

- `tag_id`: Foreign key to the tag. This is used to link the tag to the term.

- `status`: Either "pending", "rejected" or "approved". Indicates if the tag is relevant to the term. This is set by the admin user. When created, this is set to `pending`.

- `review`: Justification for the approval or rejection of the term tag. This is added by the admin user. This is used to help the LLM understand which tags are relevant to a term and which are not.
