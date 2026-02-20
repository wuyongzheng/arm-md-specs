## D1.10 Interprocessing

| R FKKJY   | Moving between the AArch64 and AArch32 Execution states is called interprocessing .                                                                                                                                                                                                                   |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R NKBQL   | The Execution state can only change on a change of Exception level.                                                                                                                                                                                                                                   |
| I WNJBK   | Therefore, Execution state can change only on taking an exception to a higher Exception level or returning from an exception to a lower Exception level. For an exception that is taken to the same Exception level or is returning from the same Exception level, the Execution state cannot change. |
| R GLNVF   | When taking an exception to a higher Exception level, the Execution state is one of the following: • Unchanged. • Changed from AArch32 state to AArch64 state.                                                                                                                                        |
| R KTCXV   | When returning from an exception to a lower Exception level, the Execution state is one of the following: • Unchanged.                                                                                                                                                                                |

- Changed from AArch64 state to AArch32 state.

## D1.10.1 Register mappings between AArch32 state and AArch64 state

IXVDJR

Register mappings between AArch32 state and AArch64 state describe the following:

- For exceptions taken from AArch32 state to AArch64 state, where the AArch32 register content is found.

- For exception returns from AArch64 state to AArch32 state, how the AArch32 register content is derived.

RPCCLL

The AArch32 state register contents occupy the bottom 32 bits of the AArch64 state registers.

RCTBNQ

If in AArch32 state, the upper 32 bits of AArch64 state registers are inaccessible and are ignored.

RGMLYF

For bits[63:32] of AArch64 registers that are not mapped to AArch32 registers, the unmapped bits are unchanged by AArch32 state execution.

## D1.10.1.1 Mapping of the general-purpose registers between the Execution states

IPYKVS

The following table shows the mappings of general-purpose registers between Execution states:

| AArch32 register   | AArch64 register   |
|--------------------|--------------------|
| R0                 | X0                 |
| R1                 | X1                 |
| R2                 | X2                 |
| R3                 | X3                 |
| R4                 | X4                 |
| R5                 | X5                 |
| R6                 | X6                 |
| R7                 | X7                 |
| R8_usr             | X8                 |
| R9_usr             | X9                 |
| R10_usr            | X10                |
| R11_usr            | X11                |
| R12_usr            | X12                |

| AArch32 register   | AArch64 register   |
|--------------------|--------------------|
| SP_usr             | X13                |
| LR_usr             | X14                |
| SP_hyp             | X15                |
| LR_irq             | X16                |
| SP_irq             | X17                |
| LR_svc             | X18                |
| SP_svc             | X19                |
| LR_abt             | X20                |
| SP_abt             | X21                |
| LR_und             | X22                |
| SP_und             | X23                |
| R8_fiq             | X24                |
| R9_fiq             | X25                |
| R10_fiq            | X26                |
| R11_fiq            | X27                |
| R12_fiq            | X28                |
| SP_fiq             | X29                |
| LR_fiq             | X30                |

IJCWRB

For some exceptions, the exception syndrome given in the ESR\_ELx identifies one or more register numbers from the issued instruction that generated the exception. If one of these exceptions is taken from an Exception level using AArch32, the register numbers give the AArch64 view of the register.

IVSFBC

For example, if an exception is taken from AArch32 Abort mode and the faulting instruction specified R14, the ESR\_ELx.ISS field would report this using the EC value 0b10100 , because register X20 provides the AArch64 view of LR\_abt, which is the copy of R14 used in Abort mode.

## D1.10.1.2 Mapping of the SIMD and floating-point registers between the Execution states

IDPNRF

The following table shows the mappings of SIMD and floating-point registers between the Execution states:

| AArch32 register   | AArch64 register   |
|--------------------|--------------------|
| V0                 | Q0                 |
| V1                 | Q1                 |
| V2                 | Q2                 |
| .                  | .                  |
| .                  | .                  |
| .                  | .                  |
| V15                | Q15                |

RTJJVC

The AArch64 state registers V16-V31 are not accessible from AArch32 state.

IVTZXL

The mapping between the V, D, and S registers in AArch64 state is not the same as the mapping between the Q, D, and S registers in AArch32 state.

RVSTPQ

In AArch64 state, there are:

- 32 128-bit V registers, V0-V31.

- 32 64-bit D registers, D0-D31.

- 32 32-bit S registers, S0-S31.

RWJGSQ

Asmaller register occupies the least significant bytes of the corresponding larger register.

IFFHKC

The following graphic shows the mapping of V, D, and S registers in AArch64 state:

<!-- image -->

RDHVZF

In AArch32 state, there are:

- 16 128-bit Q registers, Q0-Q15.

- 32 64-bit D registers, D0-D31.

- 32 32-bit S registers, S0-S31.

RBPYPZ

Smaller registers are packed into larger registers.

IYHYWN

The following graphic shows the mapping of Q, D and S registers in AArch32 state:

<!-- image -->

RGXGJK

In AArch32 state:

- There are no S registers that correspond to Q8-Q15.

- D16-D31 pack into Q8-Q15.

IMKXYB

