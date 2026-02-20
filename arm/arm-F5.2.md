## F5.2 Encoding and use of banked register transfer instructions

Software executing at EL1 or higher can use the MRS (banked register) and MSR (banked register) instructions to transfer values between the general-purpose registers and Special-purpose registers. One particular use of these instructions is for a hypervisor to save or restore the register values of a Guest OS. The following sections give more information about these instructions:

- Register arguments in the banked register transfer instructions.
- Usage restrictions on the banked register transfer instructions.
- Encoding the register argument in the banked register transfer instructions.
- Pseudocode support for the banked register transfer instructions.

For descriptions of the instructions see MRS (Banked register)and MSR (Banked register).

## F5.2.1 Register arguments in the banked register transfer instructions

Figure F5-1shows the banked general-purpose registers and Special-purpose registers:

<!-- image -->

|                           | Associated PE mode   | Associated PE mode   | Associated PE mode   | Associated PE mode   | Associated PE mode   | Associated PE mode   | Associated PE mode   | Associated PE mode   |
|---------------------------|----------------------|----------------------|----------------------|----------------------|----------------------|----------------------|----------------------|----------------------|
| General-purpose registers | User or System       | Hyp                  | Supervisor           | Abort                | Undefined            | Monitor              | IRQ                  | FIQ                  |
| General-purpose registers | R8_usr               |                      |                      |                      |                      |                      |                      | R8_fiq               |
| General-purpose registers | R9_usr               |                      |                      |                      |                      |                      |                      | R9_fiq               |
| General-purpose registers | R10_usr              |                      |                      |                      |                      |                      |                      | R10_fiq              |
| General-purpose registers | R11_usr              |                      |                      |                      |                      |                      |                      | R11_fiq              |
| General-purpose registers | R12_usr              |                      |                      |                      |                      |                      |                      | R12_fiq              |
| General-purpose registers | SP_usr               | SP_hyp               | SP_svc               | SP_abt               | SP_und               | SP_mon               | SP_irq               | SP_fiq               |
| General-purpose registers | LR_usr               |                      | LR_svc               | LR_abt               | LR_und               | LR_mon               | LR_irq               | LR_fiq               |
| Special-purpose registers |                      | SPSR_hyp             | SPSR_svc             | SPSR_abt             | SPSR_und             | SPSR_mon             | SPSR_irq             | SPSR_fiq             |
| Special-purpose registers |                      | ELR_hyp              |                      |                      |                      |                      |                      |                      |

For the general-purpose registers, if no other register is shown, the current mode register is the \_usr register. So, for example, the full set of current mode registers, including the registers that are not banked:

-   For Hyp mode, is {R0\_usr - R12\_usr, SP\_hyp, LR\_usr, SPSR\_hyp, ELR\_hyp}.
-   For Abort mode, is {R0\_usr - R12\_usr, SP\_abt, LR\_abt, SPSR\_abt}.

Figure F5-1 Banking of general-purpose and Special-purpose registers

Figure F5-1is based on Figure G1-2, that shows the complete set of general-purpose registers and Special-purpose registers accessible in each mode.

Note

- System mode uses the same set of registers as User mode. Neither of these modes can access an SPSR, except that System mode can use the MRS (banked register) and MSR (banked register) instructions to access some SPSRs, as described in Usage restrictions on the banked register transfer instructions.
- General-purpose registers R0-R7, that are not banked, cannot be accessed using the MRS (banked register) and MSR (banked register) instructions.
- In addition to the registers shown in Figure F5-1, the DLRand DSPSRare AArch32 System registers that map onto the AArch64 Special-purpose registers DLR\_EL0and DSPSR\_EL0. However, DLRand DSPSRare not accessible using the MRS (banked register) and MSR (banked register) instructions.

Software using an MRS (banked register) or MSR (banked register) instruction specifies one of these registers using a name shown in Figure F5-1, or an alternative name for SP or LR. These registers can be grouped as follows:

R8-R12

Each of these registers has two banked copies, \_usr and \_fiq, for example R8\_usr and R8\_fiq.

SP

