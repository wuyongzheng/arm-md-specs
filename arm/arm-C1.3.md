## C1.3 Address generation

The A64 instruction set supports 64-bit virtual addresses (V As). The valid V A range is determined by the following factors:

- The size of the implemented virtual address space.
- Memory Management Unit (MMU) configuration settings.
- Memory Protection Unit (MPU) configuration settings.

Limits on the V A size mean that the most significant bits of the virtual address do not hold valid address bits. These unused bits can hold:

- Atag, see Address tagging.
- If FEAT\_PAuth is implemented, a Pointer authentication code (PAC), see Pointer authentication.

For more information on memory management and address translation, see The AArch64 Virtual Memory System Architecture.

## C1.3.1 Register indexed addressing

The A64 instruction set allows a 64-bit index register to be added to the 64-bit base register, with optional scaling of the index by the access size. Additionally it allows for sign-extension or zero-extension of a 32-bit value within an index register, followed by optional scaling.

## C1.3.2 PC-relative addressing

The A64 instruction set has support for position-independent code and data addressing:

- PC-relative literal loads have an offset range of ± 1MB.
- Process state flag and compare based conditional branches have a range of ± 1MB. Test bit conditional branches have a restricted range of ± 32KB.
- Unconditional branches, including branch and link, have a range of ± 128MB.

PC-relative load/store operations, and address generation with a range of ± 4GB can be performed using two instructions.

## C1.3.3 Load/store addressing modes

Load/store addressing modes in the A64 instruction set require a 64-bit base address from a general-purpose register X0-X30 or the current stack pointer, SP , with an optional immediate or register offset. Table C1-7 shows the assembler syntax for the complete set of load/store addressing modes.

Table C1-7 A64 Load/store addressing modes