If software executing in AArch64 state interprets D or S registers from AArch32 state, the software must unpack the D or

S registers from the V registers before it uses them.

## D1.10.1.3 Mapping of the System registers between the Execution states

IMPMNZ

For a full list of mappings of writable AArch64 System registers to the AArch32 System registers, see Table K14-5.

RBQSMK

The relationship between the AArch64 System registers and the AArch32 System registers is architecturally defined.

RLPDQL

Modifications made to AArch32 System registers affect only the parts of the AArch64 state registers that are mapped to

the AArch32 System registers.

IHTCVH

Supervisory code, such as a hypervisor, executing in AArch64 state, can save, restore, and interpret the System registers belonging to a lower Exception level that is using AArch32.

ILYHXS

In some cases, two AArch32 System registers are packed into a single AArch64 System register.

| R QXNZN                 | If EL3 is implemented and is using AArch32, some System registers are banked between Secure and Non-secure states. In this type of banking, there is an instance of the register in Secure state and another instance of the register in Non-secure state.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R TVZJS                 | If any of the following are true, banking between Secure and Non-secure states is not supported: • EL3 is not implemented.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| I JRZXQ                 | If EL3 is implemented and is using AArch64, the same, non-banked, registers are accessed in the following state: • Secure EL1 with EL1 using AArch32.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| I HSRHJ                 | If EL3 is implemented and is using AArch64, it is not possible to architecturally determine whether an AArch64 register is mapped onto the Secure or the Non-secure instance of corresponding AArch32 register.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                         | that is asserted by the Non-secure AArch32 CNTP_* timer when EL3 is using AArch32. Although not required, Arm expects that implementations map many of the AArch64 registers for use by EL3 to the Secure instances of the banked AArch32 registers, and map many of the AArch64 registers for use by EL1 to the Non-secure instances of the banked AArch32 registers. However, if EL2 and EL3 are implemented and both support use                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| I JSZYM                 | of AArch32, this mapping is not possible for the following registers: • IFAR - This is because when EL3 is using AArch32, HIFAR is an alias of the Secure IFAR. • DFAR - This is because when EL3 is using AArch32, HDFARis an alias of the Secure DFAR. There are some AArch32 System registers that are only used in AArch32 state and do not have an equivalent AArch64 System register. However, there are AArch64 registers that can access, from a higher Exception level, the AArch32                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| I BYYWR                 | registers that do not have an AArch64 state equivalent.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| I VGXRBR                | For a full list of AArch64 registers that access AArch32 System registers with no AArch64 equivalent, see Table K14-6.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| I WRKYQ                 | For a full list AArch64 registers that allow access to the AArch32 ID registers from AArch64 state, see Table K14-7.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                         | D1.10.1.4 State of the general-purpose registers on taking an exception to AArch64 state                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| R WWJWP                 | When an exception is taken from AArch32 state to AArch64 state and the general- purpose register was accessible from AArch32 state, the upper 32 bits have one of the following IMPLEMENTATION DEFINED values and might vary dynamically within an implementation: • The upper 32 bits retain the value that the same architectural register held before any AArch32 execution. • The upper 32 bits are set to zero. The IMPLEMENTATION DEFINED behavior applies regardless of whether any execution occurred at the Exception level that was using AArch32.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| I TKQYW I QFBYM R RHRQX | For example, the IMPLEMENTATION DEFINED behavior described inR WWJWP applies even if AArch32 state was entered by an exception return from AArch64 state, and another exception was immediately taken to AArch64 state without any instruction execution in AArch32 state. When an exception is taken from AArch32 state to AArch64 state, software must regard the value of the upper 32 bits as a CONSTRAINED UNPREDICTABLE choice between the two values described inR WWJWP . D1.10.1.4.2 If the general-purpose register was not accessible from AArch32 state If all of the following apply, when an exception is taken from AArch32 state to AArch64 state, the X15 register is treated as if it is accessible and therefore the upper 32 bits of X15 might either be set to zero or retain their previous value: • The target Exception level is EL3. • EL2 is not implemented or EL1 is in Secure state. • SCR_EL3.RW is 0. Otherwise, when an exception is taken from AArch32 state to AArch64 state, for a general-purpose register that was not |

RZJBSH

RDGVGF

## D1.10.1.4.3 Determining the upper 32 bits of AArch64 registers on taking an exception from AArch32 state

Whether a general-purpose register has its upper 32 bits set to zero or retained on taking an exception from AArch32 to AArch64 is affected by all of the following:

- The AArch64 state target Exception level.
- The values of both:
- -SCR\_EL3.RW.
- -HCR\_EL2.RW or HCR.RW, where HCR.RW is a notional bit that is RES 0.

The following table shows which general-purpose registers can have their upper 32 bits set to zero on taking an exception from AArch32 state to AArch64 state. In this table, a dash (-) indicates that the RW values are not valid for the targeted Exception level.

