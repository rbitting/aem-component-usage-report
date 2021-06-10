# aem-component-usage-report

A command line script to generate a report of component usage from your local AEM instance. The report queries your local instance for all usage of each component under `/content` and spits out the component, component path, and page path into a CSV.

## Get Started

1. Make sure you have a local instance of AEM running on `localhost:4502`. 
2. Create a text file with a list of relative paths to the components you want to audit. One component per line with `/apps/` removed.

Example:

`components.txt`
```
core/wcm/components/text/v1/text
core/wcm/components/title/v2/title
...
```

## Run

Pass the path to the list of components as a command line argument. Example:

`python report.py components.txt`