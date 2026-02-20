## G1.16 Asynchronous exception behavior for exceptions taken from AArch32 state

In an implementation that does not include EL2 or EL3, the asynchronous exceptions behave as follows when EL1 and EL0 are both using AArch32:

- An SError exception is taken to Abort mode.
- An IRQ exception is taken to IRQ mode.
- An FIQ exception is taken to FIQ mode.

These are the default PE modes for taking these exceptions.

However, the PSTATE.{A, I, F} bits mask the asynchronous exceptions, meaning that when the value of one of these PSTATE bits is 1, the corresponding exception is not taken.

If a masked asynchronous exception remains signaled, then the exception remains pending unless the value of the PSTATE bit is changed to 0.

EL2 and EL3 provide controls that affect:

- The routing of these exceptions, see Asynchronous exception routing controls.
- Masking of these exceptions in Non-secure state, see Asynchronous exception masking controls.

Similar register control bits are provided regardless of whether EL2 and EL3 are using AArch32 or AArch64:

- The EL2 controls are provided by the HCR when EL2 is using AArch32, and by the HCR\_EL2 when EL2 is using AArch64.
- The EL3 controls are provided by the SCR when EL3 is using AArch32, and by the SCR\_EL3 when EL3 is using AArch64.

Therefore, most references to the HCR or SCR in this section are to entries in Table K14-1, which disambiguates between AArch32 registers and AArch64 registers. However, the Execution states used by EL2 and EL3 do affect some aspects of the routing and masking of the asynchronous exceptions, see Asynchronous exception routing and masking with higher Exception levels using AArch64.

## G1.16.1 Virtual exceptions when an implementation includes EL2

When implemented, EL2 provides the following virtual exceptions, which correspond to the physical asynchronous exceptions:

- Virtual SError, which corresponds to a physical external SError exception.
- Virtual IRQ, which corresponds to a physical IRQ.
- Virtual FIQ, which corresponds to a physical FIQ.

When the value of HCR.TGE is 0 and the value of an HCR.{AMO, IMO, FMO} routing control bit is 1, the corresponding virtual interrupt is enabled and a virtual exception is generated either:

- By setting the corresponding virtual interrupt pending bit, HCR.{V A, VI, VF}, to 1.
- For a Virtual IRQ or Virtual FIQ, by an IMPLEMENTATION DEFINED mechanism. This might be a signal from an interrupt controller. See, for example, the ARMGeneric Interrupt Controller Architecture Specification .

When the value of HCR\_EL2.TGE is 1, all virtual interrupts are disabled.

When a virtual interrupt is disabled:

- It cannot be taken.
- It cannot be seen in the ISR.

In AArch32 state, a virtual exception is taken only from a Non-secure EL1 or EL0 mode. In any other mode, if the exception is generated it is not taken.

Avirtual exception is taken in Non-secure state to the default mode for the corresponding physical exception. This means:

- AVirtual SError is taken to Non-secure Abort mode.
- AVirtual IRQ is taken to Non-secure IRQ mode.
- AVirtual FIQ is taken to Non-secure FIQ mode.

Table G1-15 summarizes the HCR bits that route asynchronous exceptions to EL2, and the bits that generate the virtual exceptions.

Table G1-15 HCR bits controlling asynchronous exceptions

| Exception   | Routing the physical exception to EL2   | Generating the virtual exception   |
|-------------|-----------------------------------------|------------------------------------|
| SError      | HCR.AMO                                 | HCR.VA                             |
| IRQ         | HCR.IMO                                 | HCR.VI                             |
| FIQ         | HCR.FMO                                 | HCR.VF                             |

The HCR.{VA, VI, VF} bits generate a virtual exception only if set to 1 when the value of the corresponding HCR.{AMO, IMO, FMO} is 1.

Similarly, if the implementation also includes EL3, the HCR.{AMO, IMO, FMO} bits route the corresponding physical exception to Hyp mode only if the physical exception is not routed to Monitor mode by the SCR.{EA, IRQ, FIQ} bit. For more information, see Asynchronous exception routing controls.

When the value of an HCR.{AMO, IMO, FMO} control bit is 1, the corresponding mask bit in PSTATE:

- Does not mask the physical exception.
- Masks the virtual exception when the PE is executing in a Non-secure EL1 or EL0 mode.

Taking a Virtual Abort exception clears HCR.V A to zero. Taking a Virtual IRQ exception or a Virtual FIQ exception does not affect the value of HCR.VI or HCR.VF.

Note

