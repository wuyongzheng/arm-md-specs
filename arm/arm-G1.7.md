## G1.7 Security state, Exception levels, and AArch32 execution privilege

The hierarchy of software execution privilege, within a particular Security state, is defined by the Exception levels, with higher Exception level numbers indicating higher privilege. Table G1-1 shows this hierarchy for each Security state.

Table G1-1 Execution privilege and Exception levels, by Security state

| Execution privilege   | Secure state   | Non-secure state   | Typical use                      |
|-----------------------|----------------|--------------------|----------------------------------|
| Highest               | EL3            | - a                | Secure monitor                   |
| -                     | EL2 b          | EL2                | Hypervisor                       |
| -                     | EL1            | EL1                | Secure or Non-secure OS          |
| Lowest, Unprivileged  | EL0            | EL0                | Secure or Non-secure application |

When executing in AArch32 state, within a given Security state, the current PE state, including the execution privilege, is primarily indicated by the current PE mode . In Secure state, how the PE modes map onto the Exception levels depends on whether EL3 is using AArch32 or is using AArch64, and:

- Figure G1-1 shows this mapping when EL3 is using AArch32.
- Figure G1-2 shows this mapping when EL3 is using AArch64.

Table G1-2 shows this mapping. In interpreting this table:

- Monitor mode is implemented only in Secure state, and only if EL3 is using AArch32.
- Hyp mode is implemented only in Non-secure state, and only if EL2 is using AArch32.
- System, FIQ, IRQ, Supervisor, Abort, and Undefined modes are implemented:
- User mode is implemented if EL0 is using AArch32.

In Secure state

If either:

- EL3 is using AArch32.

- EL3 is using AArch64 and EL1 is using AArch32.

In Non-secure state

If EL1 is using AArch32.

Table G1-2 Mapping of AArch32 PE modes to Exception levels

|                 | PE modes in the given Security state, and EL3 Execution state   | PE modes in the given Security state, and EL3 Execution state   |                                                |
|-----------------|-----------------------------------------------------------------|-----------------------------------------------------------------|------------------------------------------------|
| Exception level | Secure state, EL3 using AArch32                                 | Secure state, EL3 using AArch64 a                               | Non-secure state                               |
| EL3             | Monitor, System, FIQ, IRQ, Supervisor, Abort, Undefined         | -                                                               | -                                              |
| EL2             | -                                                               | -                                                               | Hyp                                            |
| EL1             | -                                                               | System, FIQ, IRQ, Supervisor, Abort, Undefined                  | System, FIQ, IRQ, Supervisor, Abort, Undefined |
| EL0             | User                                                            | User                                                            | User                                           |

Because AArch32 behavior is described in terms of the PE modes, and transitions between PE modes, the Exception levels are implicit in most of the description of operation in AArch32 state.

## G1.7.1 Limited use of Privilege level in AArch32 state

As described in The VMSAv8-32 translation regimes, a translation regime maps a virtual address (V A) to the corresponding physical address (PA). The VMSAv8-64 translation regimes are defined by the Exception levels that use them. However, because the mapping between PE modes and Exception levels in Secure state depends on whether EL3 is using AArch32 or is using AArch64, as shown in Table G1-2, the VMSAv8-32 translation regimes cannot be described simply in terms of either the Exception levels or the PE modes that use them.

To provide a consistent description of address translation as seen from AArch32 state, the VMSAv8-32 translation regimes are described in terms of the Privilege levels originally defined in the Armv7 descriptions of AArch32 state. Table G1-3 shows how the PE modes map to these Privilege levels:

Table G1-3 Mapping of PE modes to AArch32 Privilege levels

| Privilege level   | Secure state                                               | Non-secure state                               |
|-------------------|------------------------------------------------------------|------------------------------------------------|
| PL2               | -                                                          | Hyp a                                          |
| PL1               | Monitor b , System, FIQ, IRQ, Supervisor, Abort, Undefined | System, FIQ, IRQ, Supervisor, Abort, Undefined |
| PL0               | User                                                       | User                                           |

Comparing Table G1-3 with Table G1-2 shows that:

## In Non-secure state

Each privilege level maps to the corresponding Exception level. For example, PL1 maps to EL1.

## In Secure state

PL0 maps to EL0.

The mapping of PL1 depends on the Execution state being used by EL3, as follows:

EL3 using AArch64 Secure PL1 maps to Secure EL1. Monitor mode is not implemented.

EL3 using AArch32 Secure PL1 maps to Secure EL3. Monitor mode is implemented as one of the Secure PL1 modes.