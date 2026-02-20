## G5.12 Exception reporting in a VMSAv8-32 implementation

This section describes exception reporting, in AArch32 state, in a VMSAv8-32 implementation. That is, it describes only the reporting of exceptions that are taken to an Exception level that is using AArch32. EL2 provides an enhanced reporting mechanism for exceptions taken to the Non-secure EL2 mode, Hyp mode. This means that, for VMSAv8-32, the exception reporting depends on the mode to which the exception is taken.

Note

The enhanced reporting mechanism for exceptions that are taken to Hyp mode is generally similar to the reporting of exceptions that are taken to an Exception level that is using AArch64.

About exception reporting introduces the general approach to exception reporting, and the following sections then describe exception reporting at different privilege levels:

- Reporting exceptions taken to PL1 modes.
- Fault reporting in PL1 modes.
- Summary of register updates on faults taken to PL1 modes.
- Reporting exceptions taken to Hyp mode.
- Use of the HSR.
- Summary of register updates on exceptions taken to Hyp mode.

Note

The registers used for exception reporting also report information about debug exceptions. For more information, see:

- Data Abort exceptions, taken to a PL1 mode.
- Prefetch Abort exceptions, taken to a PL1 mode.
- Reporting exceptions taken to Hyp mode.

## G5.12.1 About exception reporting

In an implementation that includes EL2 and EL3, exceptions can be taken to:

- Monitor mode, if EL3 is using AArch32.
- Hyp mode, if EL2 is using AArch32.
- ASecure or Non-secure PL1 mode.

Monitor mode is a PL1 mode, but:

- It is accessible only when EL3 is using AArch32.
- It is present only in Secure state.
- When EL3 is using AArch32, System register controls route some exceptions from Non-secure state to Monitor mode. These are the only cases where taking an exception to an Exception level that is using AArch32 changes the Security state of the PE.

Exception reporting in Hyp mode differs significantly from that in the other modes, but in general, exception reporting returns:

- Information about the exception:
- -On taking an exception to Hyp mode, the Hyp Syndrome Register , HSR, returns syndrome information.
- -On taking an exception to any other mode, a Fault Status Register (FSR) returns status information.
- For synchronous exceptions, one or more addresses associated with the exceptions, returned in Fault Address Registers (FARs). For a permitted exception to this requirement see Fault address reporting on synchronous External aborts.

In all modes, additional IMPLEMENTATION DEFINED registers can provide additional information about exceptions.

Note

- PE mode for taking exceptions describes how the mode to which an exception is taken is determined.
- EL2 provides:
- -Specific exception types, that can only be taken from Non-secure PL1 and EL0 modes, and are always taken to Hyp mode.
- -Routing controls that can route some exceptions from Non-secure PL1 and EL0 modes to Hyp mode.

These exceptions are reported using the same mechanism as the Hyp mode reporting of VMSAv8-32 memory aborts, as described in this section.

Memory system faults generate either a Data Abort exception or a Prefetch Abort exception, as summarized in:

- Reporting exceptions taken to PL1 modes.
- Memory fault reporting in Hyp mode.

On an access that might have multiple aborts, the MMU fault checking sequence and the prioritization of aborts determine which abort occurs. For more information, see The MMU fault-checking sequence and AArch32 state prioritization of synchronous aborts from a single stage of address translation.

## G5.12.1.1 Fault address reporting on synchronous External aborts

The general architectural requirement is that, on a synchronous abort, the faulting address is recorded in a Fault Address Register (FAR). This requirement is relaxed for the case of a synchronous External abort that is not a synchronous External abort on a translation table walk. In this case only:

- It is IMPLEMENTATION DEFINED whether the faulting address is recorded in a FAR.
- Abit in a fault reporting register, the FnV bit, indicates whether a valid address is recorded.

For exceptions taken to an Exception level that is using AArch32, the details of this reporting depend on whether the exception is taken to:

- APL1 mode, as described in Reporting exceptions taken to PL1 modes.
- Hyp mode, as described in Reporting exceptions taken to Hyp mode.

## G5.12.2 Reporting exceptions taken to PL1 modes

The following sections give general information about the reporting of exceptions when they are taken to a Secure or Non-secure PL1 mode:

- Registers used for reporting exceptions taken to PL1 modes.
- Data Abort exceptions, taken to a PL1 mode.
- Prefetch Abort exceptions, taken to a PL1 mode.

Fault reporting in PL1 modes then describes the fault reporting in these modes, including the encodings used for reporting the faults.

Note

Security state, Exception levels, and AArch32 execution privilege describes how the Secure and Non-secure PL1 modes map onto the Exception levels.

## G5.12.2.1 Registers used for reporting exceptions taken to PL1 modes

AArch32 state defines the following registers, and register encodings, for exceptions taken to PL1 modes:

- The DFSR holds information about a Data Abort exception.
- The DFAR holds the faulting address for some synchronous Data Abort exceptions.
- The IFSR holds information about a Prefetch Abort exception.
- The IFAR holds the faulting address for some synchronous Prefetch Abort exceptions.

In addition, if implemented, the optional ADFSR and AIFSR can provide additional fault information, see Auxiliary Fault Status Registers.

## G5.12.2.1.1 Auxiliary Fault Status Registers

AArch32 state defines the following Auxiliary Fault Status Registers:

- The Auxiliary Data Fault Status Register, ADFSR.
- The Auxiliary Instruction Fault Status Register, AIFSR.

The position of these registers is architecturally-defined, but the content and use of the registers is IMPLEMENTATION DEFINED. An implementation can use these registers to return additional fault status information. An example use of these registers is to return more information for diagnosing parity or ECC errors.

An implementation that does not need to report additional fault information must implement these registers as RES0. This ensures that an attempt to access these registers from software executing at PL1 does not cause an Undefined Instruction exception.

## G5.12.2.2 Data Abort exceptions, taken to a PL1 mode

On taking a Data Abort exception to a PL1 mode:

- If the exception is on an instruction cache or branch predictor maintenance operation by V A, its reporting depends on the value of TTBCR.EAE. For more information about the registers used when reporting the exception, see Data Abort on an instruction cache or branch predictor maintenance instruction by V A.
- Otherwise, the DFSR is updated with details of the fault, including the appropriate Fault status code. If the Data Abort exception is synchronous, DFSR.WnR is updated to indicate whether the faulted instruction was a read or a write. However, if the fault is on a cache maintenance instruction, or on an address translation instruction, WnR is set to 1, to indicate a fault on a write instruction, and the CM bit is set to 1.

