## G2.10 Vector Catch exceptions

Arm deprecates the use of vector catch.

This section describes Vector Catch exceptions in stage 1 of an AArch32 translation regime.

The PE is using an AArch32 translation regime when it is executing either:

- At EL1 or higher in an Exception level that is using AArch32.
- At EL0 using AArch32 when EL1 is using AArch32.

Note

Vector Catch exceptions cannot be generated when the PE is using an AArch64 translation regime.

This section contains the following subsections:

- About Vector Catch exceptions.
- Exception vectors that Vector Catch exceptions can be enabled for.
- Generation of Vector Catch exceptions.
- Usage constraints.
- Exception syndrome information and preferred return address for a Vector Catch exception.
- Pseudocode description of Vector Catch exceptions.

## G2.10.1 About Vector Catch exceptions

Whenever the PE takes an exception, execution is forced to an address that is the exception vector for that exception. Vector catch permits a debugger to trap exceptions based on the exception vector, or based on the exception type associated with the exception vector, as follows:

- If the address-matching form of vector catch is implemented, the debugger can trap exceptions based on the exception vector.
- If the exception-trapping form of vector catch is implemented, the debugger can trap exceptions based on the exception type associated with the exception vector.

The architecture supports only these two forms of vector catch. Only one form can be implemented, and which is implemented is IMPLEMENTATION DEFINED. The DBGDEVID indicates which form is implemented.

Regardless of the form of vector catch implemented, a debugger enables Vector Catch exceptions for exception vectors or types by programming the DBGVCR. This register contains vector catch enable bits . Each of these bits corresponds to a different vector. When a debugger sets a vector catch enable bit to 1, Vector Catch exceptions are enabled for the corresponding exception vector or type.

Note

EL2 using AArch64 or EL3 using AArch64 can enable Vector Catch exceptions for vectors by programming the DBGVCR32\_EL2. The DBGVCR32\_EL2 is architecturally mapped to the DBGVCR.

When Vector Catch exceptions are enabled for an exception vector, this is called an enabled vector catch . The set of exception vectors that Vector Catch exceptions are enabled for is called the enabled vector catch set .

If the form of vector catch implemented is the:

## Address-matching form:

The PE compares the virtual address of each instruction in the program flow with a subset of the enabled vector catch set.

If an address match occurs, a Vector Catch exception is generated when the instruction that caused the match is committed for execution.

## Exception-trapping form

Whenever the PE takes an exception, if the vector the exception is taken to is included in a subset of the enabled vector catch set, a Vector Catch exception is generated.

The Vector Catch exception is generated as part of entry to the exception, and must be taken before the PE either executes any instructions or takes any further exceptions.

The addresses that comprise the subset depend on whether EL3 is implemented and, for the:

- Address-matching form, the current Security state.
- Exception-trapping form, the Security state that the exception is handled in.

See Generation of Vector Catch exceptions.

Table G2-20 summarizes the differences between the address-matching and exception-trapping forms.

Table G2-20 Differences in behavior of the address-matching and exception-trapping forms of vector catch

| Address-matching                                                                                                                                                                                                                                                                                                                                                                                                                                               | Exception-trapping                                                                                                                                                                                                                                                                                                                                                                                                                 |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| An enabled vector catch generates a Vector Catch exception when an instruction that is fetched from the vector is committed for execution. This means that spurious Vector Catch exceptions might occur, where the Vector Catch exception does not result from an exception entry, but is instead caused by a branch to the vector. Abranch to the vector might occur, for example, on a return from a nested exception or when simulating an exception entry. | An enabled vector catch generates a Vector Catch exception immediately after the PE takes the exception that is associated with the vector. This means that Vector Catch exceptions always result from exception entry, and not from branches to exception vectors.                                                                                                                                                                |
| AVector Catch exception is generated as a result of an instruction fetch. This means that the Vector Catch exception has a priority relative to the other synchronous exceptions that result from an instruction fetch. Prioritization of Synchronous exceptions taken to AArch64 state describes this prioritization.                                                                                                                                         | AVector Catch exception is generated as a result of an exception entry. This means that the Vector Catch exception is part of the exception that caused the Vector Catch exception. Therefore, the Vector Catch exception has no priority associated with it. For this reason, Vector Catch exceptions are outside the scope of the prioritization that Prioritization of Synchronous exceptions taken to AArch64 state describes. |
| AVector Catch exception can be preempted by another exception. If this happens, the Vector Catch exception is generated again when the exception handler branches back to the vector.                                                                                                                                                                                                                                                                          | Vector Catch exceptions must be taken before other exceptions.                                                                                                                                                                                                                                                                                                                                                                     |
| AVector Catch exception can be generated as a result of an instruction fetch executed in any AArch32 mode except Hyp mode, including User mode.                                                                                                                                                                                                                                                                                                                | Because a Vector Catch exception is generated as the result of an exception entry, the Vector Catch exception is only generated when the PE is in the AArch32 exception handling mode.                                                                                                                                                                                                                                             |
| If HCR.TGE is 1, Vector Catch exceptions can be generated for User mode instruction fetches from Non-secure PL1 vectors.                                                                                                                                                                                                                                                                                                                                       | If HCR.TGE is 1, Vector Catch exceptions are never generated in Non-secure state, because: • Exceptions are routed away from Non-secure PL1 vectors, to PL2. • The architecture does not provide vector catch enable bits for the Hyp exception vectors.                                                                                                                                                                           |