This means that the exception handler for a Virtual IRQ exception or a Virtual FIQ exception must cause software that is executing at EL2 or EL3 to update the HCR to clear the appropriate virtual exception bit to 0.

See WFE wakeup events and Wait For Interrupt for information about how virtual exceptions affect wake up from power-saving states.

Note

A hypervisor can use virtual exceptions to signal exceptions to the current Guest OS. The Guest OS takes a virtual exception exactly as it would take the corresponding physical exception, and is unaware of any distinction between virtual exception and the corresponding physical exception.

## G1.16.1.1 Effects of the HCR.{AMO, IMO, FMO} bits

As described in this section, the HCR.{AMO, IMO, FMO} bits are part of the mechanism for enabling the virtual exceptions. In addition, for exceptions generated in Non-secure state:

- As mentioned in this section, affect the routing of the exceptions. See Asynchronous exception routing controls.
- Affect the masking of the exceptions. See Asynchronous exception masking controls.

## G1.16.2 Asynchronous exception routing controls

Note

This section describes the behavior when all Exception levels are using AArch32. For the differences when this is not the case see Asynchronous exception routing and masking with higher Exception levels using AArch64.

In an implementation that includes EL3 the following bits in the SCR control the routing of asynchronous exceptions:

- SCR.EA
- When the value of this bit is 1, any SError exception is taken to Monitor mode. Note Although this section describes the asynchronous exception routing controls, SCR.EA also controls the

routing of synchronous External aborts, see Routing of aborts taken to AArch32 state.

- SCR.FIQ When the value of this bit is 1, any FIQ exception is taken to Monitor mode.
- SCR.IRQ When the value of this bit is 1, any IRQ exception is taken to Monitor mode.

Only Secure software can change the values of these bits.

In an implementation that includes EL2, the following bits in the HCR route asynchronous exceptions to EL2, for exceptions that are both:

- Taken from a Non-secure EL1 or EL0 mode.
- If the implementation also includes EL3, not configured, by the SCR.{EA, FIQ, IRQ} controls, to be taken to EL3.
- HCR.AMO When the value of this bit is 1, an SError exception taken from a Non-secure EL1 or EL0 mode is taken to EL2, instead of to Non-secure Abort mode. If the implementation also includes EL3, this control applies only if the value of SCR.EA is 0. When the value of SCR.EA is 1, the value of the AMO bit is ignored.
- HCR.FMO When the value of this bit is 1, an FIQ exception taken from a Non-secure EL1 or EL0 mode is taken to EL2, instead of to Non-secure FIQ mode. If the implementation also includes EL3, this control applies only if the value of SCR.FIQ is 0. When the value of SCR.FIQ is 1, the value of the FMO bit is ignored.
- HCR.IMO When the value of this bit is 1, an IRQ exception taken from a Non-secure EL1 or EL0 mode is taken to

EL2, instead of to Non-secure IRQ mode. If the implementation also includes EL3, this control applies only if the value of SCR.IRQ is 0. When the value of SCR.IRQ is 1, the value of the IMO bit is ignored.

When EL2 is using AArch32 and the value of one of the HCR.{AMO, FMO, IMO} bits is 1, the exception is taken to Hyp mode.

Only software executing in Hyp mode, or Secure software executing at EL3 with SCR.NS set to 1, can change the values of these bits. If EL3 is using AArch32, this requires the Secure software to be executing in Monitor mode.

The HCR.{AMO, FMO, IMO} bits also affect the masking of asynchronous exceptions in Non-secure state, as described in Asynchronous exception masking controls.

The SCR.{EA, FIQ, IRQ} and HCR.{AMO, FMO, IMO} bits have no effect on the routing of Virtual Abort, Virtual FIQ, and Virtual IRQ exceptions.

Note

When the PE is in Hyp mode:

- Physical asynchronous exceptions that are not routed to Monitor mode are taken to Hyp mode.
- Virtual exceptions are not signaled to the PE.

See also Asynchronous exception behavior for exceptions taken from AArch32 state.

## G1.16.3 Asynchronous exception masking controls

Note

This section describes the behavior when all Exception levels are using AArch32. For the differences when this is not the case see Asynchronous exception routing and masking with higher Exception levels using AArch64.

The PSTATE.{A, I, F} bits can mask the taking of the corresponding exceptions from AArch32 state, as follows:

- PSTATE.A can mask SError exceptions.
- PSTATE.I can mask IRQ exceptions.
- PSTATE.F can mask FIQ exceptions.

