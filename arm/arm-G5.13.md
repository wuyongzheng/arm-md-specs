## G5.13 Address translation instructions

The System register encoding space includes encodings for instructions that either:

- Translate a virtual address (VA) to a physical address (PA).
- Translate a virtual address (VA) to an intermediate physical address (IPA).

Address translation system instructions summarizes these instructions.

When using the Short-descriptor translation table format, all translations performed by these instructions take account of TEX remap when this is enabled, see Short-descriptor format memory region attributes, with TEX remap.

An address translation instruction that executes successfully returns the output address, a PA or an IPA, in the PAR. This is a 64-bit register that can hold addresses of up to 40 bits.

It is IMPLEMENTATION DEFINED whether the address translation instructions return the values held in a TLB or the result of a translation table walk. Therefore, Arm recommends that these instructions are not used at a time when the TLB entries might be different from the underlying translation tables held in memory.

The following sections give more information about these instructions:

- Address translation instruction naming and operation summary.
- Encoding and availability of the address translation instructions.
- Determining the PAR format.
- Handling of faults and aborts during an address translation instruction.

## G5.13.1 Address translation instruction naming and operation summary

Some older documentation uses the original names for the address translation instructions that were included in the original Armv7 documentation. Table G5-34 summarizes the instructions that are available in AArch32 state, and relates the old instruction names to the current names.

## Table G5-34 Naming of address translation instructions

| Name                                                  | Old name                                           | Description                                                               |
|-------------------------------------------------------|----------------------------------------------------|---------------------------------------------------------------------------|
| ATS1CPR, ATS1CPW, ATS1CUR, ATS1CUW ATS1CPRP, ATS1CPWP | V2PCWPR, V2PCWPW, V2PCWUR,V2PCWUW Not applicable a | See ATS1C**, Address translation stage 1, current security state          |
| ATS12NSOPR, ATS12NSOPW, ATS12NSOUR, ATS12NSOUW        | V2POWPR, V2POWPW, V2POWUR,V2POWUW                  | See ATS12NSO**, Address translation stages 1 and 2, Non-secure state only |
| ATS1HR, ATS1HW                                        | Not applicable b                                   | See ATS1H*, Address translation stage 1, Hyp mode                         |

In an implementation that does not include EL2, there is no distinction between stage 1 translations and stage 1 and 2 combined translations.

For the stage 1 current state and stages 1 and 2 Non-secure state only instructions, the meanings of the final letters of the names are:

| PR   | PL1 mode, read operation.                               |
|------|---------------------------------------------------------|
| PRP  | PL1 mode, read operation, taking account of PSTATE.PAN. |
| PW   | PL1 mode, write operation.                              |

PWP

PL1 mode, write operation, taking account of PSTATE.PAN.

UR

User mode, read operation.

UW

User mode, write operation.

Note

User mode can be described as the unprivileged mode. It is the only EL0 mode.

For the stage 1 Hyp mode instructions, the last letter of the instruction name is R for the read operation and W for the write operation.

See also Encoding and availability of the address translation instructions.

## G5.13.1.1 ATS1C**, Address translation stage 1, current security state

Any VMSAv8-32 implementation supports the ATS1C** instructions. They can be executed by any software executing at PL1 or higher, in either Security state.

The ATS1C** instructions are ATS1CPR, ATS1CPW, ATS1CUR, and ATS1CUW and, when FEAT\_PAN2 is implemented, ATS1CPRP and ATS1CPWP. These instructions perform the address translations of the PL1&amp;0 translation regime.

In an implementation that includes EL2, when executed in Non-secure state, these instructions return the IPA that is the output address of the stage 1 translation. Figure G5-1 shows the different translation regimes.

Note

The Non-secure PL1 and EL0 modes have no visibility of the stage 2 address translations, that can be defined only at EL2, and translate IPAs to be PAs.

See Determining the PAR format for the format used when returning the result of these instructions.

