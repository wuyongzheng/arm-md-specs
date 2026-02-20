## H6.7 Reset and debug

All registers in the Core power domain are either:

- Reset by both a Cold and a Warm reset.
- Reset only by a Cold reset and are not changed by a Warm reset.

For more information, see Resets and power domains.

All registers in the Debug power domain are reset by an External Debug reset.

If FEAT\_SPMU is implemented, the reset signals for a System PMU are IMPLEMENTATION DEFINED.

Figure H6-1 shows this reset scheme. The following three reset signals are an example implementation of the reset scheme:

- CORERESET , which must be asserted for a Warm reset.
- CPUPORESET , which must be asserted for a Cold reset.
- PRESETDBG , which must be asserted for an External Debug reset.

As shown in the figure, the external debug logic is split between the Debug power domain and the Core power domain.

Figure H6-1 Power and reset domains

<!-- image -->

For more information about power domains and power states, see Power domains and debug.

When power is first applied to the Debug power domain, PRESETDBG must be asserted.

When power is first applied to the Core power domain, CPUPORESET must be asserted.

Note

In this scheme, logic in the Warm reset domain is reset by asserting either CORERESET or CPUPORESET . This implies a particular implementation style that permits these approaches.

CPUPORESET is not normally asserted on moving from a low-power state, where power has not been removed, to a full-power state. This can occur, for example, on exiting a low-power retention state. See also Emulating low-power states and the EDPRSR register description.

## H6.7.1 External debug interface accesses to registers in reset

If a reset signal is asserted and the external debug interface:

- Writes a register, or indirectly writes a register or register field as a side-effect of an access:

- -Then, if the register or register field is reset by that reset signal, it is CONSTRAINED UNPREDICTABLE whether the register or register field takes the reset value or the value written. The reset value might be UNKNOWN.
- -Otherwise, the register or register field takes the value that is written.
- Reads a register, or indirectly reads a register or register field, as part of an access:
- -Then, if the register or register field is reset by that reset signal, the value returned in UNKNOWN.
- -Otherwise, the value of the register or register field is returned.

It is IMPLEMENTATION DEFINED whether any register can be accessed when External Debug reset is being asserted. The result of these accesses is IMPLEMENTATION DEFINED.

## Chapter H7

## The PC Sample-based Profiling Extension

This chapter describes the OPTIONAL PC Sample-based Profiling Extension that provides a non-invasive external debug component.

It contains the following section:

- About the PC Sample-based Profiling Extension.