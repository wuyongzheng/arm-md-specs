## B6.1 PSCI overview

- In this section,
- rec refers to the currently executing REC
- exit refer to the RmiRecExit object which was provided to the RMI\_REC\_ENTER command
- target\_rec refers to the REC object identified by an MPIDR value passed to a PSCI function.
- The RMM provides a trusted implementation of parts of the PSCI ABI. This section describes the checks performed by the RMM when a Realm executes a PSCI command, and the internal RMM state changes which result from a successful PSCI command execution. Successful execution by the RMM of some PSCI commands results in a REC exit due to PSCI , which allows the Host to perform further processing of the command.


- The HVC conduit for PSCI is not supported for Realms.

See also:

- Arm Power State Coordination Interface (PSCI) [16]
- A2.3.2 REC attributes
- A4.3.7 REC exit due to PSCI
- A4.5 Host call
- D1.4 PSCI flows

## B6.2 PSCI version

- The RMM must support version &gt;= 1.1 of the Power State Control Interface.

See also:

- B6.3.8 PSCI\_VERSION command