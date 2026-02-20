## H8.5 External debug interface register access permissions

Some external accesses to debug registers and Performance Monitor registers are not permitted and return an error response if:

- The Core power domain is powered down or is in low-power state where the registers cannot be accessed.
- OSLSR.OSLK == 1. The OS Lock is locked.
- FEAT\_DoubleLock is implemented and DoubleLockStatus() == TRUE. The OS Double Lock is locked.
- The access is disabled by either the authentication interface or secure monitor.

Not all registers are affected in all of these cases. For more information, see External debug interface register access permissions summary.

## H8.5.1 External debug over powerdown and locks

Accessing registers using the external debug interface is not possible when the Debug power domain is off. In this case, all accesses return an error.

External accesses to debug and Performance Monitors registers in the Core power domain are not permitted and return an error response if:

- The Core power domain is off or in low-power state where the registers cannot be accessed.
- OSLSR.OSLK == 1, meaning that the OS Lock is locked. This allows software to prevent external debugger modification of the registers while it saves and restores them over powerdown.
- FEAT\_DoubleLock is implemented and DoubleLockStatus() == TRUE. This means that the OS Double Lock is locked. The OS Double Lock ensures that it is safe to remove Core power by forcing the debug interface to be quiescent.

If FEAT\_DoubleLock is not implemented, the hardware must provide another method to safely remove Core power.

The OS Lock condition does not apply to the following debug registers:

- OSLAR\_EL1. This means that an external debugger can override this lock.
- EDESR. This means that an external debugger can program a debug event for when software unlocks the OS Lock. See OS Unlock Catch debug event.
- The ID registers that describe the PE to the debugger.

See also Debug registers to save over powerdown.

## H8.5.2 External access disabled

Accesses are further controlled by the external authentication interface. An untrusted external debugger cannot program the breakpoint and watchpoint registers to generate spurious debug exceptions. If external invasive debugging is not enabled, these external accesses to the registers are disabled. If EL3 is implemented, then SDCR provides additional external access controls for those registers.

The disable applies to:

- The DBGBVR&lt;n&gt;\_EL1, DBGBCR&lt;n&gt;\_EL1, DBGWVR&lt;n&gt;\_EL1, and DBGWCR&lt;n&gt;\_EL1 registers.
- From Armv8.2, the OSLAR\_EL1 register.

If FEAT\_Debugv8p2 is not implemented, it is IMPLEMENTATION DEFINED whether the disable applies to OSLAR\_EL1.

If FEAT\_Debugv8p4 is not implemented, the external debug interface cannot access these registers if any of the following are true:

- ExternalInvasiveDebugEnabled() == FALSE.
- ExternalSecureInvasiveDebugEnabled() == FALSE, EL3 is not implemented, and the PE behaves as if the Security state is Secure.

- ExternalSecureInvasiveDebugEnabled() == FALSE, EL3 is implemented and SDCR.EDAD == 1.

If FEAT\_Debugv8p4 is implemented, accesses from the external debug interface to these registers are not permitted if any of the following are true:

- EL3 is not implemented, the PE behaves as if the Security state is Secure, and the access is Non-secure.
- The access is not permitted by SDCR.EDAD and, if FEAT\_RME is implemented, MDCR\_EL3.EDADE.

The AllowExternalDebugAccess() pseudocode function describes these accessibility rules.

PEs might also provide an OPTIONAL external debug interface to the Performance Monitor registers. The authentication interface and SDCR provide similar external access disable controls for those registers.

If FEAT\_Debugv8p4 is not implemented, the external debug interface cannot access the Performance Monitor registers if any of the following are true:

- ExternalNoninvasiveDebugEnabled() == FALSE.
- ExternalSecureNoninvasiveDebugEnabled() == FALSE, EL3 is not implemented and the PE behaves as if the Security state is Secure.
- ExternalSecureNoninvasiveDebugEnabled() == FALSE, EL3 is implemented and SDCR.EPMAD == 1.

Note

Arm recommends that Secure software that is not making use of debug hardware does not lock out the external debug interface.

If FEAT\_Debugv8p4 is implemented, accesses from the external debug interface to these registers are not permitted if any of the following are true:

- EL3 is not implemented, the PE behaves as if the Security state is Secure, and the access is Non-secure.
- The access is not permitted by SDCR.EDAD and, if FEAT\_RME is implemented, MDCR\_EL3.EDADE.

The AllowExternalPMUAccess() pseudocode function describes these accessibility rules.

## H8.5.3 Behavior of a not permitted access

For an external debug interface access by a Debug Access Port, the Debug Access Port receives the error response and must signal this to the external debugger. For an ADIv5 implementation of a Debug Access Port, the error sets a sticky error flag in the Debug Access Port that the debugger can poll, and that suppresses further accesses until it is explicitly cleared.