## G5.13.1.2 ATS12NSO**, Address translation stages 1 and 2, Non-secure state only

AVMSAv8-32 implementation supports the ATS12NSO** instructions only if it includes EL2. In an implementation that includes EL2, in AArch32 state, they can be executed:

- By software executing in Non-secure state at EL2. This means by software executing in Hyp mode.
- If the implementation includes EL3, when EL3 is using AArch32, by software executing in Secure state at PL1.

The ATS12NSO** instructions are ATS12NSOPR, ATS12NSOPW, ATS12NSOUR, and ATS12NSOUW.

In an implementation that includes EL3, when EL3 is using AArch64 and EL1 is using AArch32, any execution of an ATS12NSO** instruction at Secure EL1 is trapped as an exception that is taken to EL3.

In an implementation that does not include EL2, but includes EL3, when EL3 is using AArch32 these instructions are not UNDEFINED but each instruction behaves in the same way as the equivalent ATS1C** instruction.

If an implementation does not include EL2 and does not include EL3 then these instructions are CONSTRAINED UNPREDICTABLE, with the permitted behavior that the instructions are UNDEFINED, see Unallocated System register access instructions.

Arm deprecates use of these instructions from any Secure PL1 mode other than Monitor mode.

In Secure state and in Non-secure Hyp mode these instructions perform the translations made by the Non-secure PL1&amp;0 translation regime.

These instructions always return the PA and final attributes generated by the translation. That is, for an implementation that includes EL2, they return:

- The result of the two stages of address translation for the specified Non-secure input address.
- The memory attributes obtained by the combination of the stage 1 and stage 2 attributes.

Note

From Hyp mode, the ATS1C** and ATS12NSO** instructions both return the results of address translations that would be performed in the Non-secure modes other than Hyp mode. The difference is:

- The ATS1C** instructions return the Non-secure PL1 view of the associated address translation. That is, they return the IPA output address corresponding to the V A input address.
- The ATS12NSO** instructions return the EL2, or Hyp mode, view of the associated address translation. That is, they return the PA output address corresponding to the V A input address, generated by two stages of translation.

See Determining the PAR format for the format used when returning the result of these instructions.

## G5.13.1.3 ATS1H*, Address translation stage 1, Hyp mode

AVMSAv8-32 implementation supports the ATS1H* instructions only if it includes EL2. They can be executed by:

- Software executing in Non-secure state at EL2. This means by software executing in Hyp mode.
- Software executing in Secure state in Monitor mode.

The ATS1H* instructions are ATS1HR and ATS1HW. In an implementation that includes EL3, these instructions are CONSTRAINED UNPREDICTABLE if executed in a Secure PL1 mode other than Monitor mode.

If an implementation does not include EL2 then these instructions are CONSTRAINED UNPREDICTABLE, with the permitted behavior that the instructions are UNDEFINED, see Unallocated System register access instructions.

These instructions perform the translations made by the Non-secure EL2 translation regime. The instruction takes a V A input address and returns a PA output address.

These instructions always return a result in a 64-bit format PAR.

## G5.13.2 Encoding and availability of the address translation instructions

Software executing at EL0 never has any visibility of the address translation instructions, but software executing at PL1 or higher can use the unprivileged address translation instructions to find the address translations used for memory accesses by software executing at PL1 and EL0.

Note

For information about translations when the stage of address translation is disabled see The effects of disabling address translation stages on VMSAv8-32 behavior.

Table G5-35 shows the encodings for the address translation instructions, and their availability in different implementations in different PE modes and states.

Table G5-35 Address translation instructions in AArch32 state

