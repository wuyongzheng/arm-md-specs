## C3.2 Loads and stores

This section describes the load/store instructions. It contains the following subsections:

- Load/store register.
- Load/store register (unscaled offset).
- Load/store pair.
- Load/store pair unprivileged.
- Load/store non-temporal pair.
- Load/store non-temporal pair unprivileged.
- Load/store unprivileged.
- Load-Exclusive/Store-Exclusive.
- Load-Exclusive/Store-Exclusive unprivileged.
- Load-Acquire/Store-Release.
- Load-Acquire/Store-Release unprivileged.
- LoadLOAcquire/StoreLORelease.
- Load/store scalar SIMD and floating-point.
- Load/store Advanced SIMD.
- Prefetch memory.
- Atomic instructions.
- Memory Tagging instructions.
- Memory Copy and Memory Set instructions.

The requirements for the alignment of data memory accesses are strict. For more information, see Alignment of data accesses.

The additional control bits SCTLR\_ELx.SA and SCTLR\_EL1.SA0 control whether the stack pointer must be quadword aligned when used as a base register. See SP alignment checking. Using a misaligned stack pointer generates an SP alignment fault exception.

Note

In some cases, load/store instructions can lead to CONSTRAINED UNPREDICTABLE behavior. See AArch64 CONSTRAINED UNPREDICTABLE behaviors.

## C3.2.1 Load/store register

The load/store register instructions support the following addressing modes:

- Base plus a scaled 12-bit unsigned immediate offset or base plus an unscaled 9-bit signed immediate offset.
- Base plus a 64-bit register offset, optionally scaled.
- Base plus a 32-bit extended register offset, optionally scaled.
- Pre-indexed by an unscaled 9-bit signed immediate offset.
- Post-indexed by an unscaled 9-bit signed immediate offset.
- PC-relative literal for loads of 32 bits or more.

See also Load/store addressing modes.

If a Load instruction specifies writeback and the register being loaded is also the base register, then behavior is CONSTRAINED UNPREDICTABLE and one of the following behaviors must occur:

- The instruction is treated as UNDEFINED.
- The instruction is treated as a NOP .

- The instruction performs the load using the specified addressing mode and the base register becomes UNKNOWN. In addition, if an exception occurs during the execution of such an instruction, the base address might be corrupted so that the instruction cannot be repeated.

If a Store instruction performs a writeback and the register that is stored is also the base register, then behavior is CONSTRAINED UNPREDICTABLE and one of the following behaviors must occur:

- The instruction is treated as UNDEFINED.
- The instruction is treated as a NOP .
- The instruction performs the store to the designated register using the specified addressing mode, but the value stored is UNKNOWN.

Table C3-21 shows the load/store register instructions.

Table C3-21 Load/store register instructions

| Mnemonic   | Instruction                             | See               |
|------------|-----------------------------------------|-------------------|
| LDR        | Load register (register offset)         | LDR(register)     |
| LDR        | Load register (immediate offset)        | LDR(immediate)    |
| LDR        | Load register (PC-relative literal)     | LDR(literal)      |
| LDRB       | Load byte (register offset)             | LDRB(register)    |
| LDRB       | Load byte (immediate offset)            | LDRB(immediate)   |
| LDRSB      | Load signed byte (register offset)      | LDRSB (register)  |
| LDRSB      | Load signed byte (immediate offset)     | LDRSB (immediate) |
| LDRH       | Load halfword (register offset)         | LDRH(register)    |
| LDRH       | Load halfword (immediate offset)        | LDRH(immediate)   |
| LDRSH      | Load signed halfword (register offset)  | LDRSH (register)  |
| LDRSH      | Load signed halfword (immediate offset) | LDRSH (immediate) |
| LDRSW      | Load signed word (register offset)      | LDRSW(register)   |
| LDRSW      | Load signed word (immediate offset)     | LDRSW(immediate)  |
| LDRSW      | Load signed word (PC-relative literal)  | LDRSW(literal)    |
| STR        | Store register (register offset)        | STR (register)    |
| STR        | Store register (immediate offset)       | STR (immediate)   |
| STRB       | Store byte (register offset)            | STRB (register)   |
| STRB       | Store byte (immediate offset)           | STRB (immediate)  |
| STRH       | Store halfword (register offset)        | STRH (register)   |
| STRH       | Store halfword (immediate offset)       | STRH (immediate)  |

## C3.2.2 Load/store register (unscaled offset)

The load/store register instructions with an unscaled offset support only one addressing mode:

- Base plus an unscaled 9-bit signed immediate offset.

See Load/store addressing modes.

The load/store register (unscaled offset) instructions are required to disambiguate this instruction class from the load/store register instruction forms that support an addressing mode of base plus a scaled, unsigned 12-bit immediate offset, because that can represent some offset values in the same range.

The ambiguous immediate offsets are byte offsets that are both:

- In the range 0-255, inclusive.
- Naturally aligned to the access size.

Other byte offsets in the range -256 to 255 inclusive are unambiguous. An assembler program translating a load/store instruction, for example LDR , is required to encode an unambiguous offset using the unscaled 9-bit offset form, and to encode an ambiguous offset using the scaled 12-bit offset form. A programmer might force the generation of the unscaled 9-bit form by using one of the mnemonics in Table C3-22. Arm recommends that a disassembler outputs all unscaled 9-bit offset forms using one of these mnemonics, but unambiguous offsets can be output using a load/store single register mnemonic, for example, LDR .

Table C3-22 shows the load/store register instructions with an unscaled offset.

Table C3-22 Load/store register (unscaled offset) instructions

| Mnemonic   | Instruction                            | See    |
|------------|----------------------------------------|--------|
| LDUR       | Load register (unscaled offset)        | LDUR   |
| LDURB      | Load byte (unscaled offset)            | LDURB  |
| LDURSB     | Load signed byte (unscaled offset)     | LDURSB |
| LDURH      | Load halfword (unscaled offset)        | LDURH  |
| LDURSH     | Load signed halfword (unscaled offset) | LDURSH |
| LDURSW     | Load signed word (unscaled offset)     | LDURSW |
| STUR       | Store register (unscaled offset)       | STUR   |
| STURB      | Store byte (unscaled offset)           | STURB  |
| STURH      | Store halfword (unscaled offset)       | STURH  |

## C3.2.3 Load/store pair

The load/store pair instructions support the following addressing modes:

- Base plus a scaled 7-bit signed immediate offset.
- Pre-indexed by a scaled 7-bit signed immediate offset.
- Post-indexed by a scaled 7-bit signed immediate offset.

See also Load/store addressing modes.

If a Load Pair instruction specifies the same register for the two registers that are being loaded, then behavior is CONSTRAINED UNPREDICTABLE and one of the following behaviors must occur:

- The instruction is treated as UNDEFINED.
- The instruction is treated as a NOP .
- The instruction performs all the loads using the specified addressing mode and the register that is loaded takes an UNKNOWN value.

If a Load Pair instruction specifies writeback and one of the registers being loaded is also the base register, then behavior is CONSTRAINED UNPREDICTABLE and one of the following behaviors must occur:

- The instruction is treated as UNDEFINED.
- The instruction is treated as a NOP .
- The instruction performs all of the loads using the specified addressing mode, and the base register becomes UNKNOWN. In addition, if an exception occurs during the instruction, the base address might be corrupted so that the instruction cannot be repeated.

If a Store Pair instruction performs a writeback and one of the registers being stored is also the base register, then behavior is CONSTRAINED UNPREDICTABLE and one of the following behaviors must occur:

- The instruction is treated as UNDEFINED.
- The instruction is treated as a NOP .
- The instruction performs all the stores of the registers indicated by the specified addressing mode, but the value stored for the base register is UNKNOWN.

Table C3-23 shows the load/store pair instructions.

## Table C3-23 Load/store pair instructions

| Mnemonic   | Instruction            | See   |
|------------|------------------------|-------|
| LDP        | Load Pair              | LDP   |
| LDPSW      | Load Pair signed words | LDPSW |
| STP        | Store Pair             | STP   |

## C3.2.4 Load/store pair unprivileged

The Load unprivileged pair and Store unprivileged pair instructions are added as part of the FEAT\_LSUI architecture feature. These instructions belong to the class of unprivileged memory access instructions. The privileges of the Explicit Memory Effects generated by these instructions are controlled by PSTATE.UAO. For more information, see PSTATE.UAO.

The load/store unprivileged pair instructions support the following address modes:

- Base plus a scaled 7-bit signed immediate offset.
- Pre-indexed by a scaled 7-bit signed immediate offset.
- Post-indexed by a scaled 7-bit signed immediate offset.

See Load/store addressing modes.

## Table C3-24 Load/store unprivileged pair instructions

| Mnemonic   | Instruction             | See   |
|------------|-------------------------|-------|
| LDTP       | Load unprivileged Pair  | LDTP  |
| STTP       | Store unprivileged Pair | STTP  |

## C3.2.5 Load/store non-temporal pair

The load/store non-temporal pair instructions support only one addressing mode:

- Base plus a scaled 7-bit signed immediate offset.

See Load/store addressing modes.

The load/store non-temporal pair instructions provide a hint to the memory system that an access is non-temporal or streaming, and unlikely to be repeated in the near future. This means that data caching is not required. However, depending on the memory type, the instructions might permit memory reads to be prefetched and memory writes to be gathered to accelerate bulk memory transfers.

In addition, there is an exception to the usual memory ordering rules. If an address dependency exists between two memory reads, and a Load Non-temporal Pair instruction generated the second read, then in the absence of any other barrier mechanism to achieve order, the memory accesses can be observed in any order by the other observers within the shareability domain of the memory addresses being accessed.

If a Load Non-Temporal Pair instruction specifies the same register for the two registers that are being loaded, then behavior is CONSTRAINED UNPREDICTABLE and one of the following must occur:

- The instruction is treated as UNDEFINED.
- The instruction is treated as a NOP .
- The instruction performs all the loads using the specified addressing mode and the register that is loaded takes an UNKNOWN value.

Table C3-25 shows the load/store non-temporal pair instructions.

## Table C3-25 Load/store non-temporal pair instructions

| Mnemonic   | Instruction             | See   |
|------------|-------------------------|-------|
| LDNP       | Load Non-temporal Pair  | LDNP  |
| STNP       | Store Non-temporal Pair | STNP  |

## C3.2.6 Load/store non-temporal pair unprivileged

The load/store non-temporal pair unprivileged instructions are added as part of the FEAT\_LSUI architecture feature. These intructions belong to the class of unprivileged memory access instructions. The privileges of the Explicit Memory Effects generated by these instructions are controlled by PSTATE.UAO. For more information, see PSTATE.UAO.

The load/store non-temporal pair instructions support only one addressing mode:

- Base plus a scaled 7-bit signed immediate offset.

## Table C3-26 Load/store non-temporal pair instructions

| Mnemonic   | Instruction             | See   |
|------------|-------------------------|-------|
| LDTNP      | Load Non-temporal Pair  | LDTNP |
| STTNP      | Store Non-temporal Pair | STTNP |