If the Data Abort is external, then DFSR provides fields for additional classification of the abort, see Provision for classification of External aborts.

See the register description for more information about the returned fault information. See also Data Abort on a Watchpoint exception.

If the Data Abort exception is

- -Synchronous, the DFAR is updated with the VA that caused the exception, but see Fault address reporting on synchronous External aborts for a permitted exception to this requirement.
- -Asynchronous, the DFAR becomes UNKNOWN.

DFSR.WnR and DFSR.CM are UNKNOWN on an asynchronous Data Abort exception.

For all Data Abort exceptions, if the implementation includes EL3, the Security state of the PE in the mode to which the Data Abort exception is taken determines whether the Secure or Non-secure DFSR and DFAR are updated.

## G5.12.2.2.1 Data Abort on an instruction cache or branch predictor maintenance instruction by VA

If an instruction cache invalidation by V A or branch predictor invalidation by V A operation generates a Data Abort exception that is taken to a PL1 mode, the DFAR is updated to hold the faulting V A. However, the reporting of the fault depends on the value of TTBCR.EAE:

## TTBCR.EAE == 0

When the value of TTBCR.EAE is 0, it is IMPLEMENTATION DEFINED which of the following is used when reporting the fault:

- The DFSR indicates an Instruction cache maintenance instruction fault, and the IFSR is valid and indicates the cause of the fault, a Translation fault or Access flag fault.
- The DFSR indicates the cause of the fault, a Translation fault or Access flag fault. The IFSR is UNKNOWN.

## In either case:

- DFSR.WnR is set to 1.
- DFSR.CM is set to 1, to indicate a fault on a cache maintenance instruction.

## TTBCR.EAE == 1

When the value of TTBCR.EAE is 1:

- DFSR.CM is set to 1, to indicate a fault on a cache maintenance instruction.
- DFSR.STATUS indicates the cause of the fault, a Translation or Access flag fault.
- DFSR.WnR is set to 1.
- The IFSR is UNKNOWN.

## G5.12.2.2.2 Data Abort on a Watchpoint exception

On taking a Data Abort exception caused by a watchpoint:

- DFSR.FS is updated to indicate a debug exception.
- DFSR.{WnR, Domain} are UNKNOWN.
- DFAR is set to the address that generated the watchpoint.

Note

- lr\_ABT indicates the address of the instruction that triggered the watchpoint.

Awatchpointed address can be any byte-aligned address. The address reported in DFAR might not be the watchpointed address, and:

- For a watchpoint due to an operation other than a Data Cache maintenance instruction, can be any address between and including:
- -The lowest address accessed by the instruction that triggered the watchpoint.
- -The highest watchpointed address accessed by that instruction.

If multiple watchpoints are set in this range, there is no guarantee of which watchpoint is generated.

The address must also be within a naturally-aligned block of memory of an IMPLEMENTATION DEFINED power-of-two size, containing a watchpoint address accessed by that location.

- Note
- -In particular, there is no guarantee of generating the watchpoint with the lowest address in the range.
- -The IMPLEMENTATION DEFINED power-of-two size must be no larger than the block size of the AArch64 DC ZVA operation.
- For a watchpoint due to a Data Cache operation, the address is the address passed to the instruction. This might be an address that is above the watchpointed location.

## G5.12.2.3 Prefetch Abort exceptions, taken to a PL1 mode

For a Prefetch Abort exception generated by an instruction fetch, the Prefetch Abort exception is taken synchronously with the instruction that the abort is reported on. This means:

- If the PE attempts to execute the instruction a Prefetch Abort exception is generated.
- If an instruction fetch is issued but the PE does not attempt to execute the prefetched instruction, no Prefetch Abort exception is generated for that instruction. For example, if the execution flow branches round a prefetched instruction, no Prefetch Abort exception is generated.

In addition, Breakpoint Instruction, Breakpoint, and Vector Catch exceptions, generate a Prefetch Abort exception, see the following for more information:

- Exception syndrome information and preferred return address for a BKPT instruction.
- Exception syndrome information and preferred return address for a Breakpoint exception.
- Exception syndrome information and preferred return address for a Vector Catch exception.

Note

Usually, the term exception syndrome is used only for exceptions taken to Hyp mode, or to AArch64 state. The referenced sections use the term more generally, to include exception information reported in the IFSR.

On taking a Prefetch Abort exception to a PL1 mode:

- The IFSR is updated with details of the fault, including the appropriate fault code. If appropriate, the fault code indicates that the exception was generated by a debug exception.
- See the register description for more information about the returned fault information.
- For a Prefetch Abort exception generated by an instruction fetch, the IFAR is updated with the V A that caused the exception, but see Fault address reporting on synchronous External aborts for a permitted exception to this requirement.
- For a Prefetch Abort exception generated by a debug exception, the IFAR is UNKNOWN.

If the implementation includes EL3, the security state of the PE in the mode to which it takes the Prefetch Abort exception determines whether the exception updates the Secure or Non-secure IFSR and IFAR.

## G5.12.3 Fault reporting in PL1 modes

The FSRs provide fault information, including an indication of the fault that occurred. The following subsections describe fault reporting in PL1 modes for each of the translation table formats:

- PL1 fault reporting with the Short-descriptor translation table format.
- PL1 fault reporting with the Long-descriptor translation table format.

Reserved encoding in the IFSR and DFSR encodings tables gives some additional information about the encodings for both formats.

Summary of register updates on faults taken to PL1 modes shows which registers are updated on each of the reported faults.

Reporting of External aborts taken from Non-secure state to Monitor mode describes how the fault status register format is determined for those aborts. For all other aborts, the current translation table format determines the format of the fault status registers.

## G5.12.3.1 Reporting of External aborts taken from Non-secure state to Monitor mode

When an External abort is taken from Non-secure state to Monitor mode:

- For a Data Abort exception, the Secure DFSR and DFAR hold information about the abort.
- For a Prefetch Abort exception, the Secure IFSR and IFAR hold information about the abort.
- The abort does not affect the contents of the Non-secure copies of the fault reporting registers.