| opc1                                                                                                                            | CRm                                                                                                                             | opc2                                                                                                                            | Name                                                                                                                            | Type                                                                                                                            | Description                                                                                                                     |
|---------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| All VMSAv8-32 implementations, in all modes, at PL1 or higher, see ATS1C**, Address translation stage 1, current security state | All VMSAv8-32 implementations, in all modes, at PL1 or higher, see ATS1C**, Address translation stage 1, current security state | All VMSAv8-32 implementations, in all modes, at PL1 or higher, see ATS1C**, Address translation stage 1, current security state | All VMSAv8-32 implementations, in all modes, at PL1 or higher, see ATS1C**, Address translation stage 1, current security state | All VMSAv8-32 implementations, in all modes, at PL1 or higher, see ATS1C**, Address translation stage 1, current security state | All VMSAv8-32 implementations, in all modes, at PL1 or higher, see ATS1C**, Address translation stage 1, current security state |
| 0                                                                                                                               | c8                                                                                                                              | 0                                                                                                                               | ATS1CPR                                                                                                                         | WO                                                                                                                              | PL1 stage 1 read translation, current state                                                                                     |
|                                                                                                                                 |                                                                                                                                 | 1                                                                                                                               | ATS1CPW                                                                                                                         | WO                                                                                                                              | PL1 stage 1 write translation, current state                                                                                    |
|                                                                                                                                 |                                                                                                                                 | 2                                                                                                                               | ATS1CUR                                                                                                                         | WO                                                                                                                              | Unprivileged stage 1 read translation, current state                                                                            |
|                                                                                                                                 |                                                                                                                                 | 3                                                                                                                               | ATS1CUW                                                                                                                         | WO                                                                                                                              | Unprivileged stage 1 write translation, current state                                                                           |
|                                                                                                                                 | c9                                                                                                                              | 0                                                                                                                               | ATS1CPRP a                                                                                                                      | WO                                                                                                                              | PL1 stage 1 read translation, current state, PSTATE.PAN a                                                                       |
|                                                                                                                                 |                                                                                                                                 | 1                                                                                                                               | ATS1CPWP a                                                                                                                      | WO                                                                                                                              | PL1 stage 1 write translation, current state, PSTATE.PAN a                                                                      |

| opc1                                                                                                                                                | CRm                                                                                                                                                 | opc2                                                                                                                                                | Name                                                                                                                                                | Type                                                                                                                                                | Description                                                                                                                                         |
|-----------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Implementation includes EL2, in Non-secure Hyp mode and Secure PL1 modes, see ATS12NSO**, Address translation stages 1 and 2, Non-secure state only | Implementation includes EL2, in Non-secure Hyp mode and Secure PL1 modes, see ATS12NSO**, Address translation stages 1 and 2, Non-secure state only | Implementation includes EL2, in Non-secure Hyp mode and Secure PL1 modes, see ATS12NSO**, Address translation stages 1 and 2, Non-secure state only | Implementation includes EL2, in Non-secure Hyp mode and Secure PL1 modes, see ATS12NSO**, Address translation stages 1 and 2, Non-secure state only | Implementation includes EL2, in Non-secure Hyp mode and Secure PL1 modes, see ATS12NSO**, Address translation stages 1 and 2, Non-secure state only | Implementation includes EL2, in Non-secure Hyp mode and Secure PL1 modes, see ATS12NSO**, Address translation stages 1 and 2, Non-secure state only |
| 0                                                                                                                                                   | c8                                                                                                                                                  | 4                                                                                                                                                   | ATS12NSOPR                                                                                                                                          | WO                                                                                                                                                  | Non-secure PL1 stage 1 and 2 read translation                                                                                                       |
|                                                                                                                                                     |                                                                                                                                                     | 5                                                                                                                                                   | ATS12NSOPW                                                                                                                                          | WO                                                                                                                                                  | Non-secure PL1 stage 1 and 2 write translation                                                                                                      |
|                                                                                                                                                     |                                                                                                                                                     | 6                                                                                                                                                   | ATS12NSOUR                                                                                                                                          | WO                                                                                                                                                  | Non-secure unprivileged stage 1 and 2 read translation                                                                                              |
|                                                                                                                                                     |                                                                                                                                                     | 7                                                                                                                                                   | ATS12NSOUW                                                                                                                                          | WO                                                                                                                                                  | Non-secure unprivileged stage 1 and 2 write translation                                                                                             |
| Implementation includes EL2, in Non-secure Hyp mode and Secure Monitor mode, see ATS1H*, Address translation stage 1, Hyp mode                      | Implementation includes EL2, in Non-secure Hyp mode and Secure Monitor mode, see ATS1H*, Address translation stage 1, Hyp mode                      | Implementation includes EL2, in Non-secure Hyp mode and Secure Monitor mode, see ATS1H*, Address translation stage 1, Hyp mode                      | Implementation includes EL2, in Non-secure Hyp mode and Secure Monitor mode, see ATS1H*, Address translation stage 1, Hyp mode                      | Implementation includes EL2, in Non-secure Hyp mode and Secure Monitor mode, see ATS1H*, Address translation stage 1, Hyp mode                      | Implementation includes EL2, in Non-secure Hyp mode and Secure Monitor mode, see ATS1H*, Address translation stage 1, Hyp mode                      |
| 4                                                                                                                                                   | c8                                                                                                                                                  | 0                                                                                                                                                   | ATS1HR                                                                                                                                              | WO                                                                                                                                                  | Hyp mode stage 1 read translation                                                                                                                   |
|                                                                                                                                                     |                                                                                                                                                     | 1                                                                                                                                                   | ATS1HW                                                                                                                                              | WO                                                                                                                                                  | Hyp mode stage 1 write translation                                                                                                                  |

