## A2.1 About the A-profile architecture extensions

An architecture extension defines a set of features that, when implemented, may make an implementation compliant with the extension.

Each feature description includes:

- Afeature name.
- Abrief description of the feature.
- The Execution state the feature is supported in.
- Whether the implementation of the feature is mandatory or OPTIONAL.
- Dependencies on the implementation of other features if any.
- The register field that identifies the presence of the feature.

## A2.1.1 Permitted implementation of subsets of the A-profile architectural features

Arm regularly introduces new features to the architecture. When a feature is introduced, the architecture specifies when the feature can be implemented. Typically, a feature introduced as part of Armv8. x or Armv9. x is permitted to be built in Armv8.( x -1) or Armv9.( x -1), subject only to those constraints that require that certain features be implemented together.

See the individual feature descriptions for details of when each feature is permitted or required to be built.

## A2.1.2 Withdrawn architecture features

This section lists features previously described in the architecture but subsequently withdrawn. Features listed in this section are not permitted to be included in any version of the architecture:

## FEAT\_TME, Transactional Memory Extension

FEAT\_TME introduced a set of instructions to support hardware transaction memory, which means a group of instructions can appear to be collectively executed as a single atomic operation.