There is a banked copy of SP for every mode except System mode. For example, SP\_svc is the SP for Supervisor mode.

| LR      | There is a banked copy of LR for every mode except System mode and Hyp mode. For example, LR_svc is the LR for Supervisor mode.                   |
|---------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| SPSR    | There is a banked copy of SPSRfor every mode except System mode and User mode.                                                                    |
| ELR_hyp | Except for the operations provided by MRS (banked register) and MSR (banked register), ELR_hypis accessible only from Hyp mode. It is not banked. |

## F5.2.2 Usage restrictions on the banked register transfer instructions

MRS (banked register) and MSR (banked register) instructions are CONSTRAINED UNPREDICTABLE if any of the following applies:

- The instruction is executed in User mode.
- The instruction accesses a banked register that is not implemented, or that either:
- -Is not accessible from the current Privilege level and Security state.
- -Can be accessed from the current mode by using a different instruction.

MSR(banked register) and MRS (banked register)describes the permitted CONSTRAINED UNPREDICTABLE behavior.

An MRS (banked register) instruction or an MSR (banked register) instruction executed:

- At Non-secure EL1 cannot access any Hyp mode banked registers.
- At Non-secure EL1 or EL2 cannot access any Monitor mode banked registers.
- In a Secure mode other than Monitor mode cannot access any Hyp banked registers.

This means that the banked registers that MRS (banked register) and MSR (banked register) instructions cannot access are:

## From Monitor mode

- The current mode registers R8\_usr-R12\_usr, SP\_mon, LR\_mon, and SPSR\_mon.

## From Hyp mode

## From FIQ mode

- The Monitor mode registers SP\_mon, LR\_mon, and SPSR\_mon.
- The current mode registers R8\_usr-R12\_usr, SP\_hyp, LR\_usr, and SPSR\_hyp.

Note

MRS (banked register) and MSR (banked register) instructions can access the current mode register ELR\_hyp.

- From Non-secure EL1, the Monitor mode registers SP\_mon, LR\_mon, and SPSR\_mon.
- The Hyp mode registers SP\_hyp, SPSR\_hyp, and ELR\_hyp.
- The current mode registers R8\_fiq-R12\_fiq, SP\_fiq, LR\_fiq, and SPSR\_fiq.

## From System mode

- From Non-secure EL1, the Monitor mode registers SP\_mon, LR\_mon, and SPSR\_mon.
- The Hyp mode registers SP\_hyp, SPSR\_hyp, and ELR\_hyp.
- The current mode registers R8\_usr-R12\_usr, SP\_usr, and LR\_usr.

## From Supervisor mode, Abort mode, Undefined mode, and IRQ mode

- From Non-secure EL1, the Monitor mode registers SP\_mon, LR\_mon, and SPSR\_mon.
- The Hyp mode registers SP\_hyp, SPSR\_hyp, and ELR\_hyp.
- The current mode registers R8\_usr-R12\_usr, SP\_&lt;current\_mode&gt;, LR\_&lt;current\_mode&gt;, and SPSR\_&lt;current\_mode&gt;.

If EL3 is using AArch64, all MRS (banked register) and MSR (banked register) accesses to the Monitor mode registers from Secure EL1 modes are trapped to EL3.

For more information, see:

- Encoding the register argument in the banked register transfer instructions.
- Pseudocode support for the banked register transfer instructions.
- MRS(Banked register).
- MSR(Banked register).

Note

CONSTRAINED UNPREDICTABLE behavior must not give access to registers that are not accessible from the current Privilege level and Security state.

## F5.2.3 Encoding the register argument in the banked register transfer instructions

The MRS (banked register) and MSR (banked register) instructions include a 5-bit field, SYSm, and an R bit, that together encode the register argument for the instruction.

When the R bit is set to 0, the argument is a register other than a banked copy of the SPSR, and Table F5-116shows how the SYSm field defines the required register argument.

## Table F5-116 Banked register encodings when R==0