Depending on the implementation, some vector catch enable bits in the DBGVCR might be RES0. For example, if EL3 is not implemented or is implemented but is using AArch64, Monitor mode is not implemented, and so the enable bits for exception vectors for exceptions taken to Monitor mode are RES0. See Exception vectors that Vector Catch exceptions can be enabled for for the vector catch enable bits that exist for different implementations.

The debug exception enable controls describes the enable controls for Vector Catch exceptions.

## G2.10.2 Exception vectors that Vector Catch exceptions can be enabled for

When the PE takes an exception, the exception vector is contained in a vector table at the Privilege level the exception is taken to.

Depending on the Security state and AArch32 mode the exception is taken to, when the exception is taken, the vector table used is the table that contains one of:

- Local exception vectors .
- Non-secure Local exception vectors .
- Secure Local exception vectors .
- Hyp exception vectors .
- Monitor exception vectors .

Table G2-21 shows which vector tables are implemented for different implementations. In the table:

- Adash, -, means that the Exception level is not implemented.
- 64 means that the Exception level is using AArch64.
- 32 means that the Exception level is using AArch32.

Table G2-21 Vector tables implemented for different implementations

| Implementation   | Implementation   |     |     | Vector table or tables implemented                                                                                    |
|------------------|------------------|-----|-----|-----------------------------------------------------------------------------------------------------------------------|
| EL0              | EL1              | EL2 | EL3 |                                                                                                                       |
| 32               | 32               | -   | -   | Local exception vectors.                                                                                              |
|                  |                  | 64  | -   | Non-secure Local exception vectors.                                                                                   |
|                  |                  | 32  | -   | Non-secure Local exception vectors. Hyp exception vectors.                                                            |
|                  |                  | -   | 64  | Secure Local exception vectors. Non-secure Local exception vectors.                                                   |
|                  |                  | -   | 32  | Secure Local exception vectors. Non-secure Local exception vectors. Monitor exception vectors.                        |
|                  |                  | 64  | 64  | Secure Local exception vectors. Non-secure Local exception vectors.                                                   |
|                  |                  | 32  | 64  | Secure Local exception vectors. Non-secure Local exception vectors. Hyp exception vectors.                            |
|                  |                  | 32  | 32  | Secure Local exception vectors. Non-secure Local exception vectors. Hyp exception vectors. Monitor exception vectors. |

For example, in an AArch32-only implementation that includes EL0, EL1, and EL3, when the PE takes an exception to Monitor mode, it uses the vector table containing Monitor exception vectors.

The tables that follow show the vectors that Vector Catch exceptions can be enabled for, and their corresponding vector catch enable bits in the DBGVCR:

- Table G2-22 shows the Local exception vectors, Secure Local exception vectors, and Non-secure Local exception vectors that Vector Catch exceptions can be enabled for.
- Table G2-23 shows the Monitor exception vectors that Vector Catch exceptions can be enabled for.

The architecture does not provide vector catch enable bits for the Hyp exception vectors.

Table G2-22 Local exception vectors, Secure Local exception vectors, and Non-secure Local exception vectors that Vector Catch exceptions can be enabled for

| Vector catch enable bit Local or Secure Local   | Non-secure Local exception   | Exception type        | Local exception vectors   | Local exception vectors   |
|-------------------------------------------------|------------------------------|-----------------------|---------------------------|---------------------------|
| exception vectors                               | vectors                      |                       | Normal. SCTLR.V is 0. a   | High. SCTLR.V is 1.       |
| SF                                              | NSF                          | FIQ interrupt         | VBAR+ 0x0000_001C         | 0xFFFF_001C               |
| SI                                              | NSI                          | IRQ interrupt         | VBAR+ 0x0000_0018         | 0xFFFF_0018               |
| SD                                              | NSD                          | Data Abort            | VBAR+ 0x0000_0010         | 0xFFFF_0010               |
| SP                                              | NSP                          | Prefetch Abort        | VBAR+ 0x0000_000C         | 0xFFFF_000C               |
| SS                                              | NSS                          | Supervisor Call       | VBAR+ 0x0000_0008         | 0xFFFF_0008               |
| SU                                              | NSU                          | Undefined Instruction | VBAR+ 0x0000_0004         | 0xFFFF_0004               |