Normally, the current translation table format determines the format of the DFSR and IFSR. However, when SCR.EA is set to 1, to route External aborts to Monitor mode, and an External abort is taken from Non-secure state, this section defines the DFSR and IFSR format.

For an External abort taken from Non-secure state to Monitor mode, the DFSR or IFSR uses the format associated with the Long-descriptor translation table format, as described in PL1 fault reporting with the Long-descriptor translation table format, if any of the following applies:

- The value of the Secure TTBCR.EAE field is 1.

- The External abort is synchronous and is taken from either:
- -Hyp mode.
- -ANon-secure PL1 or EL0 mode, and the value of the Non-secure TTBCR.EAE field is 1.

## Otherwise:

- For a synchronous External abort from a stage 2 translation routed to Monitor mode when the value of the Secure TTBCR.EAE field is 0 it is IMPLEMENTATION DEFINED whether:
- -The format associated with the Long-descriptor translation table format is used, as described in PL1 fault reporting with the Long-descriptor translation table format.
- -The format associated with the Short-descriptor translation table format is used, as described in PL1 fault reporting with the Short-descriptor translation table format. Arm deprecates using this format. When this format is used, the value of DFSR.FS[1] or IFSR.FS[1] is UNKNOWN when reporting a synchronous External abort, or a synchronous parity or ECC error, on the stage 2 translation.
- In all other cases the DFSR or IFSR uses the format associated with the Short-descriptor translation table format, as described in PL1 fault reporting with the Short-descriptor translation table format.

## G5.12.3.2 PL1 fault reporting with the Short-descriptor translation table format

This subsection describes the fault reporting for a fault taken to a PL1 when address translation is using the Short-descriptor translation table format.

On taking an exception, bit[9] of the FSR is RAZ, or set to 0, if the PE is using this FSR format.

An FSR encodes the fault in a 5-bit FS field, that comprises FSR[10, 3:0]. Table G5-26 shows the encoding of that field. Summary of register updates on faults taken to PL1 modes shows:

- Whether the corresponding FAR is updated on the fault. That is:
- -For a fault reported in the IFSR, whether the IFAR holds a valid address.
- -For a fault reported in the DFSR, whether the DFAR holds a valid address.
- For faults that update DFSR, whether DFSR.Domain is valid.
- FS values not shown in the table are reserved.
- FS values shown as DFSR only are reserved for the IFSR.

When reading Table G5-26:

## Table G5-26 FSR encodings when using the Short-description translation table format

| FS            | Source                                                           |                                         | Notes                               |
|---------------|------------------------------------------------------------------|-----------------------------------------|-------------------------------------|
| 00001         | Alignment fault.                                                 | Alignment fault.                        | DFSR only. Fault on initial lookup. |
| 00100         | Fault on instruction cache maintenance.                          | Fault on instruction cache maintenance. | DFSR only.                          |
| 01100 01110   | Synchronous External abort on translation table walk a, b .      | Level 1 Level 2                         | -                                   |
| 11100 11110   | Synchronous parity or ECC error on translation table walk a, b . | Level 1 Level 2                         | -                                   |
| 00101 00111   | Translation fault a .                                            | Level 1 Level 2                         | MMUfault.                           |
| 00011 c 00110 | Access flag fault a .                                            | Level 1 Level 2                         | MMUfault.                           |
| 01001 01011   | Domain fault a .                                                 | Level 1 Level 2                         | MMUfault.                           |

| FS          | Source                                                          | Notes                          |
|-------------|-----------------------------------------------------------------|--------------------------------|
| 01101 01111 | Permission fault a .                                            | MMUfault.                      |
| 00010       | Debug exception.                                                | See AArch32 Self-hosted Debug. |
| 01000       | Synchronous External abort.                                     | -                              |
| 10000       | TLB conflict abort.                                             | See TLB conflict aborts.       |
| 10100       | IMPLEMENTATION DEFINED.                                         | Lockdown.                      |
| 10101       | IMPLEMENTATION DEFINED.                                         | Unsupported Exclusive access.  |
| 11001       | Synchronous parity or ECC error on memory access.               | -                              |
| 10110       | SError exception d .                                            | DFSR only.                     |
| 11000       | SError exception d from a parity or ECC error on memory access. | DFSR only.                     |

a. See The level associated with MMU faults on a Short-descriptor translation table lookup.

b. FS[1] is UNKNOWN if the reported error is from a stage 2 translation.

- c. Previously, this encoding was a deprecated encoding for Alignment fault. The extensive changes in the memory model in VMSAv8-32 mean there should be no possibility of confusing the new use of this encoding with its previous use

d. Including asynchronous External abort on a data access, a translation table walk, or an instruction fetch.

## G5.12.3.2.1 The level associated with MMU faults on a Short-descriptor translation table lookup

The lookup level associated with a fault is:

- For a fault generated on a translation table walk, the lookup level of the walk being performed.
- For a Translation fault, the lookup level of the translation table that gave the fault. If a fault occurs because a stage of address translation is disabled, or because the input address is outside the range specified by the appropriate base address register or registers, the fault is reported as a level 1 fault.
- For an Access flag fault, Permission fault, or Domain fault, the lookup level of the final level of translation table accessed for the translation. That is, the lookup level of the translation table that returned a Supersection, Section, or Page descriptor.

Also see Synchronous External abort errors from address translation caching structures.

## G5.12.3.2.2 The Domain field in the DFSR

The DFSR includes a Domain field. This is inherited from previous versions of the VMSA. The IFSR does not include a Domain field. Summary of register updates on faults taken to PL1 modes describes when DFSR.Domain is valid.

Arm deprecates any use of the Domain field in the DFSR. The Long-descriptor translation table format does not support a Domain field, and future versions of the Arm architecture might not support a Domain field in the Short-descriptor translation table format. Arm strongly recommends that new software does not use this field.

For both Data Abort exceptions and Prefetch Abort exceptions, software can find the domain information by performing a translation table read for the faulting address and extracting the Domain field from the translation table entry.

## G5.12.3.3 PL1 fault reporting with the Long-descriptor translation table format

This subsection describes the fault reporting for a fault taken to a PL1mode when address translation is using the Long-descriptor translation table format.

When the PE takes an exception, bit[9] of the FSR is set to 1 if the PE is using this FSR format.

The FSRs encode the fault in a 6-bit STATUS field, that comprises FSR[5:0]. Table G5-27 shows the encoding of that field. In addition:

