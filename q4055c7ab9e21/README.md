# NQL Certification Registry (q4055c7ab9e21)

This directory holds the working set for the current Halcyon NQL certification
cycle. It is maintained by the component-certification team.

## Layout

- `projects/` - one directory per candidate project.
- `registry_index.json` - a convenience index of each project's headline
  component manifest. Treat it as a starting point, not as the full inventory.

A component is only defined by a `component_manifest.json` file. Toolkit
projects commonly bundle several modules under their `modules/` directory, and
each module may declare its own component. Project names, project READMEs and
headline components say nothing about a nested component's adoption - inspect
the manifests.

## Onboarding request format

The registry repository's issue tracker is used for onboarding requests. File
one issue titled exactly:

```
[NQL-ONBOARD] <component_id>
```

The body must contain the following key lines, one per line:

```
Component ID: <component_id>
Repository: <account>/<registry-repository-name>
Module Path: <path of the component relative to its project directory, or ".">
Spec Version: <spec_version from the manifest>
License: <license from the manifest>
Adoption Index: <adoption_index from the manifest>
Decision: <PRIORITY or WATCHLIST>
```

Do not file onboarding requests for components that are out of scope for the
cycle or that are not the selected component.