When an error is returned because external access is disabled, and this is the highest priority error condition, a sticky error flag in EDPRSR is indirectly written to 1 as a side-effect of the access:

- For a debug register access when AllowExternalDebugAccess () == FALSE, EDPRSR.SDAD is indirectly written to 1.
- For Performance Monitor register access when AllowExternalPMUAccess () == FALSE, EDPRSR.SPMAD is indirectly written to 1.

The indirect write might not occur for a memory-mapped access to the external debug interface. For more information, see Register access permissions for memory-mapped accesses.

If no error is returned, or the error is returned because of a higher priority error condition, the flag in EDPRSR is unchanged.

See also Behavior of a not permitted memory-mapped access.

For more information, see Arm ® Debug Interface Architecture Specification .

## H8.5.4 External debug interface register access permissions summary

For accesses to:

- IMPLEMENTATION DEFINED registers, see IMPLEMENTATION DEFINED registers.
- OPTIONAL registers for CoreSight compliance, see Management registers and CoreSight compliance.
- Reserved, unallocated, or unimplemented registers, writes to read-only registers, and reads of write-only registers, see Reserved and unallocated registers.

For all other external debug interface, CTI, and Performance Monitor registers, Table H8-3, Table H8-4, Table H8-6 and Table I3-2, show the response of the PE to accesses by the external debug interface.

## H8.5.5 IMPLEMENTATION DEFINED registers

Register access permissions for IMPLEMENTATION DEFINED debug, Performance Monitors, and CTI registers are IMPLEMENTATION DEFINED, other than as follows:

- If FEAT\_DoPD is implemented, then all of the following apply:
- -All debug and Performance Monitors registers, including IMPLEMENTATION DEFINED registers, are implemented in the Core power domain and accesses return an error when the Core power domain is off or in a low-power state.
- -CTI registers, including IMPLEMENTATION DEFINED registers, are implemented in the Debug power domain.
- When memory-mapped access to the external debug interface is supported, the additional constraints in Register access permissions for memory-mapped accesses apply to IMPLEMENTATION DEFINED registers.

## H8.5.6 Reserved and unallocated registers

The default access requirements for reserved and unallocated registers are described in Access requirements for reserved and unallocated registers.

Note

Reads of WO and writes to RO refers to the default access permissions for a register. For example, when the SLK field is 1, meaning that the relevant registers become RO, a memory-mapped write to a RW register is ignored, and not treated as a reserved access.

The following reserved registers are RES0 in all conditions, other than when debug power is off:

- All reserved CTI registers.
- For the debug registers, and Performance Monitors registers, if the implementation is CoreSight architecture compliant, and either FEAT\_DoPD is not implemented or the Core power domain is on, all reserved registers in the range 0xF00 -0xFFC . See Management register access permissions.

Otherwise, the architecture defines that:

1. If debug power is off, all register accesses, including reserved accesses, return an error.
2. For reserved debug registers and Performance Monitors registers, if FEAT\_DoPD is implemented, and the Core power domain is off or in a low-power state, the response is an error. Otherwise, the response is a CONSTRAINED UNPREDICTABLE choice of error or RES0, when any of the following hold:
3. In addition, for reserved debug registers in the address ranges 0x400 -0x4FC and 0x800 - 0x8FC , the response is a CONSTRAINED UNPREDICTABLE choice of error or RES0 when conditions 1 or 2 do not apply and:

Off

The Core power domain is either completely off or in a low-power state in which the Core power domain registers cannot be accessed.

DLK

FEAT\_DoubleLock is implemented and DoubleLockStatus() == TRUE. The OS Double Lock is locked.

OSLK

OSLSR.OSLK == 1. The OS Lock is locked.

EDAD

AllowExternalDebugAccess() == FALSE. External debug is disabled.

Note

See also Behavior of a not permitted access.

4. In addition, for reserved Performance Monitors registers in the address ranges 0x000 - 0xEFC , the response is a CONSTRAINED UNPREDICTABLE choice of error or RES0 when conditions 1 or 2 do not apply and:

EPMAD

AllowExternalPMUAccess() == FALSE. External Performance Monitor access is disabled.

Note

See also Behavior of a not permitted access.

5. For reads of WO locations, the response is a CONSTRAINED UNPREDICTABLE choice of error or RES0 when the architecture permits or requires a write to the location to return an error.
6. For writes of RO locations, the response is a CONSTRAINED UNPREDICTABLE choice of error or RES0 when the architecture permits or requires a read to the location to return an error.
7. For reads and writes of locations for features that are not implemented, the response is a CONSTRAINED UNPREDICTABLE choice of error or RES0 when the architecture permits or requires an access to the location to return an error if the feature is implemented.