## B1.2 Registers in AArch64 Execution state

The following registers are visible at EL0 using AArch64:

R0-R30 31 general-purpose registers, R0 to R30. Each can be accessed as:

- A64-bit general-purpose register named X0 to X30.
- A32-bit general-purpose register named W0 to W30.

Figure B1-1 General-purpose register naming

<!-- image -->

The X30 general-purpose register is used as the procedure call link register.

- SP A64-bit dedicated Stack Pointer register. The least significant 32 bits of the stack pointer can be accessed using the register name WSP.

The use of SP as an operand in an instruction, indicates the use of the current stack pointer.

Note

Stack pointer alignment to a 16-byte boundary is configurable at EL1. For more information, see the Procedure Call Standard for the Arm 64-bit Architecture .

- PC A64-bit Program Counter holding the address of the current instruction.

Software cannot write directly to the PC. It can be updated only on a branch, exception entry or exception return.

Note

Attempting to execute an A64 instruction that is not word-aligned generates a PC alignment fault, see PC alignment checking.

- V0-V31 32 SIMD&amp;FP registers, V0 to V31. Each can be accessed as:
- A128-bit register named Q0 to Q31.
- A64-bit register named D0 to D31.
- A32-bit register named S0 to S31.
- A16-bit register named H0 to H31.
- An 8-bit register named B0 to B31.
- A128-bit vector of elements. See Figure A1-1.
- A64-bit vector of elements. See Figure A1-1.

Where the number of bits described by a register name does not occupy an entire SIMD&amp;FP register, it refers to the least significant bits. See Figure B1-2.

For more information about data types and vector formats, see Supported data types.

Figure B1-2 SIMD and floating-point register naming

<!-- image -->

FPCR, FPSR The FPCR is the floating-point control register. The FPSR is the floating-point status register.

Z0-Z31 32 SVE scalable vector registers, Z0 to Z31, of equal length. Each register can be accessed as:

- Aconfigurable-length vector of elements. The length, VL, is a power of two, from a minimum of 128 bits to an IMPLEMENTATION DEFINED maximum no greater than 2048 bits. See Figure B1-3, Figure A1-5, and Configurable SVE vector lengths.
- ASIMD&amp;FPregister, as described in V0-V31. Bits[127:0] of each Zn register hold the correspondingly numbered V0-V31 SIMD&amp;FP register, as Figure B1-3 shows:

Figure B1-3 SVE scalable vector register naming

<!-- image -->

## See also:

- Maximum implemented SVE vector lengths.
- Configurable SVE vector lengths.
- Treatment of SVE scalable vector registers.
- SVE writes of scalar values to registers.

P0-P15 16 SVE predicate registers, named P0 to P15. Each SVE predicate register holds one bit for each byte of an SVE scalar vector register.

Note

The Maximum implemented SVE predicate length is the Maximum implemented SVE vector length divided by 8. See Maximum implemented SVE vector lengths.

Also see Vector predication.

FFR The dedicated SVE First Fault Register that has the same size and format as the SVE predicate registers, P0-P15. See FFR, First Fault Register.

ZA

Architectural state capable of holding a two-dimensional array of bytes. See ZA storage.

ZT0

See also:

A512-bit SME2 lookup table register. See SME2 ZT0 register.

- System registers.
- Pseudocode description of registers in AArch64 state.
- Registers for instruction processing and exception handling.

## B1.2.1 FFR, First Fault Register