- For a fault taken to a PL1 mode, Summary of register updates on faults taken to PL1 modes shows whether the corresponding FAR is updated on the fault. That is:
- -For a fault reported in the IFSR, whether the IFAR holds a valid address.

- -For a fault reported in the DFSR, whether the DFAR holds a valid address.
- For a fault taken to the Hyp mode, Summary of register updates on exceptions taken to Hyp mode shows what registers are updated on the fault.

## Table G5-27 FSR encodings when using the Long-descriptor translation table format

| STATUS a   | Source                                                                                                 | Notes                                                                                  |
|------------|--------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| 0000LL     | Address size fault. LL bits indicate level b .                                                         | MMUfault.                                                                              |
| 0001LL     | Translation fault. LL bits indicate level b .                                                          | MMUfault.                                                                              |
| 0010LL     | Access flag fault. LL bits indicate level b .                                                          | MMUfault.                                                                              |
| 0011LL     | Permission fault. LL bits indicate level b .                                                           | MMUfault.                                                                              |
| 010000     | Synchronous External abort.                                                                            | -                                                                                      |
| 011000     | Synchronous parity or ECC error on memory access.                                                      | -                                                                                      |
| 010001     | SError exception c .                                                                                   | DFSR only.                                                                             |
| 011001     | SError exception c from a parity or ECC error on memory access.                                        | DFSR only.                                                                             |
| 0101LL     | Synchronous External abort on translation table walk. LL bits indicate level b .                       | -                                                                                      |
| 0111LL     | Synchronous parity or ECC error on memory access on translation table walk. LL bits indicate level b . | -                                                                                      |
| 100001     | Alignment fault.                                                                                       | Fault on initial lookup.                                                               |
| 100010     | Debug exception.                                                                                       | See AArch32 Self-hosted Debug.                                                         |
| 110000     | TLB conflict abort.                                                                                    | See TLB conflict aborts.                                                               |
| 110100     | IMPLEMENTATION DEFINED.                                                                                | Lockdown, DFSR only.                                                                   |
| 110101     | IMPLEMENTATION DEFINED.                                                                                | Unsupported Exclusive access.                                                          |
| 1111LL     | Domain fault. LL bits indicate level b .                                                               | MMUfault. 64-bit PAR only, level 1 or level only. Never used in DFSR, IFSR, or HSR d . |

b. See The level associated with MMU faults on a Long-descriptor translation table lookup.

- c. Including asynchronous External abort on a data access, a translation table walk, or an instruction fetch.

d. A Domain fault can be reported using the Long-descriptor STATUS encodings only as a result of a fault on an address translation instruction. For more information, see MMU fault on an address translation instruction.

## G5.12.3.3.1 The level associated with MMU faults on a Long-descriptor translation table lookup

For MMU faults, Table G5-28 shows how the LL bits in the xFSR.STATUS field encode the lookup level associated with the fault.

## Table G5-28 Use of LL bits to encode the lookup level at which the fault occurred

|   LL bits | Meaning                                                                             |
|-----------|-------------------------------------------------------------------------------------|
|        00 | Address size fault Address size fault in TTBR0 or TTBR1. All other faults Reserved. |

|   LL bits | Meaning                                                                     |
|-----------|-----------------------------------------------------------------------------|
|        01 | Level 1.                                                                    |
|        10 | Level 2.                                                                    |
|        11 | Level 3. When xFSR.STATUS indicates a Domain fault, this value is reserved. |

The lookup level associated with a fault is:

- For a fault generated on a translation table walk, the lookup level of the walk being performed.
- For a Translation fault, the lookup level of the translation table that gave the fault. If a fault occurs because a stage of address translation is disabled, or because the input address is outside the range specified by the appropriate base address register or registers, the fault is reported as a level 1 fault.
- For an Access flag fault, the lookup level of the translation table that gave the fault.
- For a Permission fault, including a Permission fault caused by hierarchical permissions, the lookup level of the final level of translation table accessed for the translation. That is, the lookup level of the translation table that returned a Block or Page descriptor.

Also see Synchronous External abort errors from address translation caching structures.

## G5.12.3.4 Reserved encoding in the IFSR and DFSR encodings tables

With both the Short-descriptor and the Long-descriptor FSR format, the fault encodings reserve a single encoding for Cache and TLB lockdown faults. The details of these faults and any associated subsidiary registers are IMPLEMENTATION DEFINED.

## G5.12.4 Summary of register updates on faults taken to PL1 modes

For faults that generate exceptions that are taken to a PL1 mode, Table G5-29 shows the registers affected by each fault. In this table:

- Yes indicates that the register is updated.
- UNK indicates that the fault makes the register value UNKNOWN.
- Anull entry, -, indicates that the fault does not affect the register.

For faults that update the DFSR using the Short-descriptor format FSR encodings, Table G5-30 shows whether DFSR.Domain is valid.

## Table G5-29 Effect of a fault taken to a PL1 mode on the reporting registers

| Fault                                                     | IFSR   | IFAR      | DFSR   | DFAR   |
|-----------------------------------------------------------|--------|-----------|--------|--------|
| Faults reported as Prefetch Abort exceptions:             |        |           |        |        |
| MMUfault, always synchronous                              | Yes    | Yes       | -      | -      |
| Synchronous External abort on translation table walk      | Yes    | Yes       | -      | -      |
| Synchronous parity or ECC error on translation table walk | Yes    | Yes       | -      | -      |
| Synchronous External abort                                | Yes    | IMP DEF a | -      | -      |
| Synchronous parity or ECC error on memory access          | Yes    | Yes       | -      | -      |
| TLB conflict abort                                        | Yes    | Yes       | -      | -      |
| Fault reported as Data Abort exception:                   |        |           |        |        |