In an implementation that does not include either of EL2 and EL3, setting one of these bits to 1 masks the corresponding exception, meaning the exception cannot be taken.

In an implementation that includes EL2, the HCR.{AMO, IMO, FMO} bits modify the masking of exceptions taken from Non-secure state.

Similarly, in an implementation that includes EL3, the SCR.{AW, FW} bits modify the masking of exceptions taken from Non-secure state by the PSTATE.{A, F} bits.

An implementation that includes only EL1 and EL0 does not provide any masking of the PSTATE.{A, I, F} bits. The following subsections describe the masking of these bits in other implementations:

- Asynchronous exception masking in an implementation that includes EL2 but not EL3.
- Asynchronous exception masking in an implementation that includes EL3 but not EL2.
- Asynchronous exception masking in an implementation that includes both EL2 and EL3.
- Summary of the asynchronous exception masking controls.

## G1.16.3.1 Asynchronous exception masking in an implementation that includes EL2 but not EL3

The HCR.{AMO, IMO, FMO} bits modify the effect of the PSTATE.{A, I, F} bits. When the value of an HCR.{AMO, IMO, FMO} mask override bit is 1, the value of the corresponding PSTATE.{A, I, F} bit is ignored when the exception is taken from a Non-secure mode other than Hyp mode.

## G1.16.3.2 Asynchronous exception masking in an implementation that includes EL3 but not EL2

The SCR.{AW, FW} bits modify the effect of the PSTATE.{A, F} bits. When the value of one of the SCR.{AW, FW} bits is 0, the corresponding PSTATE bit is ignored when both of the follow apply:

- The corresponding exception is taken from Non-secure state.
- The value of the corresponding SCR.{EA, FIQ} bit is 1, routing the exception to EL3. This means the exception is routed to Monitor mode if EL3 is using AArch32.

Note

Whenever the value of PSTATE.I is 1, IRQ exceptions are masked and cannot be taken.

## G1.16.3.3 Asynchronous exception masking in an implementation that includes both EL2 and EL3

When the value of an HCR.{AMO, IMO, FMO} mask override bit is 1, the value of the corresponding PSTATE.{A, I, F} bit is ignored when both of the following apply:

- The exception is taken from Non-secure state.
- Either:
- -The corresponding SCR.{EA, IRQ, FIQ} bit routes the exception to Monitor mode.
- -The exception is taken from a Non-secure mode other than Hyp mode.

In addition, when the value of an SCR.{AW, FW} bit is 0, the value of the corresponding PSTATE.{A, F} bit is ignored when all of the following apply:

- The exception is taken from Non-secure state.
- The corresponding SCR.{EA, FIQ} bit routes the exception to Monitor mode.
- The corresponding HCR.{AMO, FMO} mask override bit is set to 0.

## G1.16.3.4 Summary of the asynchronous exception masking controls

The tables in this section show the masking controls for each of the PSTATE.{A, I, F} bits. For an implementation that does not include all of the Exception levels:

## If the implementation includes only EL1 and EL0

The PSTATE bits cannot be masked. The behavior is as shown in the Secure row of the tables.

## If the implementation includes EL2 but not EL3

The behavior is as shown in the Non-secure table rows when the control bits in the SCR are both 0.

## If the implementation includes EL3 but not EL2

The behavior is as shown in the table rows where the control bit in the HCR is 0.

Table G1-16 shows the controls of the masking of SError exceptions by PSTATE.A.

Table G1-16 Control of masking by PSTATE.A

| Security state   | HCR.AMO   | SCR.EA   | SCR.AW   | Mode    | PSTATE.A                              |
|------------------|-----------|----------|----------|---------|---------------------------------------|
| Secure           | x         | x        | x        | x       | Masks SError exception, when set to 1 |
| Non-secure       | 0         | 0        | x        | x       | Masks SError exception, when set to 1 |
| Non-secure       | 0         | 1        | 0        | x       | Ignored                               |
| Non-secure       | 0         |          | 1        | x       | Masks SError exception, when set to 1 |
| Non-secure       | 1         | x        | x        | Not Hyp | Ignored                               |
| Non-secure       | 1         | 0        | x        | Hyp     | Masks SError exception, when set to 1 |
| Non-secure       | 1         | 1        | x        | x       | Ignored                               |

Table G1-17 shows the controls of the masking of IRQ exceptions by PSTATE.I.

Table G1-17 Control of masking by PSTATE.I