| R TRLWH   | SVE has a dedicated First Fault Register named FFR.                                                                                                                                              |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I XPLQW   | The FFR captures the cumulative fault status of a sequence of SVE First-fault and Non-fault vector load instructions.                                                                            |
| R CPQQN   | The FFR and the predicate registers have the same size and format.                                                                                                                               |
| I PBWPM   | The FFR is a Special-purpose register.                                                                                                                                                           |
| R CGHCK   | All bits in the FFR that are accessible at the current Exception level are initialized to 1 by using the SETFFR instruction.                                                                     |
| R WZJVT   | Bits in the FFR are indirectly set to 0 as a result of a suppressed access or suppressed fault corresponding to an Active element of an SVE First-fault or Non-fault vector load.                |
| R BZLJG   | Bits in the FFR are never set to 1 as a result of a vector load instruction.                                                                                                                     |
| I XLZQY   | After a sequence of one or more SVE First-fault or Non-fault loads that follow a SETFFR instruction, without any intervening WRFFR instruction, the FFR contains a monotonic predicate value.    |
| D SRDGX   | Amonotonic predicate value is one that consists of, starting from predicate element 0, a sequence of zero or more TRUE elements, followed only by zero or more FALSE elements.                   |
| I TQMTV   | The TRUE elements in the FFR indicate the shortest sequence of consecutive elements that could contain valid data loaded from memory.                                                            |
| R GHFRQ   | The only instructions that directly read the FFR are: • RDFFR . • RDFFRS .                                                                                                                       |
| R LHBRN   | The only instructions that directly write the FFR are: • WRFFR . • SETFFR .                                                                                                                      |
| I DTHXN   | The WRFFR instruction requires that its source predicate contains a monotonic predicate value. If the source is not a monotonic predicate value, then the resulting value in the FFR is UNKNOWN. |
| R XXMMP   | All direct and indirect reads and writes to the FFR occur in program order relative to other instructions, without explicit synchronization.                                                     |

## B1.2.2 System registers

System registers provide support for execution control, status and general system configuration. The majority of the System registers are not accessible at EL0.

However, some System registers can be configured to allow access from software executing at EL0. Any access from EL0 to a System register without access permission causes the instruction to be trapped. The registers that can be accessed from EL0 are:

Debug registers ADebug Communications Channel is supported by the MDCCSR\_EL0, DBGDTR\_EL0, DBGDTRRX\_EL0, DBGDTRTX\_EL0, DLR\_EL0 and DSPSR\_EL0 registers.

General system control registers

- The CTR\_EL0 and DCZID\_EL0 registers provide implementation parameters for EL0 cache management support.
- The SCXTNUM\_EL0 register provides a number that can be used to separate out different context numbers.
- The POR\_EL0 Permission Overlay register determines the unprivileged stage 1 overlay permissions for the EL1&amp;0 and EL2&amp;0 translation regimes.
- The TPIDR\_EL0, TPIDR2\_EL0, and TPIDRRO\_EL0 registers provide locations where software can store thread identifying information.

## Generic timer registers

- Read access to the system counter effective frequency using CNTFRQ\_EL0.
- Physical and virtual timer count registers, CNTPCT\_EL0, CNTVCT\_EL0, CNTPCTSS\_EL0 and CNTVCTSS\_EL0.
- Physical up-count comparison, down-count value and timer control registers, CNTP\_CVAL\_EL0, CNTP\_TVAL\_EL0, and CNTP\_CTL\_EL0.
- Virtual up-count comparison, down-count value and timer control registers, CNTV\_CVAL\_EL0, CNTV\_TVAL\_EL0, and CNTV\_CTL\_EL0.

## Performance Monitors registers

The Performance Monitors Extension provides counters and configuration registers. Software executing at EL1 or a higher Exception level can configure some of these registers to be accessible at EL0.

For more details, see The Performance Monitors Extension.

## Activity Monitors registers

The Activity Monitors Extension provides counters and configuration registers. Software executing at EL1 or a higher Exception level can configure these registers to be accessible at EL0.

For more details, see The Activity Monitors Extension.

## B1.2.3 Pseudocode description of registers in AArch64 state

The AArch64 pseudocode uses getter and setter accessor functions to read and write register files that are visible at EL0:

- The setter or assignment accessor, for example ' X[num, width] = result ', is used for register writes.
- The getter or non-assignment accessor, ' operand = X[num, width] ', is used for register reads.
- The num parameter specifies the register number to be accessed within the named register file, and width specifies the bit width of the register access.
- For the general-purpose register X[] accessor, register number 31 accesses the zero register, ZR, which reads as zero and ignores writes.
- For other register accessors, such as the SIMD&amp;FP V[] accessors, there is no special interpretation of the register number.

Other special AArch64 accessors include:

- The SP[] accessors have no parameters and are used to read or write the currently selected 64-bit stack pointer at the current Exception level.
- The PC64[] accessor has no parameter list and is used to read the 64-bit Program Counter.
- The Vpart[] accessors are used to perform a partial read or write of an Advanced SIMD vector register, using an additional part parameter to select which half of the vector register to access.
- The Z[] , V[] , and Vpart[] accessors read and write the same underlying vector register file.

Other register accessors are defined as required by other architectural features. See A-profile Architecture Pseudocode, sections aarch64/functions/registers/.