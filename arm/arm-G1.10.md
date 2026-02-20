## G1.10 AArch32 general-purpose registers, the PC, and the Special-purpose registers

The general-purpose registers, and the PC, in AArch32 state describes the application level view of the general-purpose registers, and the PC. This view provides:

- The general-purpose registers R0-R14, of which:
- -The preferred name for R13 is SP ( stack pointer ).
- -The preferred name for R14 is LR ( link register ).
- The PC, which can be described as R15.

These registers are selected from a larger set of registers that includes banked copies of some registers, with the current register selected by the execution mode. The implementation and banking of the general-purpose registers depends on whether or not the implementation includes EL2 and EL3, and whether those Exception levels are using AArch32. Figure G1-3 shows the full set of banked general-purpose registers, and the Special-purpose registers:

- The Program Status Registers CPSR and SPSR.
- ELR\_hyp.

Note

The architecture uses system level register names, such as R0\_usr, R8\_usr, and R8\_fiq, when it must identify a specific register. The application level names refer to the registers for the current mode, and usually are sufficient to identify a register.

| Application level view   | System level view   | System level view   | System level view   | System level view   | System level view   | System level view   | System level view   | System level view   | System level view   |
|--------------------------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|
|                          | User                | System              | Hyp †               | Supervisor          | Abort               | Undefined           | Monitor ‡           | IRQ                 | FIQ                 |
| R0                       | R0_usr              |                     |                     |                     |                     |                     |                     |                     |                     |
| R1                       | R1_usr              |                     |                     |                     |                     |                     |                     |                     |                     |
| R2                       | R2_usr              |                     |                     |                     |                     |                     |                     |                     |                     |
| R3                       | R3_usr              |                     |                     |                     |                     |                     |                     |                     |                     |
| R4                       | R4_usr              |                     |                     |                     |                     |                     |                     |                     |                     |
| R5                       | R5_usr              |                     |                     |                     |                     |                     |                     |                     |                     |
| R6                       | R6_usr              |                     |                     |                     |                     |                     |                     |                     |                     |
| R7                       | R7_usr              |                     |                     |                     |                     |                     |                     |                     |                     |
| R8                       | R8_usr              |                     |                     |                     |                     |                     |                     |                     | R8_fiq              |
| R9                       | R9_usr              |                     |                     |                     |                     |                     |                     |                     | R9_fiq              |
| R10                      | R10_usr             |                     |                     |                     |                     |                     |                     |                     | R10_fiq             |
| R11                      | R11_usr             |                     |                     |                     |                     |                     |                     |                     | R11_fiq             |
| R12                      | R12_usr             |                     |                     |                     |                     |                     |                     |                     | R12_fiq             |
| SP                       | SP_usr              |                     | SP_hyp              | SP_svc              | SP_abt              | SP_und              | SP_mon              | SP_irq              | SP_fiq              |
| LR                       | LR_usr              |                     |                     | LR_svc              | LR_abt              | LR_und              | LR_mon              | LR_irq              | LR_fiq              |
| PC                       | PC                  |                     |                     |                     |                     |                     |                     |                     |                     |
| APSR                     | CPSR                |                     |                     |                     |                     |                     |                     |                     |                     |
|                          |                     |                     | SPSR_hyp            | SPSR_svc            | SPSR_abt            | SPSR_und            | SPSR_mon            | SPSR_irq            | SPSR_fiq            |

ELR\_hyp

‡ Part of EL3. Exists only in Secure state, and only when EL3 is using AArch32.

† Part of EL2. Exists only in Non-secure state, and only when EL2 is using AArch32.

Cells with no entry indicate that the User mode register is used.

Figure G1-3 AArch32 general-purpose registers, PC, and Special-purpose registers, showing banking

As described in PE mode for taking exceptions, on taking an exception the PE changes mode, unless it is already in the mode to which it must take the exception. Each mode that the PE might enter in this way has:

- Abanked copy of the stack pointer, for example SP\_irq and SP\_hyp.
- Aregister that holds a preferred return address for the exception. This is:

- -For the EL2 mode, Hyp mode, the Special-purpose register ELR\_hyp.
- -For the other privileged modes to which exceptions can be taken, a banked copy of the link register, for example LR\_und and LR\_mon.
- Asaved copy of PSTATE, made on exception entry, for example SPSR\_irq and SPSR\_hyp.

In addition, FIQ mode has banked copies of the general-purpose registers R8 to R12.

User mode and System mode share the same general-purpose registers.