## C3.2.7 Load/store unprivileged

The load/store unprivileged instructions support only one addressing mode:

- Base plus an unscaled 9-bit signed immediate offset.

See Load/store addressing modes.

The access permissions that apply to accesses made at EL0 apply to the memory accesses made by a load/store unprivileged instruction that is executed either:

- At EL1 when the Effective value of PSTATE.UAO is 0.
- At EL2 when both the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1} and the Effective value of PSTATE.UAO is 0.

Otherwise, memory accesses made by a load/store unprivileged instruction are subject to the access permissions that apply to the Exception level at which the instruction is executed. These are the permissions that apply to the corresponding load/store register instruction, see Load/store register.

Note

This means that when the value of PSTATE.UAO is 1 the access permissions for a load/store unprivileged instruction are always the same as those for the corresponding load/store register instruction.

Table C3-27 shows the load/store unprivileged instructions.

## Table C3-27 Load-Store unprivileged instructions

| Mnemonic   | Instruction                       | See    |
|------------|-----------------------------------|--------|
| LDTR       | Load unprivileged register        | LDTR   |
| LDTRB      | Load unprivileged byte            | LDTRB  |
| LDTRSB     | Load unprivileged signed byte     | LDTRSB |
| LDTRH      | Load unprivileged halfword        | LDTRH  |
| LDTRSH     | Load unprivileged signed halfword | LDTRSH |
| LDTRSW     | Load unprivileged signed word     | LDTRSW |
| STTR       | Store unprivileged register       | STTR   |
| STTRB      | Store unprivileged byte           | STTRB  |
| STTRH      | Store unprivileged halfword       | STTRH  |

## C3.2.8 Single-copy atomic 64-byte load/store

If FEAT\_LS64 is implemented, the following instructions are implemented:

- LD64B.
- ST64B.

If FEAT\_LS64\_V is implemented, the following instructions are implemented:

- LD64B.
- ST64B.
- ST64BV.

If FEAT\_LS64\_ACCDATA is implemented, the following instructions are implemented:

- LD64B.
- ST64B.
- ST64BV.
- ST64BV0.

LD64B and ST64B can only target Device or Normal Non-cacheable memory unless FEAT\_LS64WB is implemented.

The single-copy atomic 64-byte load/store instructions support one addressing mode:

- Base register only.

See also Load/store addressing modes.

The memory location accessed by the instructions is required to be aligned on a 64-byte boundary, otherwise an Alignment fault occurs.

If an ST64BV, ST64BV0, or if FEAT\_LS64WB is not implemented an LD64B or ST64B, attempts to access a memory type that is not one of the following, then a Data Abort with DFSC code 0b110101 is generated:

- Normal Inner Non-cacheable, Outer Non-cacheable.
- Device-GRE.
- Device-nGRE.
- Device-nGnRE.
- Device-nGnRnE.

It is IMPLEMENTATION DEFINED which of the following approaches is used to provide this check:

- The check is performed at each enabled stage of translation, and the fault is reported for the first stage of translation that provides an inappropriate memory type. In this case, the value of the HCR\_EL2.DC bit does not cause accesses generated by the instructions to generate a stage 1 Data abort,
- The check is performed against the resulting memory type after all enabled stages of translation. In this case the fault is reported at the final enabled stage of translation.
- The check is performed against the resulting memory type after all enabled stages of translation. In this case the fault is reported for the first stage of translation that provided an inappropriate memory type. The value of the HCR\_EL2.DC bit does not cause accesses generated by the instructions to generate a stage 1 Data abort.

If FEAT\_LS64WB is implemented, then LD64B and ST64B are also supported and 64-byte single-copy atomic for Conventional memory that is Inner and Outer Write-Back Cacheable, Shareable. In this case, if an LD64B or ST64B attempts to access:

- Amemory region that is Inner and Outer Write-Back Cacheable, Shareable, but the target memory location is not in Conventional memory, then it is IMPLEMENTATION DEFINED whether:
- -Astage 1 Data Abort with DFSC code 0b110101 is generated.
- -The access succeeds but is not guaranteed to be single-copy atomic above the byte level.
- Acacheable type of memory other than Inner and Outer Write-Back Cacheable, Shareable, then it is IMPLEMENTATION DEFINED whether:
- -Astage 1 Data Abort with DFSC code 0b110101 is generated.
- -The access succeeds as a 64-byte single-copy atomic operation.

For behavior when FEAT\_LS64WB is implemented and an LD64B or ST64B targets Tagged memory that is Inner and Outer Write-Back Cacheable, Shareable, see Tag Check Faults.

If the target memory location does not support the LD64B or ST64B instructions, then one of the following behaviors occurs:

- Astage 1 Data Abort with DFSC code of 0b110101 , is generated.

- The instruction performs the memory accesses, but the accesses are not single-copy atomic above the byte level.

If the target memory location does not support the ST64BV or ST64BV0 instructions, then the register specified by &lt;Xs&gt; is set to 0xFFFF\_FFFF\_FFFF\_FFFF .

Regardless of the memory type:

- The memory access generated by an ST64BV or ST64BV0 instruction is not merged with any accesses.
- The memory access generated by an ST64B instruction is not merged with any accesses generated by store instructions appearing in program order after the instruction.

Table C3-28 shows the single-copy atomic 64-byte load/store instructions.

## Table C3-28 Single-copy atomic 64-byte load/store instructions

| Mnemonic   | Instruction                                            | See   |
|------------|--------------------------------------------------------|-------|
| LD64B      | Single-copy atomic 64-byte load                        | LD64B |
| ST64B      | Single-copy atomic 64-byte store without status result | ST64B |

Table C3-29 shows the single-copy atomic 64-byte store with status result.

## Table C3-29 Single-copy atomic 64-byte store with status result instructions

| Mnemonic   | Instruction                                         | See    |
|------------|-----------------------------------------------------|--------|
| ST64BV     | Single-copy atomic 64-byte store with status result | ST64BV |

Table C3-30 shows the single-copy atomic 64-byte EL0 store with status result.

## Table C3-30 Single-copy atomic 64-byte EL0 store with status result instructions

| Mnemonic   | Instruction                                             | See     |
|------------|---------------------------------------------------------|---------|
| ST64BV0    | Single-copy atomic 64-byte EL0 store with status result | ST64BV0 |

## C3.2.9 Load-Exclusive/Store-Exclusive

The Load-Exclusive/Store-Exclusive instructions support only one addressing mode:

- Base register with no offset.

See Load/store addressing modes.

The Load-Exclusive instructions mark the physical address being accessed as an exclusive access. This exclusive access mark is checked by the Store-Exclusive instruction, permitting the construction of atomic read-modify-write operations on shared memory variables, semaphores, mutexes, and spinlocks. See Synchronization and semaphores.

If FEAT\_LSE2 is not implemented then:.

- The Load-Exclusive/Store-Exclusive instructions other than Load-Exclusive pair and Store-Exclusive pair require natural alignment, and an unaligned address generates an Alignment fault.
- Memory accesses generated by Load-Exclusive pair or Store-Exclusive pair instructions must be aligned to the size of the pair, otherwise the access generates an Alignment fault. For more information on alignment requirements and behaviors, see Load-Exclusive/ Store-Exclusive and Atomic instructions.

When a Store-Exclusive pair succeeds, it causes a single-copy atomic update of the entire memory location being stored to.

Table C3-31 shows the Load-Exclusive/Store-Exclusive instructions.

## Table C3-31 Load-Exclusive/Store-Exclusive instructions

| Mnemonic   | Instruction              | See   |
|------------|--------------------------|-------|
| LDXR       | Load Exclusive register  | LDXR  |
| LDXRB      | Load Exclusive byte      | LDXRB |
| LDXRH      | Load Exclusive halfword  | LDXRH |
| LDXP       | Load Exclusive pair      | LDXP  |
| STXR       | Store Exclusive register | STXR  |
| STXRB      | Store Exclusive byte     | STXRB |
| STXRH      | Store Exclusive halfword | STXRH |
| STXP       | Store Exclusive pair     | STXP  |

## C3.2.10 Load-Exclusive/Store-Exclusive unprivileged

The Load-Exclusive unprivileged and Store-Exclusive unprivileged instructions are added as part of the FEAT\_LSUI architecture feature. These instructions belong to the class of unprivileged memory access instructions. The privileges of the Explicit Memory Effects generated by these instructions are controlled by PSTATE.UAO. For more information, see PSTATE.UAO.

The load-exclusive/store-exclusive unprivileged instructions support only one address mode:

- Base register with no offset.

See Load/store addressing modes.

Table C3-32 Load-exclusive/Store-exclusive unprivileged instructions

| Mnemonic   | Instruction                           | See   |
|------------|---------------------------------------|-------|
| LDTXR      | Load unprivileged exclusive register  | LDTXR |
| STTXR      | Store unprivileged exclusive register | STTXR |

## C3.2.11 Load-Acquire/Store-Release

The Load-Acquire, Load-AcquirePC and Store-Release instructions are added as part of the FEAT\_LRCPC, FEAT\_LRCPC2, and FEAT\_LRCPC3 architecture features.

If FEAT\_LSE2 is not implemented, then:

- The Load-Acquire, Load-AcquirePC, and Store-Release instructions other than Load-Acquire pair and Store-Release pair require natural alignment, and an unaligned address generates an Alignment fault.
- Memory accesses generated by Load-Acquire pair or Store-Release pair instructions must be aligned to the size of the accessed element in the pair, otherwise the access generates an Alignment fault.

For more information on alignment requirements and behaviors, see Non-atomic Load-Acquire/Store-Release instructions.

The Load-Acquire, Load-AcquirePC, and Store-Release instructions can remove the requirement to use the explicit DMBmemory barrier instruction. For more information about the ordering of Load-Acquire, Load-AcquirePC, and Store-Release, see Load-Acquire, Load-AcquirePC, and Store-Release.

AStore-Release Exclusive instruction has the Release semantics only if the store is successful.

Armv8.1 adds more instructions with load-acquire and store-release mechanisms, see LoadLOAcquire/StoreLORelease.

Table C3-33 shows the Non-exclusive Load-Acquire/Store-Release instructions.

Table C3-33 Non-exclusive Load-Acquire and Store-Release instructions