| SYSm<2:0>   | SYSm<4:3>                 |                           |        |                           |
|-------------|---------------------------|---------------------------|--------|---------------------------|
|             | 0b00                      | 0b01                      | 0b10   | 0b11                      |
| 0b000       | R8_usr                    | R8_fiq                    | LR_irq | CONSTRAINED UNPREDICTABLE |
| 0b001       | R9_usr                    | R9_fiq                    | SP_irq | CONSTRAINED UNPREDICTABLE |
| 0b010       | R10_usr                   | R10_fiq                   | LR_svc | CONSTRAINED UNPREDICTABLE |
| 0b011       | R11_usr                   | R11_fiq                   | SP_svc | CONSTRAINED UNPREDICTABLE |
| 0b100       | R12_usr                   | R12_fiq                   | LR_abt | LR_mon                    |
| 0b101       | SP_usr                    | SP_fiq                    | SP_abt | SP_mon                    |
| 0b110       | LR_usr                    | LR_fiq                    | LR_und | ELR_hyp                   |
| 0b111       | CONSTRAINED UNPREDICTABLE | CONSTRAINED UNPREDICTABLE | SP_und | SP_hyp                    |

When the R bit is set to 1, the argument is a banked copy of the SPSR, and Table F5-117shows how the SYSm field defines the required register argument.

## Table F5-117 Banked register encodings when R==1

| SYSm<2:0>   | SYSm<4:3>                 | 0b01                      | 0b10     | 0b11                      |
|-------------|---------------------------|---------------------------|----------|---------------------------|
| 0b000       | CONSTRAINED UNPREDICTABLE | CONSTRAINED UNPREDICTABLE | SPSR_irq | CONSTRAINED UNPREDICTABLE |

| SYSm<2:0>   | SYSm<4:3>                 |                           |                           | 0b11                      |
|-------------|---------------------------|---------------------------|---------------------------|---------------------------|
| 0b001       | CONSTRAINED UNPREDICTABLE | CONSTRAINED UNPREDICTABLE | CONSTRAINED UNPREDICTABLE | CONSTRAINED UNPREDICTABLE |
| 0b010       | CONSTRAINED UNPREDICTABLE | CONSTRAINED UNPREDICTABLE | SPSR_svc                  | CONSTRAINED UNPREDICTABLE |
| 0b011       | CONSTRAINED UNPREDICTABLE | CONSTRAINED UNPREDICTABLE | CONSTRAINED UNPREDICTABLE | CONSTRAINED UNPREDICTABLE |
| 0b100       | CONSTRAINED UNPREDICTABLE | CONSTRAINED UNPREDICTABLE | SPSR_abt                  | SPSR_mon                  |
| 0b101       | CONSTRAINED UNPREDICTABLE | CONSTRAINED UNPREDICTABLE | CONSTRAINED UNPREDICTABLE | CONSTRAINED UNPREDICTABLE |
| 0b110       | CONSTRAINED UNPREDICTABLE | SPSR_fiq                  | SPSR_und                  | SPSR_hyp                  |
| 0b111       | CONSTRAINED UNPREDICTABLE | CONSTRAINED UNPREDICTABLE | CONSTRAINED UNPREDICTABLE | CONSTRAINED UNPREDICTABLE |

## F5.2.4 Pseudocode support for the banked register transfer instructions

The pseudocode functions BankedRegisterAccessValid() and SPSRaccessValid() check the validity of MRS (banked register) and MSR (banked register) accesses. That is, they filter the accesses that are CONSTRAINED UNPREDICTABLE either because:

- They attempt to access a register that Usage restrictions on the banked register transfer instructions shows is not accessible.
- They use an SYSm&lt;4:0&gt; encoding that Encoding the register argument in the banked register transfer instructions shows as CONSTRAINED UNPREDICTABLE.

BankedRegisterAccessValid() applies to accesses to the banked general-purpose registers, or to ELR\_hyp, and SPSRaccessValid() applies to accesses to the SPSRs.

## Chapter F6 T32 and A32 Advanced SIMD and Floating-point

## Instruction Descriptions

This chapter describes each instruction. It contains the following sections:

- Alphabetical list of Advanced SIMD and floating-point instructions.

Note

Some headings in this chapter use the term floating-point register . This is an abbreviated description, and means a register in the Advanced SIMD and floating-point register file.