| SCR_EL3.RW   | HCR_EL2.RW or HCR.RW   | Registers when the target Exception level is:                                          | Registers when the target Exception level is:                                          |                                                                                        |
|--------------|------------------------|----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| SCR_EL3.RW   | HCR_EL2.RW or HCR.RW   | EL3                                                                                    | EL2                                                                                    | EL1                                                                                    |
| 0            | 0                      | X0-X30                                                                                 | -                                                                                      | -                                                                                      |
| 0            | 1                      | Not valid because the RWbit values would imply that EL2 is AArch32 and EL1 is AArch64. | Not valid because the RWbit values would imply that EL2 is AArch32 and EL1 is AArch64. | Not valid because the RWbit values would imply that EL2 is AArch32 and EL1 is AArch64. |
| 1            | 0                      | X0-X14, X16-X30                                                                        | X0-X14, X16-X30                                                                        | -                                                                                      |
| 1            | 1                      | X0-X14                                                                                 | X0-X14                                                                                 | X0-X14                                                                                 |

RWKWVT

If EL2 is not implemented, or the SCR\_EL3.NS or SCR.NS bits prevent its use, the registers that can have their upper 32 bits set to zero on taking an exception from AArch32 state to AArch64 state are the same as when HCR\_EL2.RW has the same value as SCR\_EL3.RW.

RWPVQR

The following table shows which general-purpose registers can retain their upper 32 bits on taking an exception from AArch32 state to AArch64 state. In this table, a dash (-) indicates that the RW values are not valid for the target Exception level.

| SCR_EL3.RW   | HCR_EL2.RW or HCR.RW   | Registers when the target Exception level is:                                          | Registers when the target Exception level is:                                          |                                                                                        |
|--------------|------------------------|----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| SCR_EL3.RW   | HCR_EL2.RW or HCR.RW   | EL3                                                                                    | EL2                                                                                    | EL1                                                                                    |
| 0            | 0                      | None                                                                                   | -                                                                                      | -                                                                                      |
| 0            | 1                      | Not valid because the RWbit values would imply that EL2 is AArch32 and EL1 is AArch64. | Not valid because the RWbit values would imply that EL2 is AArch32 and EL1 is AArch64. | Not valid because the RWbit values would imply that EL2 is AArch32 and EL1 is AArch64. |
| 1            | 0                      | X15                                                                                    | X15                                                                                    | -                                                                                      |
| 1            | 1                      | X15-X30                                                                                | X15-X30                                                                                | X15-X30                                                                                |

RLGSLY

IPSRRS

If EL2 is not implemented, or SCR\_EL3.NS prevents its use, the registers that can have their upper 32 bits retained on taking an exception to AArch64 state from AArch32 state are the same as when HCR\_EL2.RW has the same value as SCR\_EL3.RW.

## D1.10.1.5 SPSR, ELR, and AArch64 SP relationships on changing Execution state

The following table shows SPSR and ELR registers that are architecturally mapped between AArch32 state and AArch64 state:

| AArch32 register   | AArch64 register   |
|--------------------|--------------------|
| SPSR_svc           | SPSR_EL1           |
| SPSR_hyp           | SPSR_EL2           |
| ELR_hyp            | ELR_EL2            |

## RCHHXX

RWFDMR

ITBFWN

IWRPZP

RMBVJZ

RSWQGH

RGXKNK

IMWQNV

IWYKRM

When an exception is taken from an Exception level using AArch32 to EL3 using AArch64 and EL2 has been using AArch32 state, the upper 32 bits of ELR\_EL2 have one of the following IMPLEMENTATION DEFINED values:

- The upper 32 bits retain the value that the same architectural register held before any AArch32 execution.
- The upper 32 bits are set to zero.

The following AArch32 registers are used only during execution in AArch32 state. However, they retain their state if there is execution at EL1 and EL1 is using AArch64 state.

- SPSR\_abt.
- SPSR\_und.
- SPSR\_irq.
- SPSR\_fiq.

For the purposes of context switching, the registers in RWFDMR are accessible during execution in AArch64 state at Exception levels higher than EL1.

If EL1 does not support execution in AArch32 state, the registers in RWFDMR are RES0.

If an exception is taken from an Exception level using AArch32 to an Exception level using AArch64, the AArch64 stack pointers and Exception Link Registers associated with an Exception level that are not accessible during AArch32 execution at the Exception level from which the exception was taken, retain the state that they had before AArch32 execution. This applies to the following registers:

- SP\_EL0.
- SP\_EL1.
- SP\_EL2.
- ELR\_EL1.

## D1.10.1.6 PSTATE.SM and PSTATE.ZA behaviors on changing Execution state

The values of PSTATE.{SM, ZA} do not change when any of the following occurs:

- An exception return from AArch64 to AArch32 Execution state.
- An exception taken from AArch32 to AArch64 Execution state.

In AArch32 state, the Effective value of PSTATE.SM is 0.

When PSTATE.SM is 1, a change in Execution state from AArch64 to AArch32, or from AArch32 to AArch64,causes all implemented bits of the SVE registers (including SIMD&amp;FP registers) and the FPSR to be reset to a fixed value.

The value of PSTATE.ZA does not change in AArch32 Execution state. Therefore, a transition between AArch64 and AArch32 Execution state when PSTATE.ZA is 1 has no effect on the contents of ZA storage, or the ZT0 register when FEAT\_SME2 is implemented.