Table G2-23 Monitor exception vectors that Vector Catch exceptions can be enabled for

| Vector catch enable bit   | Exception type      | Monitor exception vectors   |
|---------------------------|---------------------|-----------------------------|
| MF                        | FIQ interrupt       | MVBAR+ 0x0000_001C          |
| MI                        | IRQ interrupt       | MVBAR+ 0x0000_0018          |
| MD                        | Data Abort          | MVBAR+ 0x0000_0010          |
| MP                        | Prefetch Abort      | MVBAR+ 0x0000_000C          |
| MS                        | Secure Monitor Call | MVBAR+ 0x0000_0008          |

Note

There is no vector catch enable bit for Monitor trap exceptions.

## G2.10.3 Generation of Vector Catch exceptions

How Vector Catch exceptions are generated depends on which form is implemented:

- Address-matching form.
- Exception-trapping form.

## G2.10.3.1 Address-matching form

The PE compares the virtual address of each instruction in the program flow is with some or all of the addresses in the enabled vector catch set, as follows:

- If EL3 is not implemented, the enabled vector catch set contains only Local exception vectors. The PE compares the virtual address of each instruction in the program flow, including those executed at EL0, with all addresses in the enabled vector catch set.
- If EL3 is implemented, the enabled vector catch set might contain one or more of the following:
- -Monitor exception vectors, if EL3 is using AArch32.
- -Secure Local exception vectors.
- -Non-secure Local exception vectors.

In this case, Table G2-24 shows which addresses, in the enabled vector catch set, the virtual address of each instruction in the program flow is compared with.

## Table G2-24 Comparisons made if the implementation includes EL3

| EL3 is using   | For exceptions taken to: Secure PL1 modes                    | Non-secure PL1 modes               |
|----------------|--------------------------------------------------------------|------------------------------------|
| AArch64        | Secure Local exception vectors                               | Non-secure Local exception vectors |
| AArch32        | Secure Local exception vectors and Monitor exception vectors |                                    |

For example, for exceptions taken to a Secure PL1 mode when EL3 is using AArch64, the virtual address of each instruction in the program flow is compared with each Secure Local exception vector in the enabled vector catch set.

For each instruction in the program flow, the PE tests for any possible Vector Catch exceptions before executing the instruction. If a match occurs, a Vector Catch exception is generated when the instruction is committed for execution, regardless of all of the following:

- Whether the instruction passes its Condition code check.
- Whether the instruction is executed as part of exception entry.
- If EL2 is implemented, what HCR.{IMO, FMO, AMO} are set to.
- If EL3 is implemented, what SCR.{IRQ, FIQ, EA} are set to.

## G2.10.3.2 Exception-trapping form

When the PE takes an exception, it tests whether the exception is by branching to an exception vector in a subset of the enabled vector catch set, as follows:

- If EL3 is not implemented, the enabled vector catch set contains only Local exception vectors. The PE tests whether the exception is by branching to any address in the enabled vector catch set.
- If EL3 is implemented, the enabled vector catch set might contain one or more of the following:
- -Monitor exception vectors, if EL3 is using AArch32.
- -Secure Local exception vectors.
- -Non-secure Local exception vectors.

In this case, the PE tests whether the exception is by branching to a vector in one of the subsets that Table G2-25 shows. In the table, n/a means not applicable.

| EL3 is using   | For exceptions taken to:   | Other Secure PL1 modes         | Non-secure PL1 modes               |
|----------------|----------------------------|--------------------------------|------------------------------------|
| AArch64        | n/a                        | Secure Local exception vectors | Non-secure Local exception vectors |
| AArch32        | Monitor exception vectors  |                                |                                    |

For example, for an exception taken to a Secure PL1 mode when EL3 is using AArch64, the PE tests whether the exception is by branching to any of the Secure Local exception vectors in the enabled vector address set.

If the exception is by branching to a vector in the subset, a Vector Catch exception is generated as part of exception entry. That is, a Vector Catch exception is generated instead of the exception handler executing its first instruction.

## G2.10.4 Usage constraints

See the following subsections:

- Usage constraints that apply to both forms of vector catch.
- Usage constraints that apply only to the address-matching form.

## G2.10.4.1 Usage constraints that apply to both forms of vector catch

For Vector Catch exceptions enabled for either the Prefetch Abort exception vector or the Data Abort exception vector, if one of these exception types is taken to the Exception level that debug exceptions are targeting, behavior is CONSTRAINED UNPREDICTABLE. Either:

- Vector catch is ignored, therefore a Vector Catch exception is not generated.
- Vector catch generates a Prefetch Abort debug exception. For Vector Catch exceptions enabled for the Prefetch Abort exception vector, the PE might enter a recursive loop of Prefetch Abort exceptions causing Vector Catch exceptions and Vector Catch exceptions causing Prefetch Abort exceptions.

Note

The Exception level that debug exceptions are targeting is called the debug target Exception level , ELD. Routing debug exceptions describes how ELD is derived.

## G2.10.4.2 Usage constraints that apply only to the address-matching form

Exception vectors are at word-aligned addresses, and:

- It is CONSTRAINED UNPREDICTABLE whether an enabled vector catch generates a Vector Catch exception for a 32-bit T32 instruction starting at the halfword-aligned address immediately prior to the vector address.
- T32 instructions that start at the halfword-aligned address immediately after the exception vector do not generate Vector Catch exceptions.

For the address-matching form, Vector Catch exceptions have the same priority as Breakpoint exceptions. If a single instruction causes both a Vector Catch exception and a Breakpoint exception, it is CONSTRAINED UNPREDICTABLE which of these debug exceptions the PE takes.

## G2.10.5 Exception syndrome information and preferred return address for a Vector Catch exception

See the following:

- Exception syndrome information for a Vector Catch exception.
- Preferred return address for a Vector Catch exception.

Note

Usually, the term exception syndrome is used only for exceptions taken to Hyp mode, or to AArch64 state. The referenced section uses the term more generally, to include exception information reported in the IFSR.

## G2.10.5.1 Exception syndrome information for a Vector Catch exception

The PE takes a Vector Catch exception as either:

- APrefetch Abort exception if it is taken to PL1. In this case, it is taken to Abort mode.
- AHyptrap exception, if it is taken to PL2 because HCR.TGE or HDCR.TDE is 1. In this case, it is taken to Hyp mode.

If the exception is taken to:

## PL1 Abort mode

The PE sets all of the following:

- IFSR.FS to the code for a debug exception, 0b00010 .
- DBGDSCRext.MOE to 0b0101 , to indicate a Vector Catch exception.
- The IFAR with an UNKNOWN value.

The PE does all of the following:

- Records information about the exception in the Hypervisor Syndrome Register , HSR. See Table G2-26.
- Sets DBGDSCRext.MOE to 0b0101 , to indicate a Vector Catch exception.
- Sets the HIFAR to an unknown value.

## PL2 Hyp mode

## Table G2-26 Information recorded in the HSR

| HSR field                           | Information recorded                                                                                                                                                                                   |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Exception Class , EC                | The PE sets this to the code for a Prefetch Abort exception routed to Hyp mode, 0x20 .                                                                                                                 |
| Instruction Length , IL             | The PE sets this to 1.                                                                                                                                                                                 |
| Instruction Specific Syndrome , ISS | ISS[24:10] RES0. ISS[9] External Abort type (EA). The PE sets this to 0 . ISS[8:6] RES0. ISS[5:0] Instruction Fault Status Code (IFSC). The PE sets this to the code for a debug exception, 0b100010 . |

Note

For information about how debug exceptions can be routed to PL2, see Routing debug exceptions.

## G2.10.5.2 Preferred return address for a Vector Catch exception

The preferred return address of a Vector Catch exceptions is the address of the instruction that was not executed because the PE took the Vector Catch exception instead.

This means that the preferred return address is the exception vector. This is true regardless of whether the address-matching form or the exception trapping form is implemented.

## G2.10.6 Pseudocode description of Vector Catch exceptions

The AArch32.VCRMatch() pseudocode function checks whether the instruction at address generates a Vector Catch exception. It therefore shows the address-matching form of vector catch.

The AArch32.CheckVectorCatch() pseudocode function uses AArch32.VCRMatch() to test whether the instruction generates a Vector Catch exception, and if AArch32.VCRMatch() returns TRUE it generates that event.

The AArch32.Abort() function processes the FaultRecord object returned by AArch32.CheckVectorCatch() , as described in Abort exceptions. If there is a Vector Catch exception, the AArch32.Abort() function generates a Prefetch Abort exception.