| Mnemonic   | Instruction                                                  | See      |
|------------|--------------------------------------------------------------|----------|
| LDAPR      | Load-Acquire RCpc Register                                   | LDAPR    |
| LDAPRB     | Load-Acquire RCpc Register Byte                              | LDAPRB   |
| LDAPRH     | Load-Acquire RCpc Register Halfword                          | LDAPRH   |
| LDAPUR     | Load-Acquire RCpc Register (unscaled)                        | LDAPUR   |
| LDAPURB    | Load-Acquire RCpc Register Byte (unscaled)                   | LDAPURB  |
| LDAPURH    | Load-Acquire RCpc Register Halfword (unscaled)               | LDAPURH  |
| LDAPURSB   | Load-Acquire RCpc Register Signed Byte (unscaled) 32-bit     | LDAPURSB |
| LDAPURSB   | Load-Acquire RCpc Register Signed Byte (unscaled) 64-bit     | LDAPURSB |
| LDAPURSH   | Load-Acquire RCpc Register Signed Halfword (unscaled) 32-bit | LDAPURSH |
| LDAPURSH   | Load-Acquire RCpc Register Signed Halfword (unscaled) 64-bit | LDAPURSH |
| LDAPURSW   | Load-Acquire RCpc Register Signed Word (unscaled)            | LDAPURSW |
| LDAR       | Load-Acquire Register                                        | LDAR     |
| LDARB      | Load-Acquire Byte                                            | LDARB    |
| LDARH      | Load-Acquire Halfword                                        | LDARH    |
| STLR       | Store-Release Register                                       | STLR     |
| STLRB      | Store-Release Byte                                           | STLRB    |
| STLRH      | Store-Release Halfword                                       | STLRH    |
| STLUR      | Store-Release Register (unscaled)                            | STLUR    |
| STLURB     | Store-Release Register Byte (unscaled)                       | STLURB   |
| STLURH     | Store-Release Register Halfword (unscaled)                   | STLURH   |

Table C3-34 shows the Exclusive Load-Acquire/Store-Release instructions.

## Table C3-34 Exclusive Load-Acquire and Store-Release instructions

| Mnemonic   | Instruction                      | See    |
|------------|----------------------------------|--------|
| LDAXR      | Load-Acquire Exclusive register  | LDAXR  |
| LDAXRB     | Load-Acquire Exclusive byte      | LDAXRB |
| LDAXRH     | Load-Acquire Exclusive halfword  | LDAXRH |
| LDAXP      | Load-Acquire Exclusive pair      | LDAXP  |
| STLXR      | Store-Release Exclusive register | STLXR  |
| STLXRB     | Store-Release Exclusive byte     | STLXRB |
| STLXRH     | Store-Release Exclusive halfword | STLXRH |
| STLXP      | Store-Release Exclusive pair     | STLXP  |

Table C3-35 Register Pair Ordered Load-AcquirePC and Store-Release instructions

| Mnemonic   | Instruction                                 | See    |
|------------|---------------------------------------------|--------|
| LDIAPP     | Load-Acquire RCpc Ordered Pair of Registers | LDIAPP |
| STILP      | Store-Release Pair Ordered                  | STILP  |

## C3.2.12 Load-Acquire/Store-Release unprivileged

The Load-Acquire unprivileged and Store-Release unprivileged instructions are added as part of the FEAT\_LSUI architecture feature. These instructions belong to the class of unprivileged memory access instructions. The privileges of the Explicit Memory Effects generated by these instructions are controlled by PSTATE.UAO. For more information, see PSTATE.UAO.

The load-acquire/store-release unprivileged instructions support only one addressing mode:

- Base register with no offset.

See Load/store addressing modes.

Table C3-36 Load-Acquire/Store-Release unprivileged instructions

| Mnemonic   | Instruction                                   | See    |
|------------|-----------------------------------------------|--------|
| LDATXR     | Load-acquire unprivileged exclusive register  | LDATXR |
| STLTXR     | Store-release unprivileged exclusive register | STLTXR |

## C3.2.13 LoadLOAcquire/StoreLORelease

The LoadLOAcquire/StoreLORelease instructions support only one addressing mode:

- Base register with no offset.

See Load/store addressing modes.

The LoadLOAcquire/StoreLORelease instructions can remove the requirement to use the explicit DMB memory barrier instruction. For more information about the ordering of LoadLOAcquire/StoreLORelease, see LoadLOAcquire, StoreLORelease.

If FEAT\_LSE2 is not implemented, then the LoadLOAcquire/StoreLORelease instructions require natural alignment, and an unaligned address generates an Alignment fault.

Table C3-37 shows the LoadLOAcquire/StoreLORelease instructions.

## Table C3-37 LoadLOAcquire and StoreLORelease instructions

| Mnemonic   | Instruction             | See    |
|------------|-------------------------|--------|
| LDLARB     | LoadLOAcquire byte      | LDLARB |
| LDLARH     | LoadLOAcquire halfword  | LDLARH |
| LDLAR      | LoadLOAcquire register  | LDLAR  |
| STLLRB     | StoreLORelease byte     | STLLRB |
| STLLRH     | StoreLORelease halfword | STLLRH |
| STLLR      | StoreLORelease register | STLLR  |

## C3.2.14 Load/store scalar SIMD and floating-point

The load/store scalar SIMD and floating-point instructions operate on scalar values in the SIMD and floating-point register file as described in Advanced SIMD and floating-point scalar register names. The memory addressing modes available, described in Load/store addressing modes, are identical to the general-purpose register load/store instructions, and like those instructions permit arbitrary address alignment unless strict alignment checking is enabled. However, unlike the load/store instructions that transfer general-purpose registers, load/store scalar SIMD and floating-point instructions make no guarantee of atomicity, even when the address is naturally aligned to the size of the data.

## C3.2.14.1 Load/store scalar SIMD and floating-point register

The load/store scalar SIMD and floating-point register instructions support the following addressing modes:

- Base plus a scaled 12-bit unsigned immediate offset or base plus unscaled 9-bit signed immediate offset.
- Base plus 64-bit register offset, optionally scaled.
- Base plus 32-bit extended register offset, optionally scaled.
- Pre-indexed by an unscaled 9-bit signed immediate offset.
- Post-indexed by an unscaled 9-bit signed immediate offset.
- PC-relative literal for loads of 32 bits or more.

For more information on the addressing modes, see Load/store addressing modes.

Note

The unscaled 9-bit signed immediate offset address mode requires its own instruction form, see Load/store scalar SIMD and floating-point register (unscaled offset).

Table C3-38 shows the load/store instructions for a single SIMD and floating-point register.

## Table C3-38 Load/store single SIMD and floating-point register instructions

| Mnemonic   | Instruction                                        | See                      |
|------------|----------------------------------------------------|--------------------------|
| LDR        | Load scalar SIMD&FP register (register offset)     | LDR(register, SIMD&FP)   |
|            | Load scalar SIMD&FP register (immediate offset)    | LDR(immediate, SIMD&FP)  |
|            | Load scalar SIMD&FP register (PC-relative literal) | LDR(literal, SIMD&FP)    |
| STR        | Store scalar SIMD&FP register (register offset)    | STR (register, SIMD&FP)  |
|            | Store scalar SIMD&FP register (immediate offset)   | STR (immediate, SIMD&FP) |

## C3.2.14.2 Load/store scalar SIMD and floating-point register (unscaled offset)

The load /store scalar SIMD and floating-point register instructions support only one addressing mode:

- Base plus an unscaled 9-bit signed immediate offset.

See also Load/store addressing modes.

The load/store scalar SIMD and floating-point register (unscaled offset) instructions are required to disambiguate this instruction class from the load/store single SIMD and floating-point instruction forms that support an addressing mode of base plus a scaled, unsigned 12-bit immediate offset. This is similar to the load/store register (unscaled offset) instructions, that disambiguate this instruction class from the load/store register instruction, see Load/store register (unscaled offset).

Table C3-39 shows the load/store SIMD and floating-point register instructions with an unscaled offset.

## Table C3-39 Load/store SIMD and floating-point register instructions

| Mnemonic   | Instruction                                     | See            |
|------------|-------------------------------------------------|----------------|
| LDUR       | Load scalar SIMD&FP register (unscaled offset)  | LDUR(SIMD&FP)  |
| STUR       | Store scalar SIMD&FP register (unscaled offset) | STUR (SIMD&FP) |

## C3.2.14.3 Load/store SIMD and floating-point register pair

The load/store SIMD and floating-point register pair instructions support the following addressing modes:

- Base plus a scaled 7-bit signed immediate offset.
- Pre-indexed by a scaled 7-bit signed immediate offset.
- Post-indexed by a scaled 7-bit signed immediate offset.

See also Load/store addressing modes.

If a Load pair instruction specifies the same register for the two registers that are being loaded, then behavior is CONSTRAINED UNPREDICTABLE and one of the following behaviors must occur:

- The instruction is treated as UNDEFINED.
- The instruction is treated as a NOP.
- The instruction performs all of the loads using the specified addressing mode and the register being loaded takes an UNKNOWN value.

For behavior when FEAT\_LS64WB is implemented, see Requirements for single-copy atomicity.

Table C3-40 shows the load/store SIMD and floating-point register pair instructions.

## Table C3-40 Load/store SIMD and floating-point register pair instructions

| Mnemonic   | Instruction                            | See           |
|------------|----------------------------------------|---------------|
| LDP        | Load pair of scalar SIMD&FP registers  | LDP (SIMD&FP) |
| STP        | Store pair of scalar SIMD&FP registers | STP (SIMD&FP) |

## C3.2.14.4 Load/store unprivileged SIMD and floating-point register pair

The load/store unprivileged SIMD and floating-point register pair instructions are added as part of the FEAT\_LSUI architecture feature. These intructions belong to the class of unprivileged memory access instructions. The privileges of the Explicit Memory Effects generated by these instructions are controlled by PSTATE.UAO. For more information, see PSTATE.UAO.

The load/store unprivileged SIMD and floating-point register pair instructions support the following addressing modes:

- Base plus a scaled 7-bit signed immediate offset.
- Pre-indexed by a scaled 7-bit signed immediate offset.
- Post-indexed by a scaled 7-bit signed immediate offset.

See also Load/store addressing modes.

## Table C3-41 Load/store unprivileged SIMD and floating-point register pair instructions

| Mnemonic   | Instruction                                         | See            |
|------------|-----------------------------------------------------|----------------|
| LDTP       | Load unprivileged pair of scalar SIMD&FP registers  | LDTP (SIMD&FP) |
| STTP       | Store unprivileged pair of scalar SIMD&FP registers | STTP (SIMD&FP) |

## C3.2.14.5 Load/store SIMD and floating-point non-temporal pair

The load/store SIMD and floating-point non-temporal pair instructions support only one addressing mode:

- Base plus a scaled 7-bit signed immediate offset.

See also Load/store addressing modes.

The load/store non-temporal pair instructions provide a hint to the memory system that an access is non-temporal or streaming, and unlikely to be repeated in the near future. This means that data caching is not required. However, depending on the memory type, the instructions might permit memory reads to be prefetched and memory writes to be gathered to accelerate bulk memory transfers.

In addition, there is an exception to the usual memory ordering rules. If an address dependency exists between two memory reads, and a load non-temporal pair instruction generated the second read, then in the absence of any other barrier mechanism to achieve order, those memory accesses can be observed in any order by the other observers within the shareability domain of the memory addresses being accessed.

If a load non-temporal pair instruction specifies the same register for the two registers that are being loaded, then behavior is CONSTRAINED UNPREDICTABLE and one of the following behaviors must occur:

- The instruction is treated as UNDEFINED.
- The instruction is treated as a NOP.
- The instruction performs all the loads using the specified addressing mode and the register that is loaded takes an UNKNOWN value.

Table C3-42 shows the load/store SIMD and floating-point Non-temporal pair instructions.

## Table C3-42 Load/store SIMD and floating-point non-temporal pair instructions

| Mnemonic   | Instruction                            | See            |
|------------|----------------------------------------|----------------|
| LDNP       | Load pair of scalar SIMD&FP registers  | LDNP (SIMD&FP) |
| STNP       | Store pair of scalar SIMD&FP registers | STNP (SIMD&FP) |

## C3.2.14.6 Load/store unprivileged SIMD and floating-point non-temporal pair

The load/store unprivileged SIMD and floating-point non-temporal pair instructions are added as part of the FEAT\_LSUI architecture feature. These intructions belong to the class of unprivileged memory access instructions. The privileges of the Explicit Memory Effects generated by these instructions are controlled by PSTATE.UAO. For more information, see PSTATE.UAO.

The load/store SIMD and floating-point non-temporal pair instructions support only one addressing mode:

- Base plus a scaled 7-bit signed immediate offset.

## Table C3-43 Load/store unprivileged SIMD and floating-point non-temporal pair instructions

| Mnemonic   | Instruction                          | See             |
|------------|--------------------------------------|-----------------|
| LDTNP      | Load Unprivileged Non-temporal Pair  | LDTNP (SIMD&FP) |
| STTNP      | Store Unprivileged Non-temporal Pair | STTNP (SIMD&FP) |

## C3.2.15 Load/store Advanced SIMD

The Advanced SIMD load/store structure instructions support the following addressing modes:

- Base register only.
- Post-indexed by a 64-bit register.
- Post-indexed by an immediate, equal to the number of bytes transferred.

Load/store vector instructions, like other load/store instructions, allow any address alignment, unless strict alignment checking is enabled. If strict alignment checking is enabled, then alignment checking to the size of the element is performed. However, unlike the load/store instructions that transfer general-purpose registers, the load/store vector instructions do not guarantee atomicity, even when the address is naturally aligned to the size of the element.

## C3.2.15.1 Load/store structures

Table C3-44 shows the load/store structure instructions. A post-increment immediate offset, if present, must be 8, 16, 24, 32, 48, or 64, depending on the number of elements transferred.

## Table C3-44 Load/store multiple structures instructions

| Mnemonic   | Instruction                                                                                              | See                       |
|------------|----------------------------------------------------------------------------------------------------------|---------------------------|
| LD1        | Load single 1-element structure to one lane of one register                                              | LD1 (single structure)    |
| LD1        | Load multiple 1-element structures to one register or to two, three, or four consecutive registers       | LD1 (multiple structures) |
| LD2        | Load single 2-element structure to one lane of two consecutive registers                                 | LD2 (single structure)    |
| LD2        | Load multiple 2-element structures to two consecutive registers                                          | LD2 (multiple structures) |
| LD3        | Load single 3-element structure to one lane of three consecutive registers                               | LD3 (single structure)    |
| LD3        | Load multiple 3-element structures to three consecutive registers                                        | LD3 (multiple structures) |
| LD4        | Load single 4-element structure to one lane of four consecutive registers                                | LD4 (single structure)    |
| LD4        | Load multiple 4-element structures to four consecutive registers                                         | LD4 (multiple structures) |
| ST1        | Store single 1-element structure from one lane of one register                                           | ST1 (single structure)    |
| ST1        | Store multiple 1-element structures from one register, or from two, three, or four consecutive registers | ST1 (multiple structures) |
| ST2        | Store single 2-element structure from one lane of two consecutive registers                              | ST2 (single structure)    |
| ST2        | Store multiple 2-element structures from two consecutive registers                                       | ST2 (multiple structures) |
| ST3        | Store single 3-element structure from one lane of three consecutive registers                            | ST3 (single structure)    |
| ST3        | Store multiple 3-element structures from three consecutive registers                                     | ST3 (multiple structures) |
| ST4        | Store single 4-element structure from one lane of four consecutive registers                             | ST4 (single structure)    |
| ST4        | Store multiple 4-element structures from four consecutive registers                                      | ST4 (multiple structures) |

## C3.2.15.2 Load single structure and replicate

Table C3-45 shows the Load single structure and replicate instructions. A post-increment immediate offset, if present, must be 1, 2, 3, 4, 6, 8, 12, 16, 24, or 32, depending on the number of elements transferred.

## Table C3-45 Load single structure and replicate instructions

| Mnemonic   | Instruction                                                                   | See   |
|------------|-------------------------------------------------------------------------------|-------|
| LD1R       | Load single 1-element structure and replicate to all lanes of one register    | LD1R  |
| LD2R       | Load single 2-element structure and replicate to all lanes of two registers   | LD2R  |
| LD3R       | Load single 3-element structure and replicate to all lanes of three registers | LD3R  |
| LD4R       | Load single 4-element structure and replicate to all lanes of four registers  | LD4R  |

## Table C3-46 SIMD and floating-point Non-exclusive Load-AcquirePC and Store-Release instructions

| Mnemonic         | Instruction                                                                | See             |
|------------------|----------------------------------------------------------------------------|-----------------|
| LDAP1 (SIMD&FP)  | Load-Acquire RCpc one single-element structure to one lane of one register | LDAP1 (SIMD&FP) |
| LDAPUR (SIMD&FP) | Load-Acquire RCpc SIMD&FP Register (unscaled offset)                       | LDAPUR(SIMD&FP) |
| STL1 (SIMD&FP)   | Store-Release a single-element structure from one lane of one register     | STL1 (SIMD&FP)  |
| STLUR (SIMD&FP)  | Store-Release SIMD&FP Register (unscaled offset)                           | STLUR (SIMD&FP) |

## C3.2.16 Prefetch memory

The Prefetch memory instructions support the following addressing modes:

- Base register with no offset.
- Base plus a scaled 12-bit unsigned immediate offset or base plus an unscaled 9-bit signed immediate offset.
- Base plus a 64-bit register offset. This can be optionally scaled by 8-bits, for example LSL #3.
- Base plus a 32-bit extended register offset. This can be optionally scaled by 8-bits.
- PC-relative literal.

The Prefetch memory instructions signal to the memory system that memory accesses from a specified address or range of addresses are likely to occur in the near future. The memory system can respond by taking actions that are expected to speed up the memory access when they do occur, such as prefetching the specified address or range of addresses into one or more caches. Because these signals are only hints, it is valid for the PE to treat any or all prefetch instructions as a NOP .

Because they are hints to the memory system, the operation of a prefetch memory instruction cannot cause a synchronous exception. However, a memory operation performed as a result of one of these memory system hints might in exceptional cases trigger an asynchronous event, and thereby influence the execution of the PE. An example of an asynchronous event that might be triggered is an SError exception.

Aprefetch memory instruction can only have an effect on software visible structures as defined in the translation regime of the current Exception level, such as caches and translation lookaside buffers associated with memory locations that can be accessed by reads, writes, or execution.

A PRFM , PRFUM , or RPRFM instruction is guaranteed not to access Device memory.

A PRFM or PRFUM instruction using a PLI hint cannot result in any access that could not be performed by the PE speculatively fetching an instruction. Therefore, if all associated MMUs are disabled, a PLI hint can only access memory locations consistent with instruction fetches permitted by The effects of disabling an address translation stage.

Arm recommends that when a PRFM or a PRFUM instruction describes a particular cache level, then the memory location described at that cache level should be made available at that same cache level, even if the line had previously been at a level of the cache that is closer to the PE than the specified cache level.

Note

For a PRFM PST instruction, this might result in the demotion of a cache line from a level that was closer to the cache.

Table C3-47 shows the Prefetch memory instructions.

Table C3-47 Prefetch memory instructions

| Mnemonic   | Instruction                          | See             |
|------------|--------------------------------------|-----------------|
| PRFM       | Prefetch memory (register offset)    | PRFM(register)  |
| PRFM       | Prefetch memory (immediate offset)   | PRFM(immediate) |
| PRFM       | Prefetch memory (PC-relative offset) | PRFM(literal)   |
| PRFUM      | Prefetch memory (unscaled offset)    | PRFUM           |
| RPRFM      | Range prefetch memory                | RPRFM           |

## C3.2.17 Atomic instructions

The atomic instructions perform atomic read and write operations on a memory location such that the architecture guarantees that no modification of that memory location by another observer can occur between the read and the write defined by that instruction.

This section describes the following operations:

- Atomic integer memory operations.
- Atomic floating-point memory operations.
- Unprivileged atomic memory operations.
- Swap operations.
- Swap unprivileged.
- Compare and Swap operations.
- Compare and Swap unprivileged.
- Read-Check-Write.

The atomic instructions support only one addressing mode:

- Base register only.

See also Load/store addressing modes.

For the purpose of permission checking, and for watchpoints, all of the Atomic memory operation instructions are treated as performing both a load and a store.

The instructions are provided with ordering options, which map to the acquire and release definitions used in the architecture. The atomic instructions with release semantics have the same rules as Store-Release instructions regarding multi-copy atomicity. These operations map to the acquire and release definitions, and are counted as Load-Acquire and Store-Release operations respectively.

## C3.2.17.1 Atomic integer memory operations

The address accessed by the 128-bit atomic instructions must be aligned to 128-bits, otherwise the instructions generate an Alignment fault.

For the LD&lt;OP&gt; instructions, where the source and destination registers are the same, if the instruction generates a synchronous Data Abort, then the source register is restored to the value it held before the instruction was executed.

The ST&lt;OP&gt; instructions, and LD&lt;OP&gt; instructions where the destination register is WZR or XZR, are not regarded as doing a read for the purpose of a DMB LD barrier.

For information on alignment requirements and behaviors, see Load-Exclusive/ Store-Exclusive and Atomic instructions.

## Table C3-48 Atomic integer memory operation instructions