| Addressing Mode                | Offset Immediate   | Register               | Extended Register                         |
|--------------------------------|--------------------|------------------------|-------------------------------------------|
| Base register only (no offset) | [base{, #0}]       | -                      | -                                         |
| Base plus offset               | [base{, #imm}]     | [base, Xm{, LSL #imm}] | [base, Wm, (S&#124;U)XT(X&#124;W) {#imm}] |
| Pre-indexed                    | [base, #imm]!      | -                      | -                                         |
| Post-indexed                   | [base], #imm       | [base], Xm a           | -                                         |
| Literal (PC-relative)          | label              | -                      | -                                         |

a. The post-indexed by register offset mode can be used with the SIMD load/store structure instructions described in Load/store Advanced SIMD. Otherwise the post-indexed by register offset mode is not available.

Some types of load/store instruction support only a subset of the load/store addressing modes listed in Table C1-7. Details of the supported modes are as follows:

- Base plus offset addressing means that the address is the value in the 64-bit base register plus an offset.
- Pre-indexed addressing means that the address is the sum of the value in the 64-bit base register and an offset, and the address is then written back to the base register.
- Post-indexed addressing means that the address is the value in the 64-bit base register, and the sum of the address and the offset is then written back to the base register.
- Literal addressing means that the address is the value of the 64-bit program counter for this instruction plus a 19-bit signed word offset. This means that it is a 4 byte aligned address within ±1MB of the address of this instruction with no offset. Literal addressing can be used only for loads of at least 32 bits and for prefetch instructions. The PC cannot be referenced using any other addressing modes. The syntax for labels is specific to individual toolchains.
- An immediate offset can be unsigned or signed, and scaled or unscaled, depending on the type of load/store instruction. When the immediate offset is scaled it is encoded as a multiple of the transfer size, although the assembly language always uses a byte offset, and the assembler or disassembler performs the necessary conversion. The usable byte offsets therefore depend on the type of load/store instruction and the transfer size. Table C1-8 shows the offset and the type of load/store instruction.
- Aregister offset means that the offset is the 64 bits from a general-purpose register, Xm, optionally scaled by the transfer size, in bytes, if LSL #imm is present and where imm must be equal to log2(transfer\_size). The SXTX extend/shift option is functionally equivalent to LSL , but the LSL option is preferred in source code.
- An extended register offset means that offset is the bottom 32 bits from a general-purpose register Wm, sign-extended or zero-extended to 64 bits, and then scaled by the transfer size if so indicated by #imm , where imm must be equal to log2(transfer\_size). An assembler must accept Wm or Xm as an extended register offset, but Wm is preferred for disassembly.
- Generating an address lower than the value in the base register requires a negative signed immediate offset or a register offset holding a negative value.
- When stack alignment checking is enabled by system software and the base register is the SP, the current stack pointer must be initially quadword aligned, that is aligned to 16 bytes. Misalignment generates a Stack Alignment fault. The offset does not have to be a multiple of 16 bytes unless the specific load/store instruction requires this. SP cannot be used as a register offset.

Table C1-8 Immediate offsets and the type of load/store instruction

|   Offset bits | Sign     | Scaling   | Write-Back   | Load/store type           |
|---------------|----------|-----------|--------------|---------------------------|
|             0 | -        | -         | -            | Exclusive/acquire/release |
|             7 | Signed   | Scaled    | Optional     | Register pair             |
|             9 | Signed   | Unscaled  | Optional     | Single register           |
|            12 | Unsigned | Scaled    | No           | Single register           |

## C1.3.3.1 Address calculation

General-purpose arithmetic instructions can calculate the result of most addressing modes and write the address to a general-purpose register or, in most cases, to the current stack pointer.

Table C1-9 shows the arithmetic instructions that can compute addressing modes.

Table C1-9 Arithmetic instructions to compute addressing modes

| Addressing Form           | Offset Immediate                                         | Register                             | Extended Register                                                      |
|---------------------------|----------------------------------------------------------|--------------------------------------|------------------------------------------------------------------------|
| Base register (no offset) | MOV Xd&#124;SP, base                                     | -                                    | -                                                                      |
| Base plus offset          | ADD Xd&#124;SP, base, #imm or SUB Xd&#124;SP, base, #imm | ADD <Xd&#124;SP>, base, Xm{,LSL#imm} | ADD <Xd&#124;SP>, base, Wm,(S&#124;U)XT(W&#124;H&#124;B&#124;X) {#imm} |
| Pre-indexed               | -                                                        | -                                    | -                                                                      |
| Post-indexed              | -                                                        | -                                    | -                                                                      |
| Literal (PC-relative)     | ADR Xd, label                                            | -                                    | -                                                                      |

## Note

- For the 64-bit base plus register offset form, the UXTX mnemonic is an alias for the LSL shift option, but LSL is preferred for disassembly. Similarly the SXTX extend/shift option is functionally equivalent to the LSL option, but the LSL option is preferred in source code.
- To calculate a base plus immediate offset the ADD instructions defined in Arithmetic (immediate) accept an unsigned 12-bit immediate offset, with an optional left shift by 12. This means that a single ADD instruction cannot support the full range of byte offsets available to a single register load/store with a scaled 12-bit immediate offset. For example, a quadword LDR effectively has a 16-bit byte offset. To calculate an address with a byte offset that requires more than 12 bits it is necessary to use two ADD instructions. The following example shows this:
- To calculate a base plus extended register offset, the ADD instructions defined in Arithmetic (extended register) provide a superset of the addressing mode that also supports sign-extension or zero-extension of a byte or halfword value with any shift amount between 0 and 4, for example:
- If the same extended register offset is used by more than one load/store instruction, then, depending on the implementation, it might be more efficient to calculate the extended and scaled intermediate result just once, and then reuse it as a simple register offset. The extend and scale calculation can be performed using the SBFIZ and UBFIZ bitfield instructions defined in Bitfield move, for example:

```
ADD Xd, base, #(imm & 0xFFF) ADD Xd, Xd, #(imm>>12),
```

```
LSL #12
```

```
ADD Xd, base, Wm, SXTW #3 // Xd = base + (SignExtend(Wm) LSL 3) ADD Xd, base, Wm, UXTH #4 // Xd = base + (ZeroExtend(Wm<15:0>)
```

```
LSL 4)
```

```
SBFIZ Xd, Xm, #3, #32 //Xd = "Wm, SXTW #3" UBFIZ Xd, Xm, #4, #16 //Xd = "Wm, UXTH #4"
```