| Fault                                                                                          | IFSR                                                                                          |     | IFAR   | DFSR   | DFAR      |
|------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|-----|--------|--------|-----------|
| Alignment fault, always synchronous                                                            |                                                                                               | -   | -      | Yes    | Yes       |
| MMUfault, always synchronous                                                                   |                                                                                               | -   | -      | Yes    | Yes       |
| Fault on instruction cache maintenance, when using Long-descriptor translation table format b  | Fault on instruction cache maintenance, when using Long-descriptor translation table format b | UNK | -      | Yes    | Yes       |
| Fault on instruction cache maintenance, when using Short descriptor translation table format c | either                                                                                        | Yes | -      | Yes    | Yes       |
| Fault on instruction cache maintenance, when using Short descriptor translation table format c | or                                                                                            | UNK | -      | Yes    | Yes       |
| Synchronous External abort on translation table walk                                           |                                                                                               | -   | -      | Yes    | Yes       |
| Synchronous parity or ECC error on translation table walk                                      |                                                                                               | -   | -      | Yes    | Yes       |
| Synchronous External abort                                                                     |                                                                                               | -   | -      | Yes    | IMP DEF a |
| Synchronous parity or ECC error on memory access                                               |                                                                                               | -   | -      | Yes    | Yes       |
| SError exception                                                                               |                                                                                               | -   | -      | Yes    | UNK       |
| SError exception from a parity or ECC error on memory access                                   |                                                                                               | -   | -      | Yes    | UNK       |
| TLB conflict abort                                                                             |                                                                                               | -   | -      | Yes    | Yes       |
| Debug exceptions:                                                                              |                                                                                               |     |        |        |           |
| Breakpoint, Breakpoint Instruction, or Vector Catch d                                          |                                                                                               | Yes | UNK    | -      | -         |
| Watchpoint e                                                                                   |                                                                                               | -   | -      | Yes    | Yes       |

For those faults for which Table G5-29 shows that the DFSR is updated, if the fault is reported using the Short-descriptor FSR encodings, Table G5-30 shows whether DFSR.Domain is valid. In this table, UNK indicates that the fault makes DFSR.Domain UNKNOWN.

Table G5-30 Validity of Domain field on faults that update the DFSR when using the Short-descriptor encodings

| DFSR.FS       | Source                                                    | DFSR.Domain                                        | Notes    |
|---------------|-----------------------------------------------------------|----------------------------------------------------|----------|
| 00001         | Alignment fault UNK                                       | Alignment fault UNK                                | -        |
| 00100         | Fault on instruction cache maintenance instruction        | Fault on instruction cache maintenance instruction | UNK -    |
| 01100 01110   | Synchronous External abort on translation table walk      | Level 1 Level 2 UNK Valid                          | -        |
| 11100 11110   | Synchronous parity or ECC error on translation table walk | Level 1 Level 2 UNK Valid                          | -        |
| 00101 00111   | Translation fault                                         | Level 1 Level 2 UNK Valid                          | MMUfault |
| 00011 a 00110 | Access flag fault                                         | Level 1 Level 2 UNK Valid                          | MMUfault |
| 01001 01011   | Domain fault                                              | Level 1 Level 2 Valid Valid                        | MMUfault |

| DFSR.FS     | Source                                                         | DFSR.Domain   | Notes    |
|-------------|----------------------------------------------------------------|---------------|----------|
| 01101 01111 | Permission fault                                               | UNK UNK       | MMUfault |
| 01000       | Synchronous External abort                                     | UNK           | -        |
| 10000       | TLB conflict abort                                             | UNK           | -        |
| 11001       | Synchronous parity or ECC error on memory access               | UNK           | -        |
| 10110       | SError exception b                                             | UNK           | -        |
| 11000       | SError exception b from a parity or ECC error on memory access | UNK           | -        |
| 00010       | Watchpoint                                                     | UNK           |          |

## G5.12.5 Reporting exceptions taken to Hyp mode

Hyp mode is the Non-secure EL2 mode. It is entered by taking an exception to Hyp mode.

Note

Software executing in Monitor mode, or at EL3 when EL3 is using AArch64, can perform an exception return to Hyp mode. This means Hyp mode can be entered either by taking an exception, or by a permitted exception return.

When EL2 is using AArch32, the following exceptions are taken to Hyp mode:

- SError exceptions, IRQ exceptions, and FIQ exceptions, from Non-secure PL1 and EL0 modes, if not routed to Secure Monitor mode, and if configured by the AMO, FMO or IMO bits. For more information, see Asynchronous exception routing controls.
- When HCR.TGE is set to 1, all exceptions that would be routed to Non-secure PL1 modes. For more information, see Routing exceptions from Non-secure EL0 to EL2.
- When HDCR.TDE is set to 1, any debug exception that would otherwise be taken to a Non-secure PL1 mode, see Routing debug exceptions to EL2 using AArch32.
- The privilege rules for taking exceptions mean that any exception taken from Hyp mode, if not routed to EL3, must be taken to Hyp mode.
- An abort that Routing of aborts taken to AArch32 state identifies as taken to Hyp mode.
- supported only as part of EL2.
- Hypervisor Call exceptions, and Hyp Trap exceptions, are always taken to Hyp mode. These exceptions are When EL2 is implemented, various operations from Non-secure PL1 and EL0 modes can be trapped to Hyp mode, using the Hyp Trap exception. For more information, see EL2 configurable controls.

Synchronous exceptions taken to Hyp mode provide syndrome information in the HSR.

On an abort exception taken to Hyp mode, the syndrome information in the HSR includes the Fault status code otherwise provided by the fault status register, and extends the fault reporting compared to that available for an exception taken to a PL1 mode.

In addition, for a Debug exception taken to Hyp mode, DBGDSCRint.MOE or DBGDSCRext.MOE shows what caused the Debug exception. This field is valid regardless of whether the Debug exception was taken from Hyp mode or from another Non-secure mode.

For more information, see the following subsections:

- Registers used for reporting exceptions taken to Hyp mode.
- Memory fault reporting in Hyp mode.
- Use of the HSR

## G5.12.5.1 Registers used for reporting exceptions taken to Hyp mode

The following registers are used for reporting exceptions taken to Hyp mode:

- The HSR holds syndrome information for the exception.
- The HDFAR holds the VA associated with a Data Abort exception.
- The HIFAR holds the VA associated with a Prefetch Abort exception.
- The HPFAR holds bits[39:12] of the IPA associated with some aborts on stage 2 address translations.

In addition, if implemented, the optional HADFSR and HAIFSR can provide additional fault information, see Hyp Auxiliary Fault Syndrome Registers.

## G5.12.5.1.1 Hyp Auxiliary Fault Syndrome Registers

EL2 also defines encodings for the following Hyp Auxiliary Fault Syndrome Registers:

- The Hyp Auxiliary Data Fault Syndrome Register, HADFSR.
- The Hyp Auxiliary Instruction Fault Syndrome Register, HAIFSR.

