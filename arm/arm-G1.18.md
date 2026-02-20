## G1.18 Reset into AArch32 state

Resets and power domains describes the Armv8 reset model, including the defined levels of reset. When reset is deasserted, the PE starts executing instructions in the highest implemented Exception level. If that Exception level is using AArch32, then it starts execution:

- In Secure state, if the implementation includes EL3.
- With interrupts disabled:
- -In Hyp mode, if the highest implemented Exception level is EL2.
- -In Supervisor mode, otherwise.

Note

- This section describes the architectural requirements for a reset into AArch32 state. It takes no account of whether Arm licenses any particular combination of Exception levels and Execution state. For more information about the licensed combinations, see Exception levels.
- The Execution state in which the highest implemented Execution level starts executing instructions on coming out of reset might be determined by a configuration input signal.

Reset returns some PE state to architecturally-defined or IMPLEMENTATION DEFINED values, and makes other state UNKNOWN, as described in PE state on reset into AArch32 state. For more information about behavior when resetting into an Exception level using AArch32, see:

- Behavior of caches at reset.
- Enabling stages of address translation.
- TLB behavior at reset.
- Reset and debug.

When reset is deasserted, if the PE resets into an Exception level that is using AArch32, it is IMPLEMENTATION DEFINED whether execution starts:

- From an IMPLEMENTATION DEFINED address.
- If reset is into EL3 or EL1, from the low or high reset vector address, as determined by the reset value of the SCTLR.V bit. This reset value can be determined by an IMPLEMENTATION DEFINED configuration input signal.

Note

This option might be implemented for compatibility with earlier versions of the architecture.

Software might be able to identify the reset address:

- If reset is into EL3, by reading the reset value of MVBAR. That is, after coming out of reset, by reading MVBAR before the boot software has updated it. It is IMPLEMENTATION DEFINED whether this discovery mechanism is supported.
- If reset is into EL2 or EL1, by reading RVBAR. RVBAR can only be implemented at the highest implemented Exception level, and only if that Exception level is not EL3.

If RVBAR is not implemented, and at all Exception levels other than the highest implemented Exception level, the encoding for RVBAR is UNDEFINED.

The Arm architecture does not define any way of returning to a previous Execution state from a reset.

## G1.18.1 PE state on reset into AArch32 state

Immediately after a reset, much of the PE state is architecturally UNKNOWN. However, some of the PE state is defined, see the individual register descriptions for more information. The state that is reset to known values is sufficient to permit predictable initial execution at the highest Exception level, such that this execution is then capable of initializing the remaining state of the system where necessary before use.

If the PE resets to AArch32 state using either a Cold or a Warm reset, the PE state that is defined is as follows:

- The global exclusive monitor and local exclusive monitor for the PE are UNKNOWN.
- If reset is into EL2 using AArch32, then reset is into Hyp mode and PSTATE.M resets to 0b1010 , otherwise reset is into Supervisor mode and PSTATE.M resets to 0b0011 .
- PSTATE.IL resets to 0.

## G1.18.2 Pseudocode descriptions of reset

The AArch32.TakeReset() pseudocode procedure describes how the PE behaves when reset is deasserted.

The AArch32.ResetGeneralRegisters() pseudocode function resets the general-purpose registers.

The AArch32.ResetSIMDFPRegisters() pseudocode function resets the SIMD and floating-point registers.

The AArch32.ResetSpecialRegisters() pseudocode function resets the Special-purpose registers, and the debug System registers DLR and DSPSR, which are used for handling Debug exceptions.

The AArch32.ResetSystemRegisters() pseudocode function resets all System registers in the ( coproc == 0b111x ) encoding space to their reset state as defined in the register descriptions in AArch32 System Register Descriptions.

Note

The AArch32.ResetSystemRegisters () function only resets the System registers. It has no effect on memory-mapped registers.

The ResetExternalDebugRegisters() pseudocode function resets all external debug registers to their reset state as defined in the register descriptions in External Debug Register Descriptions.