The result of an instruction is always returned in the PAR. The PAR is a RW register and:

- In all implementations, the 32-bit format PAR is accessed using an MCR or MRC instruction with CRn set to c7, CRmset to c4, and opc1 and opc2 both set to 0.
- The 64-bit format PAR is accessed using an MCRR or MRRC instruction with CRm set to c7, and opc1 set to 0.

Address translation instructions that are not available in a particular implementation are reserved and CONSTRAINED UNPREDICTABLE. For example:

- In an implementation that does not include EL2, the encodings with an opc1 value of 4 are reserved and CONSTRAINED UNPREDICTABLE. These are the ATS1H* instructions.
- In an implementation that does not include either EL2 or EL3, the encodings with opc2 values of 4-7 are reserved and CONSTRAINED UNPREDICTABLE. These are the ATS12NSO** instructions.

The CONSTRAINED UNPREDICTABLE behavior of these encodings is that they are UNDEFINED, see Unallocated System register access instructions.

## G5.13.3 Determining the PAR format

The PAR is a 64-bit register that supports both 32-bit and 64-bit PAR formats. This section describes how the PAR format is determined, for returning a result from each of the groups of address translation instructions. The returned result might be the translated address, or might indicate a fault on the translation, see Handling of faults and aborts during an address translation instruction.

## ATS1C** instructions

Address translations for the current state. From modes other than Hyp mode:

- TTBCR.EAE determines whether the result is returned using the 32-bit or the 64-bit PAR format.
- If the implementation includes EL3, the translation performed is for the current security state and, depending on that state:
- -The Secure or Non-secure TTBCR.EAE determines the PAR format.
- -The result is returned to the Secure or Non-secure instance of the PAR

Instructions executed in Hyp mode always return a result to the Non-secure PAR, using the 64-bit format.

## ATS12NSO** instructions

Address translations for the Non-secure PL1 and EL0 modes. These instructions return a result using the 64-bit PAR format if at least one of the following is true:

- The Non-secure TTBCR.EAE bit is set to 1.

- The implementation includes EL2, and the value of HCR.VM is 1.

Otherwise, the instruction returns a result using the 32-bit PAR format.

Instructions executed in a Secure PL1 mode return a result to the Secure PAR. Instructions executed in Hyp mode return a result to the Non-secure PAR.

## ATS1H* instructions

Address translations from Hyp mode. These instructions always return a result using the 64-bit PAR format.