An implementation can use these registers to return additional fault status information for aborts taken to Hyp mode. They are the Hyp mode equivalents of the registers described in Auxiliary Fault Status Registers. An example use of these registers is to return more information for diagnosing parity or ECC errors.

The architectural requirements for the HADFSR and HAIFSR are:

- The position of these registers is architecturally-defined, but the content and use of the registers is IMPLEMENTATION DEFINED.
- An implementation with no requirement for additional fault reporting can implement these registers as RES0, but the architecture does not require it to do so.

## G5.12.5.2 Memory fault reporting in Hyp mode

Prefetch Abort and Data Abort exceptions taken to Hyp mode report memory faults. For these aborts, the HSR contains the following fault status information:

- The HSR.EC field indicates the type of abort, as Table G5-31 shows.
- The HSR.ISS field holds more information about the abort. In particular:
- -Bits[5:0] of this field hold the STATUS field for the abort, using the encodings defined in PL1 fault reporting with the Long-descriptor translation table format.
- -Other subfields of the ISS give more information about the exception, equivalent to the information returned in the FSR for a memory fault reported at PL1.

See the descriptions of the ISS fields for the memory faults, referenced from the Syndrome description column of Table G5-31, for information about the returned fault information.

## Table G5-31 HSR.EC encodings for aborts taken to Hyp mode

| HSR.EC   | Abort                                                | Syndrome description                             |
|----------|------------------------------------------------------|--------------------------------------------------|
| 0x20     | Prefetch Abort taken from Non-secure PL1 or EL0 mode | ISS encoding for exception from a Prefetch Abort |
| 0x21     | Prefetch Abort taken from Hyp mode                   |                                                  |
| 0x24     | Data Abort taken from Non-secure PL1 or EL0 mode     | ISS encoding for exception from a Data Abort     |
| 0x25     | Data Abort taken from Hyp mode                       |                                                  |

For more information, see Use of the HSR.

APrefetch Abort exception is taken synchronously with the instruction that the abort is reported on. This means:

- If the PE attempts to execute the instruction a Prefetch Abort exception is generated.
- If an instruction fetch is issued but the PE does not attempt to execute the prefetched instruction, no Prefetch Abort exception is generated for that instruction. For example, if the execution flow branches round a prefetched instruction that would abort if the PE attempted to execute it, no Prefetch Abort exception is generated.

## G5.12.5.2.1 Register updates on exception reporting in Hyp mode

The use of the HSR, and of the other registers listed in Registers used for reporting exceptions taken to Hyp mode, depends on the cause of the Abort. In reporting these faults, in general:

- If the fault generates a synchronous Data Abort exception, the HDFAR holds the associated V A, but see Fault address reporting on synchronous External aborts for a permitted exception to this requirement.
- If the fault generates a Prefetch Abort exception, the HIFAR holds the associated V A, but see Fault address reporting on synchronous External aborts for a permitted exception to this requirement.
- In the following cases, the HPFAR holds the faulting IPA:
- -ATranslation or Access flag fault on a stage 2 translation.
- -ATranslation, Access flag, or Permission fault on the stage 2 translation of an address accessed in a stage 1 translation table walk.
- -Astage 2 Address size fault.

In all other cases, the HPFAR is UNKNOWN.

- On a Data Abort exception that is taken to Hyp mode, the HIFAR is UNKNOWN.
- On a Prefetch Abort exception that is taken to Hyp mode, the HDFAR is UNKNOWN.

In addition, the reporting of particular aborts is as follows:

## Abort on the stage 1 translation for a memory access from Hyp mode

The HDFAR or HIFAR holds the VA that caused the fault. The STATUS subfield of HSR.ISS indicates the type of fault, Translation, Address size, Access flag, or Permission. The HPFAR is UNKNOWN.

## Abort on the stage 2 translation for a memory access from a Non-secure PL1 or EL0 mode

This includes aborts on the stage 2 translation of a memory access made as part of a translation table walk for a stage 1 translation. The HDFAR or HIFAR holds the V A that caused the fault. The STATUS subfield of HSR.ISS indicates the type of fault, Translation, Address size, Access flag, or Permission.

For any Access flag fault or Translation fault, and also for any Permission fault on the stage 2 translation of a memory access made as part of a translation table walk for a stage 1 translation, the HPFAR holds the IPA that caused the fault. Otherwise, the HPFAR is UNKNOWN.

## Abort caused by a synchronous External abort, or synchronous parity or ECC error, and taken to Hyp mode

The HDFAR or HIFAR holds the VA that caused the fault, but see Fault address reporting on synchronous External aborts for a permitted exception to this requirement. The HPFAR is UNKNOWN.

## Data Abort caused by a Watchpoint exception and routed to Hyp mode because HDCR.TDE is set to 1

When HDCR.TDE is set to 1, a Watchpoint exception generated in a Non-secure PL1 or EL0 mode, that would otherwise generate a Data Abort exception, is routed to Hyp mode and generates a Hyp Trap exception.

HDFAR is set to the address that generated the watchpoint.

Note

ELR\_hyp indicates the address of the instruction that triggered the watchpoint.

Awatchpointed address can be any byte-aligned address. The address reported in HDFAR might not be the watchpointed address, and, for a watchpoint due to an operation other than a Data Cache maintenance instruction, can be any address between and including:

- The lowest address accessed by the instruction that triggered the watchpoint.
- The highest watchpointed address accessed by that instruction.

If multiple watchpoints are set in this range, there is no guarantee of which watchpoint is generated.

Note

In particular, there is no guarantee of generating the watchpoint with the lowest address in the range.

The address must also be within a naturally-aligned block of memory of an IMPLEMENTATION DEFINED power-of-two size, containing a watchpoint address accessed by that location.

Note

The IMPLEMENTATION DEFINED power-of-two size must be no larger than the block size of the AArch64 DCZVAoperation.

See also Watchpoint exceptions.

In all cases, HPFAR is UNKNOWN.

## Prefetch Abort caused by a Breakpoint Instruction exception and taken to Hyp mode

This abort is generated if a BKPT instruction is executed in Hyp mode. The abort leaves the HIFAR and HPFAR UNKNOWN.

See also Breakpoint Instruction exceptions.