| Mnemonic   | Instruction                         | See                                    |
|------------|-------------------------------------|----------------------------------------|
| LDADD      | Atomic add                          | LDADD,LDADDA,LDADDAL,LDADDL            |
| LDADDB     | Atomic add on byte                  | LDADDB,LDADDAB,LDADDALB,LDADDLB        |
| LDADDH     | Atomic add on halfword              | LDADDH,LDADDAH,LDADDALH,LDADDLH        |
| LDCLR      | Atomic bit clear                    | LDCLR, LDCLRA, LDCLRAL, LDCLRL         |
| LDCLRB     | Atomic bit clear on byte            | LDCLRB, LDCLRAB, LDCLRALB, LDCLRLB     |
| LDCLRH     | Atomic bit clear on halfword        | LDCLRH, LDCLRAH, LDCLRALH, LDCLRLH     |
| LDCLRP     | Atomic bit clear on quadword        | LDCLRP, LDCLRPA, LDCLRPAL, LDCLRPL     |
| LDEOR      | Atomic exclusive-OR                 | LDEOR, LDEORA, LDEORAL, LDEORL         |
| LDEORB     | Atomic exclusive-OR on byte         | LDEORB, LDEORAB, LDEORALB, LDEORLB     |
| LDEORH     | Atomic exclusive-OR on halfword     | LDEORH, LDEORAH, LDEORALH,LDEORLH      |
| LDSET      | Atomic bit set                      | LDSET, LDSETA, LDSETAL, LDSETL         |
| LDSETB     | Atomic bit set on byte              | LDSETB, LDSETAB, LDSETALB, LDSETLB     |
| LDSETH     | Atomic bit set on halfword          | LDSETH, LDSETAH, LDSETALH, LDSETLH     |
| LDSETP     | Atomic bit set on quadword          | LDSETP, LDSETPA, LDSETPAL, LDSETPL     |
| LDMAX      | Atomic signed maximum               | LDSMAX,LDSMAXA,LDSMAXAL,LDSMAXL        |
| LDMAXB     | Atomic signed maximum on byte       | LDSMAXB, LDSMAXAB, LDSMAXALB, LDSMAXLB |
| LDMAXH     | Atomic signed maximum on halfword   | LDSMAXH, LDSMAXAH, LDSMAXALH, LDSMAXLH |
| LDMIN      | Atomic signed minimum               | LDSMIN, LDSMINA, LDSMINAL, LDSMINL     |
| LDMINB     | Atomic signed minimum on byte       | LDSMINB, LDSMINAB, LDSMINALB, LDSMINLB |
| LDMINH     | Atomic signed minimum on halfword   | LDSMINH, LDSMINAH, LDSMINALH, LDSMINLH |
| LDUMAX     | Atomic unsigned maximum             | LDUMAX,LDUMAXA,LDUMAXAL,LDUMAXL        |
| LDUMAXB    | Atomic unsigned maximum on byte     | LDUMAXB,LDUMAXAB,LDUMAXALB, LDUMAXLB   |
| LDUMAXH    | Atomic unsigned maximum on halfword | LDUMAXH,LDUMAXAH,LDUMAXALH, LDUMAXLH   |
| LDUMIN     | Atomic unsigned minimum             | LDUMIN, LDUMINA, LDUMINAL, LDUMINL     |
| LDUMINB    | Atomic unsigned minimum on byte     | LDUMINB, LDUMINAB, LDUMINALB, LDUMINLB |
| LDUMINH    | Atomic unsigned minimum on halfword | LDUMINH, LDUMINAH, LDUMINALH,LDUMINLH  |

| Mnemonic   | Instruction                                         | See               |
|------------|-----------------------------------------------------|-------------------|
| STADD      | Atomic add, without return                          | STADD, STADDL     |
| STADDB     | Atomic add on byte, without return                  | STADDB, STADDLB   |
| STADDH     | Atomic add on halfword, without return              | STADDH, STADDLH   |
| STCLR      | Atomic bit clear, without return                    | STCLR, STCLRL     |
| STCLRB     | Atomic bit clear on byte, without return            | STCLRB, STCLRLB   |
| STCLRH     | Atomic bit clear on halfword, without return        | STCLRH, STCLRLH   |
| STEOR      | Atomic exclusive-OR, without return                 | STEOR, STEORL     |
| STEORB     | Atomic exclusive-OR on byte, without return         | STEORB, STEORLB   |
| STEORH     | Atomic exclusive-OR on halfword, without return     | STEORH, STEORLH   |
| STSET      | Atomic bit set, without return                      | STSET, STSETL     |
| STSETB     | Atomic bit set on byte, without return              | STSETB, STSETLB   |
| STSETH     | Atomic bit set on halfword, without return          | STSETH, STSETLH   |
| STMAX      | Atomic signed maximum, without return               | STSMAX,STSMAXL    |
| STMAXB     | Atomic signed maximum on byte, without return       | STSMAXB,STSMAXLB  |
| STMAXH     | Atomic signed maximum on halfword, without return   | STSMAXH,STSMAXLH  |
| STMIN      | Atomic signed minimum, without return               | STSMIN, STSMINL   |
| STMINB     | Atomic signed minimum on byte, without return       | STSMINB, STSMINLB |
| STMINH     | Atomic signed minimum on halfword, without return   | STSMINH, STSMINLH |
| STUMAX     | Atomic unsigned maximum, without return             | STUMAX,STUMAXL    |
| STUMAXB    | Atomic unsigned maximum on byte, without return     | STUMAXB,STUMAXLB  |
| STUMAXH    | Atomic unsigned maximum on halfword, without return | STUMAXH,STUMAXLH  |
| STUMIN     | Atomic unsigned minimum, without return             | STUMIN, STUMINL   |
| STUMINB    | Atomic unsigned minimum on byte, without return     | STUMINB, STUMINLB |
| STUMINH    | Atomic unsigned minimum on halfword, without return | STUMINH, STUMINLH |

## C3.2.17.2 Atomic floating-point memory operations

The atomic floating-point memory operation instructions atomically load a value from memory, perform a floating-point arithmetic operation, and store the result back to memory.

For more information on alignment requirements and behaviors, see Load-Exclusive/ Store-Exclusive and Atomic instructions.

## Table C3-49 Atomic floating-point memory instructions

| Mnemonic                                          | Instruction                    | See                                          |
|---------------------------------------------------|--------------------------------|----------------------------------------------|
| LDBFADD , LDBFADDA , LDBFADDAL , LDBFADDL         | Atomic BFloat16 add            | LDBFADD, LDBFADDA, LDBFADDAL, LDBFADDL       |
| LDBFMAX , LDBFMAXA , LDBFMAXAL , LDBFMAXL         | Atomic BFloat16 maximum        | LDBFMAX, LDBFMAXA, LDBFMAXAL, LDBFMAXL       |
| LDBFMAXNM , LDBFMAXNMA , LDBFMAXNMAL , LDBFMAXNML | Atomic BFloat16 maximum number | LDBFMAXNM,LDBFMAXNMA, LDBFMAXNMAL,LDBFMAXNML |

| Mnemonic                                          | Instruction                                          | See                                           |
|---------------------------------------------------|------------------------------------------------------|-----------------------------------------------|
| LDBFMIN , LDBFMINA , LDBFMINAL , LDBFMINL         | Atomic BFloat16 minimum                              | LDBFMIN, LDBFMINA, LDBFMINAL, LDBFMINL        |
| LDBFMINNM , LDBFMINNMA , LDBFMINNMAL , LDBFMINNML | Atomic BFloat16 minimum number                       | LDBFMINNM, LDBFMINNMA, LDBFMINNMAL,LDBFMINNML |
| LDFADD , LDFADDA , LDFADDAL , LDFADDL             | Atomic floating-point add                            | LDFADD, LDFADDA, LDFADDAL, LDFADDL            |
| LDFMAX , LDFMAXA , LDFMAXAL , LDFMAXL             | Atomic floating-point maximum                        | LDFMAX, LDFMAXA, LDFMAXAL, LDFMAXL            |
| LDFMAXNM , LDFMAXNMA , LDFMAXNMAL , LDFMAXNML     | Atomic floating-point maximum number                 | LDFMAXNM,LDFMAXNMA,LDFMAXNMAL, LDFMAXNML      |
| LDFMIN , LDFMINA , LDFMINAL , LDFMINL             | Atomic floating-point minimum                        | LDFMIN, LDFMINA, LDFMINAL, LDFMINL            |
| LDFMINNM , LDFMINNMA , LDFMINNMAL , LDFMINNML     | Atomic floating-point minimum number                 | LDFMINNM, LDFMINNMA, LDFMINNMAL, LDFMINNML    |
| STBFADD , STBFADDL                                | Atomic BFloat16 add, without return                  | STBFADD, STBFADDL                             |
| STBFMAX , STBFMAXL                                | Atomic BFloat16 maximum, without return              | STBFMAX,STBFMAXL                              |
| STBFMAXNM , STBFMAXNML                            | Atomic BFloat16 maximum number, without return       | STBFMAXNM,STBFMAXNML                          |
| STBFMIN , STBFMINL                                | Atomic BFloat16 minimum, without return              | STBFMIN, STBFMINL                             |
| STBFMINNM , STBFMINNML                            | Atomic BFloat16 minimum number, without return       | STBFMINNM, STBFMINNML                         |
| STFADD , STFADDL                                  | Atomic floating-point add, without return            | STFADD, STFADDL                               |
| STFMAX , STFMAXL                                  | Atomic floating-point maximum, without return        | STFMAX,STFMAXL                                |
| STFMAXNM , STFMAXNML                              | Atomic floating-point maximum number, without return | STFMAXNM,STFMAXNML                            |
| STFMIN , STFMINL                                  | Atomic floating-point minimum, without return        | STFMIN, STFMINL                               |
| STFMINNM , STFMINNML                              | Atomic floating-point minimum number, without return | STFMINNM, STFMINNML                           |

## C3.2.17.3 Unprivileged atomic memory operations

The unprivileged atomic memory operation instructions are added as part of the FEAT\_LSUI architecture feature. These intructions belong to the class of unprivileged memory access instructions. The privileges of the Explicit Memory Effects generated by these instructions are controlled by PSTATE.UAO. For more information, see PSTATE.UAO.

The atomic memory operation instructions support only one addressing mode:

- Base register only.

See also Load/store addressing modes.

## Table C3-50 Unprivileged atomic memory operation instructions

| Mnemonic   | Instruction                                   | See                                |
|------------|-----------------------------------------------|------------------------------------|
| LDTADD     | Atomic add unprivileged                       | LDTADD, LDTADDA, LDTADDAL,LDTADDL  |
| STTADD     | Atomic add unprivileged, without return       | STTADD, STTADDL                    |
| LDTSET     | Atomic bit set unprivileged                   | LDTSET, LDTSETA, LDTSETAL, LDTSETL |
| STTSET     | Atomic bit set unprivileged, without return   | STTSET, STTSETL                    |
| LDTCLR     | Atomic bit clear unprivileged                 | LDTCLR, LDTCLRA, LDTCLRAL, LDTCLRL |
| STTCLR     | Atomic bit clear unprivileged, without return | STTCLR, STTCLRL                    |

## C3.2.17.4 Swap operations

For the SWP instructions, where the source and destination registers are the same, if the instruction generates a synchronous Data Abort, then the source register is restored to the value it held before the instruction was executed.

If the destination register Rt is WZR or XZR, this is not regarded as doing a read for the purpose of a DMB LD barrier.

For information on alignment requirements and behaviors, see Load-Exclusive/ Store-Exclusive and Atomic instructions.

## Table C3-51 Swap instructions

| Mnemonic   | Instruction   | See                        |
|------------|---------------|----------------------------|
| SWP        | Swap          | SWP, SWPA, SWPAL,SWPL      |
| SWPB       | Swap byte     | SWPB, SWPAB, SWPALB,SWPLB  |
| SWPH       | Swap halfword | SWPH, SWPAH, SWPALH,SWPLH  |
| SWPP       | Swap quadword | SWPP, SWPPA, SWPPAL, SWPPL |

## C3.2.17.4.1 Swap unprivileged

The swap unprivileged instructions are added as part of the FEAT\_LSUI architecture feature. These intructions belong to the class of unprivileged memory access instructions. The privileges of the Explicit Memory Effects generated by these instructions are controlled by PSTATE.UAO. For more information, see PSTATE.UAO.

The swap unprivileged instructions support only one addressing mode:

- Base register only.

See also Load/store addressing modes.

## Table C3-52 Swap unprivileged instructions

| Mnemonic   | Instruction   | See                        |
|------------|---------------|----------------------------|
| SWPT       | Swap          | SWPT, SWPTA, SWPTAL, SWPTL |

## C3.2.17.5 Compare and Swap operations

If FEAT\_LSE2 is not implemented then:

- The CAS instructions require natural alignment.
- The CASP instructions require alignment to the total size of the memory being accessed.

If a compare and swap instruction does not perform a store, then the instruction does not have release semantics, regardless of the instruction ordering options.

For the CAS and CASP instructions, the architecture permits that a data read clears any Exclusives monitors associated with that location, even if the compare subsequently fails. If these instructions generate a synchronous Data Abort, the registers which are compared and loaded are restored to the values held in the registers before the instruction was executed.

If the destination register Rs is WZR or XZR, this is not regarded as doing a read for the purpose of a DMB LD barrier.

For more information on alignment requirements and behaviors, see Load-Exclusive/ Store-Exclusive and Atomic instructions.

## Table C3-53 Compare and swap instructions

| Mnemonic   | Instruction               | See                        |
|------------|---------------------------|----------------------------|
| CAS        | Compare and swap          | CAS, CASA, CASAL, CASL     |
| CASB       | Compare and swap byte     | CASB, CASAB, CASALB, CASLB |
| CASH       | Compare and swap halfword | CASH, CASAH, CASALH, CASLH |
| CASP       | Compare and swap pair     | CASP, CASPA, CASPAL, CASPL |

## C3.2.17.5.1 Compare and Swap unprivileged

The Compare and Swap unprivileged instructions are added as part of the FEAT\_LSUI architecture feature. These intructions belong to the class of unprivileged memory access instructions. The privileges of the Explicit Memory Effects generated by these instructions are controlled by PSTATE.UAO. For more information, see PSTATE.UAO.

The Compare and Swap unprivileged instructions support only one addressing mode:

- Base register only.

See also Load/store addressing modes.

## Table C3-54 Compare and swap unprivileged instructions

| Mnemonic   | Instruction                        | See                            |
|------------|------------------------------------|--------------------------------|
| CAST       | Compare and swap unprivileged      | CAST, CASAT, CASALT, CASLT     |
| CASPT      | Compare and swap pair unprivileged | CASPT, CASPAT, CASPALT, CASPLT |

## C3.2.17.6 Read-Check-Write

If FEAT\_THE is implemented, then the Read-Check-Write instructions, RCW , and Read-Check-Write Software instructions, RCWS , are provided to conditionally update stage 1 descriptors.

RCW and RCWS instructions update PSTATE.{N, Z, C, V} to {0, 0, 1, 0}, with all of the following exceptions:

- For the compare and swap variants of the RCW and RCWS instructions, if the compare fails, then PSTATE.N is set to 1.
- Otherwise, all of the following apply:
- -If RCW and RCWS instructions fail the RCW checks, then PSTATE.Z is set to 1.

- -If RCWS instructions fail the RCWS checks, then PSTATE.C is set to 0.

If FEAT\_D128 is implemented, then RCW and RCWS instructions that operate on 128 bits of data are provided.

If the address is not aligned to the data transfer size, then RCW and RCWS instructions generate an Alignment fault.

The following table shows the RCW and RCWS instructions that operate on 64 bits of data:

## Table C3-55 64 bit Read-Check-Write instructions

| Mnemonic   | Instruction                                              | See                                    |
|------------|----------------------------------------------------------|----------------------------------------|
| RCWCAS     | Read Check Write Compare and Swap doubleword             | RCWCAS,RCWCASA,RCWCASL,RCWCASAL        |
| RCWSCAS    | Read Check Write Software Compare and Swap doubleword    | RCWSCAS, RCWSCASA, RCWSCASL, RCWSCASAL |
| RCWCLR     | Read Check Write Atomic bit clear on doubleword          | RCWCLR,RCWCLRA,RCWCLRL,RCWCLRAL        |
| RCWSCLR    | Read Check Write Software Atomic bit clear on doubleword | RCWSCLR, RCWSCLRA, RCWSCLRL, RCWSCLRAL |
| RCWSET     | Read Check Write Atomic bit set on doubleword            | RCWSET, RCWSETA, RCWSETL,RCWSETAL      |
| RCWSWP     | Read Check Write Swap doubleword                         | RCWSWP,RCWSWPA,RCWSWPL,RCWSWPAL        |
| RCWSSWP    | Read Check Write Software Swap doubleword                | RCWSSWP, RCWSSWPA, RCWSSWPL, RCWSSWPAL |

The following table shows the RCW and RCWS instructions that operate on 128 bits of data:

Table C3-56 128 bit Read-Check-Write instructions

| Mnemonic   | Instruction                                            | See                                        |
|------------|--------------------------------------------------------|--------------------------------------------|
| RCWCASP    | Read Check Write Compare and Swap quadword             | RCWCASP, RCWCASPA, RCWCASPL,RCWCASPAL      |
| RCWSCASP   | Read Check Write Software Compare and Swap quadword    | RCWSCASP, RCWSCASPA, RCWSCASPL, RCWSCASPAL |
| RCWCLRP    | Read Check Write Atomic bit clear on quadword          | RCWCLRP, RCWCLRPA, RCWCLRPL,RCWCLRPAL      |
| RCWSCLRP   | Read Check Write Software Atomic bit clear on quadword | RCWSCLRP, RCWSCLRPA, RCWSCLRPL, RCWSCLRPAL |
| RCWSETP    | Read Check Write Atomic bit set on quadword            | RCWSETP, RCWSETPA, RCWSETPL, RCWSETPAL     |
| RCWSWPP    | Read Check Write Swap quadword                         | RCWSWPP,RCWSWPPA,RCWSWPPL,RCWSWPPAL        |
| RCWSSWPP   | Read Check Write Software Swap quadword                | RCWSSWPP, RCWSSWPPA, RCWSSWPPL, RCWSSWPPAL |

## C3.2.18 Memory Tagging instructions

C3.2.18.1

Tag load

Table C3-57 shows the Memory Tagging Extension Tag load instructions.

## Table C3-57 Tag load instructions

| Mnemonic   | Instruction         | See   |
|------------|---------------------|-------|
| LDG        | Load Allocation Tag | LDG   |

## C3.2.18.2 Tag store

Table C3-58 shows the Memory Tagging Extension Tag store instructions.

Also see DC GVA.

## Table C3-58 Tag store instructions

| Mnemonic   | Instruction           | See   |
|------------|-----------------------|-------|
| STG        | Store Allocation Tag  | STG   |
| ST2G       | Store Allocation Tags | ST2G  |

## C3.2.18.3 Tag and Data store

Table C3-59 shows the Memory Tagging Extension Tag and Data store instructions.

Also see DC GZVA and Table C3-63.

## Table C3-59 Tag and Data store instructions

| Mnemonic   | Instruction                                | See   |
|------------|--------------------------------------------|-------|
| STZG       | Store Allocation Tag, zeroing              | STZG  |
| STZ2G      | Store Allocation Tags, zeroing             | STZ2G |
| STGP       | Store Allocation Tag and pair of registers | STGP  |

## C3.2.18.4 Bulk Allocation tag access

Table C3-60 shows the Memory Tagging Extension Bulk Allocation tag access instructions.

## Table C3-60 Bulk Allocation tag access instructions

| Mnemonic   | Instruction                            | See   |
|------------|----------------------------------------|-------|
| LDGM       | Load tag multiple                      | LDGM  |
| STGM       | Store Allocation Tag multiple          | STGM  |
| STZGM      | Store Allocation Tag and zero multiple | STZGM |

## C3.2.19 Memory Copy and Memory Set instructions

If FEAT\_MOPS is implemented, the CPY* , SETE* , SETM* , and SETP* instructions described in this section are implemented. If FEAT\_MOPS and FEAT\_MTE are implemented, the SETG* instructions described in this section are also implemented. Collectively, the instructions described in this section are referred to as Memory Copy and Memory Set instructions.

To perform a memory copy or memory set, three instructions - a prologue, then a main, and then an epilogue - are expected to be run in succession, with no instruction appearing in the code between them:

- To perform a memory copy, forward-only: CPYFP* , then CPYFM* , and then CPYFE* .
- To perform a memory copy, forward or backward: CPYP* , then CPYM* , and then CPYE* .
- To perform a memory set with tag setting: SETGP* , then SETGM* , and then SETGE* .
- To perform a memory set without tag setting: SETP* , then SETM* , and then SETE* .

The variant of each instruction is also expected to be the same throughout one of these sequences. For example, CPYFPWTWN , CPYFMWTWN , CPYFEWTWN .

Note

The Memory Copy and Memory Set instructions are expected to be the preferred approach for compilation for performance for any of the following cases:

- The size or alignments of the copy or set operation are not known at compile time.
- The size or alignments of the copy or set operation are known at compile time, but not amenable to the operation being performed using load and store instructions without looping.

Arm recommends that hardware implementations optimise the performance of these cases.

Fetching of a Memory Copy and Memory Set instruction multiple times during its execution is permissible.

The handling of synchronous exceptions generated by Memory Copy and Memory Set instructions is described in ESR\_ELx, FAR\_ELx, Definition of a precise exception and imprecise exception, and Synchronous exception entry.

The handling of asynchronous exceptions generated by Memory Copy and Memory Set instructions is described in Definition of a precise exception and imprecise exception and Asynchronous exception entry.

Memory Copy and Memory Set exceptions can be generated by execution of Memory Copy and Memory Set instructions restarting on a physical hardware PE implementation that is different from the physical hardware PE implementation that an exception was taken from. For more information, see Memory Copy and Memory Set exceptions.

If an exception is taken during the execution of a Memory Copy and Memory Set instruction, that instruction has not been executed for the purposes of instruction counting, instruction tracing, statistical profiling, or single stepping.

For the purposes of single stepping and performance monitoring, each Memory Copy and Memory Set instruction is regarded as a single instruction that performs a store and, in the case of CPY* instructions, also performs a load.

For Memory Copy and Memory Set instructions, the following are not architecturally defined:

- The size of the memory transactions they create.
- The order between accesses to different addresses.

The CPY* instructions are guaranteed to make forward progress if none of the following leaf level translation table entries fault:

- The source leaf level translation table entry used to translate the address encoded in Xs .
- If the range of remaining source addresses, encoded in Xs and Xn , crosses a page boundary:
- -The next leaf level translation table entry, as determined by the copy direction, adjacent to the source leaf level translation table entry used to translate the address encoded in Xs .
- The destination leaf level translation table entry used to translate the address encoded in Xd .
- If the range of remaining destination addresses, encoded in Xd and Xn , crosses a page boundary:

- -The next leaf level translation table entry, as determined by the copy direction, adjacent to the destination leaf level translation table entry used to translate the address encoded in Xd .

The SET* instructions are guaranteed to make forward progress if none of the following leaf level translation table entries fault:

- The destination leaf level translation table entry used to translate the address encoded in Xd .
- If the the range of remaining addresses, encoded in Xd and Xn , crosses a page boundary:
- -The next leaf level translation table entry adjacent to the destination leaf level translation table entry used to translate the address encoded in Xd .

Note

For a CPY* instruction, destination address, source address and copy size are encoded in Xd , Xs and Xn depending on the Option and Direction chosen by the implementation.

For a SET* instruction, destination address and set size are encoded in Xd and Xn depending on the Option and Direction chosen by the implementation.

APEcanensure that the forward progress described in this section can be achieved by ensuring that, when an MMU fault is encountered, all bytes leading up to the fault have been operated on and the operand registers have been updated. APEshould not report MMU faults other than for the leaf level translation table entries described in this section.

Table C3-61 shows the memory copy, forward-only instructions.

Table C3-61 Memory copy, forward-only instructions

| Mnemonic   | Instruction                                                                           | See                                              |
|------------|---------------------------------------------------------------------------------------|--------------------------------------------------|
| CPYFE      | Memory Copy Forward-only Epilogue                                                     | CPYFP, CPYFM, CPYFE Epilogue variant             |
| CPYFEN     | Memory Copy Forward-only Epilogue, reads and writes non-temporal                      | CPYFPN, CPYFMN, CPYFEN Epilogue variant          |
| CPYFERN    | Memory Copy Forward-only Epilogue, reads non-temporal                                 | CPYFPRN, CPYFMRN, CPYFERN Epilogue variant       |
| CPYFERT    | Memory Copy Forward-only Epilogue, reads unprivileged                                 | CPYFPRT, CPYFMRT, CPYFERT Epilogue variant       |
| CPYFERTN   | Memory Copy Forward-only Epilogue, reads unprivileged, reads and writes non-temporal  | CPYFPRTN, CPYFMRTN, CPYFERTN Epilogue variant    |
| CPYFERTRN  | Memory Copy Forward-only Epilogue, reads unprivileged and non-temporal                | CPYFPRTRN, CPYFMRTRN, CPYFERTRN Epilogue variant |
| CPYFERTWN  | Memory Copy Forward-only Epilogue, reads unprivileged, writes non-temporal            | CPYFPRTWN,CPYFMRTWN,CPYFERTWN Epilogue variant   |
| CPYFET     | Memory Copy Forward-only Epilogue, reads and writes unprivileged                      | CPYFPT, CPYFMT, CPYFET Epilogue variant          |
| CPYFETN    | Memory Copy Forward-only Epilogue, reads and writes unprivileged and non-temporal     | CPYFPTN, CPYFMTN, CPYFETN Epilogue variant       |
| CPYFETRN   | Memory Copy Forward-only Epilogue, reads and writes unprivileged, reads non-temporal  | CPYFPTRN, CPYFMTRN, CPYFETRN Epilogue variant    |
| CPYFETWN   | Memory Copy Forward-only Epilogue, reads and writes unprivileged, writes non-temporal | CPYFPTWN, CPYFMTWN, CPYFETWNEpilogue variant     |
| CPYFEWN    | Memory Copy Forward-only Epilogue, writes non-temporal                                | CPYFPWN, CPYFMWN,CPYFEWNEpilogue variant         |
| CPYFEWT    | Memory Copy Forward-only Epilogue, writes unprivileged                                | CPYFPWT, CPYFMWT, CPYFEWTEpilogue variant        |

| Mnemonic   | Instruction                                                                           | See                                              |
|------------|---------------------------------------------------------------------------------------|--------------------------------------------------|
| CPYFEWTN   | Memory Copy Forward-only Epilogue, writes unprivileged, reads and writes non-temporal | CPYFPWTN, CPYFMWTN, CPYFEWTNEpilogue variant     |
| CPYFEWTRN  | Memory Copy Forward-only Epilogue, writes unprivileged, reads non-temporal            | CPYFPWTRN, CPYFMWTRN, CPYFEWTRNEpilogue variant  |
| CPYFMWTWN  | Memory Copy Forward-only Epilogue, writes unprivileged and non-temporal               | CPYFPWTWN, CPYFMWTWN,CPYFEWTWNEpilogue variant   |
| CPYFM      | Memory Copy Forward-only Main                                                         | CPYFP, CPYFM, CPYFE Main variant                 |
| CPYFMN     | Memory Copy Forward-only Main, reads and writes non-temporal                          | CPYFPN, CPYFMN, CPYFEN Main variant              |
| CPYFMRN    | Memory Copy Forward-only Main, reads non-temporal                                     | CPYFPRN, CPYFMRN, CPYFERN Main variant           |
| CPYFMRT    | Memory Copy Forward-only Main, reads unprivileged                                     | CPYFPRT, CPYFMRT, CPYFERT Main variant           |
| CPYFMRTN   | Memory Copy Forward-only Main, reads unprivileged, reads and writes non-temporal      | CPYFPRTN, CPYFMRTN, CPYFERTN Main variant        |
| CPYFMRTRN  | Memory Copy Forward-only Main, reads unprivileged and non-temporal                    | CPYFPRTRN, CPYFMRTRN, CPYFERTRN Main variant     |
| CPYFMRTWN  | Memory Copy Forward-only Main, reads unprivileged, writes non-temporal                | CPYFPRTWN,CPYFMRTWN,CPYFERTWN Main variant       |
| CPYFMT     | Memory Copy Forward-only Main, reads and writes unprivileged                          | CPYFPT, CPYFMT, CPYFET Main variant              |
| CPYFMTN    | Memory Copy Forward-only Main, reads and writes unprivileged and non-temporal         | CPYFPTN, CPYFMTN, CPYFETN Main variant           |
| CPYFMTRN   | Memory Copy Forward-only Main, reads and writes unprivileged, reads non-temporal      | CPYFPTRN, CPYFMTRN, CPYFETRN Main variant        |
| CPYFMTWN   | Memory Copy Forward-only Main, reads and writes unprivileged, writes non-temporal     | CPYFPTWN, CPYFMTWN, CPYFETWNMain variant         |
| CPYFMWN    | Memory Copy Forward-only Main, writes non-temporal                                    | CPYFPWN, CPYFMWN,CPYFEWNMainvariant              |
| CPYFMWT    | Memory Copy Forward-only Main, writes unprivileged                                    | CPYFPWT, CPYFMWT, CPYFEWTMain variant            |
| CPYFMWTN   | Memory Copy Forward-only Main, writes unprivileged, reads and writes non-temporal     | CPYFPWTN, CPYFMWTN, CPYFEWTNMain variant         |
| CPYFMWTRN  | Memory Copy Forward-only Main, writes unprivileged, reads non-temporal                | CPYFPWTRN, CPYFMWTRN, CPYFEWTRNMain variant      |
| CPYFMWTWN  | Memory Copy Forward-only Main, writes unprivileged and non-temporal                   | CPYFPWTWN, CPYFMWTWN,CPYFEWTWNMainvariant        |
| CPYFP      | Memory Copy Forward-only Prologue                                                     | CPYFP, CPYFM, CPYFE Prologue variant             |
| CPYFPN     | Memory Copy Forward-only Prologue, reads and writes non-temporal                      | CPYFPN, CPYFMN, CPYFEN Prologue variant          |
| CPYFPRN    | Memory Copy Forward-only Prologue, reads non-temporal                                 | CPYFPRN, CPYFMRN, CPYFERN Prologue variant       |
| CPYFPRT    | Memory Copy Forward-only Prologue, reads unprivileged                                 | CPYFPRT, CPYFMRT, CPYFERT Prologue variant       |
| CPYFPRTN   | Memory Copy Forward-only Prologue, reads unprivileged, reads and writes non-temporal  | CPYFPRTN, CPYFMRTN, CPYFERTN Prologue variant    |
| CPYFPRTRN  | Memory Copy Forward-only Prologue, reads unprivileged and non-temporal                | CPYFPRTRN, CPYFMRTRN, CPYFERTRN Prologue variant |

| Mnemonic   | Instruction                                                                           | See                                             |
|------------|---------------------------------------------------------------------------------------|-------------------------------------------------|
| CPYFPRTWN  | Memory Copy Forward-only Prologue, reads unprivileged, writes non-temporal            | CPYFPRTWN,CPYFMRTWN,CPYFERTWN Prologue variant  |
| CPYFPT     | Memory Copy Forward-only Prologue, reads and writes unprivileged                      | CPYFPT, CPYFMT, CPYFET Prologue variant         |
| CPYFPTN    | Memory Copy Forward-only Prologue, reads and writes unprivileged and non-temporal     | CPYFPTN, CPYFMTN, CPYFETN Prologue variant      |
| CPYFPTRN   | Memory Copy Forward-only Prologue, reads and writes unprivileged, reads non-temporal  | CPYFPTRN, CPYFMTRN, CPYFETRN Prologue variant   |
| CPYFPTWN   | Memory Copy Forward-only Prologue, reads and writes unprivileged, writes non-temporal | CPYFPTWN, CPYFMTWN, CPYFETWNPrologue variant    |
| CPYFPWN    | Memory Copy Forward-only Prologue, writes non-temporal                                | CPYFPWN, CPYFMWN,CPYFEWNPrologue variant        |
| CPYFPWT    | Memory Copy Forward-only Prologue, writes unprivileged                                | CPYFPWT, CPYFMWT, CPYFEWTPrologue variant       |
| CPYFPWTN   | Memory Copy Forward-only Prologue, writes unprivileged, reads and writes non-temporal | CPYFPWTN, CPYFMWTN, CPYFEWTNPrologue variant    |
| CPYFPWTRN  | Memory Copy Forward-only Prologue, writes unprivileged, reads non-temporal            | CPYFPWTRN, CPYFMWTRN, CPYFEWTRNPrologue variant |
| CPYFPWTWN  | Memory Copy Forward-only Prologue, writes unprivileged and non-temporal               | CPYFPWTWN, CPYFMWTWN,CPYFEWTWNPrologue variant  |

Table C3-62 shows the memory copy, forward or backward instructions.

Table C3-62 Memory copy, forward or backward instructions

| Mnemonic   | Instruction                                                              | See                                           |
|------------|--------------------------------------------------------------------------|-----------------------------------------------|
| CPYE       | Memory Copy Epilogue                                                     | CPYP, CPYM, CPYE Epilogue variant             |
| CPYEN      | Memory Copy Epilogue, reads and writes non-temporal                      | CPYPN, CPYMN, CPYEN Epilogue variant          |
| CPYERN     | Memory Copy Epilogue, reads non-temporal                                 | CPYPRN, CPYMRN, CPYERN Epilogue variant       |
| CPYERT     | Memory Copy Epilogue, reads unprivileged                                 | CPYPRT, CPYMRT, CPYERT Epilogue variant       |
| CPYERTN    | Memory Copy Epilogue, reads unprivileged, reads and writes non-temporal  | CPYPRTN, CPYMRTN, CPYERTN Epilogue variant    |
| CPYERTRN   | Memory Copy Epilogue, reads unprivileged and non-temporal                | CPYPRTRN, CPYMRTRN, CPYERTRN Epilogue variant |
| CPYERTWN   | Memory Copy Epilogue, reads unprivileged, writes non-temporal            | CPYPRTWN, CPYMRTWN,CPYERTWNEpilogue variant   |
| CPYET      | Memory Copy Epilogue, reads and writes unprivileged                      | CPYPT, CPYMT, CPYET Epilogue variant          |
| CPYETN     | Memory Copy Epilogue, reads and writes unprivileged and non-temporal     | CPYPTN, CPYMTN, CPYETN Epilogue variant       |
| CPYETRN    | Memory Copy Epilogue, reads and writes unprivileged, reads non-temporal  | CPYPTRN, CPYMTRN, CPYETRN Epilogue variant    |
| CPYETWN    | Memory Copy Epilogue, reads and writes unprivileged, writes non-temporal | CPYPTWN, CPYMTWN,CPYETWNEpilogue variant      |

| Mnemonic   | Instruction                                                              | See                                           |
|------------|--------------------------------------------------------------------------|-----------------------------------------------|
| CPYEWN     | Memory Copy Epilogue, writes non-temporal                                | CPYPWN, CPYMWN,CPYEWNEpilogue variant         |
| CPYEWT     | Memory Copy Epilogue, writes unprivileged                                | CPYPWT, CPYMWT, CPYEWTEpilogue variant        |
| CPYEWTN    | Memory Copy Epilogue, writes unprivileged, reads and writes non-temporal | CPYPWTN, CPYMWTN,CPYEWTNEpilogue variant      |
| CPYEWTRN   | Memory Copy Epilogue, writes unprivileged, reads non-temporal            | CPYPWTRN, CPYMWTRN,CPYEWTRNEpilogue variant   |
| CPYMWTWN   | Memory Copy Epilogue, writes unprivileged and non-temporal               | CPYPWTWN,CPYMWTWN,CPYEWTWNEpilogue variant    |
| CPYM       | Memory Copy Main                                                         | CPYP, CPYM, CPYE Main variant                 |
| CPYMN      | Memory Copy Main, reads and writes non-temporal                          | CPYPN, CPYMN, CPYEN Main variant              |
| CPYMRN     | Memory Copy Main, reads non-temporal                                     | CPYPRN, CPYMRN, CPYERN Main variant           |
| CPYMRT     | Memory Copy Main, reads unprivileged                                     | CPYPRT, CPYMRT, CPYERT Main variant           |
| CPYMRTN    | Memory Copy Main, reads unprivileged, reads and writes non-temporal      | CPYPRTN, CPYMRTN, CPYERTN Main variant        |
| CPYMRTRN   | Memory Copy Main, reads unprivileged and non-temporal                    | CPYPRTRN, CPYMRTRN, CPYERTRN Main variant     |
| CPYMRTWN   | Memory Copy Main, reads unprivileged, writes non-temporal                | CPYPRTWN, CPYMRTWN,CPYERTWNMainvariant        |
| CPYMT      | Memory Copy Main, reads and writes unprivileged                          | CPYPT, CPYMT, CPYET Main variant              |
| CPYMTN     | Memory Copy Main, reads and writes unprivileged and non-temporal         | CPYPTN, CPYMTN, CPYETN Main variant           |
| CPYMTRN    | Memory Copy Main, reads and writes unprivileged, reads non-temporal      | CPYPTRN, CPYMTRN, CPYETRN Main variant        |
| CPYMTWN    | Memory Copy Main, reads and writes unprivileged, writes non-temporal     | CPYPTWN, CPYMTWN,CPYETWNMainvariant           |
| CPYMWN     | Memory Copy Main, writes non-temporal                                    | CPYPWN, CPYMWN,CPYEWNMainvariant              |
| CPYMWT     | Memory Copy Main, writes unprivileged                                    | CPYPWT, CPYMWT, CPYEWTMain variant            |
| CPYMWTN    | Memory Copy Main, writes unprivileged, reads and writes non-temporal     | CPYPWTN, CPYMWTN,CPYEWTNMainvariant           |
| CPYMWTRN   | Memory Copy Main, writes unprivileged, reads non-temporal                | CPYPWTRN, CPYMWTRN,CPYEWTRNMainvariant        |
| CPYMWTWN   | Memory Copy Main, writes unprivileged and non-temporal                   | CPYPWTWN,CPYMWTWN,CPYEWTWNMainvariant         |
| CPYP       | Memory Copy Prologue                                                     | CPYP, CPYM, CPYE Prologue variant             |
| CPYPN      | Memory Copy Prologue, reads and writes non-temporal                      | CPYPN, CPYMN, CPYEN Prologue variant          |
| CPYPRN     | Memory Copy Prologue, reads non-temporal                                 | CPYPRN, CPYMRN, CPYERN Prologue variant       |
| CPYPRT     | Memory Copy Prologue, reads unprivileged                                 | CPYPRT, CPYMRT, CPYERT Prologue variant       |
| CPYPRTN    | Memory Copy Prologue, reads unprivileged, reads and writes non-temporal  | CPYPRTN, CPYMRTN, CPYERTN Prologue variant    |
| CPYPRTRN   | Memory Copy Prologue, reads unprivileged and non-temporal                | CPYPRTRN, CPYMRTRN, CPYERTRN Prologue variant |
| CPYPRTWN   | Memory Copy Prologue, reads unprivileged, writes non-temporal            | CPYPRTWN, CPYMRTWN,CPYERTWNPrologue variant   |
| CPYPT      | Memory Copy Prologue, reads and writes unprivileged                      | CPYPT, CPYMT, CPYET Prologue variant          |

| Mnemonic   | Instruction                                                              | See                                         |
|------------|--------------------------------------------------------------------------|---------------------------------------------|
| CPYPTN     | Memory Copy Prologue, reads and writes unprivileged and non-temporal     | CPYPTN, CPYMTN, CPYETN Prologue variant     |
| CPYPTRN    | Memory Copy Prologue, reads and writes unprivileged, reads non-temporal  | CPYPTRN, CPYMTRN, CPYETRN Prologue variant  |
| CPYPTWN    | Memory Copy Prologue, reads and writes unprivileged, writes non-temporal | CPYPTWN, CPYMTWN,CPYETWNPrologue variant    |
| CPYPWN     | Memory Copy Prologue, writes non-temporal                                | CPYPWN, CPYMWN,CPYEWNPrologue variant       |
| CPYPWT     | Memory Copy Prologue, writes unprivileged                                | CPYPWT, CPYMWT, CPYEWTPrologue variant      |
| CPYPWTN    | Memory Copy Prologue, writes unprivileged, reads and writes non-temporal | CPYPWTN, CPYMWTN,CPYEWTNPrologue variant    |
| CPYPWTRN   | Memory Copy Prologue, writes unprivileged, reads non-temporal            | CPYPWTRN, CPYMWTRN,CPYEWTRNPrologue variant |
| CPYPWTWN   | Memory Copy Prologue, writes unprivileged and non-temporal               | CPYPWTWN,CPYMWTWN,CPYEWTWNPrologue variant  |

Table C3-63 shows the memory set with tag setting instructions.

## Table C3-63 Memory set with tag setting instructions

| Mnemonic   | Instruction                                                         | See                                        |
|------------|---------------------------------------------------------------------|--------------------------------------------|
| SETGE      | Memory Set with tag setting Epilogue                                | SETGP, SETGM, SETGE Epilogue variant       |
| SETGEN     | Memory Set with tag setting Epilogue, non-temporal                  | SETGPN, SETGMN, SETGEN Epilogue variant    |
| SETGET     | Memory Set with tag setting Epilogue, unprivileged                  | SETGPT, SETGMT, SETGET Epilogue variant    |
| SETGETN    | Memory Set with tag setting Epilogue, unprivileged and non-temporal | SETGPTN, SETGMTN, SETGETN Epilogue variant |
| SETGM      | Memory Set with tag setting Main                                    | SETGP, SETGM, SETGE Main variant           |
| SETGMN     | Memory Set with tag setting Main, non-temporal                      | SETGPN, SETGMN, SETGEN Main variant        |
| SETGMT     | Memory Set with tag setting Main, unprivileged                      | SETGPT, SETGMT, SETGET Main variant        |
| SETGMTN    | Memory Set with tag setting Main, unprivileged and non-temporal     | SETGPTN, SETGMTN, SETGETN Main variant     |
| SETGP      | Memory Set with tag setting Prologue                                | SETGP, SETGM, SETGE Prologue variant       |
| SETGPN     | Memory Set with tag setting Prologue, non-temporal                  | SETGPN, SETGMN, SETGEN Prologue variant    |
| SETGPT     | Memory Set with tag setting Prologue, unprivileged                  | SETGPT, SETGMT, SETGET Prologue variant    |
| SETGPTN    | Memory Set with tag setting Prologue, unprivileged and non-temporal | SETGPTN, SETGMTN, SETGETN Prologue variant |

Table C3-64 shows the memory set without tag setting instructions.

## Table C3-64 Memory set without tag setting instructions

| Mnemonic   | Instruction                                        | See                                     |
|------------|----------------------------------------------------|-----------------------------------------|
| SETE       | Memory Set Epilogue                                | SETP, SETM, SETE Epilogue variant       |
| SETEN      | Memory Set Epilogue, non-temporal                  | SETPN, SETMN, SETEN Epilogue variant    |
| SETET      | Memory Set Epilogue, unprivileged                  | SETPT, SETMT, SETET Epilogue variant    |
| SETETN     | Memory Set Epilogue, unprivileged and non-temporal | SETPTN, SETMTN, SETETN Epilogue variant |
| SETM       | Memory Set Main                                    | SETP, SETM, SETE Main variant           |
| SETMN      | Memory Set Main, non-temporal                      | SETPN, SETMN, SETEN Main variant        |
| SETMT      | Memory Set Main, unprivileged                      | SETPT, SETMT, SETET Main variant        |
| SETMTN     | Memory Set Main, unprivileged and non-temporal     | SETPTN, SETMTN, SETETN Main variant     |
| SETP       | Memory Set Prologue                                | SETP, SETM, SETE Prologue variant       |
| SETPN      | Memory Set Prologue, non-temporal                  | SETPN, SETMN, SETEN Prologue variant    |
| SETPT      | Memory Set Prologue, unprivileged                  | SETPT, SETMT, SETET Prologue variant    |
| SETPTN     | Memory Set Prologue, unprivileged and non-temporal | SETPTN, SETMTN, SETETN Prologue variant |