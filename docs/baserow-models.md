# baserow.io models

In this document, the structures of the tables in baserow.io are detailed,
in order to use sabedoria, it is necessary that all the tables are created
with the same column types, the values can vary.

The `xx-XX` notation should be replaced by the language you want to use,
I use `pt-BR` and `en-US` just to standardize, but you can use whatever
you want, actually the string you want to identify a language, you just
need to ensure that all the places they use are the same, with case
sensitivity. For each language a column, with the suffix of your choice.

- [RFC 9110 -  12.5.4. Accept-Language](https://www.rfc-editor.org/rfc/rfc9110.html#name-accept-language)

## interest

Name | Type | Example | Description
---|---|---|---
xx-XX | string | - | -

Something like:

Name | Type | Example | Description
---|---|---|---
pt-BR | string | - | -
en-US | string | - | -

## skill

Name | Type | Example | Description
---|---|---|---
name | string | python | -

## description

Name | Type | Example | Description
---|---|---|---
scope | string | cv
description_xx-XX | string | - | describe a item to a job

## course

Name | Type | Example | Description
---|---|---|---
name | string | - | name of course
platform | single select | school 1,school2 | which online teaching platform was used
status | single select | doing,done | define a status of course
completed | date | 2023-01-01 | complete date
tier | single select | 1,2,3,4,5 | define priority, internal use only, 1 high, 5 low
area | single select | personal,pro | describes the scope of the course, whether it is professional or personal
url | string | - | landing page to course or hotsite to course
certificate_url | string | rrrr | url to view certificate
certificate_credential | string | - | id of certification
certificate_download_url | string | - | direct url to download certificate
public | boolean | - | if is public to list
certificate | boolean | - | if have certificate
minutes | number | 480 | represent time (minutes) spend in couse

## job

Name | Type | Example | Description
---|---|---|---
employer | string | ACME Inc.
contract_type | single select | full-time,internship,freelancer,contract | -
location | string | São Paulo, BR | -
location_type | single select | presential,remote | -
start | date | 2023-01-01 | date started on job
end | date | 2023-01-01 | date leaves from job
skill | array | - | references to skill table as linked table witout column in skill table
description_xx-XX | array | - | references to description table as linked table witout column in description table
title_xx-XX | string | Developer | -

## project

Name | Type | Example | Description
---|---|---|---
name | string | - | -
stage | single select | prod,testing,beta,alpha,planning,dev,no-eta | -
skill | array | - | references to skill table as linked table witout column in skill table
description_xx-XX | string | - | -
visibility | single select | private,public | indicates, if code is public or private
url | string | - | url for the project, whether site, repository or other type
show | boolean | - | only displays in sabedoria if true

## education

Name | Type | Example | Description
---|---|---|---
university | string | - | -
start | date | 2023-01-01 | -
end | date | 2023-01-01 | -
thesis_xx-XX | string | - | the description of the thesis of completion of the course
location | string | - | -
title_xx-XX | string | - | the title and name of the course taken