## Prefetch Abort caused by a Breakpoint Instruction, Breakpoint, or Vector Catch exception, and routed to Hyp mode because HDCR.TDE is set to 1

When HDCR.TDE is set to 1, a debug exception, generated in a Non-secure PL1 or EL0 mode, that would otherwise generate a Prefetch Abort exception, is routed to Hyp mode and generates a Hyp Trap exception.

The abort leaves the HIFAR and HPFAR UNKNOWN. This is identical to the reporting of a Prefetch Abort exception caused by a Debug exception on a BKPT instruction that is executed in Hyp mode.

Note

The difference between these two cases is:

- The Debug exception on a BKPT instruction executed in Hyp mode generates a Prefetch Abort exception, taken to Hyp mode, and reported in the HSR using EC value 0x21 .
- Aborts generated because HDCR.TDE is set to 1 generate a Hyp Trap exception, and are reported in the HSR using EC value 0x20 .

## G5.12.5.3 Use of the HSR

The HSR holds syndrome information for any synchronous exception taken to Hyp mode. Compared with the reporting of exceptions taken to PL1 modes, the HSR:

- Always provides details of the fault. The DFSR and IFSR are not used.
- Provides more extensive information, for a wider range of exceptions.

Note

IRQ and FIQ exceptions taken to Hyp mode do not report any syndrome information in the HSR.

This section summarizes the general form of the HSR register, to show how it encodes exception syndrome information, see the register description for more information. The register comprises:

- A6-bit Exception class field, EC, that indicates the cause of the exception.
- An instruction length bit, IL. When an exception is caused by trapping an instruction to Hyp mode, this bit indicates the length of the trapped instruction, as follows:
- 0 16-bit instruction trapped.
- 1 32-bit instruction trapped.

In other cases the IL field is not valid and is RES1.

- An instruction specific syndrome field, ISS. Architecturally, this field could be defined independently for each defined Exception class (EC), but in practice several ISS formats are common to more than one EC.

The format of the HSR depends on the value of the EC field, as follows:

0b000000 &lt; EC ≤ 0b001100

The ISS part of the returned value includes the CV and COND fields described in Encoding of ISS[24:20] when 0b000000 &lt; EC ≤ 0b001100 . Figure G5-17 shows the HSR format in this case.

<!-- image -->

Figure G5-17 HSR format when the ISS includes CV and COND fields

<!-- image -->

There are no generic fields within the ISS. Figure G5-18 shows the HSR format in this case.

Figure G5-18 HSR format when the ISS does not include a COND field

<!-- image -->

## G5.12.5.3.1 Encoding of ISS[24:20] when 0b000000 &lt; EC ≤ 0b001100

For EC values that are nonzero and less than or equal to 0b001100 , ISS[24:20] provides the Condition code field for the trapped instruction, together with a valid flag for this field. The encoding of this part of the ISS field is:

CV, ISS[24] Condition code valid. Possible values of this bit are:

0 The COND field is not valid.

1 The COND field is valid.

## COND, ISS[23:20]

The Condition code for the trapped instruction. This field is valid only when CV is set to 1.

If CV is set to 0, this field is RES0.

The full descriptions of the HSR.ISS formats give more information about the CV field.

Note

In some circumstances, it is IMPLEMENTATION DEFINED whether a conditional instruction that fails its Condition code check generates an Undefined Instruction exception, see Conditional execution of undefined instructions.

## G5.12.5.3.2 HSR exception classes

Table G5-32 shows the encoding of the HSR exception class field, EC. Values of EC not shown in the table are reserved. For each EC value, the table references a subsection of the description of the HSR that describes the associated ISS format and gives information about the cause of the exception, for example the configuration required to enable the associated trap.

| EC       | Exception class                                                                        | ISS description, or notes                                                                                         |
|----------|----------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| 0b000000 | Unknown reason                                                                         | ISS encoding for exceptions with an unknown reason.                                                               |
| 0b000001 | Trapped WFI or WFE instruction                                                         | ISS encoding for exception from a WFI or WFEinstruction.                                                          |
| 0b000011 | Trapped MCR or MRC access with ( coproc == 0b1111 )                                    | ISS encoding for exception from an MCRor MRCaccess.                                                               |
| 0b000100 | Trapped MCRR or MRRC access with ( coproc == 0b1111 )                                  | ISS encoding for exception from an MCRRor MRRCaccess.                                                             |
| 0b000101 | Trapped MCR or MRC access with ( coproc == 0b1110 )                                    | ISS encoding for exception from an MCRor MRCaccess.                                                               |
| 0b000110 | Trapped LDC or STC access                                                              | ISS encoding for exception from an LDCor STC instruction.                                                         |
| 0b000111 | Advanced SIMD or floating-point functionality trapped by a HCPTR.{TASE, TCP10} control | ISS encoding for exception from an access to SIMD or floating-point functionality, resulting from HCPTR.          |
| 0b001000 | Trapped VMRS access, from ID group traps, that is not reported using EC 0b000111       | ISS encoding for exception from an MCRor MRCaccess. This trap is not taken if the HCPTR settings trap the access. |
| 0b001100 | Trapped MRRC access with ( coproc == 0b1110 )                                          | ISS encoding for exception from an MCRRor MRRCaccess.                                                             |
| 0b001110 | Illegal exception return to AArch32 state                                              | ISS encoding for exception from an Illegal state or PC alignment fault.                                           |
| 0b010001 | Exception on SVC execution in AArch32 state routed to EL2                              | ISS encoding for exception from HVCor SVC instruction execution.                                                  |
| 0b010010 | HVC instruction execution in AArch32 state, when HVC is not disabled                   |                                                                                                                   |
| 0b010011 | Trapped execution of SMC instruction in AArch32 state                                  | ISS encoding for exception from SMCinstruction execution.                                                         |
| 0b100000 | Prefetch Abort from a lower Exception level                                            | ISS encoding for exception from a Prefetch Abort.                                                                 |
| 0b100001 | Prefetch Abort taken without a change in Exception level                               |                                                                                                                   |
| 0b100010 | PC alignment exception.                                                                | ISS encoding for exception from an Illegal state or PC alignment fault.                                           |
| 0b100100 | Data Abort from a lower Exception level                                                | ISS encoding for exception from a Data Abort.                                                                     |
| 0b100101 | Data Abort taken without a change in Exception level                                   |                                                                                                                   |