Instructions executed in Secure Monitor mode return a result to the Secure PAR. Instructions executed in Non-secure Hyp mode return a result to the Non-secure PAR.

## G5.13.4 Handling of faults and aborts during an address translation instruction

When a stage of address translation is enabled, any corresponding address translation instruction requires a translation table lookup, and this might require a translation table walk. However, the input address for the translation might be a faulting address, either because:

- The translation table entries used for the translation indicate a fault.
- Astage 2 fault or an External abort occurs on the required translation table walk.

VMSAv8-32 memory aborts describes the faults that might occur on a translation table walk in AArch32 state.

How the fault is handled, and whether it generates an exception, depends on the cause of the fault, as described in:

- MMUfault on an address translation instruction.
- External abort during an address translation instruction.
- Stage 2 fault on a current state address translation instruction.

## G5.13.4.1 MMU fault on an address translation instruction

In the following cases, an MMU fault on an address translation is reported in the PAR, and no abort is taken. This applies:

- For a faulting address translation instruction executed in Hyp mode, or in a Secure PL1 mode.
- For a faulting address translation instruction executed in a Non-secure PL1 mode, for cases where the fault would generate a stage 1 abort if it occurred on the equivalent load or store operation.

Using the PAR to report a fault on an address translation instruction gives more information about how these faults are reported.

Note

- The Domain fault encodings shown in Table G5-27 are used only for reporting a fault on an address translation instruction that uses the 64-bit PAR format. That is, they are used only in an implementation that includes EL2, and are used for reporting a Domain fault on either:
- -An ATS1C** instruction executed in Hyp mode.
- -An ATS12NSO** instruction executed when the value of HCR.VM is 1.

These encodings are never used for fault reporting in the DFSR, IFSR, or HSR.

- For an address translation instruction executed in a Non-secure PL1 mode, for a fault that would generate a stage 2 abort if it occurred on the equivalent load or store operation, the stage 2 abort is generated as described in Stage 2 fault on a current state address translation instruction.

## G5.13.4.1.1 Using the PAR to report a fault on an address translation instruction

For a fault on an address translation instruction for which no abort is taken, the PAR is updated with the following information, to indicate the fault:

- The fault code, that would normally be written to the Fault status register. The code used depends on the current translation table format, as described in either:
- -PL1 fault reporting with the Short-descriptor translation table format.
- -PL1 fault reporting with the Long-descriptor translation table format.

See also the Note at the start of Determining the PAR format about the Domain fault encodings shown in Table G5-27.

- Astatus bit, that indicates that the translation operation failed.

The fault does not update any Fault Address Register.

## G5.13.4.2 External abort during an address translation instruction

As stated in External abort on a translation table walk, an External abort on a translation table walk generates a Data Abort exception. The abort can be synchronous or asynchronous, and behaves as follows:

## Synchronous External abort on a translation table walk

The fault status and fault address registers of the Security state to which the abort is taken are updated. The fault status register indicates the appropriate External abort on a Translation fault, and the fault address register indicates the input address for the translation.

The PAR is UNKNOWN.

## Asynchronous External abort on a translation table walk

The fault status register of the Security state to which the abort is taken is updated, to indicate the asynchronous External abort. No fault address registers are updated.

The PAR is UNKNOWN.

## G5.13.4.3 Stage 2 fault on a current state address translation instruction

If the PE is in a Non-secure PL1 mode and executes one of the ATS1C** instructions, then a fault in the stage 2 translation of an address accessed in a stage 1 translation table lookup generates an exception. This is equivalent to the case described in Stage 2 fault on a stage 1 translation table walk. When this fault occurs on an ATS1C** address translation instruction:

- AHypTrap exception is taken to Hyp mode.
- The PAR is UNKNOWN.
- The HSR indicates that:
- -The fault occurred on a translation table walk.
- -The operation that faulted was a cache maintenance instruction.
- The HPFAR holds the IPA that faulted.
- The HDFAR holds the VA that the executing software supplied to the address translation instruction.