| Security state   | HCR.IMO   | SCR.IRQ   | Mode    | PSTATE.I                  |
|------------------|-----------|-----------|---------|---------------------------|
| Secure           | x         | x         | x       | Masks IRQs, when set to 1 |
| Non-secure       | 0         | x         | x       | Masks IRQs, when set to 1 |
|                  | 1         | x         | Not Hyp | Ignored                   |
|                  |           | 0         | Hyp     | Masks IRQs, when set to 1 |
|                  |           | 1         | x       | Ignored                   |

Table G1-18 shows the controls of the masking of FIQ exceptions by PSTATE.F.

## Table G1-18 Control of masking by PSTATE.F

| Security state   | HCR.FMO   | SCR.FIQ   | SCR.FW   | Mode    | PSTATE.F                  |
|------------------|-----------|-----------|----------|---------|---------------------------|
| Secure           | x         | x         | x        | x       | Masks FIQs, when set to 1 |
| Non-secure       | 0         | 0         | x        | x       | Masks FIQs, when set to 1 |
| Non-secure       | 0         | 1         | 0        | x       | Ignored                   |
| Non-secure       | 0         |           | 1        | x       | Masks FIQs, when set to 1 |
| Non-secure       | 1         | x         | x        | Not Hyp | Ignored                   |
| Non-secure       | 1         | 0         | x        | Hyp     | Masks FIQs, when set to 1 |
| Non-secure       | 1         | 1         | x        | x       | Ignored                   |

## G1.16.4 Asynchronous exception routing and masking with higher Exception levels using AArch64

Asynchronous exception routing controls and Asynchronous exception masking controls give full descriptions of the routing and masking of the asynchronous exceptions when all Exception levels are using AArch32. However, when EL0 and EL1 are using AArch32:

- As already described, the SCR and HCR controls might be from Exception levels that are using AArch64.
- If EL3 is using AArch64, or EL2 is using AArch64, there are some changes to the asynchronous exception behaviors.

Therefore, the following sections summarize the asynchronous exception behaviors, taking account of the Execution state being used at EL2 and EL3:

- Summary of physical interrupt routing.
- Summary of physical interrupt masking.

## G1.16.4.1 Summary of physical interrupt routing

The Table G1-19 shows the routing of physical FIQ and IRQ interrupts, and physical SError exceptions when the highest Exception level is using AArch32.

In this table:

| NS          | The Effective value of the field that determines the Security state of the PE in SCR.                                                                 |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| FIQIRQEA    | The Effective value of the field that handles the asynchronous exception type in SCR.                                                                 |
| TGE         | The Effective value of the field that handles general exceptions in HCRif EL2 is using AArch32, or HCR_EL2 if EL2 is using AArch64.                   |
| FMOIMOAMO   | The Effective value of the mask override field for the asynchronous exception type in HCRif EL2 is using AArch32, or HCR_EL2 if EL2 is using AArch64. |
| FIQ IRQ Abt | The exception is taken to the FIQ mode, the IRQ mode or the Abort mode according to the type of asynchronous exception.                               |
| Hyp         | The exception is taken to AArch32 Hyp mode.                                                                                                           |
| Mon         | The exception is taken to AArch32 Monitor mode.                                                                                                       |
| n/a         | This field does not exist, or the Exception level is not accessible in this configuration.                                                            |

Table G1-19 Routing of physical asynchronous exceptions

| Control bits   | Control bits   | Target when taken from   | Target when taken from   | Target when taken from   | Target when taken from   | Target when taken from   | Target when taken from   |
|----------------|----------------|--------------------------|--------------------------|--------------------------|--------------------------|--------------------------|--------------------------|
| NS             | FIQ IRQ EA     | TGE                      | FMO IMO AMO              | EL0                      | EL1                      | EL2                      | EL3                      |
| 0              | 0              | x                        | x                        | FIQ IRQ Abt              | n/a                      | n/a                      | FIQ IRQ Abt              |
|                | 1              | x                        | x                        | Mon                      | n/a                      | n/a                      | Mon                      |
| 1              | 0              | 0                        | 0                        | FIQ IRQ Abt              | FIQ IRQ Abt              | Hyp                      | FIQ IRQ Abt              |
|                |                | 0                        | 1                        | Hyp                      | Hyp                      | Hyp                      | FIQ IRQ Abt              |
|                |                | 1                        | x                        | Hyp                      | n/a                      | Hyp                      | FIQ IRQ Abt              |
|                | 1              | 0                        | x                        | Mon                      | Mon                      | Mon                      | Mon                      |
|                |                | 1                        | x                        | Mon                      | n/a                      | Mon                      | Mon                      |

