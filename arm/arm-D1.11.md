## D1.11 Check Feature

IFCDFK

FEAT\_CHK provides CHKFEAT with the following properties:

- CHKFEAT is allocated from the Hint instruction space, to allow it to be used on any PE, regardless of whether FEAT\_CHK is implemented.
- CHKFEAT takes a value as an input where one or more bits of the input value is set to 1 to test whether the requested feature is enabled, and if the feature is enabled the relevant bit is cleared to 0. Otherwise, the bit is unchanged.
- When FEAT\_CHK is not implemented, the input value is unchanged, indicating the requested feature is not enabled.
- CHKFEAT returns the state of GCSEnabled() .

For the encoding allocation for CHKFEAT , see op0 == 0b00 , architectural hints, barriers and CLREX, and PSTATE access.

Since the CHKFEAT instruction is in the Hint instruction encoding space, it is effectively implemented on all PEs that support AArch64. However, the CHKFEAT instruction only returns a result value that is different from the input value when any of the features that are identified by the CHKFEAT are implemented.

An example of how CHKFEAT can be used in an implementation independent manner is shown below.

## Example D1-1 Example code for using CHKFEAT

```
MOV X16, #0x1 ; X16 has bit [0] set to select GCS CHKFEAT X16 ; Updates X16 with the status of GCS TBNZ X16, #0, skipgcs ; Skip over GCS code if GCS is not enabled ... ; GCS related code skipgcs:
```

ICZRRH

IQMQXS

RVXBTN

## Chapter D2 AArch64 Self-hosted Debug

When the PE is using self-hosted debug, it generates debug exceptions . This chapter describes the AArch64 self-hosted debug Exception model. It is organized as follows:

## Introductory information

- About self-hosted debug.
- The debug exception enable controls.

## The debug Exception model

- Routing debug exceptions.
- Enabling debug exceptions from the current Exception level and Security state.
- The effect of powerdown on debug exceptions.
- Summary of the routing and enabling of debug exceptions.
- Pseudocode description of debug exceptions.

## The debug exceptions

- Breakpoint Instruction exceptions.
- Breakpoint exceptions.
- Watchpoint exceptions.
- Vector Catch exceptions.
- Software Step exceptions.

## Synchronization requirements

The behavior of self-hosted debug after changes to System registers, or after changes to the authentication interface, but before a Context Synchronization event guarantees the effects of the changes:

- Synchronization and debug exceptions.