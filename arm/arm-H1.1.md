## H1.1 Introduction to external debug

The A-profile supports both:

## Self-hosted debug

The PE itself hosts a debugger. That is, developers developing software to run on the PE use debugger software running on the same PE.

## External debug

The debugger is external to the PE. The debugging might be either on-chip, for example in a second PE, or off-chip, for example a JTAG debugger that accesses the chip through a Debug Access Port.

External debug is particularly useful for:

- Hardware bring-up. That is, debugging during development when a system is first powered up and not all of the software functionality is available.
- PEs that are deeply embedded inside systems.

To support external debug, the Arm architecture defines required features that are called external debug features.

Note

An external debugger has a potentially high level of control over and visibility into the PE. The system sets this level using debug authentication. See Required debug authentication. If the debug authentication level is set too low, agents may be able to bypass elements of the security and privilege models. This includes both off-chip agents and on-chip agents such as unprivileged or Non-secure software.

## H1.1.1 Definition and constraints of a debugger in the context of external debug

When the description of external debug in this Part of the manual describes a debugger as controlling external debug this debugger might be a second on-chip PE or an off-chip device such as a JTAG debugger using a Debug Access Port (DAP).

If a Debug Access Port is implemented:

- When debug is prohibited at the Debug Access Port, the port must not generate accesses to the external debug interface of the PE.
- When debug is prohibited for a Security state at the Debug Access Port, it must not be possible to generate accesses to PA spaces that are not accessible for that Security state.
- When accesses for a Security state are allowed at the Debug Access Port, the port must be able to generate accesses to PA spaces that are accessible for that Security state.

If FEAT\_Debugv8p4 is not implemented, accesses to the PE are controlled by the external authentication interface functions, ExternalInvasiveDebugEnabled() , ExternalNoninvasiveDebugEnabled() , ExternalSecureNoninvasiveDebugEnabled() , and ExternalSecureInvasiveDebugEnabled() .

If FEAT\_TRBE and FEAT\_RME are implemented, the external authentication interface functions ExternalRealmNoninvasiveDebugEnabled (), ExternalRealmInvasiveDebugEnabled (), ExternalRootNoninvasiveDebugEnabled ExternalRootInvasiveDebugEnabled

(), and () are added.

If FEAT\_Debugv8p4 is implemented, the bus Requester, which may be the Debug Access Port, controls the accesses it makes to the PE and MDCR\_EL3.{EPMAD, EDAD} and, if FEAT\_TRBE is implemented, MDCR\_EL3.ETAD, control access to registers by an external debugger.

If FEAT\_TRBE and FEAT\_RME are implemented, MDCR\_EL3.{ETAD, EPMAD, EDAD, EDADE, ETADE, EPMADE} control the Security state of access to registers by an external debugger.

If FEAT\_Debugv8p4 is not implemented, the external authentication interface functions override MDCR\_EL3.{EPMAD, EDAD}.

The Debug Access Port is not required to use the same authentication interface as the PE.

Arm recommends the following authentication interface:

- When ExternalSecureInvasiveDebugEnabled() == FALSE at the PE, Secure debug is disabled at the DAP.
- When ExternalRealmInvasiveDebugEnabled () == FALSE at the PE, Realm debug is disabled at the DAP.
- When ExternalRootInvasiveDebugEnabled () == FALSE at the PE, Root debug is disabled at the DAP.
- When ExternalInvasiveDebugEnabled() == FALSE at the PE, all debug is prohibited at the DAP.

See also Required debug authentication.