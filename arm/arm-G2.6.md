## G2.6 Pseudocode description of debug exceptions

The AArch32.Abort() function processes FaultRecord() , as described in Abort exceptions, and generates:

- Data Abort exceptions for watchpoints.
- Prefetch Abort exceptions for all other debug exceptions.