## G1.16.4.2 Summary of physical interrupt masking

Table G1-20 shows the masking of physical FIQ and IRQ interrupts, and physical SError exceptions when the highest Exception level is using AArch32.

In this table:

NS

The Effective value of the field that determines the Security state of the PE in SCR.

FIQ IRQ EA

The Effective value of the field that handles the asynchronous exception type in SCR.

TGE

The Effective value of the field that handles general exceptions in HCR if EL2 is using AArch32, or HCR\_EL2 if EL2 is using AArch64.

FMOIMOAMO The Effective value of the mask override field for the asynchronous exception type in HCR.

FWAW

For FIQ interrupts, the SCR.FW field, and for SError exceptions, the SCR.AW field. For IRQ interrupts, there is no equivalent field, so the Effective value is 0 and rows where this cell is 1 should be ignored.

- A

When the interrupt is asserted, it is taken regardless of the value of the PSTATE mask bit.

- B

When the interrupt is asserted, it is subject to the corresponding PSTATE mask bit. If the value of the mask is 1, the interrupt is not taken. If the value of the mask is 0, the interrupt is taken.

- n/a This field does not exist, or the Exception level is not accessible in this configuration.

## Table G1-20 Masking of physical asynchronous exceptions

| Control bits   | Control bits   |            |     |             | Effect of the interrupt mask when executing at:   | Effect of the interrupt mask when executing at:   | Effect of the interrupt mask when executing at:   | Effect of the interrupt mask when executing at:   |
|----------------|----------------|------------|-----|-------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|
| NS             | FW AW          | FIQ IRQ EA | TGE | FMO IMO AMO | EL0                                               | EL1                                               | EL2                                               | EL3                                               |
| 0              | x              | x          | x   | x           | B                                                 | n/a                                               | n/a                                               | B                                                 |
| 1              | x              | 0          | 0   | 0           | B                                                 | B                                                 | B                                                 | B                                                 |
| 1              |                |            |     | 1           | A                                                 | A                                                 | B                                                 | B                                                 |
| 1              |                |            | 1   | x           | A                                                 | n/a                                               | B                                                 | B                                                 |
|                | 0              | 1          | 0   | x           | A                                                 | A                                                 | A                                                 | B                                                 |
|                |                |            | 1   | x           | A                                                 | n/a                                               | A                                                 | B                                                 |
|                | 1              | 1          | 0   | 0           | B                                                 | B                                                 | B                                                 | B                                                 |
|                |                |            |     | 1           | A                                                 | A                                                 | A                                                 | B                                                 |

| Control bits   | Control bits   | Control bits   | Control bits   | Control bits   | Effect of the interrupt mask when executing at:   | Effect of the interrupt mask when executing at:   | Effect of the interrupt mask when executing at:   | Effect of the interrupt mask when executing at:   |
|----------------|----------------|----------------|----------------|----------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|
| NS             | FW AW          | FIQ IRQ EA     | TGE            | FMO IMO AMO    | EL0                                               | EL1                                               | EL2                                               | EL3                                               |
|                |                |                | 1              | x              | A                                                 | n/a                                               | A                                                 | B                                                 |

## G1.16.5 Taking an interrupt or other exception during a multiple-register load or store

In AArch32 state, an interrupt cannot be taken during a sequence of memory accesses caused by a single load or store instruction, except that when FEAT\_LSMAOC is implemented and the value of the applicable LSMAOE field is 0, an interrupt can be taken between two memory accesses made by a single AArch32 Load Multiple ( LDM ) or Store Multiple ( STM ) instruction.

The applicable LSMAOE field is the field in the SCTLR\_EL1, SCTLR\_EL2, HSCTLR, or SCTLR register that applies to the Exception level and Security state at which the LDM or STM instruction is executed.

When the value of the LSMAOE bit is 0 and an interrupt is taken between two memory accesses made by a single AArch32 LDM or STM instruction, then:

- For a load, any register being loaded by the instruction other than a register used in the generation of the address by the instruction or the PC, can contain an UNKNOWN value. Any register used in the generation of the address is restored to its initial value and the LR is set on the interrupt to a value consistent with returning to the instruction.
- For a store, any data location being stored to by the instruction can contain an UNKNOWN value.
- For either a load or store, if the instruction specifies writeback of the base address, then that register is restored to its initial value.

Armv8.2 deprecates software relying on interrupts not being taken during the sequence of memory accesses caused by a single load or store instruction.