User mode, System mode, and Hyp mode share the same LR.

For more information about the application level view of the SP, LR, and PC, and the alternative descriptions of them as R13, R14 and R15, see The general-purpose registers, and the PC, in AArch32 state.

In AArch32 state, the Special-purpose registers are:

- The CPSR and its view as the APSR.
- The SPSR, including the banked copies SPSR\_abt, SPSR\_fiq, SPSR\_hyp, SPSR\_irq, SPSR\_mon, SPSR\_svc, and SPSR\_und.
- The ELR\_hyp.

## G1.10.1 Pseudocode description of general-purpose register and PC operations

The following pseudocode gives access to the general-purpose registers and the PC. These registers are an array, \_R , indexed by parameter n . This array is common to AArch32 and AArch64 operation and therefore contains 31 64-bit registers. \_PC is the Program Counter, and its definition is common to AArch32 and AArch64 operation and therefore its size is 64-bit.

LookUpRIndex() looks up the index value, n , for the specified register number and PE mode, using RBankSelect() to evaluates the result.

\_R accesses the specified general-purpose register in the current PE mode, using Rmode[] to access the register, accessing \_R if necessary. SP accesses the stack pointer, LR accesses the link register, and PC32 accesses the Program Counter. Each function has a non-assignment form for register reads and an assignment form for register writes, other than PC32 , which has only a non-assignment form.

BranchTo() performs a branch to the specified address.

The \_R \_PC , LR , PC32 , SP , LookUpRIndex() , RBankSelect() , Rmode[] , and BranchTo() functions are defined in A-profile Architecture Pseudocode.

## G1.10.2 Saved Program Status Registers (SPSRs)

The Saved Program Status Registers (SPSRs) are used to save PE state on taking exceptions. In AArch32 state, there is an SPSR for every mode that an exception can be taken to, as shown in Figure G1-3. For example, the SPSR for Monitor mode is called SPSR\_mon.

Note

Exceptions cannot be taken to EL0.

When the PE takes an exception, PE state is saved from PSTATE in the SPSR for the mode the exception is taken to. For example, if the PE takes an exception to Monitor mode, PE state is saved in SPSR\_mon. For more information on PSTATE, see Process state, PSTATE.

Note

All PSTATE fields are saved, including those which have no direct read and write access.

Saving the PSTATE fields means the exception handler can:

- On return from the exception, restore the PE state to the values it had immediately before the exception was taken. When the PE returns from an exception, PE state is restored to the state stored in the SPSR of the mode the exception is returning from, if the exception return is made using one of:

- -ERET.
- -LDM .
- -The Exception return form of the instruction described in MOV , MOVS (register).
- -The Exception return form of the instruction described in SUB, SUBS (immediate).

For example, on returning from Monitor mode, PE state is restored to the state stored in SPSR\_mon. If the exception return is made using the RFE instruction, the PE restores the PE state from an SPSR valued read from memory.

- Examine the value that PSTATE had when the exception was taken, for example to determine the instruction set state and privilege level in which the instruction that caused an Undefined Instruction exception was executed.

The SPSRs are UNKNOWN on a Warm reset. Any operation in a Non-secure EL1 or EL0 mode makes SPSR\_hyp unknown.

SPSR bits that are defined as RES0 on an exception taken from AArch32 state are ignored on any exception return to AArch32 state.

For more information on SPSR, see SPSR.

## G1.10.2.1 Pseudocode description of SPSR operations

The following pseudocode gives access to the SPSRs.

The SPSR\_ELx [] function accesses the current SPSR and is common to AArch32 and AArch64 operation.

The SPSRWriteByInstr() function is used by the MSR (register) and MSR (immediate) instructions to update the current SPSR.

The SPSR\_ELx [] and SPSRWriteByInstr() functions are defined in A-profile Architecture Pseudocode.

## G1.10.3 ELR\_hyp

Hyp mode does not provide its own banked copy of LR. Instead, on taking an exception to Hyp mode, the preferred return address is stored in ELR\_hyp, a 32-bit Special-purpose register implemented for this purpose.

ELR\_hyp can be accessed explicitly only by executing:

- An MRS or MSR instruction that targets ELR\_hyp, see:
- -MRS(Banked register).
- -MSR(Banked register).

The ERET instruction uses the value in ELR\_hyp as the return address for the exception. For more information, see ERET.

Software execution in any Non-secure EL1 or EL0 mode makes ELR\_hyp UNKNOWN.