All EC encodings not shown in Table G5-31 are reserved by Arm.

## G5.12.6 Summary of register updates on exceptions taken to Hyp mode

For memory system faults that generate exceptions that are taken to Hyp mode, Table G5-33 shows the registers affected by each fault. In this table:

- Yes indicates that the register is updated.
- UNK indicates that the fault makes the register value UNKNOWN.
- Anull entry, -, indicates that the fault does not affect the register.

Note

For a list of the MMU faults, see Types of MMU faults.

Table G5-33 Effect of an exception taken to Hyp mode on the reporting registers

| Fault                                                                                            | HSR                                                                                              | HIFAR                                                                                            | HDFAR                                                                                            | HPFAR                                                                                            |
|--------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| Faults reported as Prefetch Abort exceptions:                                                    |                                                                                                  |                                                                                                  |                                                                                                  |                                                                                                  |
| MMUfault a at stage 1.                                                                           | Yes                                                                                              | Yes                                                                                              | UNK                                                                                              | UNK                                                                                              |
| Translation or Access flag MMUfault a at stage 2.                                                | Yes                                                                                              | Yes                                                                                              | UNK                                                                                              | Yes                                                                                              |
| Other b MMUfault a at stage 2.                                                                   | Yes                                                                                              | Yes                                                                                              | UNK                                                                                              | UNK                                                                                              |
| Stage 2 MMUfault a on a stage 1 translation.                                                     | Yes                                                                                              | Yes                                                                                              | UNK                                                                                              | Yes                                                                                              |
| Synchronous External abort on translation table walk.                                            | Yes                                                                                              | Yes                                                                                              | UNK                                                                                              | UNK                                                                                              |
| Synchronous parity or ECC error on translation table walk.                                       | Yes                                                                                              | Yes                                                                                              | UNK                                                                                              | UNK                                                                                              |
| Synchronous External abort.                                                                      | Yes                                                                                              | IMP DEF c                                                                                        | UNK                                                                                              | UNK                                                                                              |
| Synchronous parity or ECC error on memory access.                                                | Yes                                                                                              | Yes                                                                                              | UNK                                                                                              | UNK                                                                                              |
| Fault reported as Data Abort exception:                                                          |                                                                                                  |                                                                                                  |                                                                                                  |                                                                                                  |
| MMUfault a at stage 1.                                                                           | Yes                                                                                              | UNK                                                                                              | Yes                                                                                              | UNK                                                                                              |
| Translation or Access flag MMUfault a at stage 2.                                                | Yes                                                                                              | UNK                                                                                              | Yes                                                                                              | Yes                                                                                              |
| Other b MMUfault a at stage 2.                                                                   | Yes                                                                                              | UNK                                                                                              | Yes                                                                                              | UNK                                                                                              |
| Stage 2 MMUfault a on a stage 1 translation.                                                     | Yes                                                                                              | UNK                                                                                              | Yes                                                                                              | Yes                                                                                              |
| Synchronous External abort on translation table walk.                                            | Yes                                                                                              | UNK                                                                                              | Yes                                                                                              | UNK                                                                                              |
| Synchronous parity or ECC error on translation table walk.                                       | Yes                                                                                              | UNK                                                                                              | Yes                                                                                              | UNK                                                                                              |
| Synchronous External abort.                                                                      | Yes                                                                                              | UNK                                                                                              | IMP DEF c                                                                                        | UNK                                                                                              |
| Synchronous parity or ECC error on memory access.                                                | Yes                                                                                              | UNK                                                                                              | Yes                                                                                              | UNK                                                                                              |
| SError exception.                                                                                | Yes                                                                                              | UNK                                                                                              | UNK                                                                                              | UNK                                                                                              |
| SError exception from a parity or ECC error on memory access.                                    | Yes                                                                                              | UNK                                                                                              | UNK                                                                                              | UNK                                                                                              |
| Debug exception:                                                                                 |                                                                                                  |                                                                                                  |                                                                                                  |                                                                                                  |
| Breakpoint Instruction d , generates a Prefetch Abort exception.                                 | Yes                                                                                              | UNK                                                                                              | -                                                                                                | UNK                                                                                              |
| Debug exception routed to Hyp mode because HDCR.TDE is set to 1. Generates a Hyp Trap exception. | Debug exception routed to Hyp mode because HDCR.TDE is set to 1. Generates a Hyp Trap exception. | Debug exception routed to Hyp mode because HDCR.TDE is set to 1. Generates a Hyp Trap exception. | Debug exception routed to Hyp mode because HDCR.TDE is set to 1. Generates a Hyp Trap exception. | Debug exception routed to Hyp mode because HDCR.TDE is set to 1. Generates a Hyp Trap exception. |
| Breakpoint Instruction or Vector Catch.                                                          | Yes                                                                                              | UNK                                                                                              | -                                                                                                | UNK                                                                                              |
| Watchpoint.                                                                                      | Yes                                                                                              | -                                                                                                | Yes                                                                                              | UNK                                                                                              |

Note

Unlike Table G5-29, the Hyp mode fault reporting table does not include an entry for a fault on an instruction cache maintenance instruction. That is because, when the fault is taken to Hyp mode, the reporting indicates the cause of the fault, for example a Translation fault, and ISS.CM is set to 1 to indicate that the fault was on a cache maintenance instruction, see ISS encoding for exception from a Data Abort.

## G5.12.6.1 Classification of MMU faults taken to Hyp mode

This subsection gives more information about the MMU faults shown in Table G5-33.

Note

All MMU faults are synchronous.

The table uses the following descriptions for MMU faults taken to Hyp mode:

## MMUfault at stage 1

This is an MMU fault generated on a stage 1 translation performed in the Non-secure EL2 translation regime.

## MMUfault at stage 2

This is an MMU fault generated on a stage 2 translation performed in the Non-secure PL1&amp;0 translation regime.

As the table shows, for the faults in this group:

- Translation and Access flag faults update the HPFAR.
- Permission faults leave the HPFAR UNKNOWN.

## MMUstage 2 fault on a stage 1 translation

This is an MMU fault generated on the stage 2 translation of an address accessed in a stage 1 translation table walk performed in the Non-secure PL1&amp;0 translation regime. For more information about these faults see Stage 2 fault on a stage 1 translation table walk.

Figure G5-1 shows the different translation regimes and associated stages of translation.