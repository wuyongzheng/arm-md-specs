## K5.3 Recommended authentication interface

An implementation of the Armv8 and later architectures must support debug authentication described in Required debug authentication.

The details of the debug authentication interface are IMPLEMENTATION DEFINED, but Arm recommends the use of the CoreSight interface, which includes the following signals for external debug authentication:

- DBGEN .
- SPIDEN .

If FEAT\_Debugv8p4 is not implemented, Arm also recommends using the following signals:

- NIDEN .
- SPNIDEN .

If FEAT\_RME is implemented, Arm recommends the following additional signals for external debug authentication:

- RLPIDEN .
- RTPIDEN .

Arm recommends an interface in which DBGEN and SPIDEN are also used for self-hosted Secure debug authentication if either:

- EL3 is using AArch32 and SDCR.SPD == 0b00 .
- Secure EL1 is using AArch32 and MDCR\_EL3.SPD32 == 0b00 .

If EL3 is not implemented and the PE is in Non-secure state, SPIDEN and SPNIDEN are not implemented, and the PE behaves as if these signals were tied LOW.

If EL3 is not implemented and the PE is in Secure state, SPIDEN is usually connected to DBGEN and SPNIDEN is connected to NIDEN , but this is not required. The recommended interface is defined as if all four signals are implemented.

In order to include External debug state in Realm attestation when FEAT\_RME is implemented, the authentication signals that control External debug in the Realm and Root Security states must be sampled before execution starts in the corresponding Security state and not change value until a system reset event:

- For the RTPIDEN authentication signal, Arm expects that this behavior will be guaranteed by system construction.
- For the RLPIDEN authentication signal, this behavior can be guaranteed by system construction or by Root firmware.

How the authentication signals are driven is IMPLEMENTATION DEFINED. For example, the signals might be hard-wired, connected to fuses, or to an authentication module. The architecture permits PEs within a cluster to have independent authentication interfaces, but this is not required. Any Trace extension has the same authentication interface as the PE it is connected to.

If FEAT\_Debugv8p4 and CoreSight ETR are both implemented, the ETR has an independent DBGEN signal that must be tied HIGH to enable self-hosted use of trace.

Table K5-2 shows the debug authentication pseudocode functions and the recommended implementations.

Table K5-2 Recommended implementation of debug enable pseudocode functions

| Pseudocode function                                       | Description                                                         | Implementation                                  |
|-----------------------------------------------------------|---------------------------------------------------------------------|-------------------------------------------------|
| ExternalNoninvasiveDebugEnabled() a                       | Non-secure non-invasive debug enabled                               | ( DBGEN OR NIDEN c )                            |
| ExternalInvasiveDebugEnabled()                            | Non-secure invasive debug enabled                                   | DBGEN                                           |
| AArch32. SelfHostedSecurePrivilegedInvasiveDebugEnabled() | Secure invasive self-hosted debug enabled in AArch32 state (legacy) | ( DBGEN AND SPIDEN )                            |
| ExternalSecureNoninvasiveDebugEnabled () b                | Secure non-invasive debug enabled                                   | ( DBGEN OR NIDEN c )AND ( SPIDEN OR SPNIDEN d ) |
| ExternalSecureInvasiveDebugEnabled() e                    | Secure invasive debug enabled                                       | ( DBGEN AND SPIDEN )                            |
| ExternalRealmInvasiveDebugEnabled() f                     | Realm invasive debug enabled                                        | ( DBGEN AND RLPIDEN )                           |
| ExternalRootInvasiveDebugEnabled() f                      | Root invasive debug enabled                                         | ( DBGEN AND RLPIDEN AND SPIDEN AND RTPIDEN )    |

Table K5-3 shows the Security states that can be externally debugged with different values for the debug authentication signals, based on the recommended mapping:

## Table K5-3 Permitted external debug of Security states

|   DBGEN | SPIDEN   | RLPIDEN   | RTPIDEN   | Non-secure   | Secure a   | Realm b   | Root b   |
|---------|----------|-----------|-----------|--------------|------------|-----------|----------|
|       0 | x        | x         | x         | No           | No         | No        | No       |
|       1 | 0        | 0         | x         | Yes          | No         | No        | No       |
|       1 | 0        | 1         | x         | Yes          | No         | Yes       | No       |
|       1 | 1        | 0         | x         | Yes          | Yes        | No        | No       |
|       1 | 1        | 1         | 0         | Yes          | Yes        | Yes       | No       |
|       1 | 1 c      | 1         | 1         | Yes          | Yes        | Yes       | Yes      |

The Debug\_authentication() pseudocode function on shared/debug defines the authentication signals DBGEN , SPIDEN , RLPIDEN , RTPIDEN , NIDEN